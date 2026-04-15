# Docstring-Leitfaden

Wir verwenden den **Google-Stil** für alle Python-Docstrings. Dies ermöglicht eine saubere, lesbare Dokumentation, die automatisch von `mkdocstrings` extrahiert werden kann.

## Beispiel

```python
def increment_version():
    """Inkrementiert die Patch-Version in der pyproject.toml.

    Wenn die Patch-Version 10 erreicht, wird die Minor-Version erhöht.
    Wenn die Minor-Version 10 erreicht, wird die Major-Version erhöht.

    Raises:
        SystemExit: Wenn die pyproject.toml fehlt oder die Version nicht gefunden wurde.
    """
```

## Abschnitte

- **Args**: Beschreibung der Parameter.
- **Returns**: Beschreibung des Rückgabewerts.
- **Raises**: Dokumentation der Fehler, die die Funktion auslösen kann.
- **Example**: Anwendungsbeispiele.
