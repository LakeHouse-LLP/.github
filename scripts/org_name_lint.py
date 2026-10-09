#!/usr/bin/env python3
"""Fail if hardcoded org login strings appear outside the allowlist."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from fnmatch import fnmatch
from pathlib import Path

# Built in pieces so this file does not itself contain the forbidden org-login literals.
_PATTERN_SRC = "LakeHouse" + "-LLP|lakehouse" + "-llp"
PATTERN = re.compile(_PATTERN_SRC)
ALLOWLIST_FILE = Path(
    os.environ.get("ORG_NAME_LINT_ALLOWLIST", ".lakehouse/org-name-lint-allowlist.txt")
)


def load_allowlist(path: Path) -> list[str]:
    if not path.is_file():
        print(f"::error::Missing allowlist: {path}", file=sys.stderr)
        sys.exit(1)
    patterns: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        patterns.append(s)
    return patterns


def repo_root() -> Path:
    try:
        return Path(
            subprocess.check_output(
                ["git", "rev-parse", "--show-toplevel"], text=True
            ).strip()
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return Path.cwd()


def list_files(root: Path) -> list[Path]:
    try:
        out = subprocess.check_output(
            ["git", "ls-files", "-z", "-c", "-o", "--exclude-standard"],
            cwd=root,
        )
        rels = [p for p in out.decode().split("\0") if p]
        return [root / p for p in rels]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]


def allowed(rel: str, patterns: list[str]) -> bool:
    return any(fnmatch(rel, pat) or rel == pat for pat in patterns)


def main() -> int:
    root = repo_root()
    patterns = load_allowlist(root / ALLOWLIST_FILE)
    hits: list[str] = []

    for path in list_files(root):
        rel = path.relative_to(root).as_posix()
        if allowed(rel, patterns):
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if b"\0" in data[:8192]:
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if PATTERN.search(line):
                hits.append(f"{rel}:{i}:{line}")

    if hits:
        print("::error::Hardcoded org login found outside allowlist.")
        print(f"Pattern: /{_PATTERN_SRC}/")
        print("Prefer .lakehouse/org.json (orgName) or ${{ github.repository_owner }}.")
        print(f"Allowed paths: {ALLOWLIST_FILE}")
        print()
        print("\n".join(hits))
        return 1

    print("org-name-lint OK (no disallowed matches).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
