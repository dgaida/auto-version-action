# Getting Started

This guide will help you integrate the Auto Version Action into your repository.

## Prerequisites

- A Python project with a `pyproject.toml`.
- GitHub Actions are enabled.

## Setup

1. Create a new workflow file at `.github/workflows/docs.yml`.
2. Add the action to your steps:

```yaml
jobs:
  maintenance:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Auto Version and Badges
        uses: dgaida/auto-version-action@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

3. Commit and push the file. The action will now run on every push to the main branch.
