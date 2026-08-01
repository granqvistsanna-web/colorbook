#!/usr/bin/env python3
"""Regenerate colors.js from the COLOURBOOK PDF.

Usage: python3 scripts/extract.py "/path/to/COLOURBOOK-V1.0_2026.pdf"
Requires: pdftotext (brew install poppler)
"""
import json, re, subprocess, sys, pathlib

PDF = sys.argv[1] if len(sys.argv) > 1 else \
    "/Users/sannagranqvist/Library/Mobile Documents/com~apple~CloudDocs/Resources/COLOURBOOK/COLOURBOOK-V1.0_2026.pdf"
OUT = pathlib.Path(__file__).parent.parent / "colors.js"

# Section divider pages carry the titles; ranges are the palette pages between them.
SECTIONS = [("Neutrals", 7, 11), ("Fresh", 13, 21), ("Vibrant", 23, 48), ("Bold", 50, 74),
            ("Muted", 76, 103), ("Earthy", 105, 126), ("Elegant", 128, 147), ("Playful", 149, 175),
            ("Heritage", 177, 182), ("Retro", 184, 191), ("Clash", 193, 205), ("Corporate", 207, 229)]

MAX_COLORS = 30  # ponytail: pages above this are tint-scale/index spreads, not palettes

text = subprocess.run(["pdftotext", PDF, "-"], capture_output=True, text=True, check=True).stdout
pages = text.split("\f")

def section_of(n):
    return next((s for s, a, b in SECTIONS if a <= n <= b), None)

palettes, counters = [], {}
for i, p in enumerate(pages, 1):
    sec = section_of(i)
    if not sec:
        continue
    hexes = []
    for h in re.findall(r"#([0-9A-Fa-f]{6})", p):
        h = "#" + h.upper()
        if h not in hexes:
            hexes.append(h)
    if not hexes or len(hexes) > MAX_COLORS:
        continue
    name = next((l.strip() for l in p.splitlines()
                 if l.strip() and not re.search(r"[#\d]", l) and "COLOURBOOK" not in l.upper()), None)
    counters[sec] = counters.get(sec, 0) + 1
    palettes.append({"page": i, "section": sec,
                     "name": name or f"{sec} {counters[sec]:02d}", "colors": hexes})

OUT.write_text("// Generated from COLOURBOOK PDF — regenerate with scripts/extract.py\n"
               "const PALETTES = " + json.dumps(palettes, indent=2) + ";\n")
print(f"{len(palettes)} palettes, {sum(len(p['colors']) for p in palettes)} colors -> {OUT}")
