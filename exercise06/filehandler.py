"""
Exercise 06: Mock interview
Requirements:
    1/ Load data from .csv file as a list of dictionaries
    2/ Group the data based on license number:
        US: first 6 characters are alphabetic,
            next 5 characters are numbers
        UK: first character is in alphabet, followed by hyphen,
            next 8 characters are numbers
        CA: first 3 characters are in alphabet,
            followed by a hyphen, 6 numbers, a hyphen,
            and 2 alphabetic characters
    3/ Write unit testing
"""
import logging
import re
import pandas as pd


logging.basicConfig(filename="log.txt", level=logging.INFO)


def is_us(license_number: str) -> bool:
    """
    US: first 6 characters are alphabetic,
        next 5 characters are numbers
    """
    logging.info("Starting is_us(%s)...", license_number)
    pattern = "[a-zA-Z]{6}[0-9]{5}"
    is_matched = re.match(pattern=pattern, string=license_number)

    return bool(is_matched) and len(license_number) == 11


def is_uk(license_number: str) -> bool:
    """
    UK: first character is in alphabet, followed by hyphen,
        next 8 characters are numbers
    """
    logging.info("Starting is_uk(%s)...", license_number)
    pattern = "[a-zA-Z]-[0-9]{8}"
    is_matched = re.match(pattern=pattern, string=license_number)

    return bool(is_matched) and len(license_number) == 10


def is_ca(license_number: str) -> bool:
    """
    CA: first 3 characters are in alphabet, followed by a hyphen,
        6 numbers, a hyphen, and 2 alphabetic characters
    """
    logging.info("Starting is_ca(%s)...", license_number)
    pattern = "[a-zA-Z]{3}-[0-9]{6}-[a-zA-Z]{2}"
    is_matched = re.match(pattern=pattern, string=license_number)

    return bool(is_matched) and len(license_number) == 13


def get_license_number_group(license_number: str) -> str:
    """ get_license_number_group
    :param license_number:
    :return:
    """
    logging.info("Start get_license_number_group(%s)...", license_number)
    if is_us(license_number):
        return "US"
    if is_uk(license_number):
        return "UK"
    if is_ca(license_number):
        return "CA"
    return "Unknown"


class FileHandler:
    """
    This class take responsibility in reading csv file and
    group the data based on the license_number
    """
    def __init__(self):
        self.file_name = ""
        self.data = []

    def load_csv_as_dictionaries(self, file_name: str):
        """ load_csv_as_dictionaries
        :param file_name:
        :return:
        """
        logging.info("Start load_csv_as_dictionaries...")
        try:
            data_from_csv = pd.read_csv(file_name)
            self.data = data_from_csv.to_dict(orient='records')

        except FileNotFoundError as file_not_found_err:
            logging.exception(file_not_found_err)
            raise

        except Exception as exception:
            logging.error(exception)
            raise

    def group_by_license_number(self):
        """ group_by_license_number
        :return:
        """
        logging.info("Start group_by_license_number()...")
        groups = {'US': [], 'UK': [], 'CA': [], 'Unknown': []}
        for info in self.data:
            if "license_number" in info:
                license_number = info["license_number"]
                group_code = get_license_number_group(license_number)
                groups[group_code].append(info)
            else:
                groups['Unknown'].append(info)
        return groups


def main():
    """ main function
    :return:
    """
    file_handler = FileHandler()
    file_handler.load_csv_as_dictionaries(file_name="input.csv")
    print(file_handler.data)
    print(file_handler.group_by_license_number())


if __name__ == "__main__":
    main()
