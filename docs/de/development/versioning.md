# Versionierung und Releases

Dieses Projekt verwendet Semantic Versioning und automatisiert den Release-Prozess.

## Workflow

1. **Änderungen committen**: Verwende [Conventional Commits](https://www.conventionalcommits.org/).  
2. **Automatisches Inkrement**: Bei jedem Push auf `main` erhöht die Action die Patch-Version in der `pyproject.toml`.  
3. **Tag-Erstellung**: Die Action erstellt automatisch einen Git-Tag (z.B. `v0.1.9`).  
4. **Changelog & Release**: Der neue Tag löst den `release.yml` Workflow aus, der das Changelog mittels `git-cliff` aktualisiert und ein GitHub Release erstellt.  

## Manuelles Eingreifen

Sollte eine Major- oder Minor-Version benötigt werden, muss diese manuell in der `pyproject.toml` angepasst werden. Die Action erkennt die Änderung und erstellt den entsprechenden Tag.
