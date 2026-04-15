# Installation

The Auto Version Action does not need to be installed locally as it is designed as a GitHub Action. However, for local development or testing of the scripts, you can install the dependencies.

## Using GitHub Action

Simply add the following step to your workflow:

```yaml
- uses: dgaida/auto-version-action@v0.1.8
```

## Local Development

Clone the repository:

```bash
git clone https://github.com/dgaida/auto-version-action.git
cd auto-version-action
```

Install test dependencies:

```bash
pip install -e ".[test]"
```
