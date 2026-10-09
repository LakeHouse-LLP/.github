#!/usr/bin/env bash
# Fail if the current GitHub org login is hardcoded outside the allowlist.
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"
exec python3 scripts/org_name_lint.py "$@"
