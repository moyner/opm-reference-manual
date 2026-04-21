#!/usr/bin/env python3
"""
Convert FODT (Flat ODF Text) files to Markdown.

Extracts the content (descriptions, examples, tables, images) from FODT files
and produces clean Markdown output with embedded images saved as separate files.
"""

import base64
import hashlib
import os
import re
import sys
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

# ODF XML namespaces
NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "xlink": "http://www.w3.org/1999/xlink",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "loext": "urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0",
    "number": "urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0",
    "math": "http://www.w3.org/1998/Math/MathML",
}

# Named styles that indicate code/example content
EXAMPLE_STYLES = {
    "_40_Example",
    "_40_Code",
    "Preformatted_20_Text",
}

# Named styles for headings
HEADING_STYLES = {
    "Heading_20_1",
    "Heading_20_2",
    "Heading_20_3",
    "Heading_20_4",
    "Heading_20_5",
    "Heading_20_6",
    "Heading_20_7",
    "Heading_20_8",
    "Heading_20_9",
    "Heading_20_10",
    "Heading",
}

# Named styles that indicate table-related content
TABLE_CAPTION_STYLES = {
    "Table",
    "Figure",
}

# Named styles for note/warning boxes
NOTE_STYLES = {
    "_40_TextNote",
}


def tag_local(elem):
    """Get the local tag name without namespace."""
    t = elem.tag
    if "}" in t:
        return t.split("}")[1]
    return t


def build_style_map(root):
    """
    Build a mapping from style names to their full ancestor chain.
    Returns a dict: style_name -> list of all styles in the chain (including self).
    """
    direct_parent = {}  # name -> parent-style-name (direct)

    # Collect from office:styles (named styles) and office:automatic-styles
    for section_tag in ["office:styles", "office:automatic-styles"]:
        section = root.find(section_tag, NS)
        if section is None:
            continue
        for style_elem in section:
            if tag_local(style_elem) != "style":
                continue
            name = style_elem.get(f'{{{NS["style"]}}}name', "")
            parent = style_elem.get(f'{{{NS["style"]}}}parent-style-name', "")
            if name:
                direct_parent[name] = parent

    # Build full ancestor chain for each style
    resolved = {}
    for name in direct_parent:
        chain = []
        current = name
        seen = set()
        while current and current not in seen:
            seen.add(current)
            chain.append(current)
            if current in direct_parent:
                current = direct_parent[current]
            else:
                break
        resolved[name] = chain
    return resolved


def style_chain_contains(style_name, style_map, target_styles):
    """Check if any style in the ancestor chain matches target_styles."""
    if style_name in target_styles:
        return True
    chain = style_map.get(style_name, [style_name])
    return bool(set(chain) & target_styles)


def is_example_style(style_name, style_map):
    """Check if a style or any of its ancestors is an example/code style."""
    return style_chain_contains(style_name, style_map, EXAMPLE_STYLES)


def is_heading_style(style_name, style_map):
    """Check if a style or any of its ancestors is a heading style."""
    return style_chain_contains(style_name, style_map, HEADING_STYLES)


def get_heading_level(elem, style_name, style_map):
    """Get heading level from element or style."""
    level = elem.get(f'{{{NS["text"]}}}outline-level', "")
    if level:
        return int(level)
    # Try to infer from style chain
    chain = style_map.get(style_name, [style_name])
    for s in chain:
        for i in range(1, 11):
            if s == f"Heading_20_{i}":
                return i
    return 1


