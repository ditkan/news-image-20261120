#!/usr/bin/env python3
"""Entry point for the news-image-20261120 submission.

The front page itself is drawn ahead of time by render.py and stored in
this repository as entry.png. All this program does is copy that picture
into the output directory the grader points at, using nothing beyond the
Python standard library, so both grading runs produce identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    size = os.path.getsize(target)
    if size != os.path.getsize(SOURCE):
        print("copy size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
