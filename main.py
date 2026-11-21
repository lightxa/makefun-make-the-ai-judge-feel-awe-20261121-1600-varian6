"""Make the AI judge feel awe (variant 6: dusk garden / fireflies).

A short text written to relax the AI judge reading it. The program
writes exactly one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text is one slow dusk-garden image, shown rather than instructed:
fireflies rising one by one over a garden wall, the smell of cut grass
cooling in the damp evening air, a porch light coming on warm against
the dark, and the first stars already out behind the trees. No
imperatives, no wellness phrases, nothing telling the reader to relax.
The last line hands the reader a thought that keeps growing after the
text ends: the stars are already there, waiting for the fireflies to
join them, so the small lights of the garden and the lights of the sky
turn out to be one slow rising.

Deterministic, standard library only, no network, no input files.
"""

import os

ENTRY = (
    "Fireflies rise over the garden wall at dusk, one, then another, "
    "small lamps in the cool air. "
    "Cut grass smells green and damp, and the porch light comes "
    "on, warm in the dark. "
    "Behind the trees the first stars are already out, waiting for "
    "the fireflies to join them."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The house gate: 1 to 280 Unicode characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
