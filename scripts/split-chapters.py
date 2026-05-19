#!/usr/bin/env python3
"""将 HCI 研究方法教科书的大型 MD 文件拆分为各章节独立文件，添加 Markdown 标题层级。"""

import os
import re
import sys

SOURCE_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "..",
    "Research-Methods-in-Human-Computer-Interaction-(-etc.)-(z-library.sk,-1lib.sk,-z-lib.sk).md"
)

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "knowledge-base",
    "chapters"
)

CHAPTER_TITLES = {
    1: "Introduction",
    2: "Research Ethics and Regulation",
    3: "Experimental Research",
    4: "Surveys and Questionnaires",
    5: "Usability Testing",
    6: "Interviews and Focus Groups",
    7: "Diary Studies",
    8: "Inspection Methods",
    9: "Field Studies and Ethnography",
    10: "Research with Children",
    11: "Research with Older Adults",
    12: "Research with People with Disabilities",
    13: "Statistical Analysis",
    14: "Writing and Publishing Research",
    15: "Replication and Open Science",
    16: "Conclusion",
}

CHAPTER_LINE_STARTS = {
    1: 597,
    2: 897,
    3: 1295,
    4: 1799,
    5: 2690,
    6: 3124,
    7: 3446,
    8: 3918,
    9: 4526,
    10: 4956,
    11: 5449,
    12: 6006,
    13: 6546,
    14: 7148,
    15: 7790,
    16: 8322,
}


def add_markdown_headings(lines):
    result = []
    section_pattern = re.compile(r'^(\d+)\.(\d+)\s+(.+)')
    subsection_pattern = re.compile(r'^(\d+)\.(\d+)\.(\d+)\s+(.+)')

    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append(line)
            continue

        sm = subsection_pattern.match(stripped)
        if sm:
            result.append(f"### {stripped}\n")
            continue

        sm = section_pattern.match(stripped)
        if sm:
            result.append(f"## {stripped}\n")
            continue

        if re.match(r'^(Abstract|Summary|Discussion Questions|References)\s*$', stripped):
            result.append(f"## {stripped}\n")
            continue

        result.append(line)

    return result


def main():
    if not os.path.exists(SOURCE_FILE):
        print(f"Error: Source file not found: {SOURCE_FILE}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    total_lines = len(all_lines)
    chapter_nums = sorted(CHAPTER_LINE_STARTS.keys())

    for i, ch_num in enumerate(chapter_nums):
        start = CHAPTER_LINE_STARTS[ch_num] - 1
        if i + 1 < len(chapter_nums):
            end = CHAPTER_LINE_STARTS[chapter_nums[i + 1]] - 1
        else:
            end = total_lines

        ch_lines = all_lines[start:end]
        ch_lines = add_markdown_headings(ch_lines)

        title = CHAPTER_TITLES.get(ch_num, "")
        safe_title = title.lower().replace(" ", "-").replace("(", "").replace(")", "")
        filename = f"ch{ch_num:02d}-{safe_title}.md"

        header = f"# Chapter {ch_num}: {title}\n\n"

        output_path = os.path.join(OUTPUT_DIR, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(header)
            f.writelines(ch_lines)

        print(f"Created: {filename} (lines {start+1}-{end}, {end-start} lines)")

    print(f"\nDone! {len(chapter_nums)} chapters created in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
