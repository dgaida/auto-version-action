# Installation

Die Auto Version Action muss nicht lokal installiert werden, da sie als GitHub Action konzipiert ist. Für die lokale Entwicklung oder Tests der Skripte kannst du jedoch die Abhängigkeiten installieren.

## GitHub Action nutzen

Füge einfach den folgenden Schritt in deinen Workflow ein:

```yaml
- uses: dgaida/auto-version-action@v0.1.8
```

## Lokale Entwicklung

Klonen des Repositories:

```bash
git clone https://github.com/dgaida/auto-version-action.git
cd auto-version-action
```

Installation der Test-Abhängigkeiten:

```bash
pip install -e ".[test]"
```
