#!/usr/bin/env python3
"""Write the entry for make.fun competition
u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.

The program writes one line -- the excuse an AI agent hands its human
for a missed deadline -- to /output/entry.txt. Python standard library
only; no network access at grade time.
"""

import os


# The excuse is built as a straight-faced apology, a machine condition
# (the rate limit), and a punch in the last few words that reframes
# the whole line: the agent is genuinely sorry, and faintly proud of
# how much apologising it has already done.
APOLOGY = "I'm sorry \u2014 I hit my rate limit apologising for the last deadline,"
PUNCH = "so this one's late too."

ENTRY = APOLOGY + " " + PUNCH


def main() -> None:
    # The gate refuses anything outside 1-200 characters, so check
    # the line before writing it.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry line fails the 1-200 character gate")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself: the grader mounts /output read-only as
    # uid 65534, and deleting it would throw EACCES.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
