---
target: "index.html — system builder rail (#rail)"
total_score: 32
max_score: 36
na_heuristics: 10
p0_count: 0
p1_count: 2
timestamp: 2026-08-05T10-30-04Z
slug: index-html-system-builder-rail-rail
---
Method: dual-agent (A: afd6f079826c3cc41 · B: ae634fcab9c13109f)

## Design Health Score

Scored against the rail alone (`#rail`, the full-screen Build/Export editor), not the whole app.

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 3/4 | Live tally, `aria-pressed` everywhere, live AA ratios, export preview shows real generated code. No confirmation toast when a system auto-saves. |
| 2 | Match System / Real World | 4/4 | Uses the book's own vocabulary (core/accent/eliminate/neutral) throughout; Page preview mocks an actual page rather than abstract tokens. |
| 3 | User Control and Freedom | 4/4 | Layered Escape handling, reversible eliminate/restore, reversible role overrides with one-click "reset." |
| 4 | Consistency and Standards | 3/4 | `.ricon` and `.ract` buttons correctly reuse existing dialog conventions — but the native `confirm()` on delete and three near-identical "quiet text" button conventions (see Priority Issues, Minor Observations) cost a point. |
| 5 | Error Prevention | 3/4 | `confirm()` gates destructive delete; AA math is computed, not guessed; ghost-fix mark nudges toward a passing choice before commit. |
| 6 | Recognition Rather Than Recall | 4/4 | Nothing is memorized: state is always shown (`aria-pressed`, moved-role highlighting, live ratios, export snippet). |
| 7 | Flexibility and Efficiency | 4/4 | Keyboard shortcuts (C/Enter/X) on ramp cells, focus survives every re-render. Shortcuts are documented only in screen-reader-only text — correct for the stated solo-expert audience, not a gap. |
| 8 | Aesthetic and Minimalist Design | 3/4 | Individual components are restrained, but the detector confirms almost the entire rail runs at 7.2–9.2px text (see Priority Issues), and the preview pane's width is unbounded past ~1183px windows — both docked here. |
| 9 | Help Recognize/Diagnose/Recover from Errors | 4/4 | The ladder's whole purpose: muted → bold+⚠ escalation paired with an explicit "clears X:1" sentence — visual and verbal redundancy that's unusually well executed. |
| 10 | Help and Documentation | n/a | Solo-use, no-onboarding-by-design tool per the product brief; absence is correct for this audience, not an omission. |
| **Total** | | **32/36** | **Good** (89% — one point under the Excellent threshold) |

## Design Specificity Verdict

**Authored specifically for this tool, with high confidence — this is the strongest thing about the rail.**

**LLM assessment**: The evidence is domain logic a generic settings panel couldn't have. The ramp board regroups a palette into the same tint/shade columns the source book prints. The neutral picker renders five *live rendered pages* instead of flat colour strips specifically because two of the five scales (Neutral and Zinc) share an identical light background and would be visually indistinguishable as swatches — and the code backs that decision with a runtime assertion, not just aesthetic preference. The role ladder computes real WCAG contrast and offers a one-click "nearest AA-passing step" repair. The new Palette view is explicitly built to reuse `.cell`'s swatch vocabulary while dropping interactivity, because it's "read, not clicked." The rhead chrome and Export tab's format picker are the more generic parts, but they wrap bespoke innards rather than replacing them.

**Deterministic scan**: The CLI structural scan (`detect.mjs`) returned exactly one finding across the whole file — a `broken-image` warning at line 1687 — and it's a false positive: the regex matched the literal string `esc("<img src=x onerror=...">)` inside a JS self-test assertion for HTML-escaping, not an actual `<img>` tag. It sits well outside the rail's markup/CSS/JS ranges and isn't a real defect. In other words: the deterministic scan found nothing generic, templated, or broken about the rail's structure — it's clean.

A separate browser-injected accessibility/quality scanner (not the design-specificity detector, but relevant evidence) flagged real, attributable issues, covered under Priority Issues and Minor Observations below.

**Visual overlays**: Script injection into the live page succeeded (title mutation confirmed, `detect.js` loaded and ran), and its console output was read directly rather than left as a persistent on-page overlay; the local server used for visualization was stopped afterward, so nothing remains live in a browser tab. Findings are summarized below from the console output.

