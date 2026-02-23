import unittest
from unittest.mock import patch, mock_open
import add_badges

class TestAddBadges(unittest.TestCase):

    @patch("os.path.exists")
    def test_is_python_repo(self, mock_exists):
        mock_exists.side_effect = lambda x: x == "pyproject.toml"
        self.assertTrue(add_badges.is_python_repo())

        mock_exists.side_effect = lambda x: False
        self.assertFalse(add_badges.is_python_repo())

    @patch("os.path.exists")
    def test_detect_version_pyproject(self, mock_exists):
        mock_exists.side_effect = lambda x: x == "pyproject.toml"
        content = '[project]\nversion = "1.2.3"\n'
        with patch("builtins.open", mock_open(read_data=content)):
            self.assertEqual(add_badges.detect_version(), "1.2.3")

    @patch("os.path.exists")
    def test_detect_python_version(self, mock_exists):
        mock_exists.side_effect = lambda x: x == "pyproject.toml"
        content = '[project]\nrequires-python = ">=3.11"\n'
        with patch("builtins.open", mock_open(read_data=content)):
            self.assertEqual(add_badges.detect_python_version(), "3.11+")

    @patch("os.path.exists")
    def test_has_mit_license(self, mock_exists):
        mock_exists.side_effect = lambda x: x == "LICENSE"
        content = "This is an MIT License."
        with patch("builtins.open", mock_open(read_data=content)):
            self.assertTrue(add_badges.has_mit_license())

    @patch("os.path.exists")
    def test_uses_ruff(self, mock_exists):
        mock_exists.side_effect = lambda x: x == "pyproject.toml"
        content = "[tool.ruff]\n"
        with patch("builtins.open", mock_open(read_data=content)):
            self.assertTrue(add_badges.uses_ruff())

if __name__ == "__main__":
    unittest.main()
