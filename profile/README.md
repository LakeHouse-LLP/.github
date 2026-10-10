<p align="center">
  <img src="../brand/final/readme-header.png" alt="LakeHouse Studio" width="640">
</p>

<p align="center"><em>A second home for your design practice.</em></p>

# LakeHouse Studio

LakeHouse Studio is a modular home-office service for designers and agents. Public work splits two ways: **LakeHouse widgets** (load into the desktop/web host) and **general open-source** products (no widget contract). Shared org defaults live here in `.github`.

## In this organization

| Area | Where |
| --- | --- |
| LakeHouse widgets (public) | `Product-LakeHouse-[DescriptiveName]` + scaffold **`Template-LakeHouse-Widget`** |
| General open-source (public) | `Product-LakeHouse-[DescriptiveName]` (or `Package-LakeHouse-*`) + scaffold **`Template-LakeHouse-OpenSource`** |
| Product host (private) | **`Template-LakeHouse-Monorepo`** (host, widget-sdk, catalog) |
| Sandbox starter (private) | **`Template-LakeHouse-Sandbox`** |
| Org defaults (this profile's source) | `.github` |
| Docs (custom domain) | See `domain` in [`.lakehouse/org.json`](../.lakehouse/org.json). Never `*.github.io`. |
| Epics / todos | [SenZhang-Plus/SenZhang-Todo](https://github.com/SenZhang-Plus/SenZhang-Todo) |

**Which template?** See [docs/naming.md](../docs/naming.md#which-template-should-i-use).

**Pinned repos** (Sen): flagship widgets and/or OSS products first, then docs entrypoint, then the relevant public template(s). Strategy: [docs/discoverability.md](../docs/discoverability.md#pinned-repositories).

**Owner:** Sen reviews and merges. Do not merge into `Template-LakeHouse-*` or `.github` without that review.
