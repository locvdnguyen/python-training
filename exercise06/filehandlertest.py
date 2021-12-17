"""
Unit-test for filehandler.py
"""

from unittest.mock import patch
import unittest
from filehandler import FileHandler
import pandas as pd


class FileHandlerTest(unittest.TestCase):
    """
    This class is responsible for testing the filehandler module
    """
    def setUp(self) -> None:
        """ This method is called at the beginning of each test
        :return:
        """
        self.file_handler = FileHandler()
        self.file_handler.file_name = "input-sample.csv"
        self.file_handler.data = [
            {
                'first_name': "Loc",
                'last_name': "Nguyen",
                'license_number': "iolskm18289",
                'site_number': 100
            },
            {
                'first_name': "Tuyet",
                'last_name': "Vo",
                'license_number': "Y-95632547",
                'site_number': 200
            },
            {
                'first_name': "Lan",
                'last_name': "Nguyen",
                'license_number': "asd-893948-oo",
                'site_number': 150
            },
            {
                'first_name': "Nhi",
                'last_name': "Nguyen",
                'license_number': "x89f54j",
                'site_number': 200
            }
        ]

    def test_load_csv_as_dictionaries_when_success(self):
        """ Test load_csv_as_dictionaries for happy case
        :return:
        """
        with patch("filehandler.pd.read_csv") as mock_pd_read_csv:
            mock_pd_read_csv.return_value = pd.DataFrame({
                'first_name': ["Loc", "Tuyet", "Lan", "Nhi"],
                'last_name': ["Nguyen", "Vo", "Nguyen", "Nguyen"],
                'license_number':
                    ['iolskm18289', 'Y-95632547', 'asd-893948-oo', 'x89f54j'],
                'site_number': [100, 200, 150, 200]
            })

            actual_handler = FileHandler()
            actual_handler.load_csv_as_dictionaries(self.file_handler.file_name)

            mock_pd_read_csv.assert_called_with(self.file_handler.file_name)
            self.assertEqual(self.file_handler.data, actual_handler.data)

    def test_load_csv_as_dictionaries_when_file_not_found(self):
        """ Test load_csv_as_dictionaries when the input file_name
            does not exist in the system
        :return:
        """
        with patch("filehandler.pd.read_csv") as mock_pd_read_csv:
            mock_pd_read_csv.side_effect = FileNotFoundError()

            actual_handler = FileHandler()
            self.assertRaises(FileNotFoundError,
                              actual_handler.load_csv_as_dictionaries,
                              "input.csv")

    def test_load_csv_as_dictionaries_when_unknown_exception(self):
        """ Test load_csv_as_dictionaries when an unexpected errors
            occurs when the function is called
        :return:
        """
        with patch("filehandler.pd.read_csv") as mock_pd_read_csv:
            mock_pd_read_csv.return_value = Exception()

            actual_handler = FileHandler()
            self.assertRaises(Exception,
                              actual_handler.load_csv_as_dictionaries,
                              "input.csv")

    def test_group_by_license_number_when_success(self):
        """ Test the function group_by_license_number_when_success
        :return:
        """
        expected_result = {
            "US": [
                {
                    'first_name': "Loc",
                    'last_name': "Nguyen",
                    'license_number': "iolskm18289",
                    'site_number': 100
                },
            ],
            "UK": [
                {
                    'first_name': "Tuyet",
                    'last_name': "Vo",
                    'license_number': "Y-95632547",
                    'site_number': 200
                }
            ],
            "CA": [
                {
                    'first_name': "Lan",
                    'last_name': "Nguyen",
                    'license_number': "asd-893948-oo",
                    'site_number': 150
                }
            ],
            "Unknown": [
                {
                    'first_name': "Nhi",
                    'last_name': "Nguyen",
                    'license_number': "x89f54j",
                    'site_number': 200
                }
            ]
        }
        actual_result = self.file_handler.group_by_license_number()
        self.assertEqual(expected_result, actual_result)
