import os
import sys

# Add the directory to sys.path to import the script
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'md-list-fixer'))
from fix_md_lists import fix_markdown_file

def test_fix_markdown_file(tmp_path):
    d = tmp_path / "test_dir"
    d.mkdir()
    md_file = d / "test.md"

    content = """# Header
Liste:
- Element1
- Element2
  - SubElement
1. Ordered
2. Ordered2

No list here.

```
- This should not be changed
```
"""
    md_file.write_text(content, encoding='utf-8')

    fix_markdown_file(str(md_file))

    fixed_content = md_file.read_text(encoding='utf-8')
    lines = fixed_content.splitlines()

    # Check that list items and their precursors have two spaces
    assert lines[1] == "Liste:  "
    assert lines[2] == "- Element1  "
    assert lines[3] == "- Element2  "
    assert lines[4] == "  - SubElement  "
    assert lines[5] == "1. Ordered  "
    assert lines[6] == "2. Ordered2  "

    # Check that normal lines and code blocks are NOT changed
    assert lines[0] == "# Header"
    assert lines[8] == "No list here."
    assert lines[11] == "- This should not be changed"

def test_no_double_spaces(tmp_path):
    d = tmp_path / "test_dir_2"
    d.mkdir()
    md_file = d / "test2.md"

    content = "Liste:  \n- Item1  \n"
    md_file.write_text(content, encoding='utf-8')

    fix_markdown_file(str(md_file))

    fixed_content = md_file.read_text(encoding='utf-8')
    assert fixed_content == content

def test_line_endings_preserved(tmp_path):
    d = tmp_path / "test_dir_3"
    d.mkdir()
    md_file = d / "test3.md"

    content = b"Liste:\n- Item1\r\n- Item2\n"
    with open(md_file, "wb") as f:
        f.write(content)

    fix_markdown_file(str(md_file))

    with open(md_file, "rb") as f:
        data = f.read()

    assert b"Liste:  \n" in data
    # Note: Depending on OS/Python version, \r\n might be preserved or normalized.
    # Our script tries to preserve them.
    assert b"- Item1  \r\n" in data or b"- Item1  \n" in data
