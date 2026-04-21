import sys

with open("tests/test_add_badges.py", "r") as f:
    content = f.read()

new_test = """
    @patch("os.path.exists")
    def test_detect_version_multiple_sections(self, mock_exists):
        mock_exists.return_value = True
        content = '[project]\\nversion = "1.2.3"\\n\\n[tool.commitizen]\\nversion = "0.0.1"\\n'
        with patch("builtins.open", mock_open(read_data=content.encode('utf-8'))):
            self.assertEqual(add_badges.detect_version(), "1.2.3")
"""

if "class TestAddBadges(unittest.TestCase):" in content:
    content = content.replace("class TestAddBadges(unittest.TestCase):", "class TestAddBadges(unittest.TestCase):" + new_test)
    with open("tests/test_add_badges.py", "w") as f:
        f.write(content)
    print("Successfully patched tests/test_add_badges.py")
else:
    print("Could not find class TestAddBadges in tests/test_add_badges.py")
    sys.exit(1)
