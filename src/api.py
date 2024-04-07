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


def calculate_statistical_measures(currency: str, analysisPeriod: AnalysisPeriod) -> tuple[float, float, float, float]:
    """
    Args:
        currency (str): The currency code for which statistical measures are to be calculated.
        analysisPeriod (AnalysisPeriod): The period for which statistical measures are to be calculated.

    Returns:
        tuple: A tuple containing four float values representing statistical measures (median, mode, standard deviation,
            and coefficient of variation).
    """
    pass


def monthly_changes_distribution(currency_1: str, currency_2: str, start_date: date, analysisPeriod: AnalysisPeriod) -> list:
    """
    Args:
        currency_1 (str): The currency code for the first currency.
        currency_2 (str): The currency code for the second currency.
        start_date (date): The start date for analyzing the monthly changes.
        analysisPeriod (AnalysisPeriod): The period for which the analysis of monthly changes is to be performed.

    Returns:
        list: A list of lists representing the distribution of monthly changes.
    """
    pass


