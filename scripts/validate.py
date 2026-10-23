"""Offline checks for required starter-kit files and local Markdown links."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md", "EVENT_CONFIG.md", "SUBMISSION.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SECURITY.md", "LICENSE", "CONTENT-LICENSE.md",
    "docs/participant-guide.md", "docs/submission-guide.md",
    "docs/judging-rubric.md", "docs/mentor-guide.md",
    "docs/organizer-checklist.md", "templates/web-app/README.md",
    "templates/python-cli/README.md", "templates/data-ai/README.md",
    ".github/workflows/validate.yml", ".github/ISSUE_TEMPLATE/submission.yml",
)
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def heading_slugs(text: str) -> set[str]:
    result: set[str] = set()
    counts: dict[str, int] = {}
    for match in HEADING_RE.finditer(text):
        heading = re.sub(r"`([^`]*)`", r"", match.group(1))
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"", heading)
        slug = re.sub(r"[^\w -]", "", heading.lower())
        slug = re.sub(r"\s+", "-", slug.strip())
        if not slug:
            continue
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    return result


def check_links() -> list[str]:
    errors: list[str] = []
    for md in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", ".venv", "node_modules"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip()
            target = raw.split(maxsplit=1)[0].strip("<>") if raw else ""
            parsed = urlparse(target)
            if not target or parsed.scheme or parsed.netloc:
                continue
            path_part = unquote(parsed.path)
            candidate = (md.parent / path_part).resolve() if path_part else md.resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Link escapes repository: {md.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"Broken local link: {md.relative_to(ROOT)} -> {target}")
                continue
            if parsed.fragment and candidate.suffix.lower() == ".md" and candidate.is_file():
                if unquote(parsed.fragment) not in heading_slugs(candidate.read_text(encoding="utf-8")):
                    errors.append(f"Broken Markdown fragment: {md.relative_to(ROOT)} -> {target}")
    return errors


def main() -> int:
    errors = [f"Missing required file: {item}" for item in REQUIRED_FILES if not (ROOT / item).is_file()]
    errors.extend(check_links())
    if errors:
        print("Starter-kit validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Starter-kit validation passed: required files and local Markdown links are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
