import pytest
import requests

from freezegun import freeze_time
from unittest.mock import patch

from app.constans import AnalysisPeriod
from app.api import get_sessions_data


def test_invalid_currency():
    """
    Test case for testing function behavior with invalid currency input.
    """

    with pytest.raises(ValueError) as e:
        get_sessions_data("ASD", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_sessions_data("ASFKJE", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_sessions_data("ÓSD", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"
    pass


def test_no_currency():
    """
    Test case for testing function behavior with no currency input.
    """
    with pytest.raises(ValueError) as e:
        get_sessions_data("", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_sessions_data("", AnalysisPeriod.YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_sessions_data("", AnalysisPeriod.WEEK)
    assert str(e.value) == "Invalid request parameters"
    pass


def test_invalid_analysis_period():
    """
    Test case for testing function behavior with invalid analysis_period.
    """
    with pytest.raises(ValueError) as e:
        get_sessions_data("USD", 7)
    assert str(e.value) == "Error: not a time period"

    with pytest.raises(ValueError) as e:
        get_sessions_data("GDP", 0)
    assert str(e.value) == "Error: not a time period"

    with pytest.raises(ValueError) as e:
        get_sessions_data("EUR", "EUR")
    assert str(e.value) == "Error: not a time period"
    pass


@freeze_time("2024-05-25")
def test_valid_requests():
    """
    Test case for testing function behavior with valid input.
    """
    up, down, steady = get_sessions_data("USD", AnalysisPeriod.WEEK)
    assert up == 1
    assert down == 1
    assert steady == 0

    up, down, steady = get_sessions_data("GBP", AnalysisPeriod.TWO_WEEKS)
    assert up == 2
    assert down == 3
    assert steady == 0

    up, down, steady = get_sessions_data("EUR", AnalysisPeriod.MONTH)
    assert up == 4
    assert down == 5
    assert steady == 0
    pass

@freeze_time("2024-05-25")
@patch('app.api.requests.get')
def test_no_internet_connection(mock_get):
    """
    Test case for testing function behavior with no internet connection.
    """
    mock_get.side_effect = requests.RequestException("Connection to NBP API not available")
    with pytest.raises(requests.RequestException) as e:
        get_sessions_data("EUR", AnalysisPeriod.MONTH)
    assert str(e.value) == "Connection to NBP API not available"

@freeze_time("2024-06-27")
def test_analysis_periods():
    """
    Test of determine the number of rising, falling and
    unchanged sessions for the periods of the last 1 week, 2 weeks, 1
    month, 1 quarter, half a year and 1 year for the currency selected by
    the user using the program option
    """
    sessions_week = get_sessions_data('USD', AnalysisPeriod.WEEK)
    assert isinstance(sessions_week, tuple)
    assert len(sessions_week) == 3
    assert all(isinstance(s, int) for s in sessions_week)
    assert sessions_week == (1, 1, 0)

    sessions_2_weeks = get_sessions_data('USD', AnalysisPeriod.TWO_WEEKS)
    assert isinstance(sessions_2_weeks, tuple)
    assert len(sessions_2_weeks) == 3
    assert all(isinstance(s, int) for s in sessions_2_weeks)
    assert sessions_2_weeks == (2, 2, 0)

    sessions_month = get_sessions_data('USD', AnalysisPeriod.MONTH)
    assert isinstance(sessions_month, tuple)
    assert len(sessions_month) == 3
    assert all(isinstance(s, int) for s in sessions_month)
    assert sessions_month == (6, 5, 0)

    sessions_quarter = get_sessions_data('USD', AnalysisPeriod.QUARTER)
    assert isinstance(sessions_quarter, tuple)
    assert len(sessions_quarter) == 3
    assert all(isinstance(s, int) for s in sessions_quarter)
    assert sessions_quarter == (15, 15, 0)

    sessions_half_year = get_sessions_data('USD', AnalysisPeriod.HALF_YEAR)
    assert isinstance(sessions_half_year, tuple)
    assert len(sessions_half_year) == 3
    assert all(isinstance(s, int) for s in sessions_half_year)
    assert sessions_half_year == (32, 31, 0)

    sessions_year = get_sessions_data('USD', AnalysisPeriod.YEAR)
    assert isinstance(sessions_year, tuple)
    assert len(sessions_year) == 3
    assert all(isinstance(s, int) for s in sessions_year)
    assert sessions_year == (59, 58, 0)

    sessions_year_eur = get_sessions_data('EUR', AnalysisPeriod.YEAR)
    assert isinstance(sessions_year_eur, tuple)
    assert len(sessions_year_eur) == 3
    assert all(isinstance(s, int) for s in sessions_year_eur)
    assert sessions_year_eur == (62, 63, 0)

    pass