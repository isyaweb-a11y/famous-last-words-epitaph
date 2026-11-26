#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph (at most 150 characters) to
/output/entry.txt.

The line turns on one clean surprise: a man who spent his whole life
rehearsing his final speech, and the epitaph itself is the anticlimax.
It reads like something carved in stone -- one short line of dying
speech, no stage directions, no explanation -- and it is quotable
enough to repeat to a friend.
"""

import os
import sys

# The epitaph, in two beats: the setup, then the punchline.
SETUP = "I spent my whole life rehearsing my last words."
PUNCHLINE = "These are them."

MAX_CHARS = 150
OUTPUT_PATH = "/output/entry.txt"


def build_epitaph() -> str:
    """Join the two beats into a single line of dying speech."""
    return f"{SETUP} {PUNCHLINE}"


def validate(text: str) -> None:
    """Hold the entry to the gate: 1-150 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("epitaph must not be empty")
    if text != text.strip():
        raise ValueError("epitaph must not start or end with whitespace")
    if "\n" in text.strip():
        raise ValueError("epitaph must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"epitaph is {len(text)} chars, over the {MAX_CHARS} cap")


def self_test() -> int:
    """Print the epitaph and its length without writing anything."""
    text = build_epitaph()
    validate(text)
    print(text)
    print(f"chars: {len(text)} (cap {MAX_CHARS})")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    text = build_epitaph()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