def extract_text(elem, style_map, in_code=False):
    """
    Recursively extract text content from an element.
    Handles text:s (spaces), text:tab, text:line-break, and text:span elements.
    """
    parts = []

    # Element's own text
    if elem.text:
        parts.append(elem.text)

    for child in elem:
        local = tag_local(child)

        if local == "s":
            # text:s is a space element, c attribute gives count
            count = int(child.get(f'{{{NS["text"]}}}c', "1"))
            parts.append(" " * count)
        elif local == "tab":
            parts.append("\t")
        elif local == "line-break":
            parts.append("\n")
        elif local == "span":
            parts.append(extract_text(child, style_map, in_code))
        elif local == "a":
            # Hyperlink
            href = child.get(f'{{{NS["xlink"]}}}href', "")
            link_text = extract_text(child, style_map, in_code)
            if href and link_text and not in_code:
                # Strip FODT-internal links (outline anchors and __RefHeading__ anchors)
                if "|outline" in href or href.startswith("#__RefHeading__"):
                    parts.append(link_text)
                else:
                    parts.append(f"[{link_text}]({href})")
            else:
                parts.append(link_text)
        elif local == "note":
            # Footnote — render as Pandoc/Quarto inline footnote
            note_body = child.find(f'{{{NS["text"]}}}note-body')
            if note_body is not None:
                note_text = ""
                for p in note_body:
                    note_text += extract_text(p, style_map, in_code)
                note_text = note_text.strip()
                if note_text:
                    parts.append(f"^[{note_text}]")
        elif local == "bookmark-start" or local == "bookmark-end":
            pass
        elif local == "bookmark-ref" or local == "bookmark":
            ref_text = extract_text(child, style_map, in_code)
            # Drop unresolved cross-references
            if "Error: Reference source not found" not in ref_text:
                parts.append(ref_text)
        elif local == "sequence" or local == "sequence-ref":
            ref_text = extract_text(child, style_map, in_code)
            # Drop unresolved cross-references
            if "Error: Reference source not found" not in ref_text:
                parts.append(ref_text)
        elif local == "soft-page-break":
            pass
        elif local == "change-start" or local == "change-end" or local == "change":
            pass
        elif local == "frame":
            # Handle embedded images/objects
            img_result = extract_frame(child)
            if img_result:
                parts.append(img_result)
        elif local in ("note-citation",):
            pass
        else:
            # For other elements, try to extract text
            parts.append(extract_text(child, style_map, in_code))

        # Tail text (text after the child element)
        if child.tail:
            parts.append(child.tail)

    return "".join(parts)


