# Guidelines for AI Agents

This repository contains a collection of GitHub Actions for repository maintenance, specifically for automatic versioning and adding status badges to README files.

## Project Structure

- `action.yml`: The main composite action that combines versioning and badge logic.  
- `add_badges.py`: Python script that detects repository features and updates `README.md`.  
- `auto-version/`:  
  - `action.yml`: Composite action for versioning only.  
  - `increment_version.py`: Python script to increment the version in `pyproject.toml`.  
- `tests/`: Pytest-based unit tests for the Python logic.  

## Tech Stack

- **Python 3.11+**: The core logic is implemented in Python.  
- **GitHub Actions**: Composite actions are used to orchestrate the workflow.  
- **Ruff**: Used for linting and code formatting.  
- **Pytest**: Used for unit testing.  

## Development Guidelines

- **Always run tests**: Before submitting changes, run `python -m pytest` to ensure no regressions.  
- **Follow coding standards**: Use Ruff to lint your code.  
- **Composite Actions**: When modifying `action.yml` files, ensure that the `if` conditions and shell commands are compatible with composite actions.  
- **Version Logic**: The versioning script (`increment_version.py`) specifically looks for `version = "X.Y.Z"` in `pyproject.toml`.  
- **Badge Logic**: `add_badges.py` uses regex to find and replace existing badges and appends new ones to the first paragraph or existing badge block.  

## Maintenance

- The project uses GitHub Actions to test itself. Ensure that `.github/workflows/tests.yml` and other CI workflows pass.  

## Skills

The skills located in the `skills/` folder should be used if applicable.

- `SKILL_coding.md`: Use this skill when performing deep code reviews, analyzing repository structure, or proposing improvements for maintainability and scalability.  
- `SKILL_docs.md`: Use this skill when setting up, improving, or automating MkDocs documentation, including bilingual support and CI/CD integration.  
