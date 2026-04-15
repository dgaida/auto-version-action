# Docstring Guide

We use the **Google style** for all Python docstrings. This allows for clean, readable documentation that can be automatically extracted by `mkdocstrings`.

## Example

```python
def increment_version():
    """Increments the patch version in pyproject.toml.

    If the patch version reaches 10, it overflows to minor.
    If the minor reaches 10, it overflows to major.

    Raises:
        SystemExit: If pyproject.toml is missing or version not found.
    """
```

## Sections

- **Args**: Description of parameters.  
- **Returns**: Description of the return value.  
- **Raises**: Documentation of exceptions the function might raise.  
- **Example**: Usage examples.  
