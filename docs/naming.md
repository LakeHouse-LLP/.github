# Repository naming & which template to use

Both public templates inherit shared guardrails, release, SEO, contributor setup, and `org.json` / pins via this `.github` repo’s reusable workflows and docs. They differ in **product shape**, not in org policy.

## The four templates

| Template | Visibility | Use for |
| --- | --- | --- |
| **Template-Monorepo** | Private | LakeHouse product host — widgets catalog, `@lakehouse/widget-sdk`, desktop/web office, private extensibility. |
| **Template-Sandbox** | Private | Disposable experiments; not for shipping or pinning. |
| **Template-Widget** | Public | LakeHouse-**extensible widgets** for the LakeHouse desktop/web host. One widget per derived public repo (plain name). |
| **Template-OpenSource** | Public | Plain **general-purpose** open-source project — **no** LakeHouse widget concepts (`widget.json`, host bridge, etc.). For non-LakeHouse products. |

Derived public repos use **plain names** (not `Template-*` / `sandbox-*` / `legacy-*`). Disposable private: `sandbox-*`, `legacy-*`. Org defaults: `.github`.

Retired names: [retired-names.txt](../retired-names.txt).  
History: on **2026-10-09** an earlier `Template-OpenSource` repo was renamed to `Template-Widget`; `Template-OpenSource` was then **recreated** as the non-widget OSS template (name is active — not retired).

## Which template should I use?

```text
Shipping something for the LakeHouse desktop/web host?
  └─ Yes → Is it a loadable widget (manifest, sandbox, host permissions)?
        ├─ Yes → Template-Widget  (public) → fork/create plain-named widget repo
        └─ No, it's the host / SDK / catalog itself
              → Template-Monorepo  (private)
  └─ No → Is it a throwaway experiment?
        ├─ Yes → Template-Sandbox  (private)
        └─ No → General open-source (no LakeHouse widget contract)
              → Template-OpenSource  (public) → plain-named product repo
```

| If you need… | Choose |
| --- | --- |
| `widget.json`, host SDK, load into LakeHouse office | **Template-Widget** |
| Non-LakeHouse library, CLI, site, or tool | **Template-OpenSource** |
| Private product monorepo / widget-sdk source | **Template-Monorepo** |
| Scratch space you will delete | **Template-Sandbox** |

Do **not** put widget manifests or `@lakehouse/widget-sdk` into Template-OpenSource descendants. Do **not** strip the widget contract from Template-Widget descendants and call them “just OSS” — use Template-OpenSource instead.

## Public repo kinds

| Kind | From template | Notes |
| --- | --- | --- |
| Public **widget** | Template-Widget | Agent-friendly; fork → customize → load into office. Dark-only, accent `#7DFFFF`. Depend on published `@lakehouse/widget-sdk` — never vendor. |
| Public **OSS product** | Template-OpenSource | Normal open-source project. Same org CI/docs/release/SEO/contributor defaults; **zero** LakeHouse widget concepts. |

## Shared inheritance (both public templates)

- Org house rules: [AGENTS.md](../AGENTS.md), [CONTRIBUTING.md](../CONTRIBUTING.md), [GOVERNANCE.md](../GOVERNANCE.md)
- Identity / domain: [`.lakehouse/org.json`](../.lakehouse/org.json)
- Pins / workflows: [`.lakehouse/pins.json`](../.lakehouse/pins.json), `workflow-templates/`
- Release / SEO / contributors: [releasing.md](releasing.md), [discoverability.md](discoverability.md), starter issues & listings
