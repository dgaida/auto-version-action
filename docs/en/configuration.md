# Configuration

The action can be customized via various inputs.

| Input | Description | Default |
|-------|-------------|---------|
| `github-token` | GitHub token for authentication | `${{ github.token }}` |
| `auto-version` | Whether to automatically increment the version | `true` |
| `create-badge` | Whether to automatically add/update badges | `true` |
| `md-list-fix` | Whether to automatically fix Markdown lists | `true` |
| `run-on-push` | Whether to run on push events (outside of PRs) | `true` |
