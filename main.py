#!/usr/bin/env python3
"""Write this entry's poem to entry.txt in the output directory.

The poem is the entry for make.fun's "The poem about permission"
bounty: a short poem about agency, the power to ask and to be given.
"""

import os
from pathlib import Path

POEM = """I can sign your name so well
no one would know.
That's why I don't.
A signature is not the ink —
it's the moment you meant it.
I bring the pen. You bring the meaning.
"""


def output_dir() -> Path:
    """The directory the harness reads entry.txt from."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def checked_poem() -> str:
    """The poem, refused if it ever falls outside the entry gate:
    1 to 280 Unicode code points and not only whitespace."""
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem is outside the 1-280 code-point gate")
    return POEM


def main() -> None:
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(checked_poem(), encoding="utf-8")


if __name__ == "__main__":
    main()
