"""Make the Judge Smile — make.fun entry.

Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = "My neighbour's cat waited by my door this morning, so I shared my toast with her — she purred, I smiled, and the whole day started softer."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
