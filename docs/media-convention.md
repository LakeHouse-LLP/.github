# `docs/media/` convention (templates and product repos)

Every **Template-LakeHouse-*** and product repo should use `docs/media/` for screenshots and demos referenced from the README and docs.

## Layout

```text
docs/media/
  README.md          # alt-text index + what each file shows
  screenshots/       # PNG/WebP stills
  demos/             # short GIF or MP4
```

## Rules

| Rule | Detail |
| --- | --- |
| Alt text | Required for every still in docs; keep a short description in `docs/media/README.md` |
| File size | Prefer stills ≤ **1 MB**; GIFs ≤ **5 MB**; longer MP4 → **Git LFS** or **release assets**, not fat git history |
| Large media | Use Git LFS or attach to the GitHub Release; link from docs |
| Content | Show **this** product, place, or atmosphere |
| Never | Client work, **Ennead** content, secrets, personal data, or watermarks from third parties without license |
| Formats | PNG/WebP for UI; GIF/MP4 for short demos |

## README usage

Reference media with relative links from the repo README. Org-level brand logos live in the defaults repo [`brand/`](../brand/); product screenshots stay in that product’s `docs/media/`.

## This defaults repo

Org brand placeholders live under [`brand/`](../brand/) (not `docs/media/`). Product templates should still include an empty `docs/media/` with a short README when instantiated.
