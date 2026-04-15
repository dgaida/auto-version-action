import os
import re

def fix_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    new_lines = []
    in_code_block = False

    # Regex for list items: -, *, + or 1. 2. etc.
    list_item_regex = re.compile(r'^\s*([-*+]|\d+\.)\s+')

    for i in range(len(lines)):
        line = lines[i]
        stripped_line = line.strip()

        # Toggle code block
        if stripped_line.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        # Check if current line is a list item
        is_list_item = bool(list_item_regex.match(line))

        # Check if the next line is a list item (to handle the "Liste:" intro line)
        is_next_line_list_item = False
        if i + 1 < len(lines):
            is_next_line_list_item = bool(list_item_regex.match(lines[i+1]))

        # We only process non-empty lines that are either list items or preceding a list item
        if (is_list_item or is_next_line_list_item) and stripped_line:
            # Determine line ending
            current_newline = ""
            if line.endswith('\r\n'):
                current_newline = '\r\n'
            elif line.endswith('\n'):
                current_newline = '\n'

            # Remove all trailing spaces and then add exactly two
            content = line.rstrip('\r\n').rstrip(' ')

            new_line = content + "  " + current_newline
            if new_line != line:
                modified = True
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    files_to_check = []
    for root, dirs, files in os.walk('.'):
        # Skip .git and other hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                files_to_check.append(os.path.join(root, file))

    for filepath in files_to_check:
        try:
            if fix_markdown_file(filepath):
                print(f"Fixed {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    main()
