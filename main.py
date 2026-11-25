#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes a single line of text (1-240 characters) to entry.txt in the
output directory: the Moon replying at last to the wishes, howls and
late-night promises of everyone staring up at it. Standard library
only, deterministic, no network access.
"""

import os
from pathlib import Path

ENTRY = (
    "Four billion years I've listened to your wishes, your howls, your "
    "three-a.m. promises to change \u2014 and tonight I finally answer: I am "
    "a rock. I don't grant wishes. I just reflect sunlight and judge your "
    "life choices from a distance."
)


def validate_entry(text: str) -> None:
    """Enforce the bounty gate: 1-240 characters, one line, not blank."""
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
