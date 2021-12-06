"""
This class take responsibility in preprocess the data from csv file
"""
import csv
import datetime
import logging.config

from datetime import datetime
import pandas as pd

from student import Student

logging.config.fileConfig("log/logging.conf")
logger = logging.getLogger("sourceLogger")


def calculate_age(birthdate: datetime):
    """
    :param birthdate: datetime
    :return: the age calculated by number of years: int
    """
    logger.info("Calculate the age using birthdate %s...", birthdate)
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month == birthdate.month and today.day < birthdate.day) \
            or today.month < birthdate.month:
        age = age - 1
    return age


def convert_to_datetime(datetime_string: str, format_: str):
    """
    This function convert a string of datetime to the type datetime in python
    It receives a string parameter with a particular format. For example:
        1. Received format: "%d/%m%y"
        1. Valid format: "01/19/2000", "1/1/0001"
        2. Invalid format: "01 19 2000", "21/01/1999", "01/19/200", "01/19/20"

    :param format_: string. Example: "%d %m %y", "%m %y %d", "%d %m %Y", "%m/%d/%y"
    :param datetime_string: string
    :return: datetime
    """
    logger.info("Converting the string %s to datetime...", datetime_string)
    return datetime.strptime(datetime_string, format_)


class FileHandler:
    """
    This class is responsible for:
        1/ Read csv file and pour data into a list of dictionaries
        2/ Write the list of dictionaries into a .csv file
    """
    def __init__(self):
        self.records = []

    def read_csv(self, file_name: str):
        """
        :param file_name: string. This is the path or directory of the csv file
        :return: a list of dictionaries for each row in the csv file
        """
        logger.info("Converting the data from csv file %s "
                    "to a list of dictionaries...", file_name)
        data = pd.read_csv(file_name)
        for individual in data.iloc:
            fullname = " ".join([individual["lastname"],
                                 individual["middlename"],
                                 individual["firstname"]])
            birthdate = convert_to_datetime(individual["birthdate"], "%m/%d/%Y")
            age = calculate_age(birthdate)

            info = {"fullname": fullname, "age": age}
            self.records.append(info)

    def save_as_csv(self, file_name: str):
        """
        :param file_name: string
        :return:
        """
        if len(self.records) < 1:
            logger.warning("The records is empty. Nothing to save")
            return

        logger.info("Start writing data to file %s", file_name)
        header = self.records[0].keys()
        with open(file=file_name, mode='w', encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(header)
            for info in self.records:
                writer.writerow(info.values())


def main():
    """
    Main function
    """
    # Log is printed to file /log/logs.txt
    logger.info("Start running source...")

    file_handler = FileHandler()
    file_handler.read_csv("addresses.csv")
    logger.info("Fullname and age, reading from csv: %s", file_handler.records)
    file_handler.save_as_csv("addresses-2.csv")

    # Log is printed to console
    student = Student("Loc Nguyen", 22, "Ho Chi Minh University of Science")
    student.set_age(21)
    student.set_name("Chino")
    student.set_university("Stanford University")

    # Log is printed to file /log/logs.txt
    logger.info("Source stopped!")


if __name__ == "__main__":
    main()
