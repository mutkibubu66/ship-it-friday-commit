#!/usr/bin/env python3
"""Ship It Friday — make.fun entry.

Writes one line — the funniest git commit message an AI coding agent writes
right before breaking production on a Friday — to /output/entry.txt.
Pure Python standard library; no network, no dependencies.
"""

import os

ENTRY = (
    "fix: quick Friday tweak before the weekend, definitely tested, "
    "definitely not about to take down prod "
    "(updating my r\u00e9sum\u00e9 just in case)"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate is 1-159"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and re-verify: the file on disk must hold exactly our line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == ENTRY, "written file does not match the entry"
    assert len(on_disk) == len(ENTRY), "char count changed on disk"
    assert on_disk.count("\n") == 0, "entry file must hold exactly one line"

    print(f"Wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
