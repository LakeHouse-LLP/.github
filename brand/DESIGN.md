# Design System: LakeHouse Studio

> Agent-readable design system in the taste-skill stitch format (`Leonxlnx/taste-skill`, `skills/stitch-skill/DESIGN.md`). Version 0.3, October 9, 2026. Source of truth for values: `tokens.json`. Full rationale: `BRAND.md`, `DESIGN-SYSTEM.md`, `WRITING-STYLE.md`.

## Configuration: active dials

| Dial | Value | Meaning |
|---|---|---|
| `DESIGN_VARIANCE` | 5 | Offset, left-aligned layouts with asymmetric open space on a strict grid |
| `MOTION_INTENSITY` | 3 | Hover and press feedback only; static by default |
| `VISUAL_DENSITY` | 3 (marketing), 5 (product UI) | Airy brand pages; standard app spacing in plugins |

Mode: **dark only** (explicit brand decision; overrides the dual-mode default).

## 1. Visual Theme & Atmosphere

A calm, professional, architectural home office for small design practices. It feels like professional design software at dusk: flat graphite rooms, one cyan light on the water, nothing shouting. Precise and structured like a drawing set, warm in the words rather than in decoration. The user's drawings, models and data are the brightest things on screen; the chrome stays quiet.

## 2. Color Palette & Roles

- **Canvas Graphite** (#1E1E1E): app background, logo tile, text on accent fills (locked)
- **Sunken Graphite** (#161616): inputs, code blocks, 3D viewports, outer frame
- **Surface Graphite** (#262626): cards, panels, sidebars
- **Raised Graphite** (#2E2E2E): menus, popovers, hover rows
- **Overlay Graphite** (#383838): dialogs, toasts
- **Hairline Graphite** (#474747): dividers in dense layouts only (decorative)
- **Outline Grey** (#8F8F8F): input and control outlines, at least 3:1 on every surface
- **Paper Ink** (#F2EFE9): primary text and the logo ink
- **Stone** (#C7C5C0): secondary text, the "Studio" in the wordmark
- **Muted Stone** (#AAA8A4): captions and metadata, AA on every surface
- **Disabled Stone** (#73716D): disabled controls only
- **Lake Light** (#7DFFFF): the single accent. Primary action, focus ring, links, the horizon line in the mark. Locked, fully saturated, so used once per view and under 10% of any screen
- **Status:** Reed #7FD1A0 (success), Amber #F2C46D (warning), Coral #FF8A80 (danger), Lake #8DB8D2 (info). Always paired with an icon and a word
- **Chart series** (`color.data.1-6`): accent, timber #D4A373, lake #8DB8D2, dusk #F0A98A, reed #7FD1A0, stone #C7C5C0. Charts only, never UI chrome

One grey family, pure neutral. No pure black, no pure white on screen.

## 3. Typography Rules

- **Display and UI:** Geist 400/500/600. Headlines 600, sentence case, tracking -2% at display size, -1% at h1/h2. Scale: 48 / 36 / 28 / 22 / 18 / 15 body / 13 / 12 label.
- **Body:** Geist 400, 15/24, `text.secondary` for long passages, max 65 characters per line.
- **Mono:** Geist Mono for code, IDs, coordinates, sheet numbers and data tables. Tabular figures for any column of numbers.
- **Chinese:** Noto Sans SC, line height 1.7.
- **Wordmark:** "LakeHouse" Geist 600 in Paper Ink plus "Studio" Geist 400 in Stone, one line, converted to outlines.
- **Banned:** Fraunces, Instrument Serif, Inter as a default, any second display family, all-caps eyebrows on every section, Light or Thin weights on dark.

## 4. Component Stylings

- **Buttons:** radius 8, height 36, Geist 600 15. Primary: Lake Light fill with Canvas Graphite label (14.0:1), one per view. Secondary: transparent with Outline Grey border. Ghost for toolbars. Press state darkens to `accent-pressed`; no glow, no scale bounce.
- **Cards and panels:** Surface Graphite, radius 12, padding 16-24, no border by default. Used only when elevation means something; never nested. Dense data uses dividers instead.
- **Elevation:** surface step first (sunken, canvas, surface, raised, overlay), then a 1 px white-at-6% highlight on the top inside edge of raised and overlay layers, then a soft #0A0A0A shadow as a secondary cue.
- **Inputs:** Sunken Graphite fill, 1 px Outline Grey, radius 8, label above, helper or error text below with an icon. Focus is a 2 px Lake Light ring with a 2 px offset.
- **Navigation (rooms):** Phosphor icon plus room name; only the active room carries the accent.
- **Loaders:** determinate bar on an accent track for jobs over 2 s, with "step x of y" and Cancel. Skeletons match the final layout.
- **Empty states:** a line illustration, an h3 and one literal sentence ("No exports yet. Run your first batch export.").
- **Icons:** Phosphor Regular, 16/20/24 px, `text.secondary` by default, accent only when active.

## 5. Layout Principles

- 4/8 px grid; spacing scale 0, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96.
- Left-aligned compositions with open space on one side. No centered marketing hero, no row of three equal cards, no bento of identical tiles.
- Hero: at most four text elements, headline at most two lines, subtext at most 20 words.
- Brand surfaces (social card, README header, board): mark large on one side, words stacked on the other; accent appears only in the mark.
- Container max width 1280; page margins 24 narrow, 64 wide. Single column below 768 px. `min-h-[100dvh]`, never `h-screen`.
- Radius system: 4 tags, 8 controls, 12 cards, 16 dialogs and app icons. Pills only for avatars and status dots.

## 6. Motion & Interaction

- Durations: 120 ms hover and press, 200 ms expand and fade, 320 ms panels and dialogs, 480 ms room transitions.
- Easing: standard (0.2, 0, 0, 1), enter (0, 0, 0, 1), exit (0.3, 0, 1, 1). No bounce, no spring overshoot: things settle like still water.
- Animate only `transform` and `opacity`. No scroll-triggered choreography, no parallax, no infinite loops, no auto-playing marquees.
- `prefers-reduced-motion`: durations to 0, fades at most 120 ms.

## 7. Anti-Patterns (Banned)

- Em dashes and en dashes anywhere in copy (use a period, comma, colon or parentheses; ranges with a hyphen)
- Emoji in UI, docs, release notes or brand assets
- Decorative middle-dot strips, more than one middle dot per line
- Generic taglines: "under one roof", "all-in-one", "elevate", "seamless", "unleash", "next-level"
- Purple or blue AI gradients, neon glows, gradient text, colored shadows
- A second accent color, or room colors in UI chrome
- Pure #000000 or #FFFFFF on screen (white is allowed only as paper for the mono logo)
- Warm and cool greys mixed in one view
- Centered hero with a badge above the headline; three equal feature cards
- Eyebrow labels on every section, section numbers, version stamps, "scroll to explore" cues
- Hairline decoration rules and boxes around everything
- Fraunces, Instrument Serif, Inter as default, Lucide as default icon set
- Light-mode UI, or the accent on white
- Redrawing, recoloring, rotating, outlining or adding effects to the L1 mark
- Client names, Ennead content, or fake "trusted by" logos
