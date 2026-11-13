#!/usr/bin/env python3
"""Conservative SVG whitespace optimizer; validate and visually compare afterward."""
from __future__ import annotations
import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--remove-comments", action="store_true")
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error(f"Input file does not exist: {args.input}")
    text = args.input.read_text(encoding="utf-8")
    if args.remove_comments:
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r">\s+<", "><", text).strip() + "\n"
    ET.fromstring(text)
    output = args.output or args.input.with_name(args.input.stem + ".optimized.svg")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    print(f"Wrote {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