def mathml_to_latex(elem):
    """Recursively convert a MathML element to a LaTeX string."""
    tag = elem.tag
    if "}" in tag:
        tag = tag.split("}")[1]

    # Operators that need special LaTeX commands
    MO_MAP = {
        "∂": r"\partial ",
        "∇": r"\nabla ",
        "·": r"\cdot ",
        "×": r"\times ",
        "±": r"\pm ",
        "∓": r"\mp ",
        "∞": r"\infty ",
        "≤": r"\leq ",
        "≥": r"\geq ",
        "≠": r"\neq ",
        "≈": r"\approx ",
        "→": r"\rightarrow ",
        "⟨": r"\langle ",
        "⟩": r"\rangle ",
        "∑": r"\sum ",
        "∏": r"\prod ",
        "∫": r"\int ",
        "√": r"\sqrt ",
        "∈": r"\in ",
        "−": "-",
        "˙": r"\dot",
    }

    if tag == "math":
        sem = elem.find(f'{{{NS["math"]}}}semantics')
        if sem is not None:
            return mathml_to_latex(sem)
        return "".join(mathml_to_latex(c) for c in elem)

    elif tag == "semantics":
        # First non-annotation child is the math content
        for child in elem:
            ctag = child.tag.split("}")[1] if "}" in child.tag else child.tag
            if ctag not in ("annotation", "annotation-xml"):
                return mathml_to_latex(child)
        return ""

    elif tag in ("mrow", "mpadded", "mphantom"):
        children = list(elem)
        # Detect piecewise function: mrow with opening { fence followed by mtable
        # This should become \begin{cases}...\end{cases}
        if len(children) >= 2:
            first = children[0]
            first_tag = first.tag.split("}")[1] if "}" in first.tag else first.tag
            if (first_tag == "mo" and first.text == "{"
                    and first.get("fence", "false") == "true"):
                # Check if there's an mtable somewhere in the remaining children
                rest_text = "".join(mathml_to_latex(c) for c in children[1:])
                if r"\begin{matrix}" in rest_text:
                    # Replace \begin{matrix}...\end{matrix} with cases env
                    # and strip any leading \{ that was added
                    rest_text = rest_text.replace(r"\begin{matrix}", r"\begin{cases}")
                    rest_text = rest_text.replace(r"\end{matrix}", r"\end{cases}")
                    rest_text = rest_text.replace(r"\{", "").replace(r"\}", "")
                    return rest_text
        return "".join(mathml_to_latex(c) for c in elem)

    elif tag == "mi":
        text = elem.text or ""
        variant = elem.get("mathvariant", "")
        if variant == "italic" and len(text) > 1:
            return r"\mathit{" + text + "}"
        if variant == "normal":
            return r"\mathrm{" + text + "}"
        return text

    elif tag == "mn":
        return elem.text or ""

    elif tag == "mo":
        text = elem.text or ""
        result = MO_MAP.get(text, text)
        fence = elem.get("fence", "false")
        stretchy = elem.get("stretchy", "false")
        if fence == "true" and stretchy == "true":
            # Map special delimiters but don't use \left/\right (causes
            # balancing issues with LibreOffice MathML output)
            if text == "{":
                result = r"\{"
            elif text == "}":
                result = r"\}"
        return result

    elif tag == "mfrac":
        children = list(elem)
        if len(children) >= 2:
            num = mathml_to_latex(children[0])
            den = mathml_to_latex(children[1])
            return r"\frac{" + num + "}{" + den + "}"
        return ""

    elif tag == "msup":
        children = list(elem)
        if len(children) >= 2:
            base = mathml_to_latex(children[0])
            sup = mathml_to_latex(children[1])
            return "{" + base + "}^{" + sup + "}"
        return ""

    elif tag == "msub":
        children = list(elem)
        if len(children) >= 2:
            base = mathml_to_latex(children[0])
            sub = mathml_to_latex(children[1])
            return "{" + base + "}_{" + sub + "}"
        return ""

    elif tag == "msubsup":
        children = list(elem)
        if len(children) >= 3:
            base = mathml_to_latex(children[0])
            sub = mathml_to_latex(children[1])
            sup = mathml_to_latex(children[2])
            return "{" + base + "}_{" + sub + "}^{" + sup + "}"
        return ""

    elif tag == "mtext":
        text = elem.text or ""
        if text.strip():
            return r"\text{" + text + "}"
        return text

    elif tag == "mstyle":
        variant = elem.get("mathvariant", "")
        content = "".join(mathml_to_latex(c) for c in elem)
        if variant == "bold":
            return r"\mathbf{" + content + "}"
        if variant == "normal":
            return r"\mathrm{" + content + "}"
        return content

    elif tag == "msqrt":
        content = "".join(mathml_to_latex(c) for c in elem)
        return r"\sqrt{" + content + "}"

    elif tag == "mroot":
        children = list(elem)
        if len(children) >= 2:
            base = mathml_to_latex(children[0])
            index = mathml_to_latex(children[1])
            return r"\sqrt[" + index + "]{" + base + "}"
        return ""

    elif tag == "mover":
        children = list(elem)
        if len(children) >= 2:
            base = mathml_to_latex(children[0])
            over = mathml_to_latex(children[1])
            over_stripped = over.strip()
            over_map = {
                "^": r"\hat",
                "→": r"\vec",
                "¯": r"\bar",
                "˙": r"\dot",
                "¨": r"\ddot",
                r"\dot": r"\dot",
                r"\ddot": r"\ddot",
            }
            # Special case: dot accent over empty/whitespace base → just the cdot operator
            # This pattern appears in FODT for the divergence operator (∇·)
            base_stripped = base.strip()
            if over_stripped in ("˙", r"\dot", r"\cdot") and (
                not base_stripped or base_stripped == r"\text{ }"
            ):
                return r"\cdot "
            over_cmd = over_map.get(over_stripped)
            if over_cmd:
                return over_cmd + "{" + base + "}"
            return r"\overset{" + over + "}{" + base + "}"
        return ""

    elif tag == "munder":
        children = list(elem)
        if len(children) >= 2:
            base = mathml_to_latex(children[0])
            under = mathml_to_latex(children[1])
            return r"\underset{" + under + "}{" + base + "}"
        return ""

    elif tag == "munderover":
        children = list(elem)
        if len(children) >= 3:
            base = mathml_to_latex(children[0])
            under = mathml_to_latex(children[1])
            over = mathml_to_latex(children[2])
            return "{" + base + "}_{" + under + "}^{" + over + "}"
        return ""

    elif tag == "mspace":
        return " "

    elif tag == "mtable":
        rows = []
        for row in elem:
            rtag = row.tag.split("}")[1] if "}" in row.tag else row.tag
            if rtag == "mtr":
                cells = []
                for cell in row:
                    ctag = cell.tag.split("}")[1] if "}" in cell.tag else cell.tag
                    if ctag == "mtd":
                        cells.append("".join(mathml_to_latex(c) for c in cell))
                rows.append(" & ".join(cells))
        return r"\begin{matrix}" + r" \\ ".join(rows) + r"\end{matrix}"

    elif tag in ("annotation", "annotation-xml"):
        return ""

    else:
        # Fallback: concatenate children text
        parts = []
        if elem.text:
            parts.append(elem.text)
        for child in elem:
            parts.append(mathml_to_latex(child))
            if child.tail:
                parts.append(child.tail)
        return "".join(parts)


