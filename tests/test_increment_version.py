import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Add the directory to sys.path to import the script
sys.path.append(os.path.join(os.getcwd(), "auto-version"))
import increment_version

class TestIncrementVersion(unittest.TestCase):

    @patch("os.path.exists")
    def test_increment_version(self, mock_exists):
        mock_exists.return_value = True
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

if __name__ == "__main__":
    unittest.main()
