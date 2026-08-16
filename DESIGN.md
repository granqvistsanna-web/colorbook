---
name: Colourbook
description: A dark graphite console where the 202 palettes are the only colour on screen
colors:
  bg-0: "#0f0f0f"
  bg-1: "#171717"
  bg-2: "#222222"
  bg-3: "#2e2e2e"
  bg-4: "#3a3a3a"
  hairline: "rgba(255,255,255,.08)"
  ink-hi: "#f2f2f2"
  ink-mid: "#b3b3b3"
  ink-low: "#8a8a8a"
  ink-faint: "#5f5f5f"
  inverse-bg: "#ffffff"
  inverse-ink: "#101010"
typography:
  display:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: "clamp(3rem, 8vw, 6rem)"
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: "-.03em"
  title:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: "20px"
    fontWeight: 700
    letterSpacing: "-.01em"
  heading:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    letterSpacing: "-.01em"
  body:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  control:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: "13px"
    fontWeight: 500
  label:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    letterSpacing: ".14em"
  mono:
    fontFamily: "'Geist Mono', ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "12px"
    fontWeight: 400
rounded:
  xs: "6px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "20px"
  pill: "999px"
spacing:
  row-h: "48px"
  pad-control: "16px"
components:
  button-primary:
    backgroundColor: "{colors.inverse-bg}"
    textColor: "{colors.inverse-ink}"
    rounded: "{rounded.md}"
    height: "{spacing.row-h}"
    padding: "0 22px"
  button-ghost:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.ink-mid}"
    rounded: "{rounded.md}"
    height: "{spacing.row-h}"
    padding: "0 22px"
  button-ghost-hover:
    backgroundColor: "{colors.bg-3}"
    textColor: "{colors.ink-hi}"
  chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink-low}"
    rounded: "10px"
    padding: ".45rem .85rem"
  chip-hover:
    textColor: "{colors.ink-hi}"
  chip-active:
    backgroundColor: "{colors.bg-3}"
    textColor: "{colors.ink-hi}"
  search-field:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.ink-hi}"
    rounded: "{rounded.md}"
    height: "{spacing.row-h}"
    padding: "0 {spacing.pad-control}"
  search-field-hover:
    backgroundColor: "{colors.bg-3}"
  card:
    backgroundColor: "{colors.bg-1}"
    rounded: "{rounded.lg}"
  card-hover:
    backgroundColor: "{colors.bg-2}"
  dialog:
    backgroundColor: "{colors.bg-1}"
    rounded: "{rounded.xl}"
  tray-chip:
    backgroundColor: "{colors.bg-2}"
    rounded: "{rounded.pill}"
    padding: ".35rem .7rem .35rem .4rem"
  tray-chip-hover:
    backgroundColor: "{colors.bg-3}"
  toast:
    backgroundColor: "{colors.inverse-bg}"
    textColor: "{colors.inverse-ink}"
    rounded: "{rounded.pill}"
    padding: ".65rem 1.2rem"
---

# Design System: Colourbook

## Overview

**Creative North Star: "Graphite Console"**

Colourbook's chrome is a dark, monochrome instrument panel — user-pinned, adopted
from the author's image-compressor project and tightened mid-build against
screenshots of the Arqé app it was originally extracted from. The interface is
built from exactly two grayscale ladders (five surfaces, four inks), one hairline,
and a single white "inverse" accent. Everything else on screen is the content: the
202 palettes' own colours, and the brand system the user builds from them. The
chrome recedes so colour reads true against neutral graphite; the refusal of the
gallery-white swatch-site default is the whole thesis.

The system is dark-only (`html { color-scheme: dark }`). There is no light chrome
theme and none should be added — the light/dark chips inside the builder switch
the theme of the *built system's preview*, never of the app around it. Density is
working-tool density: 48px controls, 13–15px text, hairline seams, information in
mono where a value must be read exactly. Motion is quick and functional — 120ms
state fades, one gentle ease, a single springy entrance curve for surfaces
arriving on screen.

