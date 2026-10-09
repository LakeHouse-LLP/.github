# SEO checklist (reusable)

Use for `Template-Widget`, `Template-OpenSource`, their public descendants, and the org docs site. Pair with [discoverability.md](discoverability.md) and [docs-site.md](docs-site.md). Match README/topics language to the template kind (widget vs general OSS).

## GitHub repo

- [ ] Description set (keyword-rich, audience-clear)
- [ ] **8–20** topics from the approved pool
- [ ] README logo (dark) + **keyword-rich first paragraph**
- [ ] Social preview **1280×640** uploaded
- [ ] Homepage = path on `domain` (not `*.github.io`)
- [ ] `CITATION.cff` when the tool is citable
- [ ] Regular SemVer **releases**
- [ ] Discoverability CI check green

## Docs site pages

- [ ] Unique title + meta description
- [ ] Canonical URL on custom domain
- [ ] OG/Twitter cards
- [ ] JSON-LD (`Organization` / `SoftwareApplication` as relevant)
- [ ] In `sitemap.xml`; allowed by `robots.txt`
- [ ] Dark-only; accent `#7DFFFF`
- [ ] Images have alt text; no client/Ennead content
- [ ] Lighthouse accessibility/performance budget (if free CI enabled)

## Off-site

- [ ] Search Console + Bing verified ([search-and-analytics.md](search-and-analytics.md))
- [ ] Privacy-friendly analytics receiving page views
- [ ] Awesome-list submissions where appropriate ([awesome-lists.md](awesome-lists.md))
- [ ] Launch channels considered ([launch-checklist.md](launch-checklist.md))