def balance_left_right(latex: str) -> str:
    """Balance unmatched \\left and \\right delimiters in a LaTeX string.

    Inserts \\right. for unmatched \\left... and \\left. for unmatched \\right...
    """
    import re
    # Pattern to find \left or \right followed by a delimiter character.
    # Use a negative lookahead to avoid matching commands like \rightarrow, \leftarrow, etc.
    # \left/\right must be followed by a non-letter (delimiter) or a backslash sequence.
    token_re = re.compile(r'\\(left|right)(?![a-zA-Z])(\\[|{}]|[^\\\s]|\\.)?')
    tokens = list(token_re.finditer(latex))

    # Count unmatched lefts
    depth = 0
    for m in tokens:
        if m.group(1) == 'left':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                # Unmatched right — prepend \left.
                insert_pos = m.start()
                latex = latex[:insert_pos] + r'\left.' + latex[insert_pos:]
                depth = 0
                # Re-run after modification
                return balance_left_right(latex)

    # Append \right. for each unmatched \left
    if depth > 0:
        latex = latex + r'\right.' * depth

    return latex


def extract_frame(frame_elem):
    """Extract content from a draw:frame element (images or objects).

    Always returns inline notation ($...$) for math; block formatting ($$...$$)
    is the caller's responsibility when the frame is the sole content of a paragraph.
    """
    # Prefer MathML objects over rasterized images
    for obj in frame_elem:
        if tag_local(obj) == "object":
            math_elem = obj.find(f'{{{NS["math"]}}}math')
            if math_elem is not None:
                latex = mathml_to_latex(math_elem)
                latex = balance_left_right(latex)
                # Strip leading/trailing whitespace so the opening $ is not
                # immediately followed by a space (which Pandoc treats as literal $)
                latex = latex.strip()
                if not latex:
                    continue
                return f"${latex}$"
    # Fall back to image placeholder
    for image in frame_elem.iter(f'{{{NS["draw"]}}}image'):
        binary = image.find(f'{{{NS["office"]}}}binary-data')
        if binary is not None and binary.text:
            return f"<<IMAGE:base64:{binary.text.strip()[:40]}...>>"
    return ""


