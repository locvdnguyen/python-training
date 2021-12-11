"""
Exercise 05: practice on csv manipulation
Requirements:
    Question 1: Load data from two files below into a dictionary, remove duplicates and print it
    Question 2: Add a key and create value for Full Name. Then sort it by Full Name
    Question 3: Make Full Name in Camel format
        Ex: “Vinh ngoc Phan” should be changed to “Vinh Ngoc Phan”
    Question 4: Set Middle Name in only one character
        Ex: “Vinh ngoc Phan” should be changed to “Vinh N Phan”
    Question 5: Only get list of female employees have team and joined since July 15, 2019
"""
import csv
from datetime import datetime
import logging
from typing import List

logging.basicConfig(filename="log.txt", level=logging.INFO)


def load_csv_file(file_name: str) -> List[dict]:
    """ Load csv file into a list of dictionaries
    :param file_name:
    :return:
    """
    result = []
    logging.info("Loading csv file %s...", file_name)

    try:
        with open(file=file_name, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            result = list(csv_reader)

    except FileNotFoundError as file_not_found_err:
        logging.error(file_not_found_err)
        raise

    except Exception as exception:
        logging.error(exception)
        raise

    logging.info("Load csv file %s successfully!", file_name)
    return result


def remove_duplicated(data: List[dict]) -> List[dict]:
    """ Remove duplicated
    :param data:
    :return:
    """
    logging.info("Removing duplicated...")
    result = []
    available_rows = set()
    try:
        for value in data:
            tuple_val = tuple(value.values())
            if tuple_val not in available_rows:
                available_rows.add(tuple_val)
                result.append(value)

    except Exception as exception:
        logging.exception(exception)
        raise

    logging.info("Removed duplicated rows successfully!")
    return result


def add_full_name(data: List[dict]) -> List[dict]:
    """ Add full name column for data
    :param data:
    :return:
    """
    logging.info("Adding fullname column to data...")
    try:
        for info in data:
            first_name = ""
            last_name = ""
            middle_name = ""

            if "FIRST_NAME" in info.keys():
                first_name = info["FIRST_NAME"]
            if "LAST_NAME" in info.keys():
                last_name = info["LAST_NAME"]
            if "MIDDLE_NAME" in info.keys():
                middle_name = info["MIDDLE_NAME"]

            full_name_raw = " ".join([first_name, last_name, middle_name])
            info["FULL_NAME"] = " ".join(full_name_raw.split())

    except AttributeError as attribute_err:
        logging.exception(attribute_err)
        raise

    except Exception as exception:
        logging.exception(exception)
        raise

    logging.info("Added fullname column to data successfully!")
    return data


def sort_by_fullname(data: List[dict]) -> List[dict]:
    """ sort data by full name
    :param data:
    :return:
    """
    logging.info("Sorting data by fullname...")
    try:
        data.sort(key=lambda info: info["FULL_NAME"], reverse=False)

    except Exception as exception:
        logging.exception(exception)
        raise

    logging.info("Sort data by fullname successfully!")
    return data


def make_fullname_camel(data: List[dict]) -> List[dict]:
    """ change fullname to camel format
    :param data:
    :return:
    """
    logging.info("Changing fullname format to camel...")

    try:
        for info in data:
            info["FULL_NAME"] = info["FULL_NAME"].title()

    except Exception as exception:
        logging.exception(exception)
        raise

    logging.info("Changed fullname format to camel successfully!")
    return data


def set_middle_name_to_one_char(data: List[dict]) -> List[dict]:
    """ Change the middle_name to only 1 character
    :param data:
    :return:
    """
    logging.info("Changing middle_name to 1 character...")
    try:
        for info in data:
            if "MIDDLE_NAME" in info.keys() and len(info["MIDDLE_NAME"]) > 0:
                info["MIDDLE_NAME"] = info["MIDDLE_NAME"][0].upper()

    except Exception as exception:
        logging.exception(exception)
        raise

    logging.info("Changed middle_name to 1 character successfully!")
    return data


def get_employees_by(employee_info_data: List[dict],
                     employee_team_data: List[dict],
                     is_male=True,
                     have_team=False,
                     join_since=datetime(2000, 1, 1)) -> List[dict]:
    """ Query employees by gender, have a team or not, and join since
    :param employee_info_data:
    :param employee_team_data:
    :param is_male:
    :param have_team:
    :param join_since:
    :return:
    """
    results = []
    logging.info("Getting list of employees whose is_male=%s, "
                 "have_team=%s, and joined since %s",
                 is_male, have_team, join_since)

    try:
        gender = "Female"
        if is_male:
            gender = "Male"

        have_team_ids = set()
        for employee in employee_team_data:
            have_team_ids.add(employee["EMPLOYEE_ID"])

        for employee in employee_info_data:
            employee_id = employee["EMPLOYEE_ID"]
            if employee["GENDER"] == gender:
                join_date = datetime.strptime(employee["JOIN_DATE"],
                                              "%d-%b-%y")
                if join_date >= join_since and (employee_id in have_team_ids) is have_team:
                    results.append(employee)

    except Exception as exception:
        logging.exception(exception)
        raise

    logging.info("Get list of employees whose is_male=%s, "
                 "have_team=%s, and joined since %s successfully!",
                 is_male, have_team, join_since)
    return results


def main():
    """ Main function
    :return:
    """
    employee_info_data = load_csv_file("employee-info.csv")
    employee_team_data = load_csv_file("employee-team.csv")

    remove_duplicated(employee_info_data)
    remove_duplicated(employee_team_data)

    print(employee_info_data)
    print(employee_team_data)

    add_full_name(employee_info_data)
    print(employee_info_data)

    set_middle_name_to_one_char(employee_info_data)
    add_full_name(employee_info_data)
    make_fullname_camel(employee_info_data)
    sort_by_fullname(employee_info_data)

    print(employee_info_data)
    print(employee_team_data)
    employees = get_employees_by(employee_info_data,
                                 employee_team_data,
                                 is_male=False,
                                 have_team=True,
                                 join_since=datetime(2019, 7, 15))
    for employee in employees:
        print(employee["JOIN_DATE"])


if __name__ == "__main__":
    main()
