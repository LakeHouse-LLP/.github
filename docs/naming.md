# Repository naming

| Kind | Pattern | Visibility | Notes |
| --- | --- | --- | --- |
| Widget template | `Template-Widget` | Public | Scaffold for one standalone, agent-friendly widget. Formerly `Template-OpenSource` (retired). |
| Product host | `Template-Monorepo` | Private | LakeHouse product; hosts widgets, `packages/widget-sdk`, catalog. |
| Sandbox template | `Template-Sandbox` | Private | Disposable experiments. |
| Org defaults | `.github` | Public | This repo — shared community health, workflows, docs. |
| Public widgets | **Plain names** | Public | One repo = one widget service (forkable, contributable). Not `Template-*` / `sandbox-*` / `legacy-*`. |
| Disposable | `sandbox-*`, `legacy-*` | Private | Throwaway; do not pin or list. |

Retired names must not be reused — see [retired-names.txt](../retired-names.txt).

## Public widgets

Each **public** repo is a standalone, **agent-friendly widget**:

- Community can contribute, fork, modify, or bring their own.
- Agents fork → customize → load into a designer office (host product).
- Depend on published `@lakehouse/widget-sdk` (scope from `.lakehouse/org.json`); never vendor the SDK.
- Dark-mode only; accent `#7DFFFF`.

Architecture details for the host live in Template-Monorepo (`docs/architecture/widgets.md` there). Org SEO/contributor defaults for widgets: [discoverability.md](discoverability.md), [CONTRIBUTING.md](../CONTRIBUTING.md).
