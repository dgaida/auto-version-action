# Ubiquitous Language

## Versioning

| Term          | Definition                                                                 | Aliases to avoid      |
| ------------- | -------------------------------------------------------------------------- | --------------------- |
| **Version**   | A unique identifier for a specific state of the project (e.g., "0.1.0").    | Release, build        |
| **Increment** | The act of increasing the version number (patch, minor, or major).          | Bump, update          |
| **Tag**       | A persistent Git reference to a specific commit that represents a version. | Git tag, version tag  |

## Maintenance Tasks

| Term          | Definition                                                                 | Aliases to avoid      |
| ------------- | -------------------------------------------------------------------------- | --------------------- |
| **Badge**     | A visual indicator in README.md representing project metadata or status.   | Shield, icon          |
| **Detection** | The process of scanning the repository to identify features or configs.     | Scan, check           |
| **List Fixer**| A utility that enforces consistent line break formatting in Markdown lists. | Formatter, list tool  |
| **Action**    | A reusable maintenance task defined as a GitHub Action.                    | Step, script          |

## Relationships

- An **Action** performs **Detection** to determine which **Badges** to add.
- An **Action** can **Increment** the **Version** in `pyproject.toml`.
- A **Version** change triggers the creation of a corresponding **Tag**.
- The **List Fixer** ensures correct line breaks in Markdown files by appending spaces.

## Example dialogue

> **Dev:** "Should the **Action** automatically **Increment** the **Version** on every push?"
> **Domain expert:** "Yes, but only if the **Detection** logic confirms we are on the main branch. Once the **Version** is updated, it should also create a **Tag**."
> **Dev:** "And what about the **Badges**? Does the **Action** update those too?"
> **Domain expert:** "Exactly. After the **Version** is bumped, the **Badge** logic should refresh the version badge in README.md. If the **List Fixer** is enabled, it should also clean up any formatting issues."

## Flagged ambiguities

- **"Version"**: Used to mean both the string in `pyproject.toml` and the **Tag** in Git. Recommendation: Use **Version** for the metadata and **Tag** for the Git reference.
- **"Action"**: Used for both the repository as a whole and the specific composite steps. Recommendation: Use **Action** for the GitHub-compatible maintenance tasks.
