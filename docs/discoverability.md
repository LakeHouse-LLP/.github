# Discoverability standard (org + Template-Widget)

Zero-cost GitHub-side SEO for **LakeHouse Studio**. Brand tokens: dark-only, accent `#7DFFFF` ([`brand/`](../brand/)). Domain from [`.lakehouse/org.json`](../.lakehouse/org.json) — never `*.github.io`.

Scope: this `.github` defaults repo, **Template-Widget**, and **public widget** repos created from it (one standalone agent-friendly widget per repo). Naming: [naming.md](naming.md).

## Repository description

- One or two sentences; lead with **LakeHouse Studio** or the **widget** name.
- Say it is a **widget** (loadable into the designer office) and who it is for (designers / small offices / agents).
- No client names, no “WIP” as the permanent blurb.

## Topics (8–20)

Use **8 to 20** relevant lowercase topics. Prefer brand + widget keywords over the GitHub org login (rename-safe).

Suggested pool (pick what fits; do not stuff all of them):

`lakehouse-studio`, `lakehouse`, `widget`, `widgets`, `design-tools`, `revit`, `rhino`, `grasshopper`, `bim`, `aec`, `architecture`, `indesign`, `typescript`, `agent-friendly`, `opensource`

CI enforces the count via the discoverability check (see below).

## README first paragraph

The **first paragraph** after the title/logo must be keyword-rich and human:

- Name the **widget** and **LakeHouse Studio**.
- State that it is a standalone, forkable **widget** for the digital office / agents.
- Name the audience (designers and small offices).
- Avoid marketing fluff with no nouns searchers use.

## Social preview

- Upload **1280×640** [`brand/social-preview.png`](../brand/social-preview.png) (or a widget-specific dark variant).
- Dark canvas only; accent `#7DFFFF`; no client/Ennead content.

## Homepage URL

- Set the repo **Website** field to a path on `domain` from `org.json`.
- Until the placeholder is replaced, Sen may leave it empty — never use `*.github.io`.

## Releases help ranking

Ship **regular tagged releases** ([releasing.md](releasing.md)) with loadable widget bundles + `widget.json` when applicable. Fresh releases improve GitHub search and social trust.

## CITATION.cff

Citable widgets should include a root [`CITATION.cff`](../CITATION.cff) (see Template-Widget). Keep `title` / `alias` aligned with **LakeHouse Studio** branding.

## Pinned repositories

Sen pins up to six org repos. Recommended order:

1. Flagship **public widget** repo(s) users or agents should try first  
2. **Docs site** repo or the repo that hosts the org docs entrypoint (when it exists)  
3. `Template-Widget` (fork / scaffold entry)  
4. Optionally advertise the private host only if Sen wants that visibility (usually keep private)

Do not pin `sandbox-*`, `legacy-*`, or empty squat leftovers. Revisit pins when a launch checklist item ships ([launch-checklist.md](launch-checklist.md)).

## Org profile README

Source: [`profile/README.md`](../profile/README.md).

- Lead with **LakeHouse Studio** as a modular digital office; public widgets + private host.
- Link docs via custom `domain`, defaults repo, and SenZhang-Todo.
- Keep it short; details live in widget READMEs.

## CI check

Workflow template: `workflow-templates/discoverability-check.yml`  
Script: `node scripts/discoverability-check.mjs`

Validates README first paragraph presence/length, and (on GitHub Actions) repository **description** + **topics** count via `gh api` / `GITHUB_TOKEN`.
