#!/usr/bin/env python3
"""Locate literal text in a file and print stable path:line references."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search one file for one or more literal strings."
    )
    parser.add_argument("--file", required=True, help="File to search.")
    parser.add_argument(
        "--find",
        action="append",
        dest="patterns",
        required=True,
        help="Literal text to search for. Repeat for multiple patterns.",
    )
    parser.add_argument(
        "--ignore-case",
        action="store_true",
        help="Match without case sensitivity.",
    )
    return parser.parse_args()


def normalize(text: str, ignore_case: bool) -> str:
    return text.lower() if ignore_case else text


def find_matches(path: Path, patterns: list[str], ignore_case: bool) -> int:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"ERROR missing file: {path}", file=sys.stderr)
        return 2
    except UnicodeDecodeError:
        print(f"ERROR unable to decode as utf-8: {path}", file=sys.stderr)
        return 2

    normalized_patterns = [(pattern, normalize(pattern, ignore_case)) for pattern in patterns]
    matches = 0

    for line_number, line in enumerate(lines, start=1):
        normalized_line = normalize(line, ignore_case)
        for original_pattern, normalized_pattern in normalized_patterns:
            if normalized_pattern in normalized_line:
                matches += 1
                print(f"MATCH {path}:{line_number} | find={original_pattern!r} | text={line.strip()}")

    if matches == 0:
        print(f"NO_MATCH {path}", file=sys.stderr)
        return 1

    return 0


def main() -> int:
    args = parse_args()
    return find_matches(Path(args.file), args.patterns, args.ignore_case)


if __name__ == "__main__":
    raise SystemExit(main())
