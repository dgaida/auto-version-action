import sys

with open("tests/test_increment_version.py", "r") as f:
    content = f.read()

new_test = """
    @patch("os.path.exists")
    def test_increment_version_multiple_sections(self, mock_exists):
        mock_exists.return_value = True
        old_content = '[project]\\nversion = "0.1.0"\\n\\n[tool.commitizen]\\nversion = "0.1.0"\\n'

        m = mock_open(read_data=old_content)
        with patch("builtins.open", m):
            increment_version.increment_version()

            handle = m()
            written_parts = []
            for call in handle.write.call_args_list:
                written_parts.append(call.args[0])
            for call in handle.writelines.call_args_list:
                written_parts.extend(call.args[0])

            written_content = "".join(written_parts)
            self.assertIn('version = "0.1.1"', written_content)
            # Only the project version should be incremented
            self.assertIn('[tool.commitizen]\\nversion = "0.1.0"', written_content)
"""

if "class TestIncrementVersion(unittest.TestCase):" in content:
    content = content.replace("class TestIncrementVersion(unittest.TestCase):", "class TestIncrementVersion(unittest.TestCase):" + new_test)
    with open("tests/test_increment_version.py", "w") as f:
        f.write(content)
    print("Successfully patched tests/test_increment_version.py")
else:
    print("Could not find class TestIncrementVersion in tests/test_increment_version.py")
    sys.exit(1)
