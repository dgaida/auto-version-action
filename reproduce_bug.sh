#!/bin/bash
cat <<EOT > pyproject.toml
[project]
name = "test"
version = "0.4.7"

[tool.commitizen]
version = "0.4.7"
EOT

NEW_VERSION=$(grep '^version = "' pyproject.toml | cut -d'"' -f2)
echo "Extracted version: '$NEW_VERSION'"

if [[ "$NEW_VERSION" == *$'\n'* ]]; then
    echo "Bug reproduced: NEW_VERSION contains a newline"
else
    echo "Bug NOT reproduced"
fi

# Attempt to tag (this should fail)
git init
git add pyproject.toml
git commit -m "initial commit"
git tag v$NEW_VERSION
