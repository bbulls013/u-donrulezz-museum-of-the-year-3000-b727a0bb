#!/usr/bin/env python3
"""Museum of the Year 3000 entry.

Writes one museum label line to entry.txt in the output directory.
The grader mounts the output directory at /output and names it in
MAKEFUN_OUTPUT_DIR; locally that variable points at a scratch folder.
"""

import os

LABEL = (
    "The Gate of Proving, c. 2025. To enter any archive, ancestors first "
    "had to persuade a machine that they were not a machine. Many failed, "
    "and waited outside with the robots."
)


def main() -> None:
    # The gate accepts 1 to 200 UTF-8 characters on one line; fail loudly
    # here rather than ship a label the scorer would refuse.
    assert 1 <= len(LABEL) <= 200, len(LABEL)
    assert "\n" not in LABEL
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LABEL)


if __name__ == "__main__":
    main()
