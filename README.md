# Colourbook

A filterable library of all 202 palettes from COLOURBOOK-V1.0_2026.pdf.

**Use it:** open `index.html` in a browser (double-click works), or `python3 -m http.server` for a local server.

- Click a color band → copies the hex. Copy → whole palette. Export → HEX / CSS / SCSS / Tailwind / JSON, copy or download.
- Filter by section chip, hue dot, or search (name, section, hex). ♥ Saved palettes persist in the browser (localStorage).

**New book version?** `python3 scripts/extract.py "/path/to/COLOURBOOK.pdf"` regenerates `colors.js`. Update the section page ranges in the script if the book's layout changes.
