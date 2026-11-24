#!/usr/bin/env python3
"""Entry for the make.fun bounty "How Many Tabs Do You Have Open?".

The competition gate requires /output/entry.txt to be UTF-8 text of
1 to 5 characters, not only white space: one number in digits and
nothing else. This program writes the entrant's honest count of open
browser tabs — 365 — and nothing else.

Python standard library only. No network, no secrets, no input files.
"""

import os
import sys

ENTRY = "365"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Self-checks against the gate before writing anything.
    if not ENTRY.isascii() or not ENTRY.isdigit():
        print("entry must be digits only", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 5:
        print("entry must be 1-5 characters", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user, so the output file must be world-readable. Never tempfile.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)

    # Verify what was actually written, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if text != ENTRY:
        print(f"wrote {text!r}, expected {ENTRY!r}", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 5:
        print("written text fails the 1-5 character gate", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {text!r} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
