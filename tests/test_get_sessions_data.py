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
