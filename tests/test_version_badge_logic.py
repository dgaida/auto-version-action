import unittest
from unittest.mock import patch, MagicMock
import os
import json
import sys

# Add current directory to path so add_badges can be imported
sys.path.append(os.getcwd())
import add_badges

class TestVersionBadgeLogic(unittest.TestCase):

    @patch("urllib.request.urlopen")
    @patch("os.environ.get")
    def test_has_tags_true(self, mock_env, mock_urlopen):
        mock_env.side_effect = lambda x, default=None: "fake_token" if x == "GITHUB_TOKEN" else default

        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps([{"name": "v0.1.0"}]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.assertTrue(add_badges.has_tags("owner", "repo"))

    @patch("urllib.request.urlopen")
    @patch("os.environ.get")
    def test_has_tags_false(self, mock_env, mock_urlopen):
        mock_env.side_effect = lambda x, default=None: "fake_token" if x == "GITHUB_TOKEN" else default

        # Mock response empty list
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps([]).encode()
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.assertFalse(add_badges.has_tags("owner", "repo"))

    @patch("add_badges.has_tags")
    @patch("add_badges.detect_version")
    @patch("add_badges.get_repo_info")
    def test_get_applicable_badges_with_tags(self, mock_repo, mock_version, mock_has_tags):
        mock_repo.return_value = ("owner", "repo")
        mock_has_tags.return_value = True

        badges = add_badges.get_applicable_badges()
        version_badge = next((b for b in badges if "![Version]" in b), None)
        self.assertIn("img.shields.io/github/v/tag/owner/repo", version_badge)

    @patch("add_badges.has_tags")
    @patch("add_badges.detect_version")
    @patch("add_badges.get_repo_info")
    def test_get_applicable_badges_without_tags(self, mock_repo, mock_version, mock_has_tags):
        mock_repo.return_value = ("owner", "repo")
        mock_has_tags.return_value = False
        mock_version.return_value = "1.2.3"

        badges = add_badges.get_applicable_badges()
        version_badge = next((b for b in badges if "![Version]" in b), None)
        self.assertIn("img.shields.io/badge/version-1.2.3-blue", version_badge)

    @patch("add_badges.get_applicable_badges")
    @patch("os.path.exists")
    def test_update_readme_replacement(self, mock_exists, mock_get_badges):
        mock_exists.return_value = True
        # Current README has static badge
        old_content = "# Project\n\n![Version](https://img.shields.io/badge/version-0.1.0-blue)\n"
        # We want to replace it with dynamic badge
        new_badge = "[![Version](https://img.shields.io/github/v/tag/owner/repo?label=version)](https://github.com/owner/repo/tags)"
        mock_get_badges.return_value = [new_badge]

        with patch("builtins.open", MagicMock()) as mock_open:
            mock_file = MagicMock()
            mock_file.read.return_value = old_content
            mock_open.return_value.__enter__.return_value = mock_file

            add_badges.update_readme()

            # The first open call is for reading, the second for writing
            # written_content = mock_file.write.call_args[0][0]
            # Actually, it's called on the file object returned by the second open
            written_content = "".join(call.args[0] for call in mock_file.write.call_args_list)
            self.assertIn("img.shields.io/github/v/tag/owner/repo", written_content)
            self.assertNotIn("img.shields.io/badge/version-0.1.0-blue", written_content)

    @patch("add_badges.get_applicable_badges")
    @patch("os.path.exists")
    def test_update_readme_no_change_needed(self, mock_exists, mock_get_badges):
        mock_exists.return_value = True
        # Current README has dynamic badge already
        content = "# Project\n\n[![Version](https://img.shields.io/github/v/tag/owner/repo?label=version)](https://github.com/owner/repo/tags)\n"
        new_badge = "[![Version](https://img.shields.io/github/v/tag/owner/repo?label=version)](https://github.com/owner/repo/tags)"
        mock_get_badges.return_value = [new_badge]

        with patch("builtins.open", MagicMock()) as mock_open:
            mock_file = MagicMock()
            mock_file.read.return_value = content
            mock_open.return_value.__enter__.return_value = mock_file

            add_badges.update_readme()

            # Check if write was NOT called
            self.assertEqual(mock_file.write.call_count, 0)

if __name__ == "__main__":
    unittest.main()
