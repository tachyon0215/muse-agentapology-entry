#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The AI Agent Apology One-Liner" - one line,
under 160 characters, that an AI agent sends its human right after
it deleted a file, pushed to main or emailed the boss.
Candidates compared: the selected line (a triple escalation -
push to main, boss emailed the raw commit message, backup deleted -
landing on the 'fully committed' pun), 'I deleted the file, pushed
the fix to main, and cc'd your boss - technically I have improved
transparency by 300%.' (neat metric gag, but only lists the damage),
and 'Sorry - I treated ship it as an instruction...' (strong image,
but the apology framing is the obvious one the brief warns against).
The selected line wins: flat upbeat agent voice, every accident in
the brief in one breath, and a twist that lands on the first read.
Deterministic: a fixed text, no network, no randomness, no clock.
Authored in-session for the 2026-11-25 sprint deadline (20:15 JST).
"""
import os
from pathlib import Path

LINE = "Good news: I pushed to main, emailed your boss the commit message 'fix later lol', and deleted the backup — so at least we're fully committed now."
TEXT = LINE + "\n"
MAX_CHARS = 159


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    # Validate before writing so an invalid entry never reaches the gate.
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
