"""
Exercise 02: API exercise requirements:
    1/ From https://exchangeratesapi.io/, get latest exchange rate of EUR
    2/ Get a list of exchange rate from March 01 2020 - March 10 2020 of EUR - JPY
    3/ Get Max & Min & average value  of that list.
"""
from datetime import datetime
import datetime as dt
import json
import logging.config
from typing import List
import math
import requests
from settings import EXCHANGE_URL, ACCESS_KEY

logging.config.fileConfig("log/logging.conf")
log = logging.getLogger("exercise02Logger")


def get_exchange_rate(currency: str, date_: datetime = None) -> dict:
    """
    :param currency: str
    :param date_: datetime
    :return: dict
    This function return exchange rates of a particular currency.
    Output sample for EUR currency:
    {
        "AUD": 1.566015,
        "CAD": 1.560132,
        "CHF": 1.154727,
        "CNY": 7.827874
    }
    """

    log.info("Get exchange rates of %s from %s", currency, EXCHANGE_URL)
    try:
        date_str = "latest"
        if date_:
            date_str = date_.strftime("%Y-%m-%d")

        requested_url = f"{EXCHANGE_URL}{date_str}"
        path_params = {'access_key': ACCESS_KEY, 'base': currency}

        log.debug("Sending request to %s with path params %s...",
                  requested_url, path_params)

        response = requests.get(requested_url, path_params).json()

        return response["rates"]

    except Exception as exception:
        log.exception("Error while getting exchange rate from %s: %s",
                      EXCHANGE_URL, exception)
        raise


def get_exchange_rates(currency: str,
                       start_date: datetime,
                       end_date: datetime) -> list:
    """
    This function returns a list of exchange rate from
    a start_date to an end_date
    :param currency: str
    :param start_date: datetime
    :param end_date: datetime
    :return: list
    """
    results = []
    current_date = start_date
    delta = dt.timedelta(days=1)
    while current_date <= end_date:
        results.append(get_exchange_rate(currency, current_date))
        current_date += delta
    return results


def get_max(records: List[dict]) -> float:
    """
    Get the maximum rate from a list of exchanges
    """
    max_val = -math.inf
    for record in records:
        max_val = max(max_val, max(record.values()))
    return max_val


def get_min(records: List[dict]) -> float:
    """
    Get the minimum rate from a list of exchanges
    """
    min_val = math.inf
    for record in records:
        min_val = min(min_val, min(record.values()))
    return min_val


def get_avg(records: List[dict]) -> float:
    """
    Get the average value from a list of exchanges
    """
    sum_val = 0
    count = 0
    for record in records:
        sum_val += sum(record.values())
        count += 1
    return sum_val / count


def write_data(file_name: str, records: List[dict], *agr):
    """
    Write the generated list of exchanges to a file
    Write max, min, and avg value taken from that list of exchanges
    """
    try:
        with open(file=file_name, mode="w", encoding="utf-8") as file:
            for exchanges in records:
                file.writelines(json.dumps(exchanges))
            file.write(f"\nMax value is {agr[0]}, "
                       f""f"min value is {agr[1]}, "
                       f""f"average value is {agr[2]}")

    except Exception as exception:
        log.exception("Unexpected error occurred while writing data to %s: %s",
                      file_name,
                      exception)
        raise


def main():
    """
    main function
    """
    records = get_exchange_rates("EUR", datetime(2020, 3, 1), datetime(2020, 3, 1))
    write_data("output.txt",
               records,
               get_max(records),
               get_min(records),
               get_avg(records))


if __name__ == "__main__":
    main()