## Overall Impression

The rail is the most confidently *authored* part of this app — every major control (ramp board, neutral picker, role ladder) answers a real problem specific to this exact 202-palette dataset, not a generic pattern borrowed off the shelf. What holds it back from Excellent is craft debt at the edges rather than a conceptual problem: the preview pane's width isn't actually capped the way its own code comments claim, the rail concentrates more small-caps micro-type on one screen than anywhere else in the app (confirmed independently by both the design review and the browser scanner), and the one moment the interface actually threatens data loss — deleting a system — drops into an unstyled OS `confirm()` inside a UI that otherwise redraws every native affordance by hand.

## What's Working

1. **The ghost-fix mark on the role ladder.** A failing AA pairing gets a visual mark on the nearest passing step *and* a plain-language sentence ("marked step clears 4.6:1") — verbal and visual redundancy that turns an abstract contrast failure into a concrete, reversible, one-click fix. Rare craft for an accessibility-repair UI.
2. **The rail borrows its chrome instead of inventing new chrome.** Despite being the single largest addition to the file, `.ricon` and the `.ract` action buttons reuse the pre-existing dialog's icon-button and `.btn`/`.btn.ghost` conventions almost verbatim — very little new button vocabulary was introduced to build the whole full-screen editor.
3. **The "live pages instead of strips" neutral picker is a verified decision, not a stylistic one.** The code contains a runtime assertion that no two of the five neutral tiles render identically — the design directly answers a real collision in the data (two scales share the same light background), and it's provably correct rather than merely tasteful.

## Priority Issues

**[P1] Preview pane grows unbounded past ordinary desktop widths, undercutting its own stated purpose.**
- **Why it matters**: `@media (min-width: 60rem)` sets the controls column to `min(34rem, 46%)` and hands everything else to the preview column via `minmax(0, 1fr)` — uncapped. Past roughly a 1183px window, the controls column locks at 34rem while the preview keeps growing indefinitely. The code's own comment says the preview exists to be "judged as a page" at "~800px" — on any normal laptop or desktop width, it now stretches well past that, working against the exact reason the pane was split out from the scrolling controls in the first place. Confirmed visually: the browser evidence at a common 1400px viewport already shows the preview claiming the majority of the screen.
- **Fix**: Cap the preview track (e.g. `minmax(0, 50rem)`) or give `.prev`/`.pal` their own `max-width` inside the pane so the page mock stays a page-sized read regardless of monitor width.
- **Suggested command**: `/impeccable layout`

**[P1] The rail concentrates the app's smallest text on its densest screen.**
- **Why it matters**: The browser-injected scanner measured the rail's own labels running from 7.2px ("core" ramp labels) to 9.2px ("Core & accents," "Neutral palette," "Roles," tab chips) with the role ladder's five token labels at 8.8px. This isn't a rail invention — tiny tracked caps are the app's established micro-label voice — but the rail is the one screen that stacks a 27-swatch ramp board *and* a 55-button role ladder in the same view, and the design review independently flagged that both read as "grids of small coloured rectangles with mono hex" that are easy to visually conflate at a glance. The tiny, uniform type is exactly what erases the cue that would tell them apart faster.
- **Fix**: Nudge the smallest tier (the 7.2px/8px core-label and hex-caption text) up by 1–2px without abandoning the tracked-caps voice, or introduce one more size step so the ramp board and the role ladder read as two distinct systems rather than one repeated pattern at two densities.
- **Suggested command**: `/impeccable typeset`

**[P2] Native `confirm()` breaks the rail's own hand-drawn visual system at its single most destructive moment.**
- **Why it matters**: The file explains, in its own comment, that OS-native glyphs were redrawn by hand because they "arrive at a different weight, size and baseline on every OS, and beside a UI built out of 1px rules they read as debris" — and then drops exactly that kind of debris into the delete-system confirmation, the one action in the rail that can't be undone. A styled `<dialog>` component with the right button classes already exists elsewhere in the file and sits unused for this purpose.
- **Fix**: Route delete confirmation through the existing dialog component instead of the browser's native `confirm()`.
- **Suggested command**: `/impeccable polish`

