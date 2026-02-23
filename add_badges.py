import os
import re
import urllib.request
import json

def get_repo_info():
    full_repo = os.environ.get("GITHUB_REPOSITORY")
    if not full_repo or "/" not in full_repo:
        return "dgaida", "robot_mcp"
    owner, name = full_repo.split("/")
    return owner, name

def get_default_branch():
    return os.environ.get("GITHUB_REF_NAME", "master")

def detect_version():
    if os.path.exists("pyproject.toml"):
        try:
            with open("pyproject.toml", "r") as f:
                for line in f:
                    if line.strip().startswith("version ="):
                        match = re.search(r'version = "(.*?)"', line)
                        if match:
                            return match.group(1)
        except Exception:
            pass
    if os.path.exists("package.json"):
        try:
            with open("package.json", "r") as f:
                data = json.load(f)
                return data.get("version")
        except Exception:
            pass
    return None

def detect_python_version():
    if os.path.exists("pyproject.toml"):
        try:
            with open("pyproject.toml", "r") as f:
                content = f.read()
                match = re.search(r'requires-python = "(.*?)"', content)
                if match:
                    v = match.group(1).replace(">=", "").replace(">", "").strip()
                    return f"{v}+"
        except Exception:
            pass
    return None

def is_python_repo():
    return any(os.path.exists(f) for f in ["pyproject.toml", "setup.py", "requirements.txt"])

def has_mit_license():
    for f in ["LICENSE", "LICENSE.txt", "LICENSE.md", "license"]:
        if os.path.exists(f):
            try:
                with open(f, "r") as file:
                    content = file.read()
                    if "MIT License" in content or "MIT LICENSE" in content:
                        return True
            except Exception:
                pass
    return False

def uses_codecov():
    if os.path.exists(".codecov.yml") or os.path.exists("codecov.yml"):
        return True
    if os.path.exists(".github/workflows"):
        try:
            for f in os.listdir(".github/workflows"):
                if f.endswith((".yml", ".yaml")):
                    with open(os.path.join(".github/workflows", f), "r") as file:
                        if "codecov/codecov-action" in file.read():
                            return True
        except Exception:
            pass
    return False

def has_workflow(wf_name):
    return os.path.exists(f".github/workflows/{wf_name}.yml") or os.path.exists(f".github/workflows/{wf_name}.yaml")

def uses_black():
    if os.path.exists("pyproject.toml"):
        try:
            with open("pyproject.toml", "r") as f:
                if "[tool.black]" in f.read():
                    return True
        except Exception:
            pass
    return False

def uses_ruff():
    if os.path.exists("pyproject.toml"):
        try:
            with open("pyproject.toml", "r") as f:
                if "[tool.ruff]" in f.read():
                    return True
        except Exception:
            pass
    return os.path.exists("ruff.toml") or os.path.exists(".ruff.toml")

def has_github_pages(owner, name):
    url = f"https://{owner}.github.io/{name}/"
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=2) as resp:
            if resp.status == 200:
                return True
    except Exception:
        pass
    return os.path.exists("docs/") or os.path.exists("mkdocs.yml")

def get_applicable_badges():
    owner, name = get_repo_info()
    branch = get_default_branch()
    badges = []

    v = detect_version()
    if v:
        badges.append(f"![Version](https://img.shields.io/badge/version-{v}-blue)")

    if is_python_repo():
        pv = detect_python_version() or "3.8+"
        badges.append(f"[![Python](https://img.shields.io/badge/python-{pv}-blue.svg)](https://www.python.org/downloads/)")

    if has_mit_license():
        badges.append("[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)")

    if uses_codecov():
        badges.append(f"[![codecov](https://codecov.io/gh/{owner}/{name}/branch/{branch}/graph/badge.svg)](https://codecov.io/gh/{owner}/{name})")

    if has_workflow("lint"):
        badges.append(f"[![Code Quality](https://github.com/{owner}/{name}/actions/workflows/lint.yml/badge.svg)](https://github.com/{owner}/{name}/actions/workflows/lint.yml)")

    if has_workflow("tests"):
        badges.append(f"[![Tests](https://github.com/{owner}/{name}/actions/workflows/tests.yml/badge.svg)](https://github.com/{owner}/{name}/actions/workflows/tests.yml)")

    if has_workflow("codeql"):
        badges.append(f"[![CodeQL](https://github.com/{owner}/{name}/actions/workflows/codeql.yml/badge.svg)](https://github.com/{owner}/{name}/actions/workflows/codeql.yml)")

    if uses_black():
        badges.append("[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)")

    if uses_ruff():
        badges.append("[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)")

    if has_github_pages(owner, name):
        badges.append(f"[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://{owner}.github.io/{name}/)")

    badges.append(f"[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/{owner}/{name}/graphs/commit-activity)")
    badges.append(f"![Last commit](https://img.shields.io/github/last-commit/{owner}/{name})")

    return badges

def update_readme():
    filepath = "README.md"
    if not os.path.exists(filepath):
        print(f"{filepath} not found")
        return

    available_badges = get_applicable_badges()

    with open(filepath, "r") as f:
        content = f.read()

    missing_badges = []
    for badge in available_badges:
        match = re.search(r'\!\[.*?\]\((.*?)\)', badge)
        if not match:
            continue
        img_url = match.group(1)

        # Determine unique part of the URL to check for existence
        unique_part = img_url
        if "img.shields.io/badge/version-" in img_url:
            unique_part = "img.shields.io/badge/version-"
        elif "img.shields.io/badge/python-" in img_url:
            unique_part = "img.shields.io/badge/python-"
        elif "img.shields.io/badge/License-MIT" in img_url:
            unique_part = "img.shields.io/badge/License-MIT"
        elif "last-commit" in img_url:
            unique_part = "img.shields.io/github/last-commit"

        if unique_part not in content:
            missing_badges.append(badge)

    if not missing_badges:
        print("No missing badges to add.")
        return

    lines = content.splitlines()
    badge_pattern = re.compile(r'\!\[.*?\]\(.*?\)')
    badge_lines = [i for i, line in enumerate(lines) if badge_pattern.search(line)]

    if badge_lines:
        block_end = badge_lines[0]
        for i in range(1, len(badge_lines)):
            if badge_lines[i] == badge_lines[i-1] + 1:
                block_end = badge_lines[i]
            else:
                break
        # Insert them on separate lines
        new_lines = lines[:block_end+1] + missing_badges + lines[block_end+1:]
        lines = new_lines
    else:
        i = 0
        while i < len(lines) and (lines[i].startswith('#') or not lines[i].strip()):
            i += 1
        # Now i is at start of first paragraph
        while i < len(lines) and lines[i].strip():
            i += 1
        # Now i is at blank line after first paragraph or end
        lines = lines[:i] + [""] + missing_badges + [""] + lines[i:]

    with open(filepath, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Added {len(missing_badges)} badges.")

if __name__ == "__main__":
    update_readme()
