# Versioning and Releases

This project uses Semantic Versioning and automates the release process.

## Workflow

1. **Commit Changes**: Use [Conventional Commits](https://www.conventionalcommits.org/).  
2. **Automatic Increment**: On every push to `main`, the action increments the patch version in `pyproject.toml`.  
3. **Tag Creation**: The action automatically creates a Git tag (e.g., `v0.1.9`).  
4. **Changelog & Release**: The new tag triggers the `release.yml` workflow, which updates the changelog using `git-cliff` and creates a GitHub Release.  

## Manual Intervention

If a major or minor version is required, it must be manually adjusted in `pyproject.toml`. The action will detect the change and create the corresponding tag.
