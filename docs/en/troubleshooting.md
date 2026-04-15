# Troubleshooting

Here you will find solutions to common problems.

## "Permission denied" during push

Ensure that your workflow has write permissions:

```yaml
permissions:
  contents: write
```

## Version is not detected

The action looks for the pattern `version = "X.Y.Z"` in `pyproject.toml`. Ensure this format is followed.

## Badges are not added

The action adds badges after the first paragraph or in an existing badge block. If your `README.md` is empty or has an unusual format, detection might fail.
