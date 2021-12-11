import csv
from typing import List
import logging

logging.basicConfig(filename="/log.txt", level=logging.DEBUG)


def read_csv(file_name: str) -> List[dict]:
    try:
        with open(file=file_name, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return list(csv_reader)

    except FileNotFoundError as file_not_found_err:
        logging.exception(file_not_found_err)
        raise

    except Exception as exception:
        logging.exception(exception)
        raise


def replace_to_first_char(data: List[dict], column_name: str):

    number_of_record = len(data)
    for i in range(number_of_record):
        data[i][column_name] = data[i][column_name][0]


def add_last_name_size_col(data: List[dict]):
    number_of_record = len(data)
    for i in range(number_of_record):
        data[i]["last_name_size"] = len(data[i]["last_name"])


def export_to_csv(file_name: str, data: List[dict]):
    with open(file_name, mode='w') as csv_file:
        fieldnames = data[0].keys()
        csv_writer = csv.DictWriter(csv_file, fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def main():
    data = read_csv("CustomerInfo.csv")
    replace_to_first_char(data, "first_name")
    add_last_name_size_col(data)

    to_csv("output.csv", data)


if __name__ == "__main__":
    main()
