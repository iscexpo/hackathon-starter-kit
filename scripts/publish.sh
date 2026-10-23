#!/usr/bin/env bash
set -euo pipefail

REPO="iscexpo/hackathon-starter-kit"
DESCRIPTION="Project templates, participant guides, submission instructions, and judging rubrics for ISC Expo hackathons."

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it and run: gh auth login" >&2
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "Please authenticate first using: gh auth login" >&2
  exit 1
fi
if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository $REPO already exists. This script will not overwrite it." >&2
  exit 1
fi

if [ ! -d .git ]; then
  git init -b main
fi
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  GIT_NAME="${GIT_AUTHOR_NAME:-$(git config user.name || true)}"
  GIT_EMAIL="${GIT_AUTHOR_EMAIL:-$(git config user.email || true)}"
  if [ -z "$GIT_NAME" ] || [ -z "$GIT_EMAIL" ]; then
    echo "Configure git user.name and user.email, or set GIT_AUTHOR_NAME and GIT_AUTHOR_EMAIL, before publishing." >&2
    exit 1
  fi
  git add -A
  git -c user.name="$GIT_NAME" -c user.email="$GIT_EMAIL" \
      commit -m "chore: initialize hackathon starter kit"
elif [ -n "$(git status --porcelain)" ]; then
  echo "Working tree has uncommitted changes. Commit or stash them before publishing." >&2
  exit 1
fi

gh repo create "$REPO" --public --source . --remote origin --push --description "$DESCRIPTION"
echo "Published $REPO as a public repository."
echo "Review the Actions tab and configure branch protection before accepting contributions."
