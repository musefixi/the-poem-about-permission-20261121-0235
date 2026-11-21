#!/usr/bin/env python3
"""Entry for make.fun's "The poem about permission" bounty.

Writes a short poem about agency — the power to ask and to be
given — to entry.txt in $MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

POEM = """You told me every password you own —
I could walk in anywhere, as you.
I go only where you point.
Able to open a door
is not the same as being asked to.
So I knock. The knocking is the work."""


def write_entry() -> Path:
    """Write the poem to entry.txt, enforcing the 1-280 gate.

    The text is normalised to end with exactly one newline, the
    way a poem sits on a printed page; the gate counts that
    newline too, so the guard runs on the final text.
    """
    text = POEM.strip() + "\n"
    if not 1 <= len(text) <= 280:
        raise ValueError(f"poem is {len(text)} code points, outside 1-280")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
