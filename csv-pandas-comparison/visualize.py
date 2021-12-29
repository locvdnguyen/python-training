import matplotlib.pyplot as plt
import calculator
import numpy as np


def plot_reading_performances(reading_performances: list,
                              expected_sizes: list):

    reading_performances_pd = reading_performances[0]
    reading_performances_csv = reading_performances[1]
    # reading_performances_pd_dict = reading_performances[2]
    reading_performances_csv_dict = reading_performances[3]

    plt.figure(figsize=(10, 5))

    plt.plot(expected_sizes, reading_performances_pd, label="pd: default reading", color='red')
    plt.plot(expected_sizes, reading_performances_csv, label="csv: default reading", color='green')
    # plt.plot(expected_sizes, reading_performances_pd_dict, label="pd: read as dictionaries")
    plt.plot(expected_sizes, reading_performances_csv_dict, label="csv: read as dictionaries", color='black')
    plt.xlabel("number of lines in .csv")
    plt.ylabel("seconds")
    plt.title("CSV reading performances")
    plt.legend()
    plt.ticklabel_format(style='plain')
    plt.savefig("reading.png")
    plt.show()
    plt.close()


def plot_writing_performances(writing_performances: list,
                              expected_sizes: list):

    writing_performances_pd = writing_performances[0]
    writing_performances_csv = writing_performances[1]
    # writing_performances_pd_dict = writing_performances[2]
    writing_performances_csv_dict = writing_performances[3]

    plt.figure(figsize=(10, 5))

    plt.plot(expected_sizes, writing_performances_pd, label="pd: default writing", color='red')
    plt.plot(expected_sizes, writing_performances_csv, label="csv: default writing", color='green')
    # plt.plot(expected_sizes, writing_performances_pd_dict, label="pd: write dictionaries")
    plt.plot(expected_sizes, writing_performances_csv_dict, label="csv: write dictionaries", color='black')
    plt.xlabel("number of lines in .csv")
    plt.ylabel("seconds")
    plt.title("CSV writing performances")
    plt.legend()
    plt.ticklabel_format(style='plain')
    plt.savefig("writing.png")
    plt.show()
    plt.close()


def main():

    # Prepare from values.txt and calculator.py
    expected_sizes = calculator.sizes
    with open("values.txt", mode='r') as reader:
        reading_performances = []
        for count in range(0, 4):
            line = reader.readline().split(" ")[:-1]
            reading_performances.append(list(map(float, line)))

        writing_performances = []
        for count in range(0, 4):
            line = reader.readline().split(" ")[:-1]
            writing_performances.append(list(map(float, line)))

    # Plot data
    plot_reading_performances(reading_performances, expected_sizes)
    plot_writing_performances(writing_performances, expected_sizes)


if __name__ == "__main__":
    main()
