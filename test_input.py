import csv
import unittest
from main import read_csv_file

# =============================================================================
# Input Validation Tests
# Jacob Yealy & Caden Rosenberry
#
# Description:
# This class checks for cases of valid or invalid files.
# Test cases are based on the local valid and invalid CSV files.
# =============================================================================
class TestInputValidation(unittest.TestCase):

    def setUp(self):
        # Create a valid CSV file for testing
        self.valid_file = 'valid_file.csv'

        # Create an invalid CSV file for testing
        self.invalid_file = 'invalid_file.csv'

    def test_valid_file_input(self):
        try:
            graph = read_csv_file(self.valid_file)
            self.assertIsNotNone(graph)
            self.assertEqual(graph, {1.0: {2.0: 3.0}, 2.0: {3.0: 4.0}, 3.0: {4.0: 5.0}})
        except FileNotFoundError:
            self.fail("File not found.")

    def test_invalid_file_input(self):
        try:
            graph = read_csv_file(self.invalid_file)
            self.assertIsNotNone(graph)
            self.assertEqual(graph, {})
        except ValueError:
            self.fail("ValueError raised.")
        except FileNotFoundError:
            self.fail("File not found.")


if __name__ == "__main__":
    unittest.main()