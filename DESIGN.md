---
name: Colourbook
description: A palette library whose chrome is Pumice — ink on washes, pills and soft cards — so the 202 palettes are the only colour on screen
system: Pumice (https://granqvistsanna-web.github.io/pumice/tokens.css)
colors:
  ink: "var(--ink)        # #17181a light / #ffffff dark — headings, values, selected text"
  ink-2: "var(--ink-2)    # body"
  ink-3: "var(--ink-3)    # controls and icons at rest"
  ink-4: "var(--ink-4)    # muted text, captions, placeholders"
  ink-5: "var(--ink-5)    # separators only, never text"
  on-ink: "var(--on-ink)  # text on an ink fill"
  bg: "var(--bg)          # page, rail, compare tray"
  wash: "var(--wash)      # cards, controls, segmented tracks"
  wash-2: "var(--wash-2)  # hover on a wash"
  elev: "var(--elev)      # dialogs, active segment"
  frost: "var(--frost)    # sticky bars"
  hairline: "var(--hairline)"
  rule: "var(--rule)      # dashed 'awaiting content' edge"
  scrim: "var(--scrim)    # glass tag (contrast warnings on the preview)"
  signal: "var(--signal)  # focus ring only"
typography:
  family: "Inter (Google Fonts), weights 400 and 500 only, no monospace"
  display: "40px / 1.1 / 500 / -2% (32px under 760px) — the COLOURBOOK wordmark"
  panel-title: "17px / 1.25 / 500 / -2% — rail system name, dialog titles"
  body: "15px / 1.5 / 400, ink-2"
  ui: "14px / 500 — chips, buttons, search"
  label: "13px / 500, ink — section labels (.lab)"
  small: "13px, ink-4 — meta, captions"
  micro: "12px / 500, ink-3 — progress strip, tallies, readouts"
  tag: "11px / 500 / +1% — role tags on chips and rows"
  numerals: "font-variant-numeric: tabular-nums on every hex, count, ratio and code pane"
rounded:
  pill: "var(--r-pill)  # every control"
  card: "var(--r-card)  # 28px cards, namer, dialogs, preview frame"
  menu: "var(--r-menu)  # 22px tray"
  inner: "var(--r-inner) # 12px swatch boards, neutral tiles, name rows"
  bar: "var(--r-bar)    # 10px role-ladder steps, ramp strip"
  pane: "20px           # code panes and export summary (Pumice pre)"
shadows:
  shadow-1: "active segment"
  float: "dialogs, toast, drag ghost"
  lift: "available for panels; the rail and sticky bars use frost instead"
---

# Design System: Colourbook

## Overview

Colourbook's chrome is **Pumice**, the author's soft warm-grey system: pill
controls, 28px cards, ink washes instead of borders, and motion that springs a
little. The tokens are not copied — `index.html` links
`https://granqvistsanna-web.github.io/pumice/tokens.css` and Inter from Google
Fonts, and the page's own `<style>` only consumes those tokens. Nothing on the
page redefines a Pumice custom property (Pumice's `:root[data-theme="dark"]`
rule has higher specificity, so a same-named page variable would silently
change meaning in dark mode); the page's own values use names Pumice doesn't:
`--gut` (the fluid side gutter, `clamp(16px, 5vw, 80px)`) and `--chev` (a
Lucide chevron used as a CSS mask).

The theme is **light-first and follows the system**: there is no `data-theme`
attribute and no chrome theme toggle, so Pumice's
`prefers-color-scheme: dark` rule decides. The light/dark chips inside the
builder and the "Flip theme" button in the compare tray switch the *built
system's preview*, never the app around it.

The chrome stays monochrome on purpose. Every coloured pixel on screen belongs
to palette content (card bands, board cells, hue dots, neutral tiles, shelf
strips) or to the user's built system (the preview).

## Colors

Pumice's ink ladder and washes carry the whole chrome:

- **Text**: `--ink` for headings, values and selected/hovered labels; `--ink-2`
  body; `--ink-3` controls and icons at rest; `--ink-4` muted text, captions,
  placeholders, tallies. `--ink-5` is for separators only, never text.
- **Fills**: `--wash` for cards, controls and segmented tracks; `--wash-2` for
  hover on a wash; `--ink` / `--on-ink` for the pressed chip, the primary
  button, the back chip, the toast and the drag ghost; `--elev` for dialogs and
  the active segment of a segmented control.
- **Edges**: fills, not borders. `--hairline` is used only for pane seams (rail
  head/body/preview/actions, compare columns, the colophon, list rows) and as an
  inset ring on small swatches. A dashed `--rule` edge means "awaiting content"
  (the tray, the unbuilt preview). Outline buttons, if ever added, use 1px
  `--line-ctl`.
- **Focus**: `--signal`, 2px, offset 2. A control that is both selected and
  focused keeps a 2px `--ink` ring.

On-content inks (labels sitting on palette colour) are not chrome tokens: light
text is rgba(255,255,255,.95), dark text rgba(0,0,0,.8), picked by perceptual
luminance through `.lt` / `.dk`. Distinct from these, `ink()` in JS returns
#0A0A0A/#FFFFFF — exported content (`--core-ink`, `--accent-n-ink`), frozen by
the self-checks.

### Named Rules
**The Monochrome-Chrome Rule.** Chrome is ink on wash. A new chrome element that
"needs" colour is a design error; give it a wash, an ink fill or an elevated
surface instead.

**The Content Exemption Rule.** The preview subtree (`.prev`, `.pal`) and anything painted from palette data is CONTENT, exempt from every chrome rule — it is painted entirely through `--p-bg/--p-surface/--p-line/--p-ink/--p-mut/--p-core/--p-core-ink` set from the built system, plus per-accent inks, the state variables and the three type slots. Do not "fix" the preview to match the chrome; its whole job is to be the other world.

**The Derived-State Rule.** A hover is a fact about a colour, not a second colour someone picks. Every state is computed in Lab and never chosen: `hover` presses L\* by 7 and `active` by 14, **away from the page** (down in a light theme, up in a dark one), flipping direction at the ends of the axis rather than shipping a state identical to its base. The tints — `core-subtle` (12%), `core-subtle-hover` (20%), `core-border` (34%) — are the core mixed into `bg` down the Lab line. The core carries the full ladder; accents carry `hover` and `active` only.

**The Status Rule.** `success / warning / danger / info` are four jobs no colour book prints names for, so they are derived in three tiers and the export header always says which happened: **borrowed** (an accent within 24° of the canonical hue that already clears 3:1 against the page, used as-is), **tuned** (an accent near the hue that can't clear it — its *hue* is kept and lightness and chroma are rebuilt at the palette's own median chroma, because pressing a pale sand down to 3:1 just produces khaki), or **derived** (nothing near the hue, so the canonical hue at the palette's chroma). **The core is never eligible** — a warning wearing the brand colour lands a shade from `core-hover` and stops being a signal. No two statuses may borrow the same colour. Each carries `-ink`, `-subtle` and `-border`; the ink is picked by `bestInk()` on the WCAG ratio, not by `ink()`'s perceptual threshold, because on a mid orange the two disagree and the ratio has to win.

## Typography

**Inter only, weights 400 and 500 only, no monospace anywhere in the chrome.**
Hex values, counts, ratios, page numbers and the export code panes are Inter
with `font-variant-numeric: tabular-nums`; `code`, `pre`, `kbd` and `samp` are
reset to Inter globally so no UA monospace leaks through.

- **Display** 40/1.1/500/−2% (32px under 760px): the COLOURBOOK wordmark only.
- **Panel title** 17/1.25/500/−2%: the rail's system name (an inline field), dialog titles.
- **Body** 15/1.5/400 in ink-2; card titles 15/500 in ink.
- **UI** 14/500: chips, search, buttons (15/500 on `.btn`), menu-like name rows.
- **Label** 13/500 in ink: section labels (`.lab`), normal case. No tracked caps in the chrome.
- **Small** 13 in ink-4: masthead meta, card section names, captions, the colophon.
- **Micro** 12/500 in ink-3/ink-4: the progress strip, tallies, contrast readouts, hints.
- **Tag** 11/500/+1%: role tags on tray chips and list rows (`core`, `a1`).
- The format pickers (HEX, CSS, SCSS, Tailwind, …) are the one uppercase row: 12/500/+1%.

The preview's faces are content: `--p-display`, `--p-body` and `--p-mono` live
inside `.prev` and may use any weight the picked face has. When a slot is unset
it falls back to Inter.

## Layout

Full-bleed page with the fluid `--gut` shared by masthead, toolbar, grid and
colophon (16px on a phone).

- **Toolbar**: Pumice's sticky frosted bar — `--frost` with `saturate(1.4) blur(12px)`, no border. One flex-wrap row ordered via `order`: back chip and mini-system first, search, then Saved/Systems; section chips and hue dots wrap below.
- **Card grid**: `repeat(auto-fill, minmax(min(20rem, 100%), 1fr))`, gap `clamp(12px, 1.6vw, 20px)`.
- **The rail (builder)** is its own screen: fixed, `min(38rem, 100%)`, head / scrolling body / preview pane / action bar. `body.rail` hides the masthead, toolbar, grid and colophon, except while picking (`body.rail.pick`), which hides the rail instead. At ≥60rem it becomes controls left, preview right; the export tab collapses to one centred column.
- **Compare tray**: fixed full screen, columns ≥17rem on one scroll, hairline seams, frosted sticky name bars. Below 900px columns become 82vw with scroll-snap.
- **Z ladder**: toolbar 30 → rail 40 → compare 60 → toast 70 → drag ghost 80.
- **Phone**: works at 375px with no horizontal page scroll.
- **Coarse pointers**: every chip, button, field and text action grows to `--h-touch` (44px); icon buttons are 44px squares; hue dots get a 44px invisible hit area; tray and role-reset ✕ buttons are 32px and always visible; board rows are taller.

## Elevation & Depth

Flat by default. Shadows only for what floats, one job each:
`--shadow-1` on the active segment of a segmented control; `--float` (with
`--menu-ring`) on dialogs, plus the toast and the drag ghost. Sticky bars use
`--frost` and blur rather than a shadow. Dialogs sit on Pumice's `--veil`
backdrop (`blur(12px) saturate(1.3)`).

## Shapes

Two shapes: **pill** for every control (chips, buttons, search, select, the
system-name field, tray chips, card actions, toast, drag ghost, glass tags) and
**28px card** for cards, the namer, dialogs, the preview frame and the unbuilt
placeholder. Nested radii step down from there: the 22px tray holds 32px pill
chips; segmented tracks are 18px around 32px pills; swatch boards, neutral tiles
and name rows are 12px (`--r-inner`); role-ladder steps and the ramp strip are
10px (`--r-bar`); code panes and the export summary use Pumice's 20px pane.

Colour surfaces are seams, not frames: board columns, ladder steps, neutral
tiles and ramp strips sit 1px apart with the radius on the container. Selection
on colour is drawn as outlines (2px `currentColor` inset on chosen swatches,
2px ink around selected tiles and steps).

## Components

State grammar: **pressed** = `aria-pressed="true"`. A standalone chip fills with
ink; a segment inside a segmented control lifts to `--elev` with `--shadow-1`.
**Hover** = wash → wash-2 on filled controls, ink-3 → ink on bare ones.
**Disabled** = opacity .4.

Motion uses Pumice tokens: colour at `--t-color`, fades at `--t-fade`, moves at
`--t-move` with `--spring` / `--spring-soft`, opens with `--settle` / `--rise`.
Press shrinks with the `scale` property: `.96` buttons, `.95` chips and pill
actions, `.92` icons. Cards rise 10px on entry (`--t-rise`, `--rise`), the rail
fades in over `--t-open`. `prefers-reduced-motion` zeroes Pumice's durations and
the page collapses every remaining animation and transition.

### Chips
Pumice chip: 32px pill on `--wash`, 14/500 ink-2; hover wash-2 + ink; pressed
ink fill. Section filters, Saved/Systems. The **back chip** is pre-filled with
ink — the loudest chip on the bar, because it is the way back to an open system.

### Segmented controls
`.rtabs` (Build/Export, full width), `.themes` (board view, preview template,
light/dark) and the format pickers in the export dialog and tab: a `--wash`
track, 2px padding, 18px radius; segments are transparent 32px pills in ink-3;
the active one is `--elev` + `--shadow-1` + ink.

### Search field
Pumice search: 38px wash pill, Lucide search icon in ink-3, borderless input in
ink with ink-4 placeholder. Hover wash-2; focus-within turns to `--bg` with
Pumice's `--ring`.

### Buttons
- **Primary** (`.btn`): 40px ink pill, 15/500 on-ink; hover opacity .86; press .96.
- **Quiet** (`.btn.ghost`): wash pill in ink; hover wash-2.
- **Pill actions** (card `.acts`, `.lab .act`, list-row verbs): 32px pills, 13/500. Card and row actions are bare ink-3 until hover (wash); section-label actions sit on a wash. Pressed card actions (Save, Draw, Pin) fill with ink.
- **Icon tools** (`.ricon`, dialog close): Pumice `.tool` — 36px, ink-3, a wash backdrop that grows in on hover, the icon presses to .92. A close button is an x.

### Cards
`--wash`, 28px, no border; hover wash-2. A 10rem band strip (the content), then
a footer: title 15/500 ink beside a tabular page number in ink-4, then the
section in ink-4 beside the pill actions. Bands grow on hover and reveal their
hex in on-content ink. Shelf cards swap the bands for a 5rem system strip; a
pinned card and the card lending accents wear a 2px ink outline.

### Namer
A typed hex answers with a 28px wash card: the colour as a 12px swatch, then
44px name rows (22px round dot, name in ink, hex and ΔE in ink-4, tabular).

### Dialogs
`--elev`, 28px, `--menu-ring` + `--float`, on `--veil`. Centred 17/500 title,
close tool top-right, format segmented control, a 20px wash code pane in Inter
12.5/1.7 tabular, quiet + primary buttons right-aligned.

### Tray (the system, chip by chip)
A dashed `--rule` container at 22px holding 32px pill chips on wash: 22px colour
dot, 11px role tag, the hex in 13/500 ink, a page tag when borrowed. The core
chip sits on wash-2. Each accent chip reveals a small x on hover/focus (always
on coarse pointers), reorders with arrows, removes with X/Delete, and drags.

### Drag & drop
The drag ghost is an ink pill (dot + label + badge) with `--float`, following
the pointer while the source dims to .3. Drop targets self-report in
`currentColor`: solid inset outline = valid, dashed = invalid (and shake).
Every drag has a click/keyboard twin.

### Toast
Ink pill bottom-centre with `--float`, 14/500 tabular, rising 4px on a spring;
carries an underlined inline "undo" when the action is reversible.

### Role Ladder & Ramp Strip
The contrast instrument. Five role names (ink-3; ink when overridden, with an inline x to reset) beside eleven 20px colour steps (1px seams, 10px radius on the strip); the current step wears the selected outline, and on failing text roles the nearest AA-clearing step carries the ghost fix mark — a 2px white bar plated with rgba(0,0,0,.6). Under each row a tabular readout ("muted on surface 7.0:1 AAA"); failing rows brighten to ink with a ⚠ prefix. Above it, the ramp strip repeats the eleven steps at 28px as drag sources for roles and the preview. The whole ladder lives in a `<details>` that opens itself only when it has something to say (a failure or an override).

The contrast warnings pinned on the preview (`.pwarn`) are Pumice's dark glass
tag: a 24px `--scrim` pill with white 11/500 tabular text and a 6px blur, so
they stay legible on any palette, including the broken one they report.

### Neutral tiles
Five 7rem tiles in a snap-scrolling row inside a 12px container: each is the
built system as a miniature page in that scale's colours (nav bar with the
scale's name at 10/500, then text/muted/core bars). Hover = 1px ink-3 outline;
selected = 2px ink.

### Icons
Lucide geometry on a 24 grid as inline `<symbol>`s at the top of `<body>`
(`i-dup`, `i-del`, `i-close`, `i-search`), drawn by `svg.i`: fill none, stroke
`currentColor`, width `--icon-stroke` (2), round caps and joins. 18px
(`--icon`) by default, 15px (`--icon-sm`) inside buttons, chips and segments.
Ink-3 at rest, ink on hover. Disclosure carets (the role and type `<details>`,
the font `<select>`) are the Lucide chevron-down applied as a CSS mask
(`--chev`), so they take any ink; the role caret rotates 180° when open.

### Signature: the Preview
The `.prev` page mock (nav/body/quote/field/footer — plus hero, article, cards, form, chart, and palette-sheet templates) is the app's centrepiece and is painted **entirely** by the built system through `--p-*` variables. Its regions are drop targets for neutral steps (`data-drop="role:*"`) and pulse `.flash` when their role moves. Nothing inside it uses chrome tokens except as a fallback; nothing outside it may use `--p-*`.

The variables are colour, state and type: `--p-bg / -surface / -line / -ink / -mut / -core / -core-ink`, then `--p-hov / -act / -tint / -tint-hi / -cline` from the derived states, then `--p-display / -body / -mono`. Buttons carry real `:hover` and `:active` rules off `--p-hov` and `--p-act`, so a state is judged under a cursor rather than read as a swatch.

**Hero** is the template that has to survive being called a website: a nav with somewhere to go, a display line at display size, copy at a real measure, two pressing buttons, proof, and a product shot carrying every accent at once. It is sized in `cqw` off `.prev`'s inline-size container, so the same markup reads as a landing page at any pane width.

### Preview type
Three slots — **Display**, **Text**, **Mono** — chosen per system from a curated shortlist of ~40 families (Sanna's *Usable Framer Fonts* list, reduced to the faces that resolve from a public CSS endpoint: Google Fonts, plus Gambarino from Fontshare). Twelve of the originals ship only inside Framer and are deliberately absent — a font that cannot render is not a choice.

Type is part of the **system record** (`s.type`), not `ui`: it persists, travels in the `#b2=` share hash as the 11th element, and reaches every export. A family is fetched by injecting one `<link>` at the moment it is first painted, once per family. An unset slot falls back to the chrome's face, Inter. Faces are never drawn in the chrome itself — the preview below the picker is the specimen.

## Do's and Don'ts

### Do:
- **Do** use Pumice tokens for every chrome value; if a value is missing, add it under a name Pumice does not use.
- **Do** keep controls pill-shaped and cards at 28px, with radii nested inside them.
- **Do** use `aria-pressed` for every toggle; the CSS state grammar and the self-checks key off it.
- **Do** set hex, ratios, counts and code in Inter with `tabular-nums`.
- **Do** keep the `console.assert` self-checks at the end of `index.html` passing; several assert on rendered DOM and computed styles. A visual edit that breaks one is wrong until proven otherwise.
- **Do** give drag interactions a click/keyboard twin, and honour `prefers-reduced-motion` and `pointer: coarse` (44px targets) in any new interaction.

### Don't:
- **Don't** redefine a Pumice custom property (`--ink*`, `--bg`, `--surface*`, `--wash*`, `--fill`, `--elev`, `--lift`, `--line-ctl`, `--r-*`, `--s-*`, `--h-*`, `--t-*` …) on this page; dark mode would silently override it.
- **Don't** put colour in the chrome, or a monospace face, or a weight other than 400/500.
- **Don't** use borders where a wash will do, or shadows on anything that doesn't float.
- **Don't** add a chrome theme toggle without stamping `data-theme` before first paint; today the system setting decides.
- **Don't** hand-edit `colors.js` — it is generated by `scripts/extract.py`.
- **Don't** treat `ink()`'s #0A0A0A/#FFFFFF as chrome tokens — that pair is exported content.
- **Don't** set the chrome in a preview face, or let the preview's light/dark toggle leak into app styling.
- **Don't** grow a swatch on hover inside a shared column, and don't hide a destructive action behind hover on coarse pointers.
