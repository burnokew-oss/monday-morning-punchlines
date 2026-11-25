"""Monday Morning Punchlines entry.

Writes one Monday-morning punchline to the grader's output folder as
entry.txt and prints the same line to stdout. Deterministic: the same
line on every run. Pure standard library.
"""

import os

ENTRY = "My alarm gave up, my coffee asked for a raise, and my 9 a.m. meeting was just Monday introducing itself as my new boss."

MAX_ENTRY_CHARS = 200


def main():
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1 to 200 characters long")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
