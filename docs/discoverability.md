# Discoverability standard (org + Template-OpenSource)

Zero-cost GitHub-side SEO for **LakeHouse Studio**. Brand tokens: dark-only, accent `#7DFFFF` ([`brand/`](../brand/)). Domain from [`.lakehouse/org.json`](../.lakehouse/org.json) — never `*.github.io`.

Scope: this `.github` defaults repo and **Template-OpenSource** (and public OSS repos created from it).

## Repository description

- One or two sentences; lead with **LakeHouse Studio** or the product name.
- Include what it is + who it is for (designers / small offices / AEC tooling as relevant).
- No client names, no “WIP” as the permanent blurb.

## Topics (8–20)

Use **8 to 20** relevant lowercase topics. Prefer brand + domain keywords over the GitHub org login (rename-safe).

Suggested pool (pick what fits; do not stuff all of them):

`lakehouse-studio`, `lakehouse`, `revit`, `rhino`, `grasshopper`, `bim`, `aec`, `architecture`, `indesign`, `design-tools`, `typescript`, `dotnet`, `opensource`, `monorepo`

CI enforces the count via the discoverability check (see below).

## README first paragraph

The **first paragraph** after the title/logo must be keyword-rich and human:

- Name the product (**LakeHouse Studio** or repo product name).
- State the category (e.g. digital office / design tools / Revit–Rhino utilities).
- Name the audience (designers and small offices).
- Avoid marketing fluff with no nouns searchers use.

## Social preview

- Upload **1280×640** [`brand/social-preview.png`](../brand/social-preview.png) (or a product-specific dark variant).
- Dark canvas only; accent `#7DFFFF`; no client/Ennead content.

## Homepage URL

- Set the repo **Website** field to a path on `domain` from `org.json`.
- Until the placeholder is replaced, Sen may leave it empty — never use `*.github.io`.

## Releases help ranking

Ship **regular tagged releases** ([releasing.md](releasing.md)). Fresh releases improve GitHub search and social trust. Prefer small, frequent SemVer releases over rare megadumps.

## CITATION.cff

Public research-adjacent or citable tools should include a root [`CITATION.cff`](../CITATION.cff) (see Template-OpenSource). Keep `title` / `alias` aligned with **LakeHouse Studio** branding.

## Pinned repositories

Sen pins up to six org repos. Recommended order:

1. Flagship **open-source product** repo(s) users should try first  
2. **Docs site** repo or the repo that hosts the org docs entrypoint (when it exists)  
3. `Template-OpenSource` (contribution / fork entry)  
4. Optionally `Template-Monorepo` if advertising the stack  

Do not pin `sandbox-*`, `legacy-*`, or empty squat leftovers. Revisit pins when a launch checklist item ships ([launch-checklist.md](launch-checklist.md)).

## Org profile README

Source: [`profile/README.md`](../profile/README.md).

- Lead with **LakeHouse Studio** positioning: all-in-one digital office for designers and small offices; warm lakeside home-office feel.
- Link docs via custom `domain`, defaults repo, and SenZhang-Todo.
- Keep it short; details live in product READMEs.

## CI check

Workflow template: `workflow-templates/discoverability-check.yml`  
Script: `node scripts/discoverability-check.mjs`

Validates README first paragraph presence/length, and (on GitHub Actions) repository **description** + **topics** count via `gh api` / `GITHUB_TOKEN`.
