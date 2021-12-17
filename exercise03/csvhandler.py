import pandas as pd
import logging


logging.basicConfig(filename="log/logging.txt", level=logging.INFO)


class CsvHandler:
    def __init__(self):
        """ Init Csvhandler
        """
        logging.info("Initialize CsvHandler...")

        self.file_name = None
        self.data = []

    def load_csv_as_dictionaries(self, file_name: str):
        """ load csv file as a list of dictionaries
        :param file_name:
        :return:
        """
        logging.info("Start load_csv_as_dictionaries...")

        try:
            data_from_csv = pd.read_csv(file_name)
            self.file_name = file_name
            self.data = data_from_csv.to_dict(orient='records')

            logging.info("End load_csv_as_dictionaries!")

        except FileNotFoundError as file_not_found_err:
            logging.exception(file_not_found_err)
            raise

        except Exception as exception:
            logging.exception(exception)
            raise

    def count_rows(self):
        """ count_rows
        :return:
        """
        logging.info("Start count_rows...")
        return len(self.data)

    def remove_duplicated_rows(self):
        """ remove_duplicated_rows
        :return:
        """
        logging.info("Start remove_duplicated_rows...")

        available_rows = set()
        results = []
        for info in self.data:
            tuple_info = tuple(info.values())
            if tuple_info not in available_rows:
                available_rows.add(tuple(info.values()))
                results.append(info)
        self.data = results
        logging.info("End remove_duplicated_rows!")

    def capitalize(self, column_name: str):
        """ Capitalize the attendee_name
        :param column_name:
        :return:
        """
        logging.info("Start capitalize()...")
        for info in self.data:
            info[column_name] = info[column_name].title()

        logging.info("End capitalize()!")


def main():
    csv_handler = CsvHandler()
    csv_handler.load_csv_as_dictionaries(file_name="input.csv")
    print(csv_handler.data)
    print(csv_handler.count_rows())

    csv_handler.remove_duplicated_rows()
    print(csv_handler.count_rows())

    csv_handler.capitalize("attendee_name")
    print(csv_handler.data)


if __name__ == "__main__":
    main()
