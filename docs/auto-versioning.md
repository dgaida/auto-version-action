# Auto Versioning

Automatically increments the version in \`pyproject.toml\` and creates a Git tag.

## How it works

The script searches for \`version = "X.Y.Z"\` in \`pyproject.toml\`.
It increments the patch version by default. If the patch version reaches 100, it increments the minor version.
