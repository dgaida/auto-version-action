# GitHub Actions Collection

This repository provides useful GitHub Actions for repository maintenance.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dgaida/auto-version-action/graphs/commit-activity)
![Last commit](https://img.shields.io/github/last-commit/dgaida/auto-version-action)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Actions

### 1. Add Badges

Automatically detects repository features and adds relevant badges to your `README.md`.

#### Features
It checks for and adds the following badges if they apply:
- **Version**: Detects version from `pyproject.toml` or `package.json`.
- **Python Version**: Detects required Python version.
- **License**: Adds MIT license badge if an MIT license is detected.
- **Codecov**: Adds badge if Codecov is used.
- **GitHub Workflows**: Adds badges for `lint`, `tests`, and `codeql` workflows if they exist.
- **Code Style**: Adds badges for `black` or `ruff` if they are used.
- **Documentation**: Adds a Docs badge if GitHub Pages is enabled or a `docs/` folder exists.
- **Maintenance**: Adds badges for maintenance status and last commit.

#### Usage
Create a workflow file (e.g., `.github/workflows/add-badges.yml`):

```yaml
name: Add Badges
on:
  push:
    branches: [master, main]

jobs:
  add-badges:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Add Badges
        uses: dgaida/auto-version-action@main
```

---

### 2. Auto Versioning

Increments the version number in `pyproject.toml` and creates a corresponding Git tag.

#### Usage
Create a workflow file (e.g., `.github/workflows/auto-version.yml`):

```yaml
name: Auto Versioning
on:
  pull_request:
    types: [closed]
    branches:
      - master
      - main

jobs:
  versioning:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          ref: master
          fetch-depth: 0

      - name: Run Auto Versioning
        uses: dgaida/auto-version-action/auto-version@main
```

## How it works
The actions use Python scripts to analyze the repository state and modify files accordingly. Changes are then automatically committed and pushed back to the repository.