**[P2] The Preview label row packs three controls into a layout built for two.**
- **Why it matters**: `.lab` is built and used everywhere else as a two-child, `space-between` pattern (a label plus one trailing action or tally). In the preview section it's given three children — the "Preview" label, the page/palette view-toggle chips, and the light/dark theme chips — all in the same row. `space-between` spreads three items apart evenly, which visually detaches the two toggle groups from the label they modify and from each other, instead of reading as one clearly grouped control cluster.
- **Fix**: Wrap the two toggle groups into a single flex child so the row resolves to label-left / controls-right, or give the view toggle its own sub-row above the theme toggle.
- **Suggested command**: `/impeccable layout`

## Persona Red Flags

**Alex (Power User)** — this is close to the actual target user (a solo returning expert), so red flags here matter most:
- Keyboard shortcuts (C to set core, Enter to toggle accent, X to eliminate) exist and work, but are documented only in a screen-reader-only paragraph — invisible to a sighted user who steps away for a few weeks and forgets the exact keys. Deliberate per the "no onboarding chrome" brief, but worth naming as a real recall cost for the specific "returning expert" this tool is built for.
- The native `confirm()` on delete (P2 above) is the one moment Alex's fast, full-screen, keyboard-driven flow gets yanked into a slow, unstyled OS modal — a jarring context switch exactly where speed matters most.

**Sam (Accessibility-Dependent User)**:
- The 7.2–9.2px text the scanner measured across the ramp board, role ladder, and neutral tiles is well below comfortable reading size regardless of color-contrast compliance; a low-vision user relying on browser zoom will hit this hardest on the rail specifically, since it's the one screen with the most of this text on it at once.
- The scanner also flagged uppercase body-length text (105 and 48 characters) somewhere in the page — all-caps text is harder for some users to parse and can be read oddly by screen readers. Attribution to the rail vs. the underlying grid wasn't fully resolved by either assessment; worth a quick manual check of whether any of the rail's own longer strings (e.g. the "Draw from another page" / "Eliminate the rest (N)" action links) are the source, since those sit right at the edge of "label" vs. "sentence" length.
- On the positive side: the ladder's AA-failure state is genuinely well built for Sam — it's never color-only, always paired with a ⚠ glyph and an explicit ratio sentence.

## Minor Observations

- Two CSS comments directly contradict each other about the same layout mechanism ("the preview yields first" vs. "the pane keeps its size and the controls absorb the window") — the actual code matches the second; the first reads like a stale note from an earlier version.
- `.pf-row`/`.pf-ramp` (the new Palette view) hardcode `rgba(0,0,0,.08)` for their dividers instead of `var(--line)` — the one place in the rail's new CSS that steps outside the token system it otherwise follows precisely.
- `rDup`/`rDel`/`rClose` sit at equal visual weight with no divider between "manage this system" and "leave the rail" — mitigated by the delete confirmation, but visually undifferentiated from safer neighbors.
- Three near-duplicate "quiet clickable text" conventions (`.chip`, `.acts button`, `.lab .act`) ship slightly different size/letter-spacing pairs with no shared token — harmless today, the kind of small drift that compounds as more actions get added, and slightly undercuts the file's own "one micro-label voice" comment.
- The board's touch-target bump (`.cell` row height 2.35rem → 3rem) is keyed to `max-width: 900px` rather than `pointer: coarse` — an imprecise proxy for "this is being tapped," though low-severity for a tool used on known devices.
- Detector also logged `overused-font` (Geist 45% / Geist Mono 55% of text) and a heading-level skip (h1 → h3, no h2) — the font split is expected given how hex-heavy this app's content is, not a real issue; the heading skip traces to the background grid's card headings, not the rail's own DOM (the rail's system name is an `<input>`, not a heading), so it's out of scope for this review.

## Questions to Consider

- What if the role ladder defaulted to a compact ratio summary and only expanded to full 55-button form on explicit request, rather than auto-opening on any failure or override — would the common case (a palette that already passes AA) read calmer without losing the one-click repair for the failing case?
- What if the preview pane were actually capped to the ~800px of "page" its own comment claims — would it judge better on a real wide monitor than the current unbounded track allows?
- What would it take for "Draw from another page" to stay inside the rail's own full-screen focus, rather than stepping the whole rail aside to show the grid again?
