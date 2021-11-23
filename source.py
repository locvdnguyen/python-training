import csv
import pandas as pd
from datetime import datetime


def convert_string_to_datetime(datetime_string: str):
    """
    This function convert a string of datetime to the type datetime in python
    It receives a string parameter with format: mm/dd/yyyy. For example:
        1. Valid format: "01/19/2000", "1/1/0001"
        2. Invalid format: "01 19 2000", "21/01/1999", "01/19/200", "01/19/20"

    :param datetime_string: string
    :return: datetime
    """
    return datetime.strptime(datetime_string, '%m/%d/%Y')


def calculate_age(birthdate: datetime):
    """
    :param birthdate: datetime
    :return: the age calculated by number of years: int
    """
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month == birthdate.month and today.day < birthdate.day) \
            or today.month < birthdate.month:
        age = age - 1

    return age


def read_csv(file_name: str):
    """
    :param file_name: string. This is the path or directory of the csv file
    :return: a list of dictionaries for each row in the csv file
    """
    data = pd.read_csv(file_name)
    results = []
    for individual in data.iloc:
        fullname = " ".join([individual["lastname"],
                             individual["middlename"],
                             individual["firstname"]])
        birthdate = convert_string_to_datetime(individual["birthdate"])
        age = calculate_age(birthdate)

        info = {"fullname": fullname, "age": age}
        for column in data.columns:
            info[column] = individual[column]

        results.append(info)

    return results


def save_as_csv(file_name: str, records: [dict]):
    """
    :param records: a list of dictionaries
    :param file_name: string
    :return:
    """
    if len(records) < 1:
        return

    header = records[0].keys()
    with open(file_name, 'w') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        for info in records:
            writer.writerow(info.values())


def main():
    records = read_csv("addresses.csv")
    print("Dictionaries:", records)
    save_as_csv("addresses-2.csv", records)


if __name__ == "__main__":
    main()
