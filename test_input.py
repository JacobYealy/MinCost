import unittest
from unittest.mock import patch, mock_open

from main import read_csv_file

# =============================================================================
# Input Validation Tests
# Jacob Yealy & Caden Rosenberry
#
# Description:
# This class checks for cases of valid or invalid files.
# Test cases are based on the already local EdgeWeights.csv file.
# =============================================================================
class TestInputValidation(unittest.TestCase):

    def test_valid_file(self):
        self.assertTrue(read_csv_file("EdgeWeights.csv"))

    @patch('builtins.print')
    def test_invalid_file(self, mock_print):
        with self.assertRaises(SystemExit):
            read_csv_file("edgeweights.txt")
        self.assertFalse()


if __name__ == '__main__':
    unittest.main()