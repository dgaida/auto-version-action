# Fehlerbehebung

Hier findest du Lösungen für häufig auftretende Probleme.

## "Permission denied" beim Pushen

Stelle sicher, dass dein Workflow über Schreibberechtigungen verfügt:

```yaml
permissions:
  contents: write
```

## Version wird nicht erkannt

Die Action sucht in der `pyproject.toml` nach dem Muster `version = "X.Y.Z"`. Stelle sicher, dass dieses Format eingehalten wird.

## Badges werden nicht hinzugefügt

Die Action fügt Badges nach dem ersten Absatz oder in einem bestehenden Badge-Block hinzu. Wenn deine `README.md` leer ist oder ein ungewöhnliches Format hat, kann die Erkennung fehlschlagen.