class FODTConverter:
    """Convert a single FODT file to Markdown."""

    def __init__(self, fodt_path, images_dir, md_dir=None):
        self.fodt_path = Path(fodt_path)
        self.images_dir = Path(images_dir)
        self.md_dir = Path(md_dir) if md_dir else self.images_dir.parent
        self.image_counter = 0
        self.lines = []
        self.tree = None
        self.root = None
        self.style_map = {}

    def convert(self):
        """Parse the FODT and return markdown string."""
        self.tree = ET.parse(str(self.fodt_path))
        self.root = self.tree.getroot()
        self.style_map = build_style_map(self.root)

        body = self.root.find(".//office:body/office:text", NS)
        if body is None:
            return ""

        # Process body content - may have sections or direct content
        self._process_elements(body)

        return self._finalize()

    def _process_elements(self, parent):
        """Process child elements of a container (body or section)."""
        code_block = []  # Accumulate consecutive code lines

        for elem in parent:
            local = tag_local(elem)
            style = elem.get(f'{{{NS["text"]}}}style-name', "")

            if local == "section":
                # Flush code block before entering section
                self._flush_code_block(code_block)
                self._process_elements(elem)
                continue

            if local == "h":
                # Heading
                self._flush_code_block(code_block)
                level = get_heading_level(elem, style, self.style_map)
                text = extract_text(elem, self.style_map).strip()
                if text:
                    self.lines.append("")
                    self.lines.append(f"{'#' * level} {text}")
                    self.lines.append("")
                continue

            if local == "p":
                if is_example_style(style, self.style_map):
                    # Code example line
                    text = extract_text(elem, self.style_map, in_code=True)
                    code_block.append(text)
                    continue

                # Regular paragraph
                self._flush_code_block(code_block)
                text = self._process_paragraph(elem, style)
                if text is not None:
                    self.lines.append(text)
                continue

            if local == "table":
                self._flush_code_block(code_block)
                self._process_table(elem)
                continue

            if local == "list":
                self._flush_code_block(code_block)
                self._process_list(elem, indent=0)
                self.lines.append("")
                continue

            if local in (
                "forms",
                "sequence-decls",
                "user-field-decls",
                "variable-decls",
                "table-of-content",
                "alphabetical-index",
                "illustration-index",
                "table-index",
                "user-index",
            ):
                continue

            # For any other elements, try to extract text
            self._flush_code_block(code_block)
            text = extract_text(elem, self.style_map).strip()
            if text:
                self.lines.append(text)
                self.lines.append("")

        self._flush_code_block(code_block)

    def _flush_code_block(self, code_block):
        """Flush accumulated code lines as a fenced code block."""
        if not code_block:
            return
        # Strip common leading whitespace from the code block
        dedented = textwrap.dedent("\n".join(code_block))
        self.lines.append("")
        self.lines.append("```")
        for line in dedented.split("\n"):
            self.lines.append(line)
        self.lines.append("```")
        self.lines.append("")
        code_block.clear()

    def _get_sole_math_frame(self, elem):
        """Return the MathML element if the paragraph is purely a standalone equation.

        A paragraph is considered a block equation when its only direct children are
        a single draw:frame containing a math object (plus any soft-page-break elements).
        Any other children (spans with text, etc.) mean it is mixed content.
        """
        if elem.text and elem.text.strip():
            return None
        children = list(elem)
        math_elems = []
        for child in children:
            local = tag_local(child)
            if local == "frame":
                found_math = False
                for obj in child:
                    if tag_local(obj) == "object":
                        math_elem = obj.find(f'{{{NS["math"]}}}math')
                        if math_elem is not None:
                            math_elems.append(math_elem)
                            found_math = True
                            break
                if not found_math:
                    return None  # Regular image frame, not a math block
            elif local == "soft-page-break":
                pass
            else:
                return None  # Non-frame child → mixed content
            if child.tail and child.tail.strip():
                return None  # Text after a child → mixed content
        return math_elems[0] if len(math_elems) == 1 else None

    def _process_paragraph(self, elem, style):
        """Process a paragraph element and return markdown text."""
        resolved_style = self.style_map.get(style, [style])

        # --- Case 1: purely a standalone block equation ---
        math_elem = self._get_sole_math_frame(elem)
        if math_elem is not None:
            latex = mathml_to_latex(math_elem)
            latex = balance_left_right(latex)
            latex = latex.strip()
            if not latex:
                return ""
            return f"$$\n{latex}\n$$\n"

        # --- Case 2: paragraph contains any math frames (inline or mixed) ---
        # extract_text handles these as inline $...$ via extract_frame().
        all_frames = list(elem.iter(f'{{{NS["draw"]}}}frame'))
        has_any_math = any(
            any(
                tag_local(obj) == "object"
                and obj.find(f'{{{NS["math"]}}}math') is not None
                for obj in frame
            )
            for frame in all_frames
        )
        if has_any_math:
            text = extract_text(elem, self.style_map).strip()
            if not text:
                return ""
            return text + "\n"

        # --- Case 3: image-only frames (no math) ---
        if all_frames:
            result_parts = []
            for frame in all_frames:
                for image in frame.iter(f'{{{NS["draw"]}}}image'):
                    img_md = self._extract_and_save_image(image, frame)
                    if img_md:
                        result_parts.append(img_md)

            text = extract_text(elem, self.style_map).strip()
            text = re.sub(r"<<IMAGE:base64:[^>]+>>", "", text).strip()

            if result_parts:
                result = "\n".join(result_parts)
                if text:
                    result += f"\n\n{text}"
                return result + "\n"

        # Handle captions
        if set(resolved_style) & TABLE_CAPTION_STYLES:
            text = extract_text(elem, self.style_map).strip()
            if text:
                return f"*{text}*\n"
            return None

        # Handle note styles
        if set(resolved_style) & NOTE_STYLES:
            text = extract_text(elem, self.style_map).strip()
            if text:
                return f"::: {{.callout-note}}\n{text}\n:::\n"
            return None

        # Regular paragraph
        text = extract_text(elem, self.style_map).strip()

        # Skip empty paragraphs but keep track for spacing
        if not text:
            return ""

        return text + "\n"

    def _extract_and_save_image(self, image_elem, frame_elem):
        """Extract an embedded image, save to file, return markdown reference."""
        binary = image_elem.find(f'{{{NS["office"]}}}binary-data')
        if binary is None or not binary.text:
            return None

        data = binary.text.strip()
        try:
            img_bytes = base64.b64decode(data)
        except Exception:
            return None

        if len(img_bytes) < 50:
            return None

        # Determine image format from magic bytes
        ext = "png"  # default
        if img_bytes[:4] == b"\x89PNG":
            ext = "png"
        elif img_bytes[:2] == b"\xff\xd8":
            ext = "jpg"
        elif img_bytes[:4] == b"GIF8":
            ext = "gif"
        elif img_bytes[:4] == b"RIFF" and img_bytes[8:12] == b"WEBP":
            ext = "webp"
        elif img_bytes[:2] in (b"BM",):
            ext = "bmp"
        elif b"<svg" in img_bytes[:200]:
            ext = "svg"
        elif img_bytes[:4] == b"%PDF":
            ext = "pdf"
        elif img_bytes[:2] == b"PK":
            # Could be wmf/emf embedded in zip or OLE
            ext = "png"
        else:
            # Try to detect EMF/WMF
            if img_bytes[:4] == b"\x01\x00\x00\x00":
                ext = "emf"
            elif img_bytes[:4] == b"\xd7\xcd\xc6\x9a":
                ext = "wmf"
            else:
                # Unknown format, skip small equation objects
                return None

        # Skip very small images (likely equation symbols that are better as text)
        if len(img_bytes) < 200 and ext not in ("svg",):
            return None

        # Generate filename from content hash
        content_hash = hashlib.md5(img_bytes).hexdigest()[:12]
        self.image_counter += 1

        # Get frame name for a more descriptive filename
        frame_name = frame_elem.get(f'{{{NS["draw"]}}}name', "")
        if frame_name:
            safe_name = re.sub(r"[^\w]", "_", frame_name)
            filename = f"{safe_name}_{content_hash}.{ext}"
        else:
            filename = f"image_{self.image_counter}_{content_hash}.{ext}"

        # Save image
        self.images_dir.mkdir(parents=True, exist_ok=True)
        img_path = self.images_dir / filename
        with open(img_path, "wb") as f:
            f.write(img_bytes)

        # Return relative path from the markdown file's directory to the image
        rel_path = os.path.relpath(img_path, self.md_dir)
        # Use forward slashes for cross-platform compatibility
        rel_path = rel_path.replace(os.sep, "/")
        alt_text = frame_name if frame_name else f"Image {self.image_counter}"
        return f"![{alt_text}]({rel_path})"

    def _process_table(self, table_elem):
        """Convert an ODF table to Markdown table format."""
        rows = []
        for row in table_elem.iter(f'{{{NS["table"]}}}table-row'):
            # Check for repeat
            repeat = int(
                row.get(f'{{{NS["table"]}}}number-rows-repeated', "1")
            )
            if repeat > 10:
                continue  # Skip large empty row ranges

            cells = []
            for cell in row:
                cell_local = tag_local(cell)
                if cell_local == "covered-table-cell":
                    continue  # Skip spanned cells

                if cell_local == "table-cell":
                    # Check for column span
                    col_repeat = int(
                        cell.get(
                            f'{{{NS["table"]}}}number-columns-repeated', "1"
                        )
                    )
                    if col_repeat > 50:
                        continue

                    # Extract cell text - check for images too
                    cell_parts = []
                    has_images = False
                    for child in cell:
                        child_local = tag_local(child)
                        if child_local == "p":
                            imgs = list(
                                child.iter(f'{{{NS["draw"]}}}image')
                            )
                            if imgs:
                                has_images = True
                                for frame in child.iter(
                                    f'{{{NS["draw"]}}}frame'
                                ):
                                    for img in frame.iter(
                                        f'{{{NS["draw"]}}}image'
                                    ):
                                        img_md = (
                                            self._extract_and_save_image(
                                                img, frame
                                            )
                                        )
                                        if img_md:
                                            cell_parts.append(img_md)
                            text = extract_text(
                                child, self.style_map
                            ).strip()
                            text = re.sub(
                                r"<<IMAGE:base64:[^>]+>>", "", text
                            ).strip()
                            if text:
                                cell_parts.append(text)

                    cell_text = " ".join(cell_parts)
                    # Clean up for table cell
                    cell_text = cell_text.replace("|", "\\|")
                    cell_text = cell_text.replace("\n", " ")
                    cells.append(cell_text)

                    # Handle column repeat
                    for _ in range(col_repeat - 1):
                        cells.append(cell_text)

            if cells and any(c.strip() for c in cells):
                rows.append(cells)

            for _ in range(min(repeat - 1, 3)):
                if cells and any(c.strip() for c in cells):
                    rows.append(cells)

        if not rows:
            return

        # Normalize column count
        max_cols = max(len(r) for r in rows) if rows else 0
        if max_cols == 0:
            return

        for row in rows:
            while len(row) < max_cols:
                row.append("")

        # Check if this looks like a "Note" table (single cell with note content)
        if max_cols <= 2 and len(rows) >= 1:
            first_cell = rows[0][0].strip() if rows[0] else ""
            first_cell_lower = first_cell.lower()
            callout_map = {
                "note": "note",
                "notes": "note",
                "warning": "warning",
                "caution": "caution",
                "tip": "tip",
            }
            # Match either exact keyword or text starting with "Note ..." etc.
            matched_type = None
            if first_cell_lower in callout_map:
                matched_type = callout_map[first_cell_lower]
            else:
                for prefix, ctype in callout_map.items():
                    if first_cell_lower.startswith(prefix + " "):
                        matched_type = ctype
                        break
            if matched_type is not None:
                self.lines.append("")
                self.lines.append(f"::: {{.callout-{matched_type}}}")
                for row in rows:
                    for cell in row:
                        cell_stripped = cell.strip()
                        if not cell_stripped:
                            continue
                        # Remove the leading "Note"/"Warning"/etc. prefix from first cell
                        cell_lower = cell_stripped.lower()
                        if cell_lower in callout_map:
                            continue
                        for prefix in callout_map:
                            if cell_lower.startswith(prefix + " "):
                                cell_stripped = cell_stripped[len(prefix):].strip()
                                break
                        if cell_stripped:
                            self.lines.append(cell_stripped)
                self.lines.append(":::")
                self.lines.append("")
                return

        # Check if this looks like an equation table:
        # Each row has 2 cells, first cell is $...$, last is (X.Y) style number or empty
        non_empty_rows = [r for r in rows if any(c.strip() for c in r)]
        if non_empty_rows and len(non_empty_rows[0]) >= 2:
            all_eq = True
            eq_entries = []
            for row_data in non_empty_rows:
                eq_cell = row_data[0].strip()
                num_cell = row_data[-1].strip()
                eq_num_match = re.match(r"^\(?(\d+(?:\.\d+)*)\)?$", num_cell)
                if eq_cell.startswith("$") and eq_cell.endswith("$"):
                    eq_content = eq_cell[1:-1].strip()
                    if eq_num_match:
                        eq_label = eq_num_match.group(1).replace(".", "-")
                    else:
                        eq_label = None
                    eq_entries.append((eq_content, eq_label))
                else:
                    all_eq = False
                    break
            if all_eq and eq_entries:
                for eq_content, eq_label in eq_entries:
                    self.lines.append("")
                    self.lines.append("$$")
                    self.lines.append(eq_content)
                    if eq_label:
                        self.lines.append(f"$$ {{#eq-{eq_label}}}")
                    else:
                        self.lines.append("$$")
                    self.lines.append("")
                return

        # Build markdown table
        self.lines.append("")
        # Header row
        self.lines.append("| " + " | ".join(rows[0]) + " |")
        # Separator: use wider dashes for a "Description" column to give it more space
        sep_cells = []
        for col_idx, header in enumerate(rows[0]):
            if header.strip().lower() in ("description", "desc"):
                sep_cells.append(":------")
            else:
                sep_cells.append("---")
        self.lines.append("| " + " | ".join(sep_cells) + " |")
        # Data rows
        for row in rows[1:]:
            self.lines.append("| " + " | ".join(row) + " |")
        self.lines.append("")

    def _process_list(self, list_elem, indent=0):
        """Convert an ODF list to Markdown list format."""
        prefix_space = "  " * indent

        for i, item in enumerate(list_elem):
            if tag_local(item) != "list-item":
                continue

            has_text = False
            for child in item:
                local = tag_local(child)
                if local == "p":
                    text = extract_text(child, self.style_map).strip()
                    if text:
                        has_text = True
                        # Determine if ordered or unordered
                        # ODF lists with text:style-name containing "Number" are ordered
                        list_style = list_elem.get(
                            f'{{{NS["text"]}}}style-name', ""
                        )
                        if "Number" in list_style or "Ordered" in list_style:
                            self.lines.append(
                                f"{prefix_space}{i + 1}. {text}"
                            )
                        else:
                            self.lines.append(f"{prefix_space}- {text}")
                elif local == "list":
                    # If this list-item had text, indent sub-list one level deeper.
                    # If this list-item has NO text (it's just a wrapper), process the
                    # sub-list at the same indent level to avoid 4-space code-block traps.
                    self._process_list(child, indent + (1 if has_text else 0))

    def _finalize(self):
        """Clean up the markdown output."""
        text = "\n".join(self.lines)

        # Remove placeholder image markers that weren't properly handled
        text = re.sub(r"<<IMAGE:base64:[^>]+>>", "", text)

        # Remove non-printable ASCII control characters (except tab, newline, CR)
        # \x7f is DEL, \x00-\x08 and \x0b-\x0c and \x0e-\x1f are control chars
        text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)

        # Remove unresolved cross-reference error messages
        text = re.sub(r",?\s*Error: Reference source not found", "", text)

        # Collapse multiple blank lines to max 2
        text = re.sub(r"\n{4,}", "\n\n\n", text)

        # Strip trailing whitespace from lines
        lines = [line.rstrip() for line in text.split("\n")]
        text = "\n".join(lines)

        # Ensure file ends with newline
        text = text.strip() + "\n"

        return text


