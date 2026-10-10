# Repository naming & which template to use

## Naming pattern

Durable repos use:

```text
[Category]-LakeHouse-[DescriptiveName]
```

**Long and clear beats ambiguous.** Prefer a full descriptive segment over a short opaque name.

| Category | Meaning | Examples |
| --- | --- | --- |
| **Template** | Scaffold used to create other repos | `Template-LakeHouse-Widget`, `Template-LakeHouse-Monorepo` |
| **Package** | Shared library / publishable package | `Package-LakeHouse-Logger` |
| **Product** | Shippable product or widget app | `Product-LakeHouse-[DescriptiveName]` |

### Exceptions

| Pattern | Rule |
| --- | --- |
| **`.github`** | Org defaults repo (this repository). Not renamed to the Category-LakeHouse form. |
| **`sandbox-*`** | Disposable private experiments. Stay private. |
| **`legacy-*`** | Disposable private absorb / archive workspaces. Stay private. |

Do not create new repos that reuse names in [retired-names.txt](../retired-names.txt).

Both public templates inherit shared guardrails, release, SEO, contributor setup, and `org.json` / pins via this `.github` repo’s reusable workflows and docs. They differ in **product shape**, not in org policy.

## The four templates

| Template | Visibility | Use for |
| --- | --- | --- |
| **Template-LakeHouse-Monorepo** | Private | LakeHouse product host - widgets catalog, `@lakehouse/widget-sdk`, desktop/web office, private extensibility. |
| **Template-LakeHouse-Sandbox** | Private | Disposable experiments; not for shipping or pinning. |
| **Template-LakeHouse-Widget** | Public | LakeHouse-**extensible widgets** for the LakeHouse desktop/web host. One widget per derived public repo (`Product-LakeHouse-[DescriptiveName]`). |
| **Template-LakeHouse-OpenSource** | Public | General-purpose open-source project - **no** LakeHouse widget concepts (`widget.json`, host bridge, etc.). For non-LakeHouse products (`Product-LakeHouse-[DescriptiveName]` or a clear Package name when it is a library). |

Retired short template names (`Template-Monorepo`, `Template-Sandbox`, `Template-Widget`, `Template-OpenSource`): see [retired-names.txt](../retired-names.txt) (renamed **2026-10-10**).

## Which template should I use?

```text
Shipping something for the LakeHouse desktop/web host?
  └─ Yes → Is it a loadable widget (manifest, sandbox, host permissions)?
        ├─ Yes → Template-LakeHouse-Widget  (public) → Product-LakeHouse-[DescriptiveName]
        └─ No, it's the host / SDK / catalog itself
              → Template-LakeHouse-Monorepo  (private)
  └─ No → Is it a throwaway experiment?
        ├─ Yes → Template-LakeHouse-Sandbox  (private) or sandbox-*
        └─ No → Shared publishable library?
              ├─ Yes → Package-LakeHouse-[DescriptiveName] (from Template-LakeHouse-OpenSource when OSS)
              └─ No → General open-source product (no LakeHouse widget contract)
                    → Template-LakeHouse-OpenSource  (public) → Product-LakeHouse-[DescriptiveName]
```

| If you need… | Choose |
| --- | --- |
| `widget.json`, host SDK, load into LakeHouse office | **Template-LakeHouse-Widget** |
| Non-LakeHouse library, CLI, site, or tool | **Template-LakeHouse-OpenSource** |
| Private product monorepo / widget-sdk source | **Template-LakeHouse-Monorepo** |
| Scratch space you will delete | **Template-LakeHouse-Sandbox** or `sandbox-*` |

Do **not** put widget manifests or `@lakehouse/widget-sdk` into Template-LakeHouse-OpenSource descendants. Do **not** strip the widget contract from Template-LakeHouse-Widget descendants and call them “just OSS” - use Template-LakeHouse-OpenSource instead.

## Public repo kinds

| Kind | From template | Notes |
| --- | --- | --- |
| Public **widget** | Template-LakeHouse-Widget | Agent-friendly; create → customize → load into office. Dark-only, accent `#7DFFFF`. Depend on published `@lakehouse/widget-sdk` - never vendor. Name: `Product-LakeHouse-[DescriptiveName]`. |
| Public **OSS product** | Template-LakeHouse-OpenSource | Normal open-source project. Same org CI/docs/release/SEO/contributor defaults; **zero** LakeHouse widget concepts. Name: `Product-LakeHouse-[DescriptiveName]` (or `Package-LakeHouse-[DescriptiveName]` when it is a library). |

## Shared inheritance (both public templates)

- Org house rules: [AGENTS.md](../AGENTS.md), [CONTRIBUTING.md](../CONTRIBUTING.md), [GOVERNANCE.md](../GOVERNANCE.md)
- Identity / domain: [`.lakehouse/org.json`](../.lakehouse/org.json)
- Pins / workflows: [`.lakehouse/pins.json`](../.lakehouse/pins.json), `workflow-templates/`
- Release / SEO / contributors: [releasing.md](releasing.md), [discoverability.md](discoverability.md), starter issues & listings
