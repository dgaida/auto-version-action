"""Script to automatically increment the version in pyproject.toml or package.json."""
import json
import os
import re
import sys


def increment_version_string(version_str: str) -> str:
    """Increments the patch version in a version string formatted as X.Y.Z.

    If the patch version reaches 10, it overflows to minor.
    If the minor reaches 10, it overflows to major.

    Args:
        version_str: The version string (e.g., "1.2.3").

    Returns:
        The incremented version string (e.g., "1.2.4").

    Raises:
        ValueError: If the version_str format is invalid.
    """
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)$", version_str)
    if not match:
        raise ValueError(f"Invalid version format: {version_str}")
    major, minor, patch = map(int, match.groups())
    patch += 1
    if patch > 9:
        patch = 0
        minor += 1
    if minor > 9:
        minor = 0
        major += 1
    return f"{major}.{minor}.{patch}"

def detect_json_indent(content: str) -> str:
    """Detects the indentation style of a JSON file content.

    Args:
        content: The text content of the JSON file.

    Returns:
        The detected indent sequence (e.g., "  ", "    ", or "\\t").
    """
    for line in content.splitlines():
        if line.startswith((" ", "\t")):
            indent = ""
            for char in line:
                if char in (" ", "\t"):
                    indent += char
                else:
                    break
            return indent
    return "  "

def increment_pyproject(filepath: str) -> bool:
    """Increments the version in a pyproject.toml file.

    Args:
        filepath: The path to the pyproject.toml file.

    Returns:
        True if the version was successfully incremented, False otherwise.
    """
    with open(filepath, "r") as f:
        lines = f.readlines()

    new_lines = []
    found = False
    current_section = None
    section_pattern = re.compile(r"^\[(.*)\]")

    for line in lines:
        stripped_line = line.strip()

        # Check for section header
        match_section = section_pattern.match(stripped_line)
        if match_section:
            current_section = match_section.group(1)

        if not found and current_section == "project" and stripped_line.startswith('version = "'):
            match = re.search(r'version = "(\d+)\.(\d+)\.(\d+)"', line)
            if match:
                major, minor, patch = map(int, match.groups())
                old_version = f"{major}.{minor}.{patch}"
                new_version = increment_version_string(old_version)
                line = line.replace(f'version = "{old_version}"', f'version = "{new_version}"')
                found = True
                print(f"Incrementing pyproject.toml version: {old_version} -> {new_version}")
        new_lines.append(line)

    if found:
        with open(filepath, "w") as f:
            f.writelines(new_lines)
        return True
    return False

def increment_package_json(filepath: str) -> bool:
    """Increments the version in a package.json file.

    Args:
        filepath: The path to the package.json file.

    Returns:
        True if the version was successfully incremented, False otherwise.
    """
    with open(filepath, "r") as f:
        content = f.read()

    try:
        data = json.loads(content)
        if not isinstance(data, dict):
            print("Error: package.json is not a valid JSON object")
            return False
    except json.JSONDecodeError as e:
        print(f"Error parsing package.json: {e}")
        return False

    old_version = data.get("version")
    if not old_version:
        print("Error: Could not find 'version' field in package.json")
        return False

    try:
        new_version = increment_version_string(old_version)
    except ValueError as e:
        print(f"Error: {e}")
        return False

    data["version"] = new_version
    indent = detect_json_indent(content)
    new_content = json.dumps(data, indent=indent)
    if content.endswith("\n") and not new_content.endswith("\n"):
        new_content += "\n"

    with open(filepath, "w") as f:
        f.write(new_content)

    print(f"Incrementing package.json version: {old_version} -> {new_version}")
    return True

def increment_version() -> None:
    """Increments version in pyproject.toml or package.json.

    If pyproject.toml is found, it will attempt to increment the version inside
    the [project] section. If package.json is found, it will attempt to
    increment the 'version' field.

    Raises:
        SystemExit: If neither file is found or version cannot be incremented.
    """
    if os.path.exists("pyproject.toml"):
        if increment_pyproject("pyproject.toml"):
            return
        else:
            print("Error: Could not find version string in [project] section of pyproject.toml")
            sys.exit(1)
    elif os.path.exists("package.json"):
        if increment_package_json("package.json"):
            return
        else:
            sys.exit(1)
    else:
        print("Error: Neither pyproject.toml nor package.json found in the root of the repository.")
        sys.exit(1)

if __name__ == "__main__":
    increment_version()
