# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

One user: the author, working solo. She opens Colourbook while designing a site
or product and needs a colour scheme — either browsing for a starting palette or
turning one she has chosen into a brand system she can paste into a project as
code.

The site is published publicly on GitHub Pages, but strangers are not an
audience. Nothing should be designed for onboarding, explaining, or converting a
first-time visitor.

## Product Purpose

Make all 202 palettes from the author's own COLOURBOOK V1.0 (2026) usable at
working speed, instead of scrolling a PDF. Two jobs, in order:

1. **Find** — filter 202 palettes by section, hue, free text, saved, or built;
   copy a hex or a whole palette.
2. **Build** — turn one palette into a brand system the way the book's pp. 4–5
   describe, then export it as code.

Success is a scheme leaving the tool as `--core` / `--accent-n` / `--neutral-n`
and landing in a real project. Browsing that ends in nothing is not success.

## Positioning

Colourbook is the companion tool to the author's own book, so it can encode that
book's specific method rather than generic colour theory: pick a CORE, toggle
further swatches to ACCENT, the rest are eliminated, then attach one of the five
Neutrals scales. A general palette site can offer neither this book's exact 202
palettes nor its elimination method.

## Operating Context

- Opened in a browser. Live at `https://granqvistsanna-web.github.io/colorbook/`,
  published from the `colorbook-app` branch; also run locally.
- Saved palettes and builds live in `localStorage` in one browser. No account, no
  sync, no server. Clearing the browser clears the work.
- A build is shared or moved between machines by URL hash
  (`#b=<page>,<core>,<accents…>,<neutral>[,d]`), which applies once and then
  cleans itself out of the URL.
- When the book gets a new version, `python3 scripts/extract.py <pdf>`
  regenerates `colors.js`. Section page ranges are hand-maintained in that script
  and must be updated when the book's layout changes.

## Capabilities and Constraints

Confirmed capabilities: section / hue / search / saved / built filtering; copy a
hex or a palette; export in hex, CSS, SCSS, Tailwind (v3 config and a v4
`@theme` block), a paste-in Framer sheet, JSON, and W3C design tokens — each
grouped as primitives, roles, derived states and status; build a system (core,
any number of accents, one of five Neutrals scales, and a display/text/mono
typeface from a curated shortlist); light and dark theme; live preview of the
built system across seven templates, its buttons pressing the real hover and
active shades; shareable build links carrying colour, roles, order and type;
contrast-aware label and `core-ink` colours; hand-maintained **brand-study
palettes** (`brands.js` — Klarna, Stripe, ICA, Bolt, Netflix and ~30 others) in
one **Brands** section that browses, builds and exports exactly like the book's
pages; each entry records whether its hexes are officially published (✅) or
reference values (≈).

Durable constraints:

- **No runtime dependencies, and nothing at load.** The app opens cold: Geist and
  Geist Mono are self-hosted in `fonts/`, icons are inline. The one thing that
  reaches the network is a **preview typeface the user picked** — a `<link>` to
  Google Fonts or Fontshare, injected at the moment of the pick, once per family,
  never on load and never for a system that has no type set. That exception is
  the whole of it: the chrome's own faces stay self-hosted, and nothing else may
  be added to the list.
- **`colors.js` is generated, never authored.** `scripts/extract.py` is the only
  source of truth for the book's palette data. Hand-edits are lost on the next
  regeneration. `brands.js` is the one authored exception: hand-maintained brand
  palettes (documented brand colours only, synthetic page ids ≥ 900), merged at
  load and never written into `colors.js`.
- **Every Neutrals scale is exactly 11 steps, dark → light, in identical
  positions.** The dark theme is those role indices mirrored; role mapping breaks
  if that ever stops holding.
- **No backend and no accounts** — state is per-browser only.

Explicitly *not* constraints (asked and declined): staying a single file, and
opening from `file://` by double-click. A build step, split files, or a server
are all allowed if the work warrants one.

## Brand Commitments

- Name: **Colourbook**, British spelling, matching the book. Version line
  "V1.0 — 2026" refers to the book, not the app.
- The book is the naming and method authority. Its vocabulary — core, accent,
  neutral, *eliminated* — is the app's vocabulary.

## Evidence on Hand

- The book itself: `COLOURBOOK-V1.0_2026.pdf` (path recorded in
  `scripts/extract.py`), authored by the user.
- 202 real palettes across 12 sections in `colors.js`, extracted from it.
- The live GitHub Pages deployment.

Nothing else exists. There are no users besides the author, no testimonials,
customers, traffic figures, benchmarks, pricing, or licensing — future work must
not invent any of them, and there is no audience to address with them.

## Product Principles

1. **The book wins.** Where the app and COLOURBOOK disagree on method or naming,
   the book is right and the app is a bug.
2. **Data is derived, never authored.** Palettes come from the PDF through
   `extract.py`; the app reads them and never becomes their source.
3. **Built for one person who already knows how it works.** No onboarding, no
   explanatory chrome, no first-run tour — speed for a returning expert instead.
4. **Paste-ready or it didn't happen.** The tool's job ends at code in a real
   project, so export fidelity and format coverage outrank anything decorative.
5. **Nothing loaded from a network at load.** The only fetch the app ever makes
   is the typeface a user chose for a preview, at the moment they choose it.