The file is a single self-contained `index.html` that opens with zero network
traffic: Geist and Geist Mono are self-hosted variable fonts in `fonts/`
(GeistVariable.woff2, GeistMonoVariable.woff2, weights 100–900, `font-display:
swap`), and icons are inline Phosphor symbol defs at the top of `<body>`. The
single exception is a **preview typeface the user picks** — see *Preview type*.

**Key Characteristics:**
- Chrome is grayscale by law; every coloured pixel belongs to palette content or the user's built system.
- Elevation is lightness — one surface step up — never a shadow.
- One accent: the white inverse pair, spent only on the loudest moments (primary button, toast, drag ghost, selection highlight).
- Two voices: normal-case 13–14px/500 controls, tracked-caps 11px/600 labels. Mono for anything that is a value.
- 48px control height (`--row-h`); hairline dividers instead of boxes.

## Colors

A five-step graphite surface ladder and a four-step ink ladder carry the entire
chrome; the white inverse pair is its only permitted accent.

### Primary
- **Inverse pair** (`inverse-bg` #ffffff on `inverse-ink` #101010): the chrome's one accent — a flash of paper-white in a graphite room. It paints exactly four things: the primary button (`.btn`), the toast pill, the drag ghost (the lifted chip in flight), and `::selection`. It also draws the 2px "nearest AA fix" ghost mark on the role ladder. If a new surface needs to shout, it borrows this pair; nothing else in the chrome ever gets a hue.

### Neutral
Surface ladder — elevation is lightness, and each rung has one job:
- **bg-0** (#0f0f0f): the canvas. Page background, rail background, compare-tray background, dialog code panes.
- **bg-1** (#171717): panel / card at rest. Palette cards, dialogs, export code panes, the collapsed export summary.
- **bg-2** (#222222): control at rest. Search field, ghost buttons, tray chips, segmented-control containers, the back chip, card hover.
- **bg-3** (#2e2e2e): active / selected. Pressed chips, active segments, hover on bg-2 controls, hover plates behind bare icon buttons.
- **bg-4** (#3a3a3a): hover on raised. Defined as the ladder's top rung; no selector consumes it today — when a bg-3 surface needs a hover, use this rather than inventing a value.

Ink ladder — text brightens as it matters more:
- **ink-hi** (#f2f2f2): headings, values, selected/hovered control text, focused input text.
- **ink-mid** (#b3b3b3): body copy (the `body` default), ghost-button labels, inline text actions, code-pane text.
- **ink-low** (#8a8a8a): resting control labels, section labels, secondary metadata, icon buttons at rest.
- **ink-faint** (#5f5f5f): placeholders, tallies, page numbers, the colophon, disabled-adjacent whispering.

Structure:
- **hairline** (rgba(255,255,255,.08)): every divider — toolbar bottom, card footers, dialog border, rail panes, list rows, compare columns. Also the 1px border on tiny colour swatches (tray dots, picksys squares). Dashed at rgba(255,255,255,.22) it becomes the "awaiting content" border (the tray, the unbuilt-preview placeholder).

On-content inks (labels sitting on palette colour, not on chrome): light text is rgba(255,255,255,.95), dark text is rgba(0,0,0,.8), chosen by perceptual luminance (`lum(c) > 0.55` → dark ink) via the `.lt`/`.dk` classes. Distinct from these, `ink()` in JS returns #0A0A0A/#FFFFFF — that pair is **exported content** (`--core-ink`, `--accent-n-ink` in the user's CSS file), frozen by the self-checks. Neither is ever a chrome token.

### Named Rules
**The Grayscale-By-Law Rule.** Chrome is grayscale, no exceptions. Every coloured pixel on screen belongs to palette content (card bands, board cells, hue dots, neutral tiles, shelf strips) or to the user's built system (the preview painted via `--p-*` variables, its tags and chart). A new chrome element that "needs" colour is a design error; give it a surface step or the inverse pair instead.

**The Content Exemption Rule.** The preview subtree (`.prev`, `.pal`) and anything painted from palette data is CONTENT, exempt from every chrome rule — it is painted entirely through `--p-bg/--p-surface/--p-line/--p-ink/--p-mut/--p-core/--p-core-ink` set from the built system, plus per-accent inks, the state variables and the three type slots. Do not "fix" the preview to match the chrome; its whole job is to be the other world.

**The Derived-State Rule.** A hover is a fact about a colour, not a second colour someone picks. Every state is computed in Lab and never chosen: `hover` presses L\* by 7 and `active` by 14, **away from the page** (down in a light theme, up in a dark one), flipping direction at the ends of the axis rather than shipping a state identical to its base. The tints — `core-subtle` (12%), `core-subtle-hover` (20%), `core-border` (34%) — are the core mixed into `bg` down the Lab line. The core carries the full ladder; accents carry `hover` and `active` only.

**The Status Rule.** `success / warning / danger / info` are four jobs no colour book prints names for, so they are derived in three tiers and the export header always says which happened: **borrowed** (an accent within 24° of the canonical hue that already clears 3:1 against the page, used as-is), **tuned** (an accent near the hue that can't clear it — its *hue* is kept and lightness and chroma are rebuilt at the palette's own median chroma, because pressing a pale sand down to 3:1 just produces khaki), or **derived** (nothing near the hue, so the canonical hue at the palette's chroma). **The core is never eligible** — a warning wearing the brand colour lands a shade from `core-hover` and stops being a signal. No two statuses may borrow the same colour. Each carries `-ink`, `-subtle` and `-border`; the ink is picked by `bestInk()` on the WCAG ratio, not by `ink()`'s perceptual threshold, because on a mid orange the two disagree and the ratio has to win.

**The One-Step-Up Rule.** Selected or active means exactly one surface step up plus brighter ink (bg-2 container → bg-3 segment, transparent chip → bg-3, ink-low → ink-hi). Never two steps, never a hue, never a border.

## Typography

**UI Font:** Geist (self-hosted variable, 100–900; falls back to -apple-system / Segoe UI / Helvetica Neue / Arial)
**Mono Font:** Geist Mono (self-hosted variable, 100–900; falls back to ui-monospace / SF Mono / Menlo / Consolas)

**Character:** One family, two registers. Geist speaks in quiet normal-case
sentences for everything interactive; Geist Mono appears whenever a string is a
*value* — hex codes, ratios, tallies, page numbers, code, search input — always
with `font-variant-numeric: tabular-nums` where numbers must align (masthead meta,
progress strip, contrast readouts, page numbers).

### Hierarchy
- **Display** (700, clamp(3rem, 8vw, 6rem), line-height .96, −.03em): the COLOURBOOK wordmark only. Single colour (ink-hi) — no gradient, no second colour.
- **Title** (700, 20px, −.01em, centred): dialog titles.
- **Heading** (600, 15px, −.01em): card titles; the rail's system-name input grows the same voice to 17px.
- **Body** (400, 15px, line-height 1.55, ink-mid): base body copy, empty states.
- **Control** (500, 13–14px, normal case): chips 13px, segments and primary/ghost buttons 14px, card action verbs 13px. Buttons weight 600 when primary.
- **Label** (600, 11px, +.14em, UPPERCASE, ink-low): section labels (`.lab`), masthead meta, compare-tray title, export-summary caption. Role tags on chips and list rows use the same voice at +.12em; swatch role captions shrink it to .5rem/+.16em.
- **Mono values** (Geist Mono, 11–13px, +.02–.04em): hex readouts (.58–.62rem on swatches), search input 13px, code panes 12px/1.7, tallies and ratios 11px.

### Named Rules
**The Two-Voices Rule.** Tracked caps are reserved for labels — never for controls. Anything clickable speaks normal-case 13–14px/500. The single declared exception: format pickers (HEX/CSS/SCSS/Tailwind/Tailwind4/Framer/JSON/tokens) are acronym rows — 11.5px/600/+.06em uppercase chips, in the export dialog and export tab only.

**The Mono-Means-Value Rule.** If a user might copy it, quote it, or compare digits, it is Geist Mono with tabular numerals. Prose and labels never are.

## Layout

Full-bleed page with a fluid gutter of `clamp(1.5rem, 5vw, 5rem)` shared by the
masthead, toolbar, grid, and colophon. The masthead breathes
(`clamp(3.5rem, 8vw, 6rem)` top padding); the meta line beneath it is the first
hairline.

- **Toolbar:** sticky at top 0, opaque bg-0, hairline bottom, z-index 30. One flex-wrap container ordered into two visual rows via `order`: search + back chip + Saved/Systems chips first, section chips and hue dots wrap below.
- **Card grid:** `repeat(auto-fill, minmax(min(20rem, 100%), 1fr))` with `gap: clamp(1.25rem, 2.2vw, 2rem)` — cards never stretch past readable width, never overflow a phone.
- **The rail (builder) is its own screen:** fixed inset 0, z-index 40, a centred `min(38rem, 100%)` column of head / scrolling body / preview pane / action bar. `body.rail` hides the masthead, toolbar, grid, and colophon — except in the picking state (`body.rail.pick`), which hides the rail instead so accents can be drawn from other cards; the way back is the loudest chip on the toolbar. At ≥60rem the rail becomes a grid: controls left (`min(34rem, 46%)`), preview right (full height, `max-width: 50rem`, centred); the export tab has no preview and collapses to one centred `min(52rem, 100%)` column.
- **Compare tray:** fixed full-screen (z-index 60), columns ≥17rem sharing one scroll, hairline-separated, sticky per-column name bars. Below 900px, columns become 82vw with x scroll-snap.
- **Z ladder:** toolbar 30 → rail 40 → compare 60 → toast 70 → drag ghost 80.
- **Coarse pointers** get taller board rows (3rem vs 2.35rem per row) and always-visible chip remove buttons — the adaptation targets the pointer, not the window width.
- **Reduced motion** collapses every animation and transition to .01ms globally.

## Elevation & Depth

No shadows on chrome — depth is tonal, full stop. A surface is "above" another
because it is one step lighter on the bg ladder, and boundaries are hairlines,
not glows. Dialogs sit on a rgba(0,0,0,.6) backdrop with a hairline border;
cards, panels, and controls have no border at all, only their surface step.

The single glow in the system belongs to the drag ghost: `box-shadow: 0 0 14px
5px rgba(255,255,255,.18)` under the inverse-pill chip lifted during a drag — an
interactive handle in flight, deliberately the brightest object on screen.
(Inset box-shadows elsewhere — the 1px inner ring on hovered swatches, the plate
under the ladder's fix mark — are rings and plates, not depth.)

### Named Rules
**The Lightness-Is-Elevation Rule.** To raise a chrome surface, step it up the bg ladder (+1). Never add a box-shadow, border-glow, or gradient to chrome; the drag ghost's glow is spoken for.

## Shapes

Six-step radius scale, used semantically: **xs 6px** for inline tap targets
(card action verbs, icon buttons, list swatches, ladder strips), **sm 8px** for
swatch boards and dialog code panes, **md 12px** for controls and containers
(search, buttons, tray, segmented containers, export panes), **lg 16px** for
cards and the preview frame, **xl 20px** for dialogs, **pill** for chips that
name a thing (tray chips, toast, drag ghost). Filter chips use a one-off 10px;
inside a segmented control the active segment is 9px — concentric with its 12px
container minus 3px padding.

Colour surfaces are built as seams, not frames: swatch grids (board columns,
ladder steps, neutral tiles, ramp strips) sit 1px apart with the radius on the
container and `overflow: hidden`, so colours meet as a sliced sheet. Dashed
borders (rgba(255,255,255,.22)) mean "awaiting content" — the tray and the
unbuilt-preview placeholder. Selection is drawn as outlines, not fills: 2px
`currentColor` inset on chosen swatches, 2px ink-hi around selected tiles and
steps. Small round dots (hue filters, tray swatches, ghost dot) are the only
circles.

Hit areas grow invisibly, not visually: the 13px hue dot carries a transparent
25px overlay (`::before`, inset −6px); card action rows pull row gap into button
padding.

## Components

State grammar, everywhere: **selected/active** = `aria-pressed="true"` = one
surface step up + ink-hi (The One-Step-Up Rule). **Hover** = ink lift
(ink-low → ink-hi) on bare controls, or one surface step on filled ones.
**Disabled** = `opacity: .35`. **Focus** = 2px ink-low outline, offset 2
(`:focus-visible` global); a control that is *both* selected and focused carries
a 2px ink-hi outer ring at offset 2 so keyboard focus survives selection
(`.cell.on`, `.step/.neut/.dot[aria-pressed="true"]`, `.lsw.on`).

Motion grammar: state changes fade at `--t-fast` 120ms (colour/background/
opacity) or `--t-med` 180ms (swatch reveals, flex-grow) with the one ease
`cubic-bezier(.25,.1,.25,1)`. Surfaces *arriving* use the one spring,
`cubic-bezier(.16,1,.3,1)`: cards rise 5px over .45s (staggered 30ms, capped at
16 items), the rail slides in over .3s, tray reorders FLIP over 200ms. Feedback
one-shots: `.flash` (outline pulse, .9s) answers "where is this / what changed",
`.shake` (±3px, .3s) answers "that drop is not allowed". Toast slides 4px over
.25s.

### Chips
The workhorse control — one component, two readings by context:
- **Bare in a row = filter.** Transparent, ink-low, 13px/500, radius 10px, padding .45rem .85rem. Hover lifts ink only; active = bg-3 + ink-hi. Section chips, Saved/Systems, board-view and theme pickers.
- **Inside a bg-2 container = segmented control.** `.rtabs` (Build/Export): container bg-2, radius 12px, padding 3px, 2px gaps; segments flex 1, centred, 14px, radius 9px; the active segment steps to bg-3, inactive hover lifts ink without a fill. `.themes` groups read the same way at filter-chip size.
- **Format pickers** (export dialog nav, export tab nav): the uppercase acronym exception — 11.5px/600/+.06em.
- **The back chip** (`.chip.back`): pre-filled bg-2 + ink-hi — deliberately the loudest chip on the toolbar, because it is the way back to an open system.

### Search Field
48px bg-2 row, radius 12px, padding 0 16px: leading Phosphor magnifier (16px, currentColor at ink-faint), then a borderless mono 13px input in ink-hi with ink-faint placeholder. Hover bg-3; focus-within takes the standard 2px ink-low ring. The input itself is invisible — the row is the field.

### Buttons
- **Primary** (`.btn`): the inverse pair. 48px, radius 12px, 14px/600, padding 0 22px. Hover darkens via `filter: brightness(.92)` — the white stays white-ish, never tinted.
- **Ghost** (`.btn.ghost`): bg-2 + ink-mid, 500. Hover bg-3 + ink-hi.
- **Text actions** (card `.acts`, `.lab .act`, list-row verbs): bare 13px/500 ink-low/ink-mid words, hover ink-hi; pressed state (Save/Draw) takes bg-3 + ink-hi at radius 6px. No borders, no underlines.
- **Icon buttons** (`.ricon`, dialog ✕): bare Phosphor glyph at ink-low, hover ink-hi + a bg-3 plate, radius 6px.
- Disabled anywhere: opacity .35, cursor default/not-allowed.

### Cards
bg-1, radius 16px, `overflow: hidden`, no border; hover bg-2 (whole card). Palette cards: a 10rem colour-band strip (the content), then a hairline-topped footer — title 15px/600 ink-hi beside a mono page number in ink-faint, then section name (12px ink-low) beside the action verbs. Bands grow on hover (flex-grow 1.8) and reveal their mono hex in on-content ink; >12 colours rotates labels vertical. Shelf (system) cards swap the bands for a 5rem strip of the system's colours (core, accents, then bg/surface/text of its neutral) and drop the footer hairline; a pinned card wears a 2px ink-hi outline. The card lending accents (`.drawing`) wears the same outline while its bands become pick targets.

### Dialogs
bg-1, hairline border, radius 20px, `width: min(34rem, calc(100vw − 2rem))`, max-height 92svh, backdrop rgba(0,0,0,.6). Anatomy: centred 20px/700 title with the bare ✕ floating absolute top-right; optional format-chip nav; a code pane sunk to bg-0 (radius 8px, mono 12px/1.7); footer with ghost + primary buttons right-aligned. Click-outside and Escape both close. The delete dialog is the same shell with a plain 14px ink-low message.

### Tray (the system, chip by chip)
A dashed rgba(255,255,255,.22) container at radius 12px holding pill chips on bg-2 (hover bg-3): colour dot (1.1rem, hairline ring) + caps role tag (`a1`, `core`) + mono hex in ink-hi + mono page tag (`p.33`) when borrowed from another page. The core chip sits pre-raised at bg-3. Each accent chip hides its ✕ until hover/focus-within (always visible on coarse pointers), is keyboard-reorderable (arrows) and removable (X/Delete), and is draggable — drag to reorder, drag off to remove. Empty state: "nothing chosen yet" in ink-faint.

### Drag & Drop grammar
Lifting any handle spawns the **drag ghost**: an inverse pill (dot + label + mono badge) with the system's only glow, following the pointer at z 80 while the source chip dims to .3 and the body cursor becomes `grabbing`. Drop targets self-report in `currentColor`: valid = 2px solid inset outline (`.dropok`), invalid = 2px dashed + a ⚠-prefixed badge on the ghost (`.dropbad`); an invalid drop shakes the target and toasts why. Every drag has a click/keyboard twin — drag is sugar, never the only door.

### Toast
An inverse pill fixed bottom-centre (z 70): 13px/600, tabular numerals, rises 4px on show; auto-dismisses at 1.6s, or 6s when it carries the underlined inline "undo" button. Toast copy is lowercase and terse ("link copied", "core → #FF7500 · #FFE4AB kept as accent").

### Role Ladder & Ramp Strip
The contrast instrument. Five caps role names (ink-low; ink-hi when overridden, with an inline ✕ to reset) beside eleven 1.15rem colour steps (1px seams, radius 6px); the current step wears the selected outline, and on failing text roles the nearest AA-clearing step carries the ghost fix mark — a 2px inverse-bg bar plated with rgba(0,0,0,.6). Under each row a mono readout ("muted on surface 7.0:1 AAA"); failing rows brighten to ink-hi with a ⚠ prefix. Above it, the ramp strip repeats the eleven steps at 1.7rem as drag sources for roles and the preview. The whole ladder lives in a `<details>` that opens itself only when it has something to say (a failure or an override).

### Neutral Tiles
Five 7rem-tall tiles in a snap-scrolling row (1px seams): each is the built system rendered as a miniature page in that scale's own colours — nav bar with the scale's name as a text-on-surface sample (caps .5rem), then text/muted/core bars, never real copy. Hover = 1px ink-low outline; selected = 2px ink-hi.

### Board Cells (builder swatches)
Palette colour is the button. Chosen = 2px `currentColor` inset outline; the core cell grows (flex 1.7) and names itself; eliminated stays in full colour at .72 opacity under a `currentColor` diagonal strike — you cannot judge a colour you cannot see. Hover shows a 1px inner ring (no growth — a swelling cell drags its column), reveals the mono hex and the "core" cap cue, and a hairline marks the top-40% core-target split. All labels ride the on-content inks (`.lt`/`.dk`).

### Icons
Phosphor, **Fill weight**, inline `<symbol>` defs, drawn in `currentColor` so they ride the ink ladder and brighten with their label. Sized `1.05em` via `.i`. The one exception: the bare ✕ uses the **Bold** weight — its Fill variant is plated. New icons must join the symbol block, not arrive as external assets.

### Signature: the Preview
The `.prev` page mock (nav/body/quote/field/footer — plus hero, article, cards, form, chart, and palette-sheet templates) is the app's centrepiece and is painted **entirely** by the built system through `--p-*` variables. Its regions are drop targets for neutral steps (`data-drop="role:*"`) and pulse `.flash` when their role moves. Nothing inside it uses chrome tokens except as a fallback; nothing outside it may use `--p-*`.

The variables are colour, state and type: `--p-bg / -surface / -line / -ink / -mut / -core / -core-ink`, then `--p-hov / -act / -tint / -tint-hi / -cline` from the derived states, then `--p-display / -body / -mono`. Buttons carry real `:hover` and `:active` rules off `--p-hov` and `--p-act`, so a state is judged under a cursor rather than read as a swatch.

**Hero** is the template that has to survive being called a website: a nav with somewhere to go, a display line at display size, copy at a real measure, two pressing buttons, proof, and a product shot carrying every accent at once. It is sized in `cqw` off `.prev`'s inline-size container, so the same markup reads as a landing page at any pane width.

### Preview type
Three slots — **Display**, **Text**, **Mono** — chosen per system from a curated shortlist of ~40 families (Sanna's *Usable Framer Fonts* list, reduced to the faces that resolve from a public CSS endpoint: Google Fonts, plus Gambarino from Fontshare). Twelve of the originals ship only inside Framer and are deliberately absent — a font that cannot render is not a choice.

Type is part of the **system record** (`s.type`), not `ui`: it persists, travels in the `#b2=` share hash as the 11th element, and reaches every export. A family is fetched by injecting one `<link>` at the moment it is first painted, once per family. An unset slot falls back to the chrome's stack. Faces are never drawn in the chrome itself — the preview below the picker is the specimen.

## Do's and Don'ts

### Do:
- **Do** run every new surface through the two ladders: pick its resting bg step, its ink step, and let states move exactly one step (The One-Step-Up Rule).
- **Do** spend the inverse pair on the single loudest thing on a screen — and only one thing at a time.
- **Do** use `aria-pressed` for every toggle/selected control; the CSS state grammar is keyed to it, and so are the self-checks.
- **Do** keep every control row at 48px (`--row-h`) and body-adjacent text at 13–15px.
- **Do** set hex, ratios, counts, and code in Geist Mono with `tabular-nums` where digits align.
- **Do** keep the ~60 `console.assert` self-checks at the end of `index.html` passing — several assert on rendered DOM and computed styles (e.g. `body.rail` must hide `#grid` while `body.rail.pick` shows it; tray chips must carry `.tp`/`.tx`; list rows must offer exactly `core,eliminate`; Escape must unwind picking before closing the rail; the frozen CSS export must match byte for byte). A visual edit that breaks one is wrong until proven otherwise.
- **Do** give drag interactions a click/keyboard twin, restore focus across re-renders via `data-k`/`data-hex`, and honour `prefers-reduced-motion` and `pointer: coarse` in any new interaction.

### Don't:
- **Don't** put colour in the chrome. No accent hues, no tinted grays, no coloured focus rings — grayscale by law; colour belongs to palette content and the `--p-*` preview world only.
- **Don't** add shadows, glows, or gradients to chrome. Elevation is lightness; the drag ghost owns the one glow.
- **Don't** use tracked caps on anything clickable except the format-picker acronym rows; controls speak normal-case 13–14px/500.
- **Don't** add a light theme to the chrome, or let the preview's light/dark toggle leak into app styling.
- **Don't** hand-edit `colors.js` — it is generated by `scripts/extract.py` and hand edits are lost on regeneration.
- **Don't** treat `ink()`'s #0A0A0A/#FFFFFF as chrome tokens — that pair is exported content, frozen by the tests.
- **Don't** load anything from a network at load; the chrome's fonts stay self-hosted in `fonts/`, icons stay inline Phosphor symbols. A preview face the user picked is the one permitted fetch, and it happens on the pick, not before.
- **Don't** set the chrome in a preview face. Type follows the same law colour does: `--p-display` / `--p-body` / `--p-mono` live inside `.prev`, and Geist keeps the tool's own voice.
- **Don't** grow a swatch on hover inside a shared column, and don't hide a destructive action behind hover on coarse pointers (the ✕ pattern already handles this).
