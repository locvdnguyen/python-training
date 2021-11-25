import unittest
from unittest.mock import patch
import source
import pandas as pd
from datetime import datetime


class TestSource(unittest.TestCase):
    def test_convert_string_to_datetime(self):
        inputs = ["02/17/1999", "05/26/1999", "12/12/0001"]
        expected_results = [
            datetime(1999, 2, 17),
            datetime(1999, 5, 26),
            datetime(1, 12, 12)
        ]

        for index in range(0, 3):
            actual_result = source.convert_string_to_datetime(inputs[index])
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
                    "firstname": "Loc",
                    "lastname": "Nguyen",
                    "middlename": "Duc",
                    "birthdate": "02/17/1999",
                    "country": "VN",
                    "fullname": "Nguyen Duc Loc",
                    "age": 22
                },
                {
                    "firstname": "Witch",
                    "lastname": "Harry",
                    "middlename": "Potter",
                    "birthdate": "01/12/2004",
                    "country": "England",
                    "fullname": "Harry Potter Witch",
                    "age": 17
                }
            ]
            file_name = "my-address.csv"
            actual_result = source.read_csv(file_name)

            mock_pd_read_csv.assert_called_with(file_name)
            self.assertEqual(expected_result, actual_result)

    def test_save_as_csv(self):
        pass
