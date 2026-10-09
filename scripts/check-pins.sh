#!/usr/bin/env bash
# Verify workflow uses: pins match .lakehouse/pins.json (single source of truth).
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"
PINS=".lakehouse/pins.json"

if [ ! -f "$PINS" ]; then
  echo "::error::Missing ${PINS}"
  exit 1
fi

if ! command -v python3 >/dev/null; then
  echo "::error::python3 required"
  exit 1
fi

python3 - <<'PY'
import json, re, sys
from pathlib import Path

pins = json.loads(Path(".lakehouse/pins.json").read_text())
actions = pins.get("actions", {})
expected = {}
for name, meta in actions.items():
    expected[meta["uses"]] = meta["sha"]

tool_gitleaks = pins.get("tools", {}).get("gitleaks", {})
gitleaks_ver = tool_gitleaks.get("version")
gitleaks_sha = (tool_gitleaks.get("sha256") or {}).get("linux_x64")

workflow_paths = list(Path(".github/workflows").glob("*.yml")) + list(
    Path("workflow-templates").glob("*.yml")
)

uses_re = re.compile(
    r"uses:\s*(?P<action>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@(?P<sha>[0-9a-f]{40})"
)
ver_re = re.compile(r'GITLEAKS_VERSION:\s*"([^"]+)"')
sha_re = re.compile(r'GITLEAKS_SHA256:\s*"([0-9a-f]{64})"')

errors = []
for path in sorted(workflow_paths):
    text = path.read_text()
    for m in uses_re.finditer(text):
        action, sha = m.group("action"), m.group("sha")
        if action not in expected:
            # Allow unpinned third parties only if listed — flag unknown actions with SHAs
            # that aren't in pins as errors so new pins get registered.
            errors.append(f"{path}: action {action}@{sha} not listed in .lakehouse/pins.json")
            continue
        if expected[action] != sha:
            errors.append(
                f"{path}: {action} pinned to {sha}, pins.json expects {expected[action]}"
            )
    if "gitleaks" in path.name or "GITLEAKS_VERSION" in text:
        vm = ver_re.search(text)
        sm = sha_re.search(text)
        if gitleaks_ver and vm and vm.group(1) != gitleaks_ver:
            errors.append(
                f"{path}: GITLEAKS_VERSION={vm.group(1)}, pins.json expects {gitleaks_ver}"
            )
        if gitleaks_sha and sm and sm.group(1) != gitleaks_sha:
            errors.append(f"{path}: GITLEAKS_SHA256 mismatch vs pins.json")

if errors:
    print("::error::Workflow pins do not match .lakehouse/pins.json")
    for e in errors:
        print(e)
    sys.exit(1)

print("check-pins OK — workflows match .lakehouse/pins.json")
PY
