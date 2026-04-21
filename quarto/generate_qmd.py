#!/usr/bin/env python3
"""Generate Quarto .qmd wrapper files by scanning the markdown directory.

This script creates chapter and appendix .qmd files that use Quarto's
{{< include >}} directive to pull in the actual markdown content.
Re-run this script whenever new keyword files are added.
"""

import sys
import json
import shutil
from pathlib import Path

QUARTO_DIR = Path(__file__).resolve().parent
MARKDOWN_DIR = QUARTO_DIR.parent / "markdown"
CHAPTERS_DIR = QUARTO_DIR / "chapters"
APPENDICES_DIR = QUARTO_DIR / "appendices"

CHAPTER_TITLES = {
    1: "Introduction",
    2: "Installing and Running Flow",
    3: "Keyword Documentation Structure",
    4: "Global Section Keywords",
    5: "RUNSPEC Section",
    6: "GRID Section",
    7: "EDIT Section",
    8: "PROPS Section",
    9: "REGIONS Section",
    10: "SOLUTION Section",
    11: "SUMMARY Section",
    12: "SCHEDULE Section",
}

CHAPTER_SLUGS = {
    1: "01-introduction",
    2: "02-installation",
    3: "03-keyword-structure",
    4: "04-global-keywords",
    5: "05-runspec",
    6: "06-grid",
    7: "07-edit",
    8: "08-props",
    9: "09-regions",
    10: "10-solution",
    11: "11-summary",
    12: "12-schedule",
}

APPENDIX_TITLES = {
    "A": "Keyword Summary",
    "B": "Release Notes",
    "C": "OPMRUN",
    "D": "Python Interface",
    "E": "Command Line Options",
    "F": "Output File Formats",
}

APPENDIX_SLUGS = {
    "A": "A-keyword-summary",
    "B": "B-release-notes",
    "C": "C-opmrun",
    "D": "D-python",
    "E": "E-command-line",
    "F": "F-output-formats",
}

# Chapters that have keyword subsections (N.2 data requirements + N.3 keywords)
KEYWORD_CHAPTERS = range(4, 13)


def get_keyword_files(chapter_num: int) -> list[str]:
    """Return sorted list of keyword .md filenames for a chapter's subsections."""
    subsection_dir = MARKDOWN_DIR / "chapters" / "subsections" / f"{chapter_num}.3"
    if not subsection_dir.is_dir():
        return []
    keywords = []
    for f in subsection_dir.iterdir():
        if f.suffix == ".md" and f.name != ".md":
            keywords.append(f.name)
    return sorted(keywords)


def has_data_requirements(chapter_num: int) -> bool:
    """Check if a chapter has a section N/2.md (Data Requirements)."""
    section_file = MARKDOWN_DIR / "chapters" / "sections" / str(chapter_num) / "2.md"
    return section_file.is_file()


def generate_chapter_qmd(chapter_num: int) -> str:
    """Generate the content of a chapter .qmd file."""
    # Include paths are relative to the .qmd file location (quarto/chapters/)
    include_base = "../../markdown/chapters"

    lines = [
        f"{{{{< include {include_base}/{chapter_num}.md >}}}}",
        "",
    ]

    if chapter_num in KEYWORD_CHAPTERS:
        # Include data requirements section if it exists
        if has_data_requirements(chapter_num):
            lines.append(
                f"{{{{< include {include_base}/sections/{chapter_num}/2.md >}}}}"
            )
            lines.append("")

        # Include keyword files alphabetically
        keywords = get_keyword_files(chapter_num)
        if keywords:
            lines.append("## Keyword Definitions")
            lines.append("")
            for kw in keywords:
                keyword = Path(kw).stem
                lines.append(f"::: {{#kw-{keyword}}}")
                lines.append(
                    f"{{{{< include {include_base}/subsections/{chapter_num}.3/{kw} >}}}}"
                )
                lines.append(":::")
                lines.append("")

    return "\n".join(lines)


def generate_appendix_qmd(letter: str) -> str:
    """Generate the content of an appendix .qmd file."""
    title = APPENDIX_TITLES[letter]
    # Include paths are relative to the .qmd file location (quarto/appendices/)
    include_path = f"../../markdown/appendices/{letter}.md"

    lines = [
        "---",
        f'title: "{title}"',
        "---",
        "",
        f"{{{{< include {include_path} >}}}}",
        "",
    ]
    return "\n".join(lines)


def generate_index_qmd() -> str:
    """Generate the index.qmd title page."""
    return """---
title: "OPM Flow Reference Manual"
subtitle: "2025-04"
---

![](images/Image46_409be8acca21.png){fig-align="center" width="40%"}

## About This Manual

The **OPM Flow Reference Manual** provides comprehensive documentation for the
Open Porous Media (OPM) Flow reservoir simulator. OPM Flow is a fully-implicit,
black-oil and compositional reservoir simulator capable of running industry-standard
simulation models.

This manual covers:

- **Installation and Setup** -- How to install and run OPM Flow
- **Keyword Reference** -- Complete documentation of all supported keywords organized
  by input deck section (GLOBAL, RUNSPEC, GRID, EDIT, PROPS, REGIONS, SOLUTION,
  SUMMARY, SCHEDULE)
- **Appendices** -- Keyword summaries, release notes, the OPMRUN graphical interface,
  Python scripting interface, command line options, and output file formats

### How to Use This Manual

Use the table of contents or the search bar to navigate to specific keywords or topics.
Keywords are organized by their input deck section, matching the structure of OPM Flow
simulation input files.

> **Note:** This manual corresponds to **OPM Flow version 2025-04**.
"""


