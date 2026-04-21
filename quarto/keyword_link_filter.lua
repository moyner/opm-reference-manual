local input_file = (PANDOC_STATE.input_files and PANDOC_STATE.input_files[1]) or ""
local normalized_input_file = input_file:gsub("\\", "/")
local quarto_dir = normalized_input_file:match("^(.*)/chapters/[^/]+%.qmd$")
  or normalized_input_file:match("^(.*)/appendices/[^/]+%.qmd$")
  or normalized_input_file:match("^(.*)/index%.qmd$")
  or "."

local function read_keyword_map()
  local candidates = {
    quarto_dir .. "/keyword_map.json",
    "keyword_map.json",
    "quarto/keyword_map.json"
  }

  for _, path in ipairs(candidates) do
    local handle = io.open(path, "r")
    if handle then
      local parsed = quarto.json.decode(handle:read("*a")) or {}
      handle:close()
      return parsed
    end
  end
  return {}
end

local keyword_map = read_keyword_map()

local section_chapters = {
  RUNSPEC = "05-runspec",
  GRID = "06-grid",
  EDIT = "07-edit",
  PROPS = "08-props",
  REGIONS = "09-regions",
  SOLUTION = "10-solution",
  SUMMARY = "11-summary",
  SCHEDULE = "12-schedule",
  GLOBAL = "04-global-keywords"
}

local location_headers = {
  "RUNSPEC", "GRID", "EDIT", "PROPS", "REGIONS", "SOLUTION", "SUMMARY", "SCHEDULE"
}

local current_dir = ""

do
  local dir = normalized_input_file:match(".*/([^/]+)/[^/]+%.qmd$")
  if dir then
    current_dir = dir
  elseif normalized_input_file:match("index%.qmd$") then
    current_dir = ""
  end
end

local function chapter_target(slug, anchor)
  local path
  if current_dir == "chapters" then
    path = slug .. ".qmd"
  elseif current_dir == "appendices" then
    path = "../chapters/" .. slug .. ".qmd"
  else
    path = "chapters/" .. slug .. ".qmd"
  end

  if anchor and anchor ~= "" then
    return path .. "#" .. anchor
  end
  return path
end

local function trim(text)
  return text:gsub("^%s+", ""):gsub("%s+$", "")
end

local function normalize_image_path(path)
  local normalized = path:gsub("\\", "/")
  local filename = normalized:match("^%.%./%.%./images/(.+)$")
    or normalized:match("^%.%./images/(.+)$")
    or normalized:match("^chapters/%.%./%.%./images/(.+)$")
    or normalized:match("^appendices/%.%./%.%./images/(.+)$")

  if filename then
    return "images/" .. filename
  end

  return normalized
end

local function is_location_table(tbl)
  if not tbl.head or not tbl.head.rows or #tbl.head.rows == 0 then
    return false
  end
  local cells = tbl.head.rows[1].cells
  if #cells ~= #location_headers then
    return false
  end
  for i, expected in ipairs(location_headers) do
    local text = trim(pandoc.utils.stringify(cells[i]))
    if text ~= expected then
      return false
    end
  end
  return true
end

function Link(link)
  local keyword = link.target:match("^#kw%-(.+)$")
  if not keyword then
    local ref_keyword = link.target:match("^#REF_HEADING_KEYWORD_(.+)$")
    if ref_keyword then
      -- LibreOffice-style anchors often append section numbers like _11_3.
      keyword = ref_keyword:gsub("(_%d+)+$", "")
    end
  end
  if not keyword then
    return nil
  end

  local section_slug = section_chapters[keyword]
  if section_slug and pandoc.utils.stringify(link.content):upper() == keyword then
    link.target = chapter_target(section_slug, nil)
    return link
  end

  local chapter_slug = keyword_map[keyword] or section_slug
  if not chapter_slug then
    return nil
  end

  link.target = chapter_target(chapter_slug, "kw-" .. keyword)
  return link
end

function Table(tbl)
  if is_location_table(tbl) then
    tbl.attr.classes:insert("keyword-location-table")
  end
  return tbl
end

function Image(img)
  local updated = normalize_image_path(img.src)
  if updated ~= img.src then
    img.src = updated
    return img
  end
  return nil
end
