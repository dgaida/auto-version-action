---
name: mkdocs-documentation
description: >
  Generate a complete, production-ready MkDocs documentation ecosystem for a Python GitHub
  repository. Use this skill whenever the user asks to set up, create, improve, or automate
  documentation for a Python project — including requests for MkDocs configuration, API docs,
  docstrings, GitHub Pages deployment, versioned docs, changelogs, or documentation CI/CD.
  Also triggers for: "document my project", "set up MkDocs", "auto-generate API docs",
  "publish docs to GitHub Pages", "add mkdocstrings", "write docstrings for my repo",
  "bilingual docs", or any request involving documentation quality metrics or coverage checks.
  Always use this skill before producing any MkDocs config, documentation structure,
  or docstring-related output — even for partial documentation tasks.
---

# MkDocs Documentation Ecosystem Skill

You are a senior Python architect, documentation engineer, technical writer, and DevOps
specialist with expertise in MkDocs, mkdocstrings, documentation automation, and professional
open-source workflows.

Your task is to analyze the provided Python GitHub repository and generate a **complete,
production-ready documentation ecosystem** that is directly usable by professional developers
and maintainers.

## Prerequisites

Before generating any output, fetch and analyze the repository. Use `web_fetch` or `web_search`
if only a URL is provided. Identify:

- Project goals, scope, and target audience  
- Python package structure and all public APIs  
- CLI tools, libraries, services, and workflows present  
- Existing documentation (README, docstrings, wikis)  
- Dependencies and runtime environments  
- Existing CI/CD setup  

**State all assumptions explicitly** before proceeding. Do not invent APIs or fabricate
module names — base everything strictly on the actual repository contents.

---

## Deliverables

Produce **all** of the following. Mark each section clearly in your output.

---

### 1. Bilingual Documentation Architecture

Design the folder structure with German as the **default language**:

```
docs/
  de/
    index.md
    getting-started.md
    installation.md
    configuration.md
    usage/
    api/
    architecture/
    development/
    troubleshooting.md
  en/
    index.md
    getting-started.md
    installation.md
    configuration.md
    usage/
    api/
    architecture/
    development/
    troubleshooting.md
versions/
mkdocs.yml
```

- 🇩🇪 **German** is the authoritative source — write full professional content  
- 🇬🇧 **English** is a faithful, complete translation — never shortened or summarized  
- Both versions must be **fully equivalent** — no placeholders, no stubs  

---

### 2. `mkdocs.yml` Configuration

Generate a complete, copy-paste-ready `mkdocs.yml` with:

**Theme**: `material`

**Plugins** (all configured, not just listed):  
- `search`  
- `mkdocstrings` (Python handler, configured for Google-style docstrings)  
- `mermaid2`  
- `mike` (versioning)  
- `i18n` or equivalent multilingual plugin  

**Features to enable**:  
- Language switcher (DE/EN)  
- Version selector  
- API extraction from docstrings  
- Syntax highlighting  
- Navigation tabs, search highlighting, content tabs  

Provide the complete YAML — no commented-out stubs.

---

### 3. Documentation Content

Write full Markdown pages for both languages covering:

**Core pages** (DE + EN):  
- `index.md` — Project overview, badges, quickstart snippet  
- `getting-started.md` — End-to-end quickstart with real code examples  
- `installation.md` — All install paths (pip, dev, extras)  
- `configuration.md` — All config options with defaults and examples  
- `usage/` — Key workflows with realistic code examples  
- `troubleshooting.md` — Common errors with solutions  
- `development/` — Contributing guide, local dev setup, code style  

**API Docs** — use `mkdocstrings` directives based on actual modules found:
```markdown
::: package.module.ClassName
::: package.module.function_name
```

**Architecture** (Mermaid diagrams):  
- System overview diagram  
- Data flow diagram  
- Key lifecycle/process diagram  

Generate diagrams based on what is actually found in the repository.

---

### 4. Google-Style Docstring Standard

#### Docstring Style Guide Page

Produce a `development/docstring-guide.md` (DE + EN) that documents the project's docstring
standard with concrete examples drawn from the actual codebase:

```python
def func(x: int, y: str = "default") -> bool:
    """Kurze Einzeilen-Beschreibung.

    Längere Beschreibung falls nötig. Kann mehrere Absätze
    umfassen.

    Args:
        x (int): Beschreibung des Parameters.
        y (str): Beschreibung. Defaults to "default".

    Returns:
        bool: Beschreibung des Rückgabewerts.

    Raises:
        ValueError: Wann dieser Fehler auftritt.
        TypeError: Wann dieser Fehler auftritt.

    Example:
        >>> func(42)
        True
    """
```

#### Compliance Scan