def generate_keyword_map() -> dict[str, str]:
    """Generate keyword-to-chapter-slug map."""
    keyword_map = {}
    for num in KEYWORD_CHAPTERS:
        slug = CHAPTER_SLUGS[num]
        for kw_file in get_keyword_files(num):
            keyword = Path(kw_file).stem
            keyword_map[keyword] = slug
    return keyword_map


def generate_quarto_yml() -> str:
    """Generate the _quarto.yml configuration file with explicit chapter/appendix titles."""
    chapter_entries = ["    - index.qmd"]
    for num in range(1, 13):
        slug = CHAPTER_SLUGS[num]
        title = CHAPTER_TITLES[num]
        chapter_entries.append(f'    - text: "{title}"')
        chapter_entries.append(f'      href: chapters/{slug}.qmd')

    appendix_entries = []
    for letter in ["A", "B", "C", "D", "E", "F"]:
        slug = APPENDIX_SLUGS[letter]
        title = APPENDIX_TITLES[letter]
        appendix_entries.append(f'    - text: "{title}"')
        appendix_entries.append(f'      href: appendices/{slug}.qmd')

    chapters_block = "\n".join(chapter_entries)
    appendices_block = "\n".join(appendix_entries)

    return f"""project:
  type: book
  output-dir: _book
  pre-render: python3 generate_qmd.py
from: markdown+fenced_divs
filters:
  - keyword_link_filter.lua

book:
  title: "OPM Flow Reference Manual"
  subtitle: "2025-04"
  author: "Open Porous Media"
  date: "2025"
  search: true
  repo-url: https://github.com/OPM/opm-reference-manual
  chapters:
{chapters_block}
  appendices:
{appendices_block}

format:
  html:
    theme:
      light: cosmo
    css: styles.css
    code-fold: true
    toc: true
    toc-depth: 3
    number-sections: true
    smooth-scroll: true
    link-external-newwindow: true
  pdf:
    documentclass: scrreprt
    number-sections: true
    toc: true
    toc-depth: 2
    colorlinks: true
    keep-tex: false
    geometry:
      - margin=1in
    include-in-header:
      text: |
        \\usepackage{{fvextra}}
        \\DefineVerbatimEnvironment{{Highlighting}}{{Verbatim}}{{breaklines,commandchars=\\\\\\{{\\}}}}
"""


def main():
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    APPENDICES_DIR.mkdir(parents=True, exist_ok=True)

    def copy_tree(src: Path, dst: Path):
        if not src.is_dir():
            print(f"Skipping missing {src.relative_to(QUARTO_DIR.parent)}")
            return
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        elif dst.is_dir():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"Copied {src.relative_to(QUARTO_DIR.parent)} -> {dst.relative_to(QUARTO_DIR)}")

    def merge_tree(src: Path, dst: Path):
        if not src.is_dir():
            print(f"Skipping missing {src.relative_to(QUARTO_DIR.parent)}")
            return
        dst.mkdir(parents=True, exist_ok=True)
        for path in src.rglob("*"):
            rel = path.relative_to(src)
            target = dst / rel
            if path.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
        print(f"Merged {src.relative_to(QUARTO_DIR.parent)} -> {dst.relative_to(QUARTO_DIR)}")

    # Copy image directories so builds also work on platforms without symlink support.
    chapters_images = MARKDOWN_DIR / "chapters" / "images"
    appendices_images = MARKDOWN_DIR / "appendices" / "images"
    root_images = MARKDOWN_DIR / "images"

    copy_tree(chapters_images, CHAPTERS_DIR / "images")
    copy_tree(appendices_images, APPENDICES_DIR / "images")

    # Also populate quarto/images so legacy ../../images paths in included markdown
    # continue to resolve correctly during render.
    copy_tree(root_images, QUARTO_DIR / "images")
    merge_tree(chapters_images, QUARTO_DIR / "images")
    merge_tree(appendices_images, QUARTO_DIR / "images")

    # Generate keyword map for Quarto link rewriting filter
    keyword_map_path = QUARTO_DIR / "keyword_map.json"
    keyword_map_path.write_text(
        json.dumps(generate_keyword_map(), sort_keys=True, indent=2) + "\n"
    )
    print(f"Generated {keyword_map_path.relative_to(QUARTO_DIR)}")

    # Generate _quarto.yml with explicit chapter/appendix titles
    quarto_yml_path = QUARTO_DIR / "_quarto.yml"
    quarto_yml_path.write_text(generate_quarto_yml())
    print(f"Generated {quarto_yml_path.relative_to(QUARTO_DIR)}")

    # Generate index.qmd
    index_path = QUARTO_DIR / "index.qmd"
    index_path.write_text(generate_index_qmd())
    print(f"Generated {index_path.relative_to(QUARTO_DIR)}")

    # Generate chapter files
    for num in range(1, 13):
        slug = CHAPTER_SLUGS[num]
        filepath = CHAPTERS_DIR / f"{slug}.qmd"
        content = generate_chapter_qmd(num)
        filepath.write_text(content)
        keyword_count = len(get_keyword_files(num)) if num in KEYWORD_CHAPTERS else 0
        extra = f" ({keyword_count} keywords)" if keyword_count else ""
        print(f"Generated chapters/{slug}.qmd{extra}")

    # Generate appendix files
    for letter in ["A", "B", "C", "D", "E", "F"]:
        slug = APPENDIX_SLUGS[letter]
        filepath = APPENDICES_DIR / f"{slug}.qmd"
        content = generate_appendix_qmd(letter)
        filepath.write_text(content)
        print(f"Generated appendices/{slug}.qmd")

    print(f"\nDone! Generated {12 + 6 + 1} files + _quarto.yml.")


if __name__ == "__main__":
    main()
