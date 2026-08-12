import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Add the directory to sys.path to import the script
sys.path.append(os.path.join(os.getcwd(), "auto-version"))
import increment_version

class TestIncrementVersion(unittest.TestCase):
    @patch("os.path.exists")
    def test_increment_version_multiple_sections(self, mock_exists):
        # We need exists to return True for pyproject.toml but False for others (or mock_exists behavior)
        def side_effect(path):
            return path == "pyproject.toml"
        mock_exists.side_effect = side_effect
        old_content = '[project]\nversion = "0.1.0"\n\n[tool.commitizen]\nversion = "0.1.0"\n'

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
            self.assertIn('[tool.commitizen]\nversion = "0.1.0"', written_content)


    @patch("os.path.exists")
    def test_increment_version(self, mock_exists):
        def side_effect(path):
            return path == "pyproject.toml"
        mock_exists.side_effect = side_effect
        old_content = '[project]\nversion = "0.1.0"\n'

        m = mock_open(read_data=old_content)
        with patch("builtins.open", m):
            increment_version.increment_version()

            handle = m()
            # Capture all written data from write() and writelines()
            written_parts = []
            for call in handle.write.call_args_list:
                written_parts.append(call.args[0])
            for call in handle.writelines.call_args_list:
                written_parts.extend(call.args[0])

            written_content = "".join(written_parts)
            self.assertIn('version = "0.1.1"', written_content)

    @patch("os.path.exists")
    def test_increment_version_package_json(self, mock_exists):
        def side_effect(path):
            return path == "package.json"
        mock_exists.side_effect = side_effect
        old_content = '{\n  "name": "my-project",\n  "version": "1.2.3"\n}\n'

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
            self.assertIn('"version": "1.2.4"', written_content)
            # Indentation style of package.json should be preserved
            self.assertIn('\n  "version": "1.2.4"', written_content)

    @patch("os.path.exists")
    def test_increment_version_package_json_tabs(self, mock_exists):
        def side_effect(path):
            return path == "package.json"
        mock_exists.side_effect = side_effect
        old_content = '{\n\t"name": "my-project",\n\t"version": "1.2.9"\n}\n'

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
            self.assertIn('"version": "1.3.0"', written_content)
            # Tabs should be preserved
            self.assertIn('\n\t"version": "1.3.0"', written_content)

    @patch("os.path.exists")
    def test_increment_version_no_file(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(SystemExit):
            increment_version.increment_version()

if __name__ == "__main__":
    unittest.main()
