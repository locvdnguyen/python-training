"""
Exercise 01 requirements:
    1/ Read data from data_1.csv & data_2.csv, load into a list of dictionaries
    2/ Filter the data whose state is not null or site_number is not null
    3/ Save the fitered data to "output.csv"
"""

import csv
from typing import List


def load_file(file_name: str) -> list:
    """
    load file to a list of dictionaries. Each dictionary is equivalent a row in file.
    """

    with open(file=file_name, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    return data


def filter_data(data_1: List[dict], data_2: List[dict]) -> List[dict]:
    """
    Filter from data_1 and data_2,
    return a list of rows whose state is not null or site_number is not null
    """
    accepted_license_numbers = set()
    output = []
    for line in data_1:
        if line["state"]:
            output.append(line)
            accepted_license_numbers.add(line["license_number"])

    for line in data_2:
        if line["site_number"] \
                and line["license_number"] not in accepted_license_numbers:
            output.append(line)

    return output


def write_to_file(file_name: str, data: List[dict]):
    """
    :param data: a list of dictionaries - represents data to write
    :param file_name: a string - represents the location to write data
    :return:
    """
    fieldnames = ["first_name", "last_name", "license_number", "state", "site_number"]
    with open(file=file_name, mode="w", encoding="utf-8") as csv_file:
        csv_writer = csv.DictWriter(f=csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def main():
    """
    main function of this file
    """
    data_1 = load_file("data_1.csv")
    data_2 = load_file("data_2.csv")

    data = filter_data(data_1, data_2)
    write_to_file("output.csv", data)


if __name__ == "__main__":
    main()
