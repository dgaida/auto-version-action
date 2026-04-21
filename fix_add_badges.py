import sys

with open("add_badges.py", "r") as f:
    content = f.read()

old_detect_version = """def detect_version() -> str | None:
    \"\"\"Detects the project version from pyproject.toml or package.json.

    Returns:
        str: The version string if found, otherwise None.
    \"\"\"
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
    return None"""

new_detect_version = """def detect_version() -> str | None:
    \"\"\"Detects the project version from pyproject.toml or package.json.

    Returns:
        str: The version string if found, otherwise None.
    \"\"\"
    if os.path.exists("pyproject.toml"):
        try:
            import tomllib
            with open("pyproject.toml", "rb") as f:
                data = tomllib.load(f)
                return data.get("project", {}).get("version")
        except (ImportError, Exception):
            try:
                with open("pyproject.toml", "r") as f:
                    current_section = None
                    for line in f:
                        stripped = line.strip()
                        if stripped.startswith("[") and stripped.endswith("]"):
                            current_section = stripped[1:-1]
                        if current_section == "project" and stripped.startswith("version ="):
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
    return None"""

if old_detect_version in content:
    content = content.replace(old_detect_version, new_detect_version)
    with open("add_badges.py", "w") as f:
        f.write(content)
    print("Successfully patched add_badges.py")
else:
    print("Could not find old_detect_version in add_badges.py")
    sys.exit(1)
