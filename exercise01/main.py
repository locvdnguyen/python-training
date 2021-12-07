"""
Exercise 01 requirements:
    1/ Read data from data_1.csv & data_2.csv, load into a list of dictionaries
    2/ Filter the data whose state is not null or site_number is not null
    3/ Save the fitered data to "output.txt"
"""

import csv
import logging.config
from typing import List

logging.config.fileConfig("log/logging.conf")
log = logging.getLogger("exercise01Logger")


def load_file(file_name: str) -> list:
    """
     Load file to a list of dictionaries.
     Each dictionary is equivalent a row in file.
    """

    log.info("Loading file %s...", file_name)
    try:
        with open(file=file_name, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        return data

    except FileNotFoundError:
        log.error("File name %s not found!", file_name)
        raise
    except IOError:
        log.error("Error while reading the %s file...", file_name)
        raise
    except Exception as exception:
        log.exception("Unexpected error occurs...\nMessage: %s", exception)
        raise


def filter_data(data_1: List[dict], data_2: List[dict]) -> List[dict]:
    """
    Filter from data_1 and data_2,
    return a list of rows whose state is not null or site_number is not null
    """

    log.info("Filtering data from data_1 and data_2 where "
             "state or site number is not null...")

    try:
        license_state_map = {}
        for line in data_1:
            license_number = line["license_number"]
            state = line["state"]
            if state:
                license_state_map[license_number] = state

        license_site_map = {}
        for line in data_2:
            license_number = line["license_number"]
            site_number = line["site_number"]
            if site_number:
                license_site_map[license_number] = site_number

        output = []
        available_licenses_numbers = set()
        for line in data_1:
            license_number = line["license_number"]
            state = line["state"]
            if not state and license_number not in license_site_map.keys():
                continue

            if license_number in license_site_map:
                line["site_number"] = license_site_map.get(license_number)
            output.append(line)
            available_licenses_numbers.add(license_number)

        for line in data_2:
            license_number = line["license_number"]
            site_number = line["site_number"]
            if not site_number and license_number not in license_state_map:
                continue

            if site_number and license_number not in available_licenses_numbers:
                output.append(line)
                available_licenses_numbers.add(license_number)

        return output
    except Exception as exception:
        log.exception("Error while filtering data...\nMessage: %s", exception)
        raise


def write_to_file(file_name: str, data: List[dict]):
    """
    :param data: a list of dictionaries - represents data to write
    :param file_name: a string - represents the location to write data
    :return:
    """

    log.info("Writing data to %s...", file_name)
    try:
        fieldnames = ["first_name", "last_name", "license_number",
                      "state", "site_number"]
        with open(file=file_name, mode="w", encoding="utf-8") as csv_file:
            csv_writer = csv.DictWriter(f=csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    except IOError:
        log.error("Error while writing data to %s", file_name)
        raise
    except Exception as exception:
        log.exception("Unexpected error occurred!\nMessage: %s", exception)
        raise


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
