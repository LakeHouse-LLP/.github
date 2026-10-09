# Org rename runbook

How to rename the GitHub organization away from the login stored in [`.lakehouse/org.json`](../.lakehouse/org.json) (`orgName`). **Sen-only** for org settings; agents must not rename the org.

Brand (`brand`), package scope (`packageScope`), and public `domain` are **stable** and must not be renamed with the org. Package scope is brand-based (`@lakehouse`), never derived from `orgName`. Public links use the custom `domain` — never `*.github.io`.

The current login may appear in this runbook and other allowlisted files only. Everywhere else, prefer `org.json` or `${{ github.repository_owner }}`.

## Before

1. **Freeze publishing** — pause npm/container publishes, Pages deploys, and release automation that embeds org URLs.
2. **Inventory repositories** — list all repos under the current `orgName` (templates, public widgets, `sandbox-*`, `legacy-*`, this defaults repo).
3. **Runners** — inventory self-hosted runners (private repos only). Note labels and which repos use them. Public repos must stay on GitHub-hosted runners.
4. **Webhooks** — export webhook URLs/secrets per repo and org hooks.
5. **GitHub Apps** — list installed Apps and their repo access; plan re-auth after rename.
6. **Package scopes** — confirm registry packages use `packageScope` from `org.json` (not the org login). Note any legacy packages that incorrectly used the org name.
7. **GitHub Pages** — list sites and their **custom domain** (`domain` in `org.json`). Do not rely on `*.github.io`.
8. **Secrets & variables** — inventory org and repo secrets/variables (names only in public notes). Plan re-create if GitHub drops any on rename.
9. **External links** — badges, docs, Terraform, CI `uses:` literals that still embed the old login (should be none outside the allowlist after this scaffold).

## During

1. GitHub → Organization settings → **Rename organization** (Sen).
2. Choose the new login; confirm GitHub’s redirect behavior for the old URL.
3. Do **not** change `brand`, `packageScope`, or `domain` unless the brand itself is changing (separate decision).
4. Keep merge policy (merge commits only) and runner tier rules unchanged.

## After

1. **Squat the old org name immediately** — create an empty GitHub organization with the **previous** login so others cannot claim it. Leave it empty (no repos required). Record that name in [`retired-names.txt`](../retired-names.txt) (org login retirement note).
2. **Update `org.json`** — set `orgName` to the new login. Leave `brand` / `packageScope` / `domain` stable.
3. **Pages custom domain** — re-verify DNS and Pages custom domain settings for `domain` (still not `*.github.io`).
4. **Re-check runners** — self-hosted runners re-associate to the renamed org; confirm private repos still hit self-hosted and public still GitHub-hosted (`tier-guard`).
5. **Re-check webhooks** — repair delivery URLs that embedded the old login.
6. **Re-check GitHub Apps** — reinstall or repair App installations on the renamed org.
7. **Re-check package scopes** — publishing continues under `packageScope`; fix any leftover org-login-scoped packages.
8. **Update allowlisted docs** — `retired-names.txt`, this runbook’s “current example” notes if needed, and `CHANGELOG.md`.
9. **Run lints** — `node scripts/org-name-lint.mjs` and `node scripts/check-pins.mjs` must pass. Callers of reusable workflows that required a literal `uses: <org>/...` string must be updated to the new login (see [`.lakehouse/pins.json`](../.lakehouse/pins.json)).
10. **Unfreeze publishing** once inventory checks pass.

## Notes

- Epics remain in SenZhang-Plus/SenZhang-Todo (outside this org).
- There is no second owner and no auto-archive.
- Draft PRs only into `Template-*` and `.github` unless Sen merges.
