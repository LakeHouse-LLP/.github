# LakeHouse Studio: brand identity

> Version 0.3 (October 9, 2026). v0.3: taste-skill pass (Geist type, one grey family, no em dashes, design dials). v0.2: graphite surfaces, L1 mark locked. v0.1: draft. Owner: Sen Zhang. GitHub: `LakeHouse-LLP`.
> **Dark mode only.** Every surface we design sits on a dark background. The one exception is the monochrome logo, used only where a light background can't be avoided.

## 中文摘要

**LakeHouse Studio 是设计师和小型事务所的"第二个家"。** 一个湖边的数字办公室：设计软件、生产助手、InDesign 工具、工时表、Keynote/Excel 助手、设施管理（FM）、AR/VR，甚至游戏，都在同一个屋檐下。

- **名称：** 只写 `LakeHouse Studio` 或 `LakeHouse`（大写 L 和 H，中间不空格）。不要写成 Lakehouse、Lake House、LAKEHOUSE 或 LH Studio。中文语境下保留英文原名，不翻译。
- **气质：** 温暖、沉静、有建筑感；专业又有人情味，为设计师而做。不炒作，不说大话。
- **视觉：** 只用深色模式。中性深灰作底（`#1E1E1E`，像 Figma、Blender、VS Code 这类专业软件），品牌强调色是亮青色 `#7DFFFF`（唯一 token：`color.accent`，以后可能换），湖蓝、木色、黄昏暖色作辅助。浅色背景只用单色 logo。
- **字体（全部免费开源）：** Geist（标题、界面和正文）、Geist Mono（代码和数据）、Noto Sans SC（中文）。
- **Logo（已定稿 L1）：** 粗壮的 L 和 H，顶部斜切成同一条山墙坡线；L 中间是留空的“虚空”；下方一条细细的青色水平线（强调色）。旧方向 A-D 已归档。
- **隐喻：** 房子里的房间：工作室 Studio、工坊 Workshop、书房 Library、办公室 Office、影音室 Theater、游戏室 Game room。点到为止，不要过度使用。

---

## 1. Name

| Use | Don't use |
|---|---|
| **LakeHouse Studio**: full name, first mention, legal/footer, the logo | Lakehouse, Lake House, Lake-House, LAKEHOUSE, lakeHouse |
| **LakeHouse**: short form after the first mention | LH, LHS, "the LakeHouse" (except for the house metaphor, e.g. "rooms in the LakeHouse") |
| `lakehouse`: lowercase only in code identifiers: package names, CLI, URLs, repo slugs (`@lakehouse/design-tokens`, `lakehouse-revit`) | `LakeHouse-LLP` in prose; it's the GitHub org handle, not a brand name |

- Camel-case capital **L** and capital **H**, with no space. Never hyphenate or split the name across lines.
- Possessive: "LakeHouse's". Plural: avoid it.
- Product names follow the pattern **LakeHouse + plain noun**: *LakeHouse Timesheet*, *LakeHouse InDesign Helper*, *LakeHouse FM*. Don't make up a new brand name for each tool.
- In Chinese text, keep "LakeHouse Studio" in Latin letters and put a space on each side: `欢迎使用 LakeHouse Studio 工时表`. If a translation is ever required, use 湖屋工作室 as the descriptor only, never as the logo.
- "Studio" also names a room in the metaphor. When you mean the room, write it lowercase ("the studio"), or make the meaning clear from context.

## 2. Positioning

**Statement.** For independent designers and small architecture and design offices who are tired of stitching together a dozen tools, **LakeHouse Studio** is an all-in-one digital office: design-software plugins, production assistants, documentation and InDesign helpers, timesheets, Keynote and Excel helpers, facility management, AR/VR and even games, all under one roof. Unlike enterprise suites built for big firms, LakeHouse is made by a practicing architect and design technologist. It feels like a second home: calm, well made, and yours.

**One-liner.** A second home for your design practice.

**Core idea.** *The dream home you live, work and play in.* A warm, calm, architectural house by the lake, at dusk with the lights on.

