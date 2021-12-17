# python-training
Greenphore project training - Python

## Csv-pandas comparison
    This exercise focuses on estimating the performance of csv-module and pandas module
    
## Exercise 00: Introduction to pandas library
    This exercise focuses on applying pandas module to manipulate csv file
    Requirements: unit-testing, logging

## Exercise 01: Introduction to csv library
    This exercise focuses on applying csv module to handle csv file
    Requirements: logging, handle try catch exception

## Exercise 02: API exercise
    This exercise focuses mainly on requests module in Python.
    Requirements:
    1/ From https://exchangeratesapi.io/, get latest exchange rate of EUR
    2/ Get a list of exchange rate from March 01 2020 - March 10 2020 of EUR - JPY
    3/ Get Max & Min & average value  of that list.

## Exercise 03: CSV practice
    This exercise mainly focuses on using pandas to manipulate the csv file.
    Requirements:
        1/ Read data from a provided file and count how many rows
        2/ Remove duplicated rows
        3/ Capitalize the attendee names
        4/ Rewrite the code above in Python Class

## Exercise 04: Mock interview
    This exercise mainly focuses on reading .csv file
    Requirements:
        1/ Read as list of dictionaries
        2/ Replace the middle name column with the first character
        3/ Add a last name size column
        4/ Export the result to a csv file

## Exercise 05: CSV practice
    Requirements:
        1/ Load data from two files below into a dictionary, remove duplicates and print it
        2/ Add a key and create value for Full Name. Then sort it by Full Name
        3/ Make Full Name in Camel format
            ex: “Vinh ngoc Phan” should be changed to “Vinh Ngoc Phan”
        4/ Set Middle Name in only one character
            ex: “Vinh ngoc Phan” should be changed to “Vinh N Phan”
        5/ Only get list of female employees have team and joined since July 15, 2019

## Exercise 06: Mock interview
    Requirements:
        1/ Load data from .csv file as a list of dictionaries
        2/ Group the data based on license number:
            US: first 6 characters are alphabetic,
                next 5 characters are numbers
            UK: first character is in alphabet, followed by hyphen,
                next 8 characters are numbers
            CA: first 3 characters are in alphabet,
                followed by a hyphen, 6 numbers, a hyphen,
                and 2 alphabetic characters
        3/ Write unit testing