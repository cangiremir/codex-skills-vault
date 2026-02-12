#!/usr/bin/env python3
"""Generate a codex/<unit-slug> branch name from a unit title."""

import re
import sys


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "unit"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: slugify_unit.py <unit title>")
        return 1
    title = " ".join(sys.argv[1:])
    slug = slugify(title)
    print(f"codex/{slug}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
