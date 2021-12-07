"""
Unit testing for source
"""
import unittest
from unittest.mock import patch
from datetime import datetime
import pandas as pd
from source import FileHandler
import source


class TestSource(unittest.TestCase):
    """
    Unit testing class, inherits from unittest.TestCase
    """

    def test_convert_string_to_datetime(self):
        inputs_date = ["02 17 1999", "05/26/1999", "12-12-01"]
        inputs_format = ["%m %d %Y", "%m/%d/%Y", "%d-%m-%y"]
        expected_results = [
            datetime(1999, 2, 17),
            datetime(1999, 5, 26),
            datetime(2001, 12, 12)
        ]

        for index in range(0, 3):
            actual_result = source.convert_to_datetime(inputs_date[index],
                                                       inputs_format[index])
            self.assertEqual(expected_results[index], actual_result)

    def test_calculate_age(self):
        inputs = [
            datetime(1999, 2, 17),
            datetime(2005, 12, 12),
            datetime(1, 12, 12)
        ]
        expected_ages = [22, 15, 2019]
        for index in range(0, 3):
            actual_age = source.calculate_age(inputs[index])
            self.assertEqual(expected_ages[index], actual_age)

    def test_read_csv(self):
        with patch("source.pd.read_csv") as mock_pd_read_csv:
            mock_pd_read_csv.return_value = pd.DataFrame({
                "firstname": ["Loc", "Witch"],
                "lastname": ["Nguyen", "Harry"],
                "middlename": ["Duc", "Potter"],
                "birthdate": ["02/17/1999", "01/12/2004"],
                "country": ["VN", "England"]
            })
            expected_result = [
                {
                    "fullname": "Nguyen Duc Loc",
                    "age": 22
                },
                {
                    "fullname": "Harry Potter Witch",
                    "age": 17
                }
            ]
            file_name = "my-address.csv"
            file_handler = FileHandler()
            file_handler.read_csv(file_name)
            actual_result = file_handler.records

            mock_pd_read_csv.assert_called_with(file_name)
            self.assertEqual(expected_result, actual_result)

    def test_save_as_csv(self):
        pass
