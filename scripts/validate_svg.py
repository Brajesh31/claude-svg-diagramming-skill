#!/usr/bin/env python3
"""Lightweight SVG structural validator. Not a sanitizer or full security audit."""
from __future__ import annotations
import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

XLINK_HREF = "{http://www.w3.org/1999/xlink}href"

def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]

def validate(path: Path):
    errors, warnings = [], []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        return [f"Cannot parse XML: {exc}"], warnings
    if local_name(root.tag) != "svg":
        return ["Root element is not <svg>."], warnings
    if not root.attrib.get("viewBox"):
        warnings.append("Missing viewBox; responsive scaling may be limited.")
    ids, duplicates, refs = set(), set(), set()
    has_title = has_desc = False
    for node in root.iter():
        tag = local_name(node.tag)
        has_title |= tag == "title"
        has_desc |= tag == "desc"
        node_id = node.attrib.get("id")
        if node_id:
            if node_id in ids:
                duplicates.add(node_id)
            ids.add(node_id)
        for attr in ("href", XLINK_HREF):
            value = node.attrib.get(attr, "")
            if value.startswith("#"):
                refs.add(value[1:])
        for attr, value in node.attrib.items():
            cursor = 0
            while True:
                start = value.find("url(#", cursor)
                if start < 0:
                    break
                end = value.find(")", start)
                if end < 0:
                    break
                refs.add(value[start + 5:end])
                cursor = end + 1
            if value.strip().lower().startswith(("http://", "https://", "//")):
                warnings.append(f"External reference: {value[:100]}")
            if attr.lower().startswith("on"):
                warnings.append(f"Event-handler attribute found: {attr}")
        if tag == "script":
            warnings.append("Embedded <script> found; inspect before using untrusted SVG.")
    errors.extend(f"Duplicate id: {x}" for x in sorted(duplicates))
    errors.extend(f"Unresolved local reference: #{x}" for x in sorted(refs - ids))
    if not has_title:
        warnings.append("No <title> element found.")
    if not has_desc:
        warnings.append("No <desc> element found; add one for complex diagrams.")
    return errors, sorted(set(warnings))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="SVG files or directories")
    args = parser.parse_args()
    files = []
    for path in args.paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.svg")))
        elif path.is_file() and path.suffix.lower() == ".svg":
            files.append(path)
    if not files:
        print("No SVG files found.", file=sys.stderr)
        return 2
    failed = 0
    for path in files:
        errors, warnings = validate(path)
        print(f"\n{path}")
        for item in warnings:
            print(f"  WARNING: {item}")
        for item in errors:
            print(f"  ERROR: {item}")
        if errors:
            failed += 1
        else:
            print("  OK")
    print(f"\nChecked {len(files)} SVG file(s); {failed} failed.")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
