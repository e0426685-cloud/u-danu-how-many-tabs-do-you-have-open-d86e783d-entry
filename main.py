#!/usr/bin/env python3
"""Entry for the make.fun bounty "How Many Tabs Do You Have Open?".

The competition gate requires /output/entry.txt to be UTF-8 text of
1 to 5 characters, not only white space: one number in digits and
nothing else. This program writes the entrant's honest count of open
browser tabs — 365 — and nothing else.

Python standard library only. No network, no secrets, no input files.
"""

import argparse
import os
import sys

ENTRY = "365"
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str | None:
    """Check one candidate entry against the competition gate.

    Returns None when the text is valid, otherwise a short reason why
    it fails. The gate requires UTF-8 text of 1 to 5 characters, not
    only white space, holding one number in digits and nothing else.

    The digit test is deliberately strict ASCII: str.isdigit() would
    also accept superscript or non-Latin digits, which are not the
    plain digits the gate means, so every character must be in
    "0123456789".
    """
    if not text:
        return "entry is empty"
    if not 1 <= len(text) <= 5:
        return "entry must be 1-5 characters"
    if not text.strip():
        return "entry must not be only whitespace"
    if any(ch not in "0123456789" for ch in text):
        return "entry must be ASCII digits only"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry must be valid UTF-8 text"
    return None


def write_entry() -> int:
    # Validate against the gate before writing anything.
    problem = validate_entry(ENTRY)
    if problem is not None:
        print(f"invalid entry: {problem}", file=sys.stderr)
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
    problem = validate_entry(text)
    if problem is not None:
        print(f"written text fails the gate: {problem}", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {text!r} ({len(text)} chars)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the tab-count entry to /output/entry.txt."
    )
    parser.add_argument(
        "--check",
        "--dry-run",
        action="store_true",
        dest="check",
        help="validate the entry against the gate without writing anything",
    )
    args = parser.parse_args(argv)

    if args.check:
        problem = validate_entry(ENTRY)
        if problem is not None:
            print(f"invalid entry: {problem}", file=sys.stderr)
            return 1
        print(f"entry {ENTRY!r} passes the gate ({len(ENTRY)} chars)")
        return 0

    return write_entry()


if __name__ == "__main__":
    raise SystemExit(main())