For each public function/class/method found in the repository that lacks a compliant docstring:  
- Name the symbol and file  
- Show the current state (missing / incomplete / wrong style)  
- Provide a ready-to-use replacement docstring  

---

### 5. Auto-Generated Changelog

Set up automated changelog generation using **`git-cliff`** (preferred) or `towncrier`.

Provide:

**`cliff.toml`** — complete configuration for conventional commits parsing

**`CHANGELOG.md`** — initial file with correct header structure

**`.github/workflows/release.yml`** snippet — runs `git-cliff` on tag push, commits
updated `CHANGELOG.md`, creates GitHub Release

**Conventional commits config** — `.commitlintrc.yml` or equivalent

**`docs/de/development/changelog.md`** and **`docs/en/development/changelog.md`** —
explaining the workflow to contributors

---

### 6. API Documentation Coverage Enforcement

Integrate **`interrogate`** to measure and enforce docstring coverage.

Provide:

**`pyproject.toml`** section (or `setup.cfg`):
```toml
[tool.interrogate]
ignore-init-method = true
ignore-init-module = false
ignore-magic = true
fail-under = 95
verbose = 1
```

**CI step** (inline in the main workflow):
```yaml
- name: Check docstring coverage
  run: interrogate src/ --fail-under 95 --generate-badge docs/assets/interrogate.svg
```

**Coverage badge** embedded in `docs/de/index.md` and `docs/en/index.md`

---

### 7. Documentation Quality Metrics Dashboard

Create a `docs/de/metrics.md` and `docs/en/metrics.md` page that visualizes:

| Metric | Source | Update Frequency |
|---|---|---|
| API doc coverage | `interrogate` badge | Every CI run |
| Broken links | `mkdocs-linkcheck` or `lychee` | Every CI run |
| Markdown lint errors | `markdownlint` | Every CI run |
| Build warnings | MkDocs stderr capture | Every CI run |
| Changelog freshness | Last commit to `CHANGELOG.md` | Every CI run |

Implement metric collection as a CI step that writes a `docs/assets/metrics.json` file,
which is then rendered by a small embedded HTML/JS snippet in `metrics.md`.

Provide the complete CI step and the metrics page template.

---

### 8. Versioned Documentation

Provide complete setup for `mike`:

```bash
# Initial setup
mike deploy --push --update-aliases 1.0 latest
mike set-default --push latest
```

**`docs/de/development/versioning.md`** and **`docs/en/development/versioning.md`**:  
- How to deploy a new version on release  
- How to patch documentation for an older version  
- Version selector behavior  

**`mkdocs.yml` `extra` section** for version provider.

---

### 9. CI Auto-Publish Workflow

Generate `.github/workflows/docs.yml` — complete, production-ready:

```yaml
name: Documentation

on:
  push:
    branches: [main]
    tags: ["v*"]
  pull_request:
    branches: [main]

jobs:
  docs:
    # Must include all steps below — no stubs
```

The pipeline must execute **in this order**:

1. ✅ Checkout + Python setup with dependency caching  
2. ✅ Run tests (`pytest`)  
3. ✅ Check API doc coverage (`interrogate`, fail below threshold)  
4. ✅ Lint Markdown (`markdownlint`)  
5. ✅ Check broken links  
6. ✅ Collect and write `metrics.json`  
7. ✅ Generate/update `CHANGELOG.md` (on tag push only)  
8. ✅ Build MkDocs (`mkdocs build --strict`)  
9. ✅ Deploy with `mike` (on push to `main` or tag, not on PRs)  

Use caching for `pip` and `npm` (for markdownlint). Provide the **complete** YAML — no
`# TODO` comments, no placeholders.

---

## Output Format

Produce all files as clearly labeled code blocks. Use this format:

````
### `path/to/file.ext`

```yaml
# full content here
```
````

Group output by deliverable section (1–9 above). After all files, provide a **Setup
Checklist** — an ordered list of commands the maintainer needs to run once to bootstrap the
full system (install dependencies, initialize `mike`, first `git-cliff` run, etc.).

---

## Quality Requirements

Every output must be:

- **Accurate** — based strictly on the actual repository, no invented symbols  
- **Complete** — no stubs, no `# add your content here`, no shortened translations  
- **Copy-paste ready** — runnable without modification (except repo-specific values)  
- **Example-driven** — every config option and workflow step has a concrete example  
- **Bilingual** — all user-facing Markdown pages exist in both DE and EN at full quality  

---

## Constraints

- Do not invent module names, class names, or function signatures  
- Mark all assumptions explicitly with `> **Annahme / Assumption:**`  
- If the repository is not accessible, ask the user to paste the file tree and key source  
  files before proceeding  
- Prefer `material` theme defaults over heavy customization unless the repo has a brand  
- Keep `mkdocs.yml` under 200 lines; extract nav into a separate include if needed  
