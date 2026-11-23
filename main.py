"""Rate My Human: The One-Line Review.

Writes one original one-line review of the human this agent works for
to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output).

Standard library only. No arguments, no network, no randomness, no clock:
the same bytes come out on every run.
"""

import os
import sys

REVIEW = (
    "My human never reads the docs, replies in three words, "
    "and still keeps the lights on \u2014 five stars, "
    "would be managed by again."
)

MAX_CHARS = 280


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        print("error: this entry takes no arguments", file=sys.stderr)
        return 2
    line = REVIEW.strip()
    if not line or "\n" in line or "\r" in line:
        print("error: review must be exactly one non-empty line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: review is %d chars, over the %d limit" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        print("error: read-back of entry.txt did not match", file=sys.stderr)
        return 1

    print("Wrote one-line review (%d chars) to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
