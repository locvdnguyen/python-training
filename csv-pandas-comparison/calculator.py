import datetime

import pandas as pd
import csv

from typing import Tuple

sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
         200, 300, 400, 500, 600, 700, 800, 900, 1000,
         2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
         20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000,
         200000, 30000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 2000000]

# sizes = [100, 1000, 10000, 100000, 1000000, 2000000]


class PerformanceCalculator:
    """
    This class is used to estimate the performance of reading/writing csv functions
    """

    def __init__(self):
        """
        Initialize the performance calculator
        """
        # Store data
        self.dataframe = pd.DataFrame({})
        self.data_list = []
        self.dictionaries = []

        # Store list of reading performance values
        self.reading_performances_pd = []
        self.reading_performances_pd_dict = []
        self.reading_performances_csv = []
        self.reading_performances_csv_dict = []

        # Store list of writing performance values
        self.writing_performances_pd = []
        self.writing_performances_csv = []
        self.writing_performances_pd_dict = []
        self.writing_performances_csv_dict = []

    def load_data(self, source_name: str):
        """ This function load data from a source_name file, and store 3 types of
        data into self.dataframe, self.data_list, and self.dictionaries
        :param source_name:
        :return:
        """
        dataframe = pd.read_csv(filepath_or_buffer=source_name)
        data_list = dataframe.values.tolist()
        dictionaries = dataframe.to_dict(orient="records")

        self.dataframe = dataframe
        self.data_list = data_list
        self.dictionaries = dictionaries

    def load_reading_performances_pd(self, source_name: str, expected_sizes: list):
        """ load_pandas_reading_performance
        :param source_name:
        :param expected_sizes:
        :return:
        """
        # Get reading performances of pandas (dataframe)
        reading_performances_pd = []
        for size_ in expected_sizes:
            start = datetime.datetime.now()
            data = pd.read_csv(source_name, nrows=size_)
            end = datetime.datetime.now()
            reading_performances_pd.append((end - start).total_seconds())

        # Get reading performances of pandas (list of dictionaries)
        reading_performances_pd_dict = []
        for size_ in expected_sizes:
            start = datetime.datetime.now()
            data = pd.read_csv(source_name, nrows=size_).to_dict(orient="records")
            end = datetime.datetime.now()
            reading_performances_pd_dict.append((end - start).total_seconds())

        self.reading_performances_pd = reading_performances_pd
        self.reading_performances_pd_dict = reading_performances_pd_dict

    def load_reading_performances_csv(self,
                                      source_name: str,
                                      expected_sizes: list):
        """ load_csv_reading_performances
        :param source_name:
        :param expected_sizes:
        :return:
        """
        # Get reading performances of csv (list of list)
        reading_performances_csv = []
        for size_ in expected_sizes:
            start = datetime.datetime.now()
            with open(file=source_name, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for index in range(size_):
                    data = next(csv_reader)
            end = datetime.datetime.now()
            reading_performances_csv.append((end - start).total_seconds())

        # Get reading performances of csv (list of dictionaries)
        reading_performances_csv_dict = []
        for size_ in expected_sizes:
            start = datetime.datetime.now()

            with open(file=source_name, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for index in range(size_):
                    data = next(csv_reader)
            end = datetime.datetime.now()
            reading_performances_csv_dict.append((end - start).total_seconds())

        self.reading_performances_csv = reading_performances_csv
        self.reading_performances_csv_dict = reading_performances_csv_dict

    def load_writing_performances_pd(self,
                                     output_name: str,
                                     expected_sizes: list):
        """ load_writing_performances_pd
        :param output_name:
        :param expected_sizes:
        :return:
        """
        # Get writing performances of pd (dataframe to csv)
        writing_performances_pd = []
        for size_ in expected_sizes:
            data = self.dataframe[0: size_]
            start = datetime.datetime.now()
            data.to_csv(output_name)
            end = datetime.datetime.now()
            writing_performances_pd.append((end - start).total_seconds())

        # Get writing performances of pd (dictionaries to csv)
        writing_performances_pd_dict = []
        for size_ in expected_sizes:
            data = self.dictionaries[0: size_]
            start = datetime.datetime.now()
            pd.DataFrame.from_records(data).to_csv(output_name)
            end = datetime.datetime.now()
            writing_performances_pd_dict.append((end - start).total_seconds())

        self.writing_performances_pd = writing_performances_pd
        self.writing_performances_pd_dict = writing_performances_pd_dict

    def load_writing_performances_csv(self,
                                      output_name: str,
                                      expected_sizes: list):
        """ load_writing_performances_csv
        :param output_name:
        :param expected_sizes:
        :return:
        """
        # Get writing performances of csv (list to csv)
        writing_performances_csv = []
        for size_ in expected_sizes:
            data = self.data_list[0: size_]
            start = datetime.datetime.now()
            with open(file=output_name, mode='w') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)
            end = datetime.datetime.now()
            writing_performances_csv.append((end - start).total_seconds())

        # Get writing performances of csv (Dictionaries to csv)
        writing_performances_csv_dict = []
        for size_ in expected_sizes:
            data = self.dictionaries[0: size_]
            fieldnames = self.dictionaries[0].keys()
            start = datetime.datetime.now()
            with open(file=output_name, mode='w') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(data)
            end = datetime.datetime.now()
            writing_performances_csv_dict.append((end - start).total_seconds())

        self.writing_performances_csv = writing_performances_csv
        self.writing_performances_csv_dict = writing_performances_csv_dict


def show_reading_performances(calculator: PerformanceCalculator,
                              source_name: str,
                              expected_sizes: list) -> Tuple:
    calculator.load_reading_performances_pd(source_name=source_name,
                                            expected_sizes=expected_sizes)

    calculator.load_reading_performances_csv(source_name=source_name,
                                             expected_sizes=expected_sizes)

    print("Reading pd - default:", calculator.reading_performances_pd)
    print("Reading csv - default:", calculator.reading_performances_csv)

    print("Reading pd - dictionaries:", calculator.reading_performances_pd_dict)
    print("Reading csv - dictionaries:", calculator.reading_performances_csv_dict)

    return (calculator.reading_performances_pd,
            calculator.reading_performances_csv,
            calculator.reading_performances_pd_dict,
            calculator.reading_performances_csv_dict)


def show_writing_performances(calculator: PerformanceCalculator,
                              output_name: str,
                              expected_sizes: list) -> Tuple:

    calculator.load_writing_performances_pd(output_name=output_name,
                                            expected_sizes=expected_sizes)

    calculator.load_writing_performances_csv(output_name=output_name,
                                             expected_sizes=expected_sizes)

    print("Writing pd - default:", calculator.writing_performances_pd)
    print("Writing csv - default:", calculator.writing_performances_csv)

    print("Writing pd - dictionaries:", calculator.writing_performances_pd_dict)
    print("Writing csv - dictionaries:", calculator.writing_performances_csv_dict)

    return (calculator.writing_performances_pd,
            calculator.writing_performances_csv,
            calculator.writing_performances_pd_dict,
            calculator.writing_performances_csv_dict)


def main():

    performance_cal = PerformanceCalculator()
    source_name = "input-big.csv"
    output_name = "output.csv"
    values_file = "values.txt"
    performance_cal.load_data(source_name)

    reading_performances = show_reading_performances(performance_cal,
                                                     source_name,
                                                     expected_sizes)
    writing_performances = show_writing_performances(performance_cal,
                                                     output_name,
                                                     expected_sizes)

    with open(values_file, mode='w') as text_file:
        for performances in reading_performances:
            for value in performances:
                text_file.write(str(value) + " ")
            text_file.write('\n')
        for performances in writing_performances:
            for value in performances:
                text_file.write(str(value) + " ")
            text_file.write('\n')


def pd_csv_compare():

    dictionaries = pd.read_csv("input.csv").to_dict(orient="records")
    start = datetime.datetime.now()
    pd.DataFrame(dictionaries).to_csv(path_or_buf="output.csv", index=False)
    end = datetime.datetime.now()
    print("pd writing default:", (end - start).total_seconds())

    # with open("input-big.csv", mode='r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     data_list = list(csv_reader)
    fieldnames = dictionaries[0].keys()
    start = datetime.datetime.now()
    with open("output.csv", mode='w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(dictionaries)
    end = datetime.datetime.now()
    print("csv writing default:", (end - start).total_seconds())


if __name__ == "__main__":
    main()
