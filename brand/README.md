# LakeHouse Studio brand kit (v0.3)

Canonical brand assets and docs. **Dark mode only** (default theme). Semantic skins are a higher layer. Locked: L1 mark, Geist / Geist Mono, grey ramp `#161616` / `#1E1E1E` / `#262626` / `#2E2E2E` / `#383838`, accent `#7DFFFF`, tagline *A second home for your design practice.*

| Path | Purpose |
| --- | --- |
| [BRAND.md](BRAND.md) | Identity, mark rules, asset map |
| [DESIGN-SYSTEM.md](DESIGN-SYSTEM.md) | Components and layout |
| [DESIGN.md](DESIGN.md) | Design dials and taste notes |
| [WRITING-STYLE.md](WRITING-STYLE.md) | Voice, banned words, no em dashes |
| [tokens.json](tokens.json) | DTCG tokens (source of truth) |
| [contrast-table.md](contrast-table.md) | Contrast checks |
| [final/](final/) | Shipping assets (SVG/PNG/ICO) |
| `build_tokens.py`, `build_logos.py`, `contrast.py` | Brand tooling (Python) |

## Build scripts (brand tooling, not repo automation)

These regenerate tokens/logos when designers edit sources. They are **Python on purpose** (brand pipeline), not the Node `.mjs` house scripts used for CI.

```bash
# From brand/
python build_tokens.py
python build_logos.py
```

Do not call them from GitHub Actions unless Sen asks. Everyday contributors consume `final/` and `tokens.json` as committed outputs.

## Key deliverables in `final/`

| File | Use |
| --- | --- |
| `readme-header.png` / `.svg` | README / profile banner (1280×320) |
| `social-preview.png` / `.svg` | GitHub social preview (1280×640) |
| `favicon.ico`, `favicon.svg`, `favicon-{16,32,48}.png` | Site / app favicons |
| `favicon-mono.svg` | Light browser tabs only |
| `lakehouse-mark.svg` | L1 mark (color on dark) |
| `lakehouse-appicon.svg`, `png/appicon-*.png` | App icon / **org avatar** source |
| `png/` | Raster exports at multiple sizes |

## Favicon guidance

- Prefer `final/favicon.svg` plus `final/favicon.ico` in web apps.
- Ship PNG fallbacks (`favicon-16.png`, `favicon-32.png`, `favicon-48.png`).
- On unavoidable light tabs, use `favicon-mono.svg` (never put `#7DFFFF` on light chrome).

## Social preview guidance

- Upload `final/social-preview.png` (1280×640) in each public repo: **Settings → General → Social preview**.
- Do not use client or Ennead imagery. Keep the dark graphite + L1 composition from the kit.

## Sen-only (GitHub UI)

See [docs/sen-only-github-settings.md](../docs/sen-only-github-settings.md#brand-assets-github-ui):

1. **Org avatar:** upload `brand/final/png/appicon-1024.png` (square app icon).
2. **Per-repo social preview:** upload `brand/final/social-preview.png`.
