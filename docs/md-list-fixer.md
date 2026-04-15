# Markdown List Fixer

The Markdown List Fixer action scans all `*.md` files in your repository and ensures that list items (and the lines immediately preceding a list) end with two spaces.

## Why?

In many Markdown implementations (like GitHub or CommonMark), a simple line break in the source doesn't always result in a line break in the rendered output unless the line ends with two or more spaces.

Example:
\`\`\`markdown
List:
- Item 1
- Item 2
\`\`\`

Might render as:
List: - Item 1 - Item 2

By adding two spaces:
\`\`\`markdown
List:
- Item 1
- Item 2
\`\`\`

It renders correctly as:
List:
- Item 1
- Item 2

## Configuration

You can enable or disable this feature using the \`md-list-fix\` input in the main action, or use the standalone action in \`md-list-fixer/\`.
