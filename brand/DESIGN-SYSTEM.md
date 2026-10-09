# LakeHouse Studio: design system

> v0.3 (October 9, 2026: taste-skill pass, Geist, one grey family, design dials). **Dark mode only.** Source of truth: `tokens.json` (W3C Design Tokens, DTCG 2025.10 format). Agent-readable summary: `DESIGN.md`.

## 0. Design dials

Set with the taste-skill (`Leonxlnx/taste-skill`, design-taste-frontend v2). Values are stored in `tokens.json → $extensions["studio.lakehouse.dials"]`.

| Dial | Value | In practice |
|---|---|---|
| `DESIGN_VARIANCE` | 5 | Left-aligned, asymmetric open space on strict grids. No centered marketing hero, no row of three equal cards. |
| `MOTION_INTENSITY` | 3 | Hover and press feedback, expand and fade. No scroll-triggered choreography, no loops, no parallax. |
| `VISUAL_DENSITY` | 3 marketing, 5 product UI | Brand pages breathe (section gaps 96+). Plugins and the desktop app use standard app spacing (8/12/16). |
> Target: `packages/design-tokens` in the monorepo, used by the web apps, the desktop app, and the Revit/Rhino plugin UIs.

## 1. Principles
1. **A calm room to work in.** Quiet surfaces, one accent, plenty of space. The user's drawings and data are the brightest things on screen, not our chrome.
2. **Built like architecture.** A clear structure (grid, hierarchy, alignment), honest materials (real data, real states), nothing ornamental.
3. **One light in the window.** `color.accent` (#7DFFFF) marks the single most important action or state on a screen. If everything glows, nothing does.
4. **Same house, every door.** A Revit dialog, a web dashboard and the desktop app should feel like rooms of one house: same tokens, same words, same states.
5. **Respect the expert.** Designers know their tools. Keep things dense where it helps (tables, property panels) and spacious where it calms (onboarding, empty states). Keyboard first.
6. **Accessible by default.** WCAG 2.2 AA is the floor, not a target.

## 2. Tokens

### 2.1 Structure
```
tokens.json
├─ color
│  ├─ accent, accent-hover, accent-pressed   ← brand accent (single source)
│  ├─ palette.{graphite,stone,lake,timber,dusk,reed,amber,coral}.<step>   ← raw values (tier 1)
│  ├─ bg.{canvas,surface,raised,overlay,sunken,accent,accent-subtle}   ← semantic (tier 2)
│  ├─ text.{primary,secondary,muted,disabled,link,on-accent,brand-warm}
│  ├─ border.{subtle,strong,highlight,focus}, status.{success,warning,danger,info}
│  ├─ data.1-6   ← chart series only, never UI chrome
│  └─ logo.{ink,horizon-line,mono,mono-reversed,tile}
├─ font.{family,weight,size}, typography.<style> (composite)
├─ space.0-10, radius.{none,sm,md,lg,xl,full}
├─ shadow.{sm,md,lg}, motion.{duration,easing}
└─ size.{control,icon,focus-ring,hit-target-min}
```
**Rule:** components consume **semantic** tokens (`color.bg.surface`, `color.text.link`) and never `palette.*` or raw hex values. That way, swapping the accent or tuning a surface is a one-line change.

### 2.2 The accent is one token
`color.accent` = `#7DFFFF` is **provisional**. Everything that's "brand-colored" references it: `text.link`, `border.focus`, `bg.accent`, `data.1`, `logo.horizon-line`. To change it, edit `color.accent` (and re-derive `accent-hover`/`accent-pressed`, plus the alpha tint in `bg.accent-subtle`), run `build_tokens.py` to re-check contrast, then `build_logos.py` to re-render the logos (it reads the accent from `tokens.json`). Any new accent must keep ≥4.5:1 against `bg.overlay` (#383838) and ≥4.5:1 under `text.on-accent`.

The accent is locked (`#7DFFFF`) and fully saturated, above the taste-skill guideline of 80% saturation. The compensation is scarcity: one accent use per view, under 10% of the screen, never as a glow, gradient or large fill behind text.

### 2.3 Color (summary)
| Semantic | Value | Use |
|---|---|---|
| `bg.sunken` | #161616 | Inputs, code, 3D viewports, wells |
| `bg.canvas` | #1E1E1E | App background (locked) |
| `bg.surface` | #262626 | Panels, cards, sidebars |
| `bg.raised` | #2E2E2E | Menus, popovers, hover rows |
| `bg.overlay` | #383838 | Dialogs, toasts |
| `text.primary / secondary / muted` | #F2EFE9 / #C7C5C0 / #AAA8A4 | Text hierarchy (AA on every surface) |
| `text.disabled` | #73716D | Disabled controls only |
| `text.link`, `border.focus`, `bg.accent` | → `color.accent` | Brand accent |
| `text.on-accent` | #1E1E1E | Text on accent fills (14.0:1) |
| `border.subtle / strong` | #474747 / #8F8F8F | Dividers (decorative) / control outlines (≥3:1) |
| `border.highlight` | #FFFFFF at 6% | 1 px inner top edge on raised and overlay layers |
| `status.*` | reed #7FD1A0, amber #F2C46D, coral #FF8A80, lake #8DB8D2 | Status, always with an icon and a label |

**One grey family.** Surfaces are pure neutral greys (R = G = B), like professional design software, so users' drawings and models carry the color. Text tiers carry a faint warmth to match the logo ink. No blue-tinted or warm-tinted surface greys; no pure black (#000) and no pure white (#FFF) on screen.

**Elevation logic (dark mode).** On dark, shadows barely read, so depth is built in this order:
1. **Surface step.** sunken #161616 → canvas #1E1E1E → surface #262626 → raised #2E2E2E → overlay #383838. An even ramp of 8 levels per step; higher means closer to the user. Inputs and viewports sink, menus and dialogs rise.
2. **Highlight edge.** Raised and overlay layers get a 1 px `border.highlight` on the inside top edge, the way light catches the top of a step.
3. **Shadow,** secondary only: off-black #0A0A0A (`shadow.sm/md/lg`), never a colored glow.

Prefer spacing over boxes. A card exists only when elevation means something (a draggable item, a selectable option, a floating layer). Lists and settings use spacing and `border.subtle` dividers instead of nested cards.

### 2.4 Typography
| Style | Family | Size/line | Weight | Tracking |
|---|---|---|---|---|
| display | Geist | 48/52 | 600 | -1.2 px |
| h1 | Geist | 36/42 | 600 | -0.7 px |
| h2 | Geist | 28/34 | 600 | -0.3 px |
| h3 | Geist | 22/30 | 600 | 0 |
| h4 | Geist | 18/26 | 600 | 0 |
| body-lg | Geist | 17/28 | 400 | 0 |
| body | Geist | 15/24 | 400 | 0 |
| body-sm | Geist | 13/20 | 400 | 0 |
| caption | Geist | 12/16 | 500 | +0.2 px |
| label | Geist, sentence case | 12/16 | 500 | +0.2 px |
| code | Geist Mono | 13/20 | 400 | 0 |

One family for display and UI (Geist, OFL), one for code and data (Geist Mono). Hierarchy comes from weight and color before size: a 600 heading in `text.primary` over 400 body in `text.secondary`. `label` replaces the old all-caps overline: sentence case, used at most once every three sections, never as a decorative eyebrow above every heading. Turn on tabular numerals (`font-variant-numeric: tabular-nums`) in timesheets, tables and dimensions. Body text max 65 characters per line. For Chinese, use `font.family.cjk` with line height ×1.1 (body 15/26). Where fonts can't be bundled (WPF/Eto plugins), fall back to Segoe UI Variable or SF Pro and keep the scale.

### 2.5 Space, radius, size
- **Space:** 0, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96 px (`space.0` to `space.10`). Component padding uses 8/12/16, section gaps 32/48, page margins 24 (narrow) / 64 (wide).
- **Radius (shape lock):** sm 4 (tags, checkboxes), md 8 (buttons, inputs), lg 12 (cards, panels), xl 16 (dialogs, app icons), full (avatars and status dots only). One radius per component, never mixed within a component. Buttons are not pills.
- **Controls:** sm 28, md 36 (default), lg 44 (touch/AR). The minimum hit target is 24×24 px (WCAG 2.5.8); aim for 36.
- **Icons:** 16/20/24 px, 1.5 px stroke.

### 2.6 Shadow and motion
- `shadow.sm/md/lg`: off-black #0A0A0A at 50-60% alpha with 2/12/32 px blur. Raised and overlay layers only, always together with the surface step.
- **Durations:** fast 120 ms (hover, press), base 200 ms (expand, fade), slow 320 ms (panels, dialogs), calm 480 ms (page or room transitions).
- **Easing:** `standard` (0.2, 0, 0, 1), `enter` (0, 0, 0, 1), `exit` (0.3, 0, 1, 1). No bounce or spring overshoot. Things settle like still water.
- `prefers-reduced-motion: reduce` → durations drop to 0, fades stay ≤120 ms, no parallax.

## 3. Package plan: `packages/design-tokens`
```
packages/design-tokens/
├─ tokens.json                ← this file (source of truth)
├─ build/ (generated, committed for plugin consumers)
│  ├─ css/variables.css       --lh-color-accent: #7dffff; …
│  ├─ js/tokens.mjs + .d.ts   typed ES module for web/desktop (Electron/Tauri)
│  ├─ json/flat.json          flat key→value for anything else
│  ├─ csharp/LhTokens.cs      static class for Revit (WPF) and Rhino (Eto/WPF) plugins
│  └─ xaml/LhTheme.xaml       ResourceDictionary: SolidColorBrush, Thickness, CornerRadius
├─ scripts/build.mjs          Style Dictionary v4 (DTCG support), Apache-2.0, free
└─ scripts/contrast.test.mjs  fails CI if a semantic pair drops below its WCAG target
```
- Prefix: `lh` (`--lh-color-bg-surface`, `LhTokens.Color.BgSurface`).
- Version with semver. Changing a token value is a minor bump; renaming or removing one is major.
- **Revit/Rhino notes:** Revit and Rhino host UIs can be light or dark. Our plugin windows always render in our dark theme (a self-contained ResourceDictionary) and don't inherit host brushes. Dockable panes inside a light host keep `bg.canvas`. For a toolbar or ribbon button icon on a light ribbon, use the **mono** icon (#1E1E1E), the one documented light-context exception.

## 4. Components

### 4.1 General rules
- Every interactive component has these states: default, hover, focus-visible, pressed, disabled, plus loading/error where they apply. Design all of them before shipping.
- Focus: a 2 px `border.focus` (accent) ring with a 2 px offset, always visible on keyboard focus. Never remove outlines.
- At most **one primary (accent) button per view**. Everything else is secondary or ghost.
- Use labels, not placeholders. Placeholder text is a hint only (`text.muted`).
- Lay out spacing in multiples of 4 and stick to the token values.

### 4.2 Core set (v0.1)
| Component | Spec |
|---|---|
| **Button: primary** | `bg.accent` fill, `text.on-accent` label (14.0:1), radius md, height 36, padding 0 16, Geist 600 15. Hover `accent-hover`, pressed `accent-pressed`. Disabled: `bg.raised` + `text.disabled`. |
| **Button: secondary** | Transparent, 1 px `border.strong`, `text.primary`. Hover `bg.raised`. |
| **Button: ghost** | No border, `text.secondary` → `text.primary` on hover. For toolbars. |
| **Button: danger** | 1 px `status.danger` border with a danger label. Fill only inside the confirm dialog. |
| **Input / select** | `bg.sunken` fill, 1 px `border.strong`, radius md, height 36. Focus: accent ring. Error: `status.danger` border, plus a message under the field with an icon. |
| **Checkbox / radio / switch** | Unchecked outline `border.strong`. Checked fill `bg.accent` with a `text.on-accent` (#1E1E1E) glyph. |
| **Card / panel** | `bg.surface`, radius lg, padding 16-24, no border by default (the surface step separates it). Add 1 px `border.subtle` only in dense grids. Never nest cards. |
| **Table / timesheet grid** | Row height 32 (dense) / 40 (comfortable), zebra `bg.surface`/`bg.canvas`, selected row `bg.accent-subtle` with a 2 px accent left bar, tabular numerals, sticky header in `text.muted` label style. |
| **Tabs / room nav** | Text tabs with a 2 px accent underline for the active tab. Room nav uses a Phosphor icon plus the room name; only the active room uses the accent. |
| **Dialog** | `bg.overlay`, radius xl, 1 px `border.highlight` top edge, `shadow.lg`, max width 560. Title in h3. Primary action on the right. Esc closes. Focus is trapped while open and returns to the opener on close. |
| **Toast** | `bg.overlay`, status icon plus text, auto-dismiss after 5 s **unless it contains an action**. Announced via `aria-live="polite"`. |
| **Tooltip** | `bg.raised`, body-sm, delay 400 ms, appears on focus as well as hover. |
| **Empty state** | Line illustration in the house style plus an h3 and one sentence. Say what's missing and what to do, plainly ("No exports yet. Run your first batch export."). No jokes, no cute copy. |
| **Progress** | Determinate bar on an accent track for anything over 2 s. Long Revit/Rhino jobs show "step x of y" and a Cancel button. |

### 4.3 Data visualization
Use `color.data.1` to `color.data.6` in this order: accent #7DFFFF, timber.300 #D4A373, lake.300 #8DB8D2, dusk.300 #F0A98A, reed.300 #7FD1A0, stone.300 #C7C5C0. These are the only place the material colors appear in product UI; one series per chart may be the accent. Draw gridlines in `border.subtle`. Label data directly where possible, and use patterns or labels in addition to color.

## 5. Accessibility
- **Contrast:** text ≥4.5:1, large text and UI parts ≥3:1, verified on all five surfaces (see the table in `BRAND.md` §4 or `contrast-table.md`). `contrast.test` runs in CI.
- **Never use color alone.** Status = icon + word + color. Links in body text are accent **and** underlined.
- **Keyboard:** everything is reachable and operable. Visible focus. Logical tab order. Shortcuts listed in a `?` panel and never overriding host app (Revit/Rhino) shortcuts.
- **Screen readers:** semantic HTML on the web; `AutomationProperties.Name` on WPF controls. Icon-only buttons need labels.
- **Motion:** honor reduced motion. Nothing flashes more than 3 times per second. Ask before starting AR/VR sessions, and offer seated mode and comfort vignette options.
- **Text:** support 200% zoom on the web and OS text scaling on desktop. Never put body text in images.
- **Language:** set `lang="en"` / `lang="zh-Hans"` correctly. Don't use synthetic bold or italic for Chinese.
- **Target sizes:** at least 24 px, 36 px preferred, 44 px in AR/VR and touch contexts.

## 6. Light contexts (the exception)
The product is dark-only. Where a light background is unavoidable (print, a favicon on a light tab, a host ribbon icon, a partner's logo wall), use only the **mono** logo and icons in `#1E1E1E` (`color.logo.mono`, 16.7:1 on white). The accent, color logo and dark-UI screenshots should not be recolored for light.

## 7. Logo in product UI
- The logo is the locked **L1** mark (see `BRAND.md` §3 and `final/`). In app chrome use `lakehouse-mark-transparent.svg` on any graphite surface; never redraw it.
- App and window icons use `lakehouse-appicon.svg` / `final/png/appicon-*.png`; browser tabs use `final/favicon.ico` + `favicon.svg`.
- Archived directions A-D live in `archive/directions-v0/` and must not ship.

## 8. Governance
- The owner is Sen Zhang. Propose token changes via a PR to `packages/design-tokens` with a contrast report.
- Keep `BRAND.md`, `DESIGN-SYSTEM.md` and `WRITING-STYLE.md` in the repo's `brand/` folder, versioned alongside the tokens.

## 8. Pre-flight check (run before shipping any screen or asset)
Adapted from the taste-skill pre-flight.
- [ ] Dials respected: left-aligned, calm motion, density right for the surface (3 marketing, 5 product).
- [ ] Only one accent use per view, under 10% of the screen. No glow, no gradient text.
- [ ] Greys come only from the graphite family. No #000, no #FFF on screen.
- [ ] Elevation reads from the surface step plus the highlight edge; shadows are secondary.
- [ ] Geist and Geist Mono only. No third family, no all-caps eyebrow on every section.
- [ ] One radius system per component; no pills except avatars and status dots.
- [ ] Every interactive element has hover, focus-visible, pressed, disabled, and loading/error where relevant.
- [ ] Copy: zero em or en dashes, middle dot at most once per line, no emoji, no filler verbs (see `WRITING-STYLE.md`).
- [ ] Contrast checked against `contrast-table.md`; status never by color alone.
- [ ] Reduced motion honored.