### Tagline options
1. **A second home for your design practice.** *(primary; Sen's own idea, keep it)*
2. Built by an architect, for designers.
3. Small office, whole house.

Retired in v0.3 as generic: "under one roof", "Move in. Your office is ready.", "A calm place to do good work.", "Work, make, rest.", "Your digital office by the lake." Taglines stay short and specific; no slogan soup.

**Supporting line** (under 20 words, used on the social card): *Revit and Rhino tools, production helpers and office admin for small design practices.*

### Personality
| Trait | We are | We are not |
|---|---|---|
| **Warm** | Welcoming, generous, human | Cute, gushing, emoji-heavy |
| **Calm** | Unhurried, clear, quiet confidence | Urgent, loud, "10x" hype |
| **Architectural** | Precise, structured, honest about materials | Cold, sterile, jargon-proud |
| **Crafted** | Small details done well, practitioner's know-how | Over-designed, decorative for its own sake |
| **Playful at home** | A game room, a wink in an empty state | Gimmicky, juvenile |

### The rooms of the house (use lightly)
The house metaphor organizes the product family. Use it for navigation, landing pages and launch posts. Don't put it in error messages, docs, or anywhere it would slow someone down.

| Room | What lives there | Icon (Phosphor) |
|---|---|---|
| **Studio** | Design tools: Revit/Rhino plugins, geometry and modeling helpers | `compass-tool` |
| **Workshop** | Production assistants: batch export, sheet setup, QA/checkers | `wrench` |
| **Library** | Docs, templates, InDesign helpers, standards | `books` |
| **Office** | Timesheet, Excel helpers, FM (facility management), admin | `calendar-check` |
| **Theater** | Keynote helpers, presentations, AR/VR walkthroughs | `presentation` |
| **Game room** | Games and playful experiments | `game-controller` |

Rooms are told apart by **icon and name, never by color** (v0.3 removed the six room colors: one accent per system). The accent marks only the active room. Rules: one room per product; the product name always comes first ("LakeHouse Timesheet, in the Office"); never invent new rooms (a Garage, a Basement) without updating this file.

## 3. Logo

**Locked: L1** (Sen, October 9, 2026). Files in `final/`, overview at `final/brand-board.png`, generated by `build_logos.py`.

**The mark.** A bold, blocky **L** and **H**, side by side, with their tops cut along one shared gable line, so the two letters read as a house without drawing a roof. The **L is a void**: just the stem and the foot, with the space where a glass panel used to be left empty so the background shows through. Under the letters sits one **thin cyan horizon line** (`color.accent`), flush with the mark's width and separated by a small gap: the waterline of the lake.

**Construction** (120-unit grid, see `build_logos.py`):
- Letter tops on one gable line, pitch 3:4 (≈36.9°), peak centered between the letters. Baseline at 113.
- L: stem 26 wide, foot 56 wide and 24 tall. H: stems 18 wide, bar 18 tall. The gap between L and H is 8.
- Horizon line: full mark width (0 to 120), 5 units thick, 6 units below the baseline. At 16, 32 and 48 px the line is thickened (≥1.5 px) and the gap kept ≥1 px; nowhere else.
- Clear space: 20 units (one sixth of the mark width) on all sides. Minimum size: mark 16 px (use the favicon files), lockup 120 px wide.

**Color in the mark.** Letters `color.logo.ink` (stone.100 #F2EFE9), horizon line `color.logo.horizon-line` → `color.accent` (#7DFFFF), on `bg.canvas` (#1E1E1E) or any graphite surface. If the accent changes, the line follows (the build script reads `tokens.json`).

**Versions** (all in `final/`, text converted to outlines):
| File | Use |
|---|---|
| `lakehouse-mark.svg` | Primary mark on #1E1E1E |
| `lakehouse-mark-transparent.svg` | Mark for placing on any graphite surface |
| `lakehouse-mark-mono.svg` | Single ink #1E1E1E, light contexts only |
| `lakehouse-mark-mono-reversed.svg` | Single ink #F2EFE9, for photos and video |
| `lakehouse-lockup-horizontal*.svg`, `lakehouse-lockup-stacked*.svg` | Mark + wordmark, same four versions |
| `lakehouse-appicon.svg` | #1E1E1E rounded-square tile (radius 22.4%), mark at 56% of tile width |
| `favicon.svg`, `favicon.ico` (16/32/48), `favicon-mono.svg` | Browser tabs; mono for light tabs |
| `png/` | Mark, mark-transparent, mark-mono and app icon at 16 to 1024 px; lockups at 512/1024/2048 px wide |

**Wordmark** (v0.3). "LakeHouse Studio" on one line in **Geist**: "LakeHouse" SemiBold 600 in `text.primary`, "Studio" Regular 400 in `text.secondary`, tracking -1%. In the horizontal lockup the cap height is 40% of the mark width (44 of 120 units), set 40 units right of the mark and centered on the letters' mass. The stacked lockup centers the same line under the mark. Text is shaped with kerning (HarfBuzz) and converted to outlines. The v0.2 Fraunces/Inter two-tier wordmark is archived in `archive/final-v1/`.

**Light contexts (exception).** Print on white paper, a favicon on a light browser tab, partner logo walls, invoices: use **mono** (`#1E1E1E`, 16.7:1 on white). Never place the color logo or the `#7DFFFF` accent on a light background.

**Don't:** add a roof, a door, a wave or reflection back; fill the void in the L; recolor the letters; move the line onto the letters or extend it beyond the mark; add glow, gradient or shadow.

**Archived directions.** The v0.1 exploration (A Reflection, B Monogram, C Window, D Horizon) and the Gemini explorations are archived for reference only: `archive/directions-v0/` and `gemini/`. Don't use them.

## 4. Color: dark mode only

One grey family, pure neutral (R = G = B), like professional design software (Figma, Blender, VS Code), so users' drawings and models carry the color. Text tiers carry a faint warmth to match the logo ink. The cyan accent is the light on the water. Lake, timber and dusk are **material colors** for illustration, imagery and charts only, never UI chrome.

**Dark only is a deliberate brand decision** (Sen, October 2026). It overrides the taste-skill default of designing both modes; the monochrome logo covers the unavoidable light contexts. The full token set is in `tokens.json`.

### Brand accent
| Token | Hex | Role |
|---|---|---|
| `color.accent` | **#7DFFFF** | The single brand accent. Links, focus rings, primary button fill, the logo water line, key highlights. **Provisional**: Sen may change it, so everything must reference the token, never the hex value. |
| `color.accent-hover` | #B3FFFF | Hover |
| `color.accent-pressed` | #4FE0E6 | Pressed/active |
| `color.bg.accent-subtle` | #7DFFFF @ 12% | Selected rows and chips |

Use the accent sparingly: aim for under 10% of any screen. It's a lamp in the window, not wallpaper.

### Surfaces (graphite)
| Token | Hex | Use |
|---|---|---|
| `bg.sunken` | #161616 | Inputs, code blocks, 3D viewports, wells |
| `bg.canvas` | #1E1E1E | Page/app background, logo tile (locked) |
| `bg.surface` | #262626 | Cards, panels, sidebars |
| `bg.raised` | #2E2E2E | Menus, popovers, hover rows |
| `bg.overlay` | #383838 | Dialogs, toasts |
| `border.subtle` | #474747 | Dividers in dense layouts (decorative) |
| `border.strong` | #8F8F8F | Input and control outlines (≥3:1 on every surface) |
| `border.highlight` | #FFFFFF at 6% | 1 px inner top edge on raised and overlay layers |

**Elevation.** Depth comes from the surface step (sunken, canvas, surface, raised, overlay: an even ramp of about 8 levels each) plus the 1 px `border.highlight` on raised and overlay layers. Shadows are a secondary cue only, in off-black #0A0A0A, never pure black, never a glow. Prefer spacing over boxes: use a card only when the elevation means something.

### Text and supporting colors
| Token | Hex | Notes |
|---|---|---|
| `text.primary` | #F2EFE9 | Warm paper white, never pure #FFF for body text |
| `text.secondary` | #C7C5C0 | Stone |
| `text.muted` | #AAA8A4 | Captions and metadata |
| `text.disabled` | #73716D | Disabled only |
| `lake.300 / 400` | #8DB8D2 / #5E9BC2 | Water, info, charts |
| `timber.300` | #D4A373 | Warmth, wood, Workshop |
| `dusk.300` | #F0A98A | Sunset, Theater, warm highlights |
| `reed.300`, `amber.300`, `coral.300` | #7FD1A0, #F2C46D, #FF8A80 | Success, warning, danger (status only, always with an icon and a word) |

### Contrast (WCAG 2.2) on the graphite surfaces
Generated by `build_tokens.py` (also saved as `contrast-table.md`). AA body text needs 4.5:1; large text and UI components need 3:1.

| Foreground | Hex | bg.sunken `#161616` | bg.canvas `#1E1E1E` | bg.surface `#262626` | bg.raised `#2E2E2E` | bg.overlay `#383838` |
|---|---|---|---|---|---|---|
| text.primary | `#F2EFE9` | 15.77 AAA | 14.53 AAA | 13.19 AAA | 11.83 AAA | 10.22 AAA |
| text.secondary | `#C7C5C0` | 10.49 AAA | 9.67 AAA | 8.77 AAA | 7.87 AAA | 6.80 AA |
| text.muted | `#AAA8A4` | 7.62 AAA | 7.02 AAA | 6.38 AA | 5.72 AA | 4.94 AA |
| text.disabled | `#73716D` | 3.72 3:1 UI/large | 3.42 3:1 UI/large | 3.11 3:1 UI/large | 2.79 decorative only | 2.41 decorative only |
| accent / text.link | `#7DFFFF` | 15.18 AAA | 13.99 AAA | 12.70 AAA | 11.39 AAA | 9.84 AAA |
| accent-hover | `#B3FFFF` | 16.08 AAA | 14.82 AAA | 13.45 AAA | 12.07 AAA | 10.42 AAA |
| accent-pressed | `#4FE0E6` | 11.32 AAA | 10.43 AAA | 9.47 AAA | 8.50 AAA | 7.34 AAA |
| lake.300 (info) | `#8DB8D2` | 8.55 AAA | 7.87 AAA | 7.15 AAA | 6.41 AA | 5.54 AA |
| lake.400 | `#5E9BC2` | 5.98 AA | 5.51 AA | 5.00 AA | 4.49 3:1 UI/large | 3.88 3:1 UI/large |
| timber.300 | `#D4A373` | 8.00 AAA | 7.37 AAA | 6.69 AA | 6.00 AA | 5.18 AA |
| dusk.300 | `#F0A98A` | 9.26 AAA | 8.53 AAA | 7.74 AAA | 6.95 AA | 6.00 AA |
| reed.300 (success) | `#7FD1A0` | 9.94 AAA | 9.15 AAA | 8.31 AAA | 7.46 AAA | 6.44 AA |
| amber.300 (warning) | `#F2C46D` | 11.11 AAA | 10.23 AAA | 9.29 AAA | 8.34 AAA | 7.20 AAA |
| coral.300 (danger) | `#FF8A80` | 7.93 AAA | 7.30 AAA | 6.63 AA | 5.95 AA | 5.14 AA |
| border.strong | `#8F8F8F` | 5.60 AA | 5.15 AA | 4.68 AA | 4.20 3:1 UI/large | 3.63 3:1 UI/large |
| border.subtle | `#474747` | 1.95 decorative only | 1.79 decorative only | 1.63 decorative only | 1.46 decorative only | 1.26 decorative only |

| Pair | Ratio | Rating |
|---|---|---|
| text.on-accent (graphite.900) `#1E1E1E` on bg.accent `#7DFFFF` | 13.99:1 | AAA |
| graphite.900 text `#1E1E1E` on accent-hover fill `#B3FFFF` | 14.82:1 | AAA |
| graphite.900 text `#1E1E1E` on accent-pressed fill `#4FE0E6` | 10.43:1 | AAA |
| graphite.900 text `#1E1E1E` on dusk.300 fill `#F0A98A` | 8.53:1 | AAA |
| mono logo ink `#1E1E1E` on white (light contexts) `#FFFFFF` | 16.67:1 | AAA |
| accent `#7DFFFF` on white (NOT allowed) `#FFFFFF` | 1.19:1 | fail, never use |
| accent `#7DFFFF` on stone.100 (NOT allowed) `#F2EFE9` | 1.04:1 | fail, never use |

**Rules from the table**
- Body text on any surface: `text.primary`, `text.secondary` or `text.muted` all pass AA everywhere. `text.muted` on `bg.overlay` is 4.94:1.
- `#7DFFFF` passes AAA as text on every surface (9.8 to 15.2:1). Text on an accent fill must be `text.on-accent` (#1E1E1E, 14.0:1), never white.
- `lake.400` is for graphics and large text only on `bg.raised` and `bg.overlay` (4.49 and 3.88:1). Use `lake.300` for small informational text.
- `text.disabled` is below 3:1 on `bg.raised`/`bg.overlay`; acceptable for disabled controls only.
- `border.subtle` is decorative. Controls that need to be recognized use `border.strong` (≥3:1 on every surface), or a fill change.
- Never use `#7DFFFF` on white or paper (1.19:1 and 1.04:1). That's why the brand is dark only.
- The accent is fully saturated, above the taste-skill guideline of 80%. That's a locked brand choice; the compensation is scarcity: the accent stays under 10% of any screen and appears once per view.
- Don't rely on color alone: status always pairs with an icon and a word.

## 5. Typography (all free, SIL Open Font License)

| Role | Family | Use |
|---|---|---|
| Display and UI | **Geist** (400/500/600) | Wordmark, headlines, product UI, body copy, plugin dialogs. Tabular figures (`tnum`) in tables and timesheets. Fallback: Segoe UI Variable, SF Pro, system-ui. |
| Mono | **Geist Mono** | Code, CLI, IDs, coordinates, sheet numbers, data tables |
| Chinese | **Noto Sans SC** (aka Source Han Sans) | All CJK. Pair with Geist, 1.7 line height for Chinese body text |

- **Why Geist** (v0.3): the taste-skill bans Fraunces as an AI-default display serif and discourages Inter as a default sans. Geist is a neutral, slightly technical grotesk that matches the L1 mark's flat, blocky geometry. One family for display and text keeps the system quiet; hierarchy comes from weight and color, not from mixing families.
- Headlines in sentence case, tracking -2% at display sizes, -1% at h1/h2, 0 at body. Hierarchy through weight (600 vs 400) and color (`text.primary` vs `text.secondary`) before size.
- No all-caps eyebrows by default. A small label (Geist 12, 500, sentence case) may sit above a heading at most once every three sections.
- Body text max 65 characters per line, line height 1.5 or more, weight 400 or heavier on dark (no Light/Thin).
- Emphasis inside a headline uses the same family's weight, never a second typeface.
- The type scale is in `tokens.json → typography` (display 48, h1 36, h2 28, h3 22, h4 18, body 15, small 13, label 12).
- Desktop plugins (Revit/Rhino, WPF/Eto) can't always bundle fonts. Fall back to Segoe UI Variable or SF Pro, but keep the scale, colors and spacing.

## 6. Iconography
- Line icons on a 24 px grid, 1.5 px stroke, round caps and joins.
- Icon set: **Phosphor** (MIT), Regular weight, one family only. Lucide was dropped in v0.3 (taste-skill: the default AI icon choice). Custom AEC icons (section cut, grid line, sheet, family, room tag) are drawn on Phosphor's grid and stroke so they sit in the same family.
- Icons use `text.secondary` by default and `color.accent` only when active or selected.
- No filled 3D or gradient icons, and no emoji as UI icons.

## 7. Imagery and photography
- **Mood:** blue hour and dusk. A lake or water, a lit window, timber, concrete, linen, a desk with drawings. Interiors with daylight fading and warm lamps.
- **Treatment:** cool shadows, warm highlights; slightly desaturated (−10 to −20%), low contrast, no HDR. Images should sit happily on `#1E1E1E`. Darken edges or add a dark scrim for text overlays (text contrast ≥4.5:1 measured on the image).
- **Product shots:** real UI in dark mode, inside a simple device or window frame on `bg.canvas`, with one accent highlight per shot at most.
- **Illustration:** simple line drawings in the logo's stroke language: plans, sections, axonometrics of the "house" with labeled rooms. Ink #F2EFE9 lines, one accent.
- **People:** real designers at work, hands on trackpads and sketches, unposed. No stock "team high-five."
- **Never:** client projects, client logos or drawings, or any Ennead Architects content or imagery. Use only our own photos or properly licensed ones (Unsplash/Pexels with attribution kept on file), or Sen's own work if he chooses to.
- **AI imagery:** allowed for moodboards and backgrounds only, never presented as real projects or real places.

## 8. Layout and motion (summary)
4/8 px spacing grid; generous negative space ("rooms" need air). Radius system: controls 8 px, cards and panels 12 px, dialogs and app icons 16 px or the 22.4% icon squircle; never mix within one component. Left-aligned compositions with open space on one side; no centered hero, no three equal cards. Motion is calm: hover and press feedback only, 120 to 200 ms, standard easing, no auto-playing loops. Honor `prefers-reduced-motion`. Details are in `DESIGN-SYSTEM.md` and `DESIGN.md`.

## 9. Design dials and taste rules

LakeHouse follows the open-source taste-skill (`Leonxlnx/taste-skill`, `skills/taste-skill/SKILL.md`, design-taste-frontend v2) where it fits the brief.

**Design read.** A calm, professional, architectural home office for small design practices: brand and marketing surfaces plus dense product UI inside Revit and Rhino, with a quiet, Linear-adjacent minimalism leaning on Geist, one grey family and one accent.

| Dial | Value | Meaning for LakeHouse |
|---|---|---|
| `DESIGN_VARIANCE` | **5** | Offset, not chaotic. Left-aligned layouts with asymmetric open space; strict grids underneath. |
| `MOTION_INTENSITY` | **3** | Static by default. Hover and press feedback only; motion explains state, never decorates. |
| `VISUAL_DENSITY` | **3** marketing, **5** product UI | Airy brand pages; standard app spacing in plugins and the desktop app. |

The dials live in `tokens.json → $extensions["studio.lakehouse.dials"]`.

**Rules adopted from the skill**
- Zero em dashes and zero en dashes in any copy. Ranges use a hyphen (2-4, 9:00-17:00).
- The middle dot appears at most once per line. No decorative text strips ("Studio · Workshop · Library").
- One accent, under 10% of any screen; no glows, no gradient text, no neon.
- No pure black and no pure white on screen (white is allowed only as paper for the mono logo).
- Eyebrows at most once every three sections; no section numbers, version stamps or scroll cues in heroes.
- Hero: at most four text elements, headline at most two lines, subtext at most 20 words.
- Cards only when elevation means something; otherwise spacing or a surface step.
- No emoji in product UI, docs or brand assets.
- Copy self-audit before publishing (see `WRITING-STYLE.md`).

**Where LakeHouse overrides the skill** (on purpose): dark mode only; the accent `#7DFFFF` is fully saturated; the L1 mark is hand-drawn geometry (a brand mark, which the skill allows when the brief asks for it).

## 10. Never
- "Lakehouse", "Lake House", or a hyphenated name.
- Light-mode UI, light-theme marketing pages, or white slide templates.
- `#7DFFFF` on light backgrounds, as large background floods, or as body-text paragraphs.
- Hard-coding the accent hex anywhere. Always use `color.accent`.
- Recoloring, stretching, outlining, rotating or adding effects (glow, drop shadow, gradient) to the logo.
- The color logo on busy photos. Use mono-reversed.
- Any archived logo direction (A-D, Gemini explorations).
- Neon/cyberpunk styling: the accent is calm light on water, not a rave.
- Overusing the house metaphor ("Knock knock! Welcome home!").
- Clip-art houses, real-estate clichés (keys, SOLD signs), stock lakes with swans.
- Fonts with paid licenses, or unlicensed images.
- Mentioning or showing clients, client projects, or Ennead content.

- Em dashes, decorative middle-dot strips, emoji, or AI filler verbs (elevate, seamless, unleash) in any copy.
- Fraunces, Inter or any second display family in brand assets.

## 11. Asset index
| File | What |
|---|---|
| `tokens.json` | W3C DTCG design tokens v0.3 (dark only, one grey family, dials in `$extensions`) |
| `DESIGN.md` | Agent-readable design system (stitch-skill format) |
| `final/lakehouse-mark*.svg`, `final/lakehouse-lockup-*.svg`, `final/lakehouse-appicon.svg` | The L1 logo kit |
| `final/favicon.svg`, `final/favicon.ico`, `final/favicon-{16,32,48}.png`, `final/favicon-mono.svg` | Favicons |
| `final/png/` | PNG exports (16 to 1024 px; lockups 512/1024/2048 px wide) |
| `final/social-preview.png` / `.svg` | 1280×640 GitHub social preview |
| `final/readme-header.png` / `.svg` | 1280×320 README banner |
| `final/brand-board.png` | One-page overview: lockup, construction, tagline, browser and app icon, color proportions, type |
| `contrast-table.md` | Generated WCAG contrast table |
| `build_tokens.py`, `build_logos.py`, `contrast.py` | Regenerate everything. Change the accent in one place and re-run |
| `archive/directions-v0/` | Archived v0.1 directions A-D (night-blue) |
| `archive/final-v1/` | The v0.2 kit before the taste pass (Fraunces/Inter wordmark), with its source docs in `source/` |
