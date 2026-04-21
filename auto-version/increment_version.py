"""Script to automatically increment the version in pyproject.toml."""
import os
import re
import sys

def increment_version():
    """Increments the patch version in pyproject.toml.

    If the patch version reaches 10, it overflows to minor.
    If the minor reaches 10, it overflows to major.

    Only increments the version within the [project] section.

    Raises:
        SystemExit: If pyproject.toml is missing or version not found.
    """
    filepath = "pyproject.toml"
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found in the root of the repository.")
        sys.exit(1)

    with open(filepath) as f:
        lines = f.readlines()

    new_lines = []
    found = False
    current_section = None
    section_pattern = re.compile(r'^\[(.*)\]')

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

                patch += 1
                if patch > 9:
                    patch = 0
                    minor += 1
                if minor > 9:
                    minor = 0
                    major += 1

                new_version = f"{major}.{minor}.{patch}"
                line = line.replace(f'version = "{old_version}"', f'version = "{new_version}"')
                found = True
                print(f"Incrementing version: {old_version} -> {new_version}")
        new_lines.append(line)

    if found:
        with open(filepath, "w") as f:
            f.writelines(new_lines)
    else:
        print("Error: Could not find version string in [project] section of pyproject.toml")
        sys.exit(1)

if __name__ == "__main__":
    increment_version()
