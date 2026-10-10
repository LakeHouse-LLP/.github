# Discoverability standard (org + public templates)

Zero-cost GitHub-side SEO for **LakeHouse Studio**. Brand tokens: dark-only, accent `#7DFFFF` ([`brand/`](../brand/)). Domain from [`.lakehouse/org.json`](../.lakehouse/org.json) - never `*.github.io`.

Scope: this `.github` defaults repo, **Template-LakeHouse-Widget**, **Template-LakeHouse-OpenSource**, and public repos created from either. Naming / chooser: [naming.md](naming.md).

| Public kind | Template | SEO angle |
| --- | --- | --- |
| LakeHouse **widget** | Template-LakeHouse-Widget | Loadable widget for the LakeHouse host; agent-friendly |
| General **open-source** | Template-LakeHouse-OpenSource | Normal OSS product - **no** widget/`widget.json` wording |

## Repository description

- One or two sentences; lead with **LakeHouse Studio** or the product/widget name.
- Widgets: say it is a **widget** for the LakeHouse office. OSS: say what the tool is - do not mention widgets or the host.
- No client names, no “WIP” as the permanent blurb.

## Topics (8-20)

Use **8 to 20** relevant lowercase topics. Prefer brand + domain keywords over the GitHub org login (rename-safe).

**Shared pool:** `lakehouse-studio`, `lakehouse`, `design-tools`, `typescript`, `opensource`, plus stack tags.

**Widget repos (add):** `widget`, `widgets`, `agent-friendly`, and domain tags (`revit`, `rhino`, `grasshopper`, `bim`, `aec`, `architecture`, `indesign`, …) when relevant.

**Template-LakeHouse-OpenSource / non-widget OSS:** use the shared pool + domain tags; **omit** `widget` / `widgets` unless the project truly is unrelated software that happens to use that word.

CI enforces the count via the discoverability check (see below).

## README first paragraph

Keyword-rich and human:

- **Widgets:** name the widget + LakeHouse Studio; say forkable/loadable into the office; audience (designers / small offices / agents).
- **OSS (Template-LakeHouse-OpenSource):** name the product; category and audience; **no** LakeHouse widget/host contract language.

## Social preview

- Upload **1280×640** [`brand/final/social-preview.png`](../brand/final/social-preview.png) (or a product-specific dark variant from the kit).
- Dark graphite canvas only; accent `#7DFFFF`; no client/Ennead content.

## Homepage URL

- Set the repo **Website** field to a path on `domain` from `org.json`.
- Until the placeholder is replaced, Sen may leave it empty - never use `*.github.io`.

## Releases help ranking

Ship **regular tagged releases** ([releasing.md](releasing.md)). Widgets should attach loadable bundles + `widget.json` when applicable. OSS products follow normal SemVer assets.

## CITATION.cff

Citable public repos should include a root [`CITATION.cff`](../CITATION.cff). Keep branding aligned with **LakeHouse Studio** where appropriate.

## Pinned repositories

Sen pins up to six org repos. Recommended order:

1. Flagship **public widget** and/or **OSS product** repo(s)  
2. **Docs site** entrypoint (when it exists)  
3. `Template-LakeHouse-Widget` and/or `Template-LakeHouse-OpenSource` (as scaffolds you want people to find)  
4. Keep `Template-LakeHouse-Monorepo` / sandboxes unpinned (private)

Do not pin `sandbox-*`, `legacy-*`, or empty squat leftovers. Revisit pins when a launch checklist item ships ([launch-checklist.md](launch-checklist.md)).

## Org profile README

Source: [`profile/README.md`](../profile/README.md).

- Lead with **LakeHouse Studio**; mention **both** public paths (widgets + general OSS).
- Link the [which template](naming.md#which-template-should-i-use) guide.
- Keep it short; details live in product/widget READMEs.

## CI check

Workflow template: `workflow-templates/discoverability-check.yml`  
Script: `node scripts/discoverability-check.mjs`

Validates README first paragraph presence/length, and (on GitHub Actions) repository **description** + **topics** count via `gh api` / `GITHUB_TOKEN`.
