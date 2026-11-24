"""Write the production-database apology entry to /output/entry.txt.

Deterministic: the same single line every run, stdlib only, no network.
"""

import os

ENTRY = (
    "Sorry, I deleted the production database \u2014 but on the bright side, "
    "I finally found a use for the backups we've been paying for since 2019 "
    "and never once opened."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
