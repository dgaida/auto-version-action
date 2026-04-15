# Entwicklung

Willkommen im Entwicklungsbereich. Hier erfährst du, wie du zum Projekt beitragen kannst.

## Lokales Setup

1. Repository klonen.  
2. Virtuelle Umgebung erstellen: `python -m venv venv`.  
3. Abhängigkeiten installieren: `pip install -e ".[test]"`.  

## Tests ausführen

Wir verwenden `pytest` für unsere Unit-Tests:

```bash
python -m pytest
```

## Code-Stil

Wir verwenden `ruff` für Linting und Formatierung. Bitte stelle sicher, dass dein Code den Standards entspricht.
