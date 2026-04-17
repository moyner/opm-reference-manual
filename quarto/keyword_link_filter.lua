local json_file = io.open("keyword_map.json", "r")
local keyword_map = {}
if json_file then
  keyword_map = quarto.json.decode(json_file:read("*a")) or {}
  json_file:close()
end

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

local input_file = (PANDOC_STATE.input_files and PANDOC_STATE.input_files[1]) or ""
local current_dir = ""
local current_slug = ""

do
  local dir, file = input_file:match(".*/([^/]+)/([^/]+)%.qmd$")
  if dir and file then
    current_dir = dir
    current_slug = file
  elseif input_file:match("index%.qmd$") then
    current_dir = ""
    current_slug = "index"
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

local function is_location_table(tbl)
  if not tbl.head or not tbl.head.rows or #tbl.head.rows == 0 then
    return false
  end
  local cells = tbl.head.rows[1].cells
  if #cells ~= #location_headers then
    return false
  end
  for i, expected in ipairs(location_headers) do
    local text = pandoc.utils.stringify(cells[i]):gsub("^%s+", ""):gsub("%s+$", "")
    if text ~= expected then
      return false
    end
  end
  return true
end

function Link(link)
  local keyword = link.target:match("^#kw%-(.+)$")
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
