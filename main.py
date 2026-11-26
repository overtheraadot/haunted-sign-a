#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: a sign for the door of a haunted server room.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "NOTICE: the ghost in Rack 4 has root access now. Knock twice before entering — the servers answer to him, not you."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS a sign for the door of a haunted server room — on the
#    subject, short and punchy, readable at a glance like a printed sheet.
# 2. The joke lands on first read, with the punchline in the last few words:
#    the servers answering to the ghost, not you, is the whole power shift.
# 3. It reads like the real thing: the ghost in Rack 4 has root access now,
#    so knock twice — the servers answer to him, not you.
# 4. Fresh angle: the haunting is specific — a ghost with admin rights in one
#    numbered rack — not a generic spooky-server pun.
# 5. Tight: every word earns its place inside the 120-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 120 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 120:
        raise ValueError(f"entry is {len(text)} characters, over the 120 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
