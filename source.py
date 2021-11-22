import pandas as pd
from datetime import datetime


def to_datetime(datetime_string):
    """
        This function convert a string of datetime to the type datetime in python
        It receives a string parameter with format: mm/dd/yyyy. For example:
            1. Valid format: "01/19/2000", "1/1/0001"
            2. Invalid format: "01 19 2000", "21/01/1999", "01/19/200", "01/19/20"

        :param datetime_string: string
        :return: datetime
    """
    return datetime.strptime(datetime_string, '%m/%d/%Y')


def to_age(birthdate):
    """
    :param birthdate: datetime
    :return: the age calculated by number of years: int
    """
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month == birthdate.month and today.day < birthdate.day) or today.month < birthdate.month:
        age = age - 1

    return age


def read_dictionaries(file_name):
    """
    :param file_name: string. This is the path or directory of the csv file
    :return: a list of dictionaries for each row in the csv file
    """
    data = pd.read_csv(file_name)
    dictionaries = []
    for individual in data.iloc:
        fullname = " ".join([individual["lastname"], individual["middlename"], individual["firstname"]])
        birthdate = to_datetime(individual["birthdate"])
        age = to_age(birthdate)

        dictionary = {}
        for column in data.columns:
            dictionary[column] = individual[column]
        dictionary["fullname"] = fullname
        dictionary["age"] = age

        dictionaries.append(dictionary)

    return dictionaries


def main():
    data = read_dictionaries("addresses.csv")
    print("Dictionaries:", data)


if __name__ == "__main__":
    main()
