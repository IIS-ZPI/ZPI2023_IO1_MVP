from datetime import date, timedelta

import numpy as np
import pytest
import requests

from unittest.mock import patch

from app.api import get_changes_distribution
from app.constans import AnalysisPeriod


def test_invalid_currency_1():
    """
    Test case for testing function behavior with invalid first currency input.
    """
    with pytest.raises(ValueError) as e:
        get_changes_distribution("ERR", "USD", date(2023, 9, 9), AnalysisPeriod.QUARTER)
    assert str(e.value) == "Invalid request parameters"


def test_invalid_currency_2():
    """
    Test case for testing function behavior with invalid first currency input.
    """
    with pytest.raises(ValueError) as e:
        get_changes_distribution("EUR", "WWW", date(2023, 9, 9), AnalysisPeriod.QUARTER)
    assert str(e.value) == "Invalid request parameters"


def test_invalid_currency_1_and_2():
    """
    Test case for testing function behavior with invalid first and second currency input.
    """
    with pytest.raises(ValueError) as e:
        get_changes_distribution("ERR", "WWW", date(2023, 9, 9), AnalysisPeriod.QUARTER)
    assert str(e.value) == "Invalid request parameters"


def test_invalid_analysis_period():
    """
    Test case for testing function behavior with invalid analysis period input.
    """
    with pytest.raises(ValueError) as e:
        get_changes_distribution("EUR", "USD", date(2023, 9, 9), AnalysisPeriod.YEAR)
    assert str(e.value) == "Analysis period must be either 'QUARTER' or 'MONTH'"

    with pytest.raises(ValueError) as e:
        get_changes_distribution("EUR", "USD", date(2023, 9, 9), 10)
    assert str(e.value) == "Analysis period must be either 'QUARTER' or 'MONTH'"

    with pytest.raises(ValueError) as e:
        get_changes_distribution("EUR", "USD", date(2023, 9, 9), "Cat")
    assert str(e.value) == "Analysis period must be either 'QUARTER' or 'MONTH'"


def test_invalid_start_date_format():
    """
    Test case for testing function behavior with invalid start date format input.
    """
    with pytest.raises(ValueError) as e:
        get_changes_distribution("EUR", "USD", date(2001, 1, 1), AnalysisPeriod.QUARTER)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_changes_distribution(
            "EUR", "USD", date(2012, 13, 1), AnalysisPeriod.QUARTER
        )
    assert str(e.value) == "month must be in 1..12"

    start_date = date.today() + timedelta(days=10)
    with pytest.raises(ValueError) as e:
        get_changes_distribution("EUR", "USD", start_date, AnalysisPeriod.MONTH)
    assert str(e.value) == "Start date cannot be in the future"


def test_valid_requests():
    """
    Test case for testing function behavior with valid input.
    """
    hist, bins = get_changes_distribution(
        "EUR", "USD", date(2023, 9, 9), AnalysisPeriod.QUARTER
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert round(bins[0], 4) == -0.0117
    assert round(bins[-1], 4) == 0.0070
    assert hist[0] == 1
    assert hist[-1] == 5
    assert sum(hist) == 80

    hist, bins = get_changes_distribution(
        "EUR", "USD", date(2021, 1, 20), AnalysisPeriod.MONTH
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert round(bins[0], 4) == -0.0056
    assert round(bins[-1], 4) == 0.0058
    assert hist[0] == 1
    assert hist[-1] == 1
    assert sum(hist) == 22

    start_date = date.today() - timedelta(days=10)
    hist, bins = get_changes_distribution(
        "EUR", "USD", start_date, AnalysisPeriod.MONTH
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert sum(hist) <= 8  # in last 10 days there are at least 2 weekend's days

    start_date = date.today() - timedelta(days=40)
    hist, bins = get_changes_distribution(
        "EUR", "USD", start_date, AnalysisPeriod.QUARTER
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert sum(hist) <= 28  # in last 40 days there are at least 8 weekend's days

    start_date = date.today() - timedelta(days=110)
    hist, bins = get_changes_distribution(
        "EUR", "USD", start_date, AnalysisPeriod.QUARTER
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert sum(hist) <= 80  # in last 110 days there are at least 30 weekend's days

@patch('app.api.requests.get')
def test_no_internet_connection(mock_get):
    """
    Test case for testing function behavior with no internet connection.
    """
    mock_get.side_effect = requests.RequestException("Connection to NBP API not available")
    with pytest.raises(requests.RequestException) as e:
        get_changes_distribution("EUR", "USD", date(2023, 9, 9), AnalysisPeriod.QUARTER)
    assert str(e.value) == "Connection to NBP API not available"

def test_get_changes_distribution():
    """
    Test of determine distribution of monthly or quarterly
    changes in any user-selected currency pairs, e.g. EUR/USD as a
    histogram of the frequency of occurrence of value changes in a given
    range as text. The analysis consists in calculating on successive days
    of the session the changes in relation to previous sessions and
    summing them up within the counted period.
    """

    fixed_date = date(2024, 6, 27)

    hist_month, bins_month = get_changes_distribution('USD', 'EUR', fixed_date - timedelta(days=30),
                                                      AnalysisPeriod.MONTH)
    assert isinstance(hist_month, np.ndarray)
    assert isinstance(bins_month, np.ndarray)
    assert len(hist_month) == 14
    assert len(bins_month) == 15

    expected_hist_month = np.array([1, 1, 0, 0, 0, 0, 1, 3, 1, 6, 3, 3, 1, 1])
    expected_bins_month = np.array(
        [-0.01325878, -0.01188326, -0.01050775, -0.00913224, -0.00775673, -0.00638122,
         -0.0050057, -0.00363019, -0.00225468, -0.00087917, 0.00049634, 0.00187186,
         0.00324737, 0.00462288, 0.00599839])

    assert np.array_equal(hist_month, expected_hist_month)
    assert np.allclose(bins_month, expected_bins_month)

    hist_quarter, bins_quarter = get_changes_distribution('GBP', 'JPY', fixed_date - timedelta(days=90),
                                                          AnalysisPeriod.QUARTER)
    assert isinstance(hist_quarter, np.ndarray)
    assert isinstance(bins_quarter, np.ndarray)
    assert len(hist_quarter) == 14
    assert len(bins_quarter) == 15

    expected_hist_quarter = np.array([1, 0, 1, 4, 6, 13, 17, 5, 5, 6, 1, 0, 0, 1])
    expected_bins_quarter = np.array(
        [-6.49540025e-05, -5.57273537e-05, -4.65007050e-05, -3.72740562e-05, -2.80474075e-05, -1.88207587e-05,
         -9.59410995e-06, -3.67461187e-07, 8.85918757e-06, 1.80858363e-05, 2.73124851e-05, 3.65391338e-05,
         4.57657826e-05, 5.49924314e-05, 6.42190801e-05])

    assert np.array_equal(hist_quarter, expected_hist_quarter)
    assert np.allclose(bins_quarter, expected_bins_quarter)
    pass