def convert_file(fodt_path, output_dir):
    """Convert a single FODT file to Markdown."""
    fodt_path = Path(fodt_path)
    output_dir = Path(output_dir)

    # Determine output markdown path
    rel = fodt_path.relative_to(fodt_path.parent)
    md_name = fodt_path.stem + ".md"

    md_path = output_dir / md_name
    images_dir = output_dir / "images"

    converter = FODTConverter(fodt_path, images_dir)
    markdown = converter.convert()

    md_path.parent.mkdir(parents=True, exist_ok=True)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    return md_path


def main():
    repo_root = Path(__file__).parent
    parts_dir = repo_root / "parts"
    markdown_dir = repo_root / "markdown"

    # Find all FODT files
    fodt_files = sorted(parts_dir.rglob("*.fodt"))
    print(f"Found {len(fodt_files)} FODT files")

    total = len(fodt_files)
    errors = []

    for i, fodt_path in enumerate(fodt_files):
        # Compute relative path from parts/ to mirror structure
        rel_path = fodt_path.relative_to(parts_dir)
        md_rel = rel_path.with_suffix(".md")

        out_dir = markdown_dir / md_rel.parent
        out_file = markdown_dir / md_rel

        # Determine the top-level category for shared images directory
        # chapters/* and chapters/sections/* and chapters/subsections/* -> chapters/images
        # appendices/* -> appendices/images
        # other -> images
        rel_parts = md_rel.parts
        if len(rel_parts) >= 2 and rel_parts[0] == "chapters":
            images_dir = markdown_dir / "chapters" / "images"
            md_base_dir = markdown_dir / "chapters"
        elif len(rel_parts) >= 2 and rel_parts[0] == "appendices":
            images_dir = markdown_dir / "appendices" / "images"
            md_base_dir = markdown_dir / "appendices"
        else:
            images_dir = out_dir / "images"
            md_base_dir = out_dir

        try:
            converter = FODTConverter(fodt_path, images_dir, md_dir=md_base_dir)
            markdown = converter.convert()

            out_file.parent.mkdir(parents=True, exist_ok=True)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(markdown)

            if (i + 1) % 100 == 0 or i == 0:
                print(f"  [{i + 1}/{total}] Converted: {rel_path}")
        except Exception as e:
            errors.append((str(rel_path), str(e)))
            print(f"  [{i + 1}/{total}] ERROR: {rel_path}: {e}")

    print(f"\nDone! Converted {total - len(errors)}/{total} files.")
    if errors:
        print(f"\n{len(errors)} errors:")
        for path, err in errors:
            print(f"  {path}: {err}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
