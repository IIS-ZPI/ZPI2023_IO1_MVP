from datetime import date, timedelta

import numpy as np
import requests

from constans import AnalysisPeriod


def get_sessions_data(currency: str, analysisPeriod: AnalysisPeriod) -> tuple[int, int, int]:
    """
    Args:
        currency (str): The currency code for which session data is to be retrieved.
        analysisPeriod (AnalysisPeriod): The period for which the session data is to be analyzed.

    Returns:
        tuple: A tuple containing three integers representing the number of growth sessions,
            decline sessions, and unchanged sessions.

    """
    pass


def get_statistical_measures(currency: str, analysisPeriod: AnalysisPeriod) -> tuple[float, float, float, float]:
    """
    Args:
        currency (str): The currency code for which statistical measures are to be calculated.
        analysisPeriod (AnalysisPeriod): The period for which statistical measures are to be calculated.

    Returns:
        tuple: A tuple containing four float values representing statistical measures (median, mode, standard deviation,
            and coefficient of variation).
    """
    pass


def get_changes_distribution(currency_1: str, currency_2: str, start_date: date, analysisPeriod: AnalysisPeriod) -> tuple[list, list]:
    """
    Args:
        currency_1 (str): The currency code for the first currency.
        currency_2 (str): The currency code for the second currency.
        start_date (date): The start date for analyzing the monthly changes.
        analysisPeriod (AnalysisPeriod): The period for which the analysis of monthly changes is to be performed.

    Returns:
        tuple: tuple that has two lists: first representing the histogram values for every bin, and second representing bins boundries.
    """
    date_today = date.today()
    if start_date > date.today():
        raise ValueError("Start date cannot be in the future")
    
    dates = []
    match analysisPeriod:
        case AnalysisPeriod.QUARTER:
            end_date = start_date + timedelta(days=90)
            if end_date >= date_today:
                end_date = date_today
                dates.append((start_date, end_date))
            else:
                dates.append((start_date, end_date))
                end_date = end_date + timedelta(days=30)
                if end_date > date_today:
                    end_date = date_today
                dates.append((dates[-1][1] + timedelta(days=1), end_date))
        case AnalysisPeriod.MONTH:
            end_date = start_date + timedelta(days=30)
            if end_date > date_today:
                end_date = date_today
            dates.append((start_date, end_date))
        case _:
            raise ValueError("Analysis period must be either 'QUARTER' or 'MONTH'")
    
    dates_str = []
    for element in dates:
        dates_str.append((element[0].strftime('%Y-%m-%d'), element[1].strftime('%Y-%m-%d')))

    # api_data holds elements like (date, currency1_rate, currency2_rate)
    api_data: list[date, float, float] = []
    for date_str in dates_str:
        url1 = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency_1}/{date_str[0]}/{date_str[1]}"
        url2 = f"http://api.nbp.pl/api/exchangerates/rates/A/{currency_2}/{date_str[0]}/{date_str[1]}"

        try:
            response1 = requests.get(url1)
            response2 = requests.get(url2)
            if response1.status_code == 200 and response2.status_code == 200:
                data1 = response1.json()
                data2 = response2.json()

                for rate1, rate2 in zip(data1["rates"], data2["rates"]):
                    if rate1["effectiveDate"] != rate2["effectiveDate"]:
                        raise ValueError("Data inconsistency")
                    api_data.append((rate1["effectiveDate"], rate1["mid"], rate2["mid"]))
            else:
                raise ValueError("Invalid request parameters")
        except requests.RequestException as e:
            print("Error:", e)

    currency_changes = []
    last_pair_value = api_data[0][2] / api_data[0][1]
    for element in api_data[1:]:
        pair_value = element[2] / element[1]
        currency_changes.append(pair_value - last_pair_value)
        last_pair_value = pair_value

    hist, bins = np.histogram(currency_changes, bins=14)
    return hist, bins
