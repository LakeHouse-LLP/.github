# LakeHouse Studio

**An all-in-one digital office for designers and small offices** — the calm of a warm lakeside home office, without the tool sprawl.

LakeHouse Studio is a modular home-office service for designers and agents. The core is dynamic UI/UX: **public widget repos** you (or your agents) can fork and customize, loaded into the private product host.

## In this organization

| Area | Where |
| --- | --- |
| Public widgets | Standalone plain-named repos + scaffold `Template-Widget` |
| Product host (private) | `Template-Monorepo` — hosts widgets, widget-sdk, catalog |
| Sandbox starter | `Template-Sandbox` |
| Org defaults (this profile’s source) | `.github` |
| Docs (custom domain) | See `domain` in [`.lakehouse/org.json`](../.lakehouse/org.json) — never `*.github.io` |
| Epics / todos | [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo) |

**How it fits together:** use the product directly, or have agents fork a public widget, customize it, and load it into your designer office. Naming: [docs/naming.md](../docs/naming.md).

**Pinned repos** (Sen maintains the pin list): flagship public widgets first, then the docs entrypoint, then `Template-Widget`. Strategy: [docs/discoverability.md](../docs/discoverability.md#pinned-repositories).

**Owner:** Sen reviews and merges. Do not merge into `Template-*` or `.github` without that review.
