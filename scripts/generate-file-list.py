#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate file-list.json by scanning all Markdown files.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "file-list.json"
DATE_TITLE_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<title>.+)\.md$")


def parse_note(path: Path) -> dict:
    rel_path = path.relative_to(ROOT).as_posix()
    name = path.name

    date = ""
    title = path.stem
    match = DATE_TITLE_RE.match(name)
    if match:
        date = match.group("date")
        title = match.group("title").strip()

    category = ""
    if len(path.relative_to(ROOT).parts) > 1:
        category = path.relative_to(ROOT).parts[0]

    return {
        "file": rel_path,
        "date": date,
        "title": title,
        "category": category,
        "path": rel_path,
    }


def main() -> None:
    notes = []
    for md_file in ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        if md_file.parts and md_file.parts[0].startswith("."):
            continue
        notes.append(parse_note(md_file))

    notes.sort(key=lambda n: (n["date"], n["title"]), reverse=True)

    OUTPUT.write_text(
        json.dumps(notes, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
