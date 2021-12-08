"""
Exercise 03 requirements:
    1/ Read data from a provided file and count how many rows
    2/ Remove duplicate rows
    3/ Capital the attendee names
    4/ Rewrite the code above in Python Class
"""

import logging as log
import pandas as pd


log.basicConfig(filename="log/logging.txt", level=log.INFO)


class CsvHandler:
    """
    This class is implemented to handle csv file, including:
        1/ read
        2/ count the number of lines
        3/ capitalize a particular column
        4/ output the result to a particular file
    """
    def __init__(self, file_name: str):
        try:
            log.info("Initializing a CsvHandler for %s...", file_name)
            self.file_name = file_name
            self.data = pd.read_csv(file_name)

        except FileNotFoundError as file_not_found_err:
            log.exception("The file %s not found!\n%s", file_name, file_not_found_err)
            raise

        except pd.errors.EmptyDataError as empty_err:
            log.exception("The file %s is empty!\n%s", file_name, empty_err)
            raise

        except Exception as exception:
            log.exception("Unexpected error while reading %s!\n%s",
                          file_name, exception)
            raise

    def count(self) -> int:
        """
        :return: the number of line in a csv file
        """
        log.info("Counting number of lines in file %s", self.file_name)
        return self.data.shape[0]

    def remove_duplicated_rows(self):
        """
        Update the data by removing the duplicated rows
        """
        log.info("Removing duplicated rows read from file %s...", self.file_name)
        self.data = self.data.drop_duplicates()
        log.info("Duplicated file removed successfully!")

        return self.data

    def capitalize(self, column_name: str):
        """
        Capitalize a particular column
        """
        try:
            log.info("Capitalizing the column %s...", column_name)
            self.data[column_name] = self.data[column_name].apply(lambda value: value.title())
            log.info("Column %s capitalized successfully!", column_name)

            return self.data

        except KeyError as key_err:
            log.exception("Column name %s not found!\n%s\nAvailable columns: %s",
                          column_name, key_err, self.data.columns)
            raise

        except AttributeError as attribute_err:
            log.exception("Column name %s is not a string "
                          "and has no title attribute!\n%s",
                          column_name, attribute_err)
            raise

        except Exception as exception:
            log.exception("Unexpected error while capitalizing column %s\n%s",
                          column_name, exception)
            raise

    def to_csv(self, file_name: str):
        """
        Output result to a csv file
        """
        log.info("Writing data to %s...", file_name)
        try:
            self.data.to_csv(path_or_buf=file_name, index=False)
            log.info("Successfully write data to %s!", file_name)

        except FileNotFoundError as file_not_found_err:
            log.exception("File %s not found!\n%s", file_name, file_not_found_err)
            raise

        except Exception as exception:
            log.exception("Unexpected error while writing to %s\n%s",
                          file_name, exception)
            raise


def main():
    """
    Main function of this exercise
    """
    csv_handler = CsvHandler("input.csv")
    csv_handler.remove_duplicated_rows()
    csv_handler.capitalize("attendee_name")
    csv_handler.to_csv("output.txt")


if __name__ == "__main__":
    main()
