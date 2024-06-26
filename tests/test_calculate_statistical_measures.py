import pytest
import requests

from freezegun import freeze_time
from unittest.mock import patch

from app.constans import AnalysisPeriod
from app.api import get_statistical_measures


def test_invalid_currency():
    """
    Test case for testing function behavior with invalid currency input.
    """

    with pytest.raises(ValueError) as e:
        get_statistical_measures("ASD", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_statistical_measures("ASFKJE", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_statistical_measures("ÓSD", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"
    pass


def test_no_currency():
    """
    Test case for testing function behavior with no currency input.
    """
    with pytest.raises(ValueError) as e:
        get_statistical_measures("", AnalysisPeriod.HALF_YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_statistical_measures("", AnalysisPeriod.YEAR)
    assert str(e.value) == "Invalid request parameters"

    with pytest.raises(ValueError) as e:
        get_statistical_measures("", AnalysisPeriod.WEEK)
    assert str(e.value) == "Invalid request parameters"
    pass


def test_invalid_analysis_period():
    """
    Test case for testing function behavior with invalid analysis_period.
    """
    with pytest.raises(ValueError) as e:
        get_statistical_measures("USD", 7)
    assert str(e.value) == "Error: not a time period"

    with pytest.raises(ValueError) as e:
        get_statistical_measures("GDP", 0)
    assert str(e.value) == "Error: not a time period"

    with pytest.raises(ValueError) as e:
        get_statistical_measures("EUR", "EUR")
    assert str(e.value) == "Error: not a time period"
    pass


@freeze_time("2024-05-25")
def test_valid_requests():
    """
    Test case for testing function behavior with valid input.
    """
    median_value, mode, standard_deviation, coefficient_of_variation = get_statistical_measures("USD", AnalysisPeriod.WEEK)
    assert median_value == 3.9243
    assert round(mode, 4) == 3.9149
    assert round(standard_deviation, 4) == 0.0113
    assert round(coefficient_of_variation, 4) == 0.0029

    median_value, mode, standard_deviation, coefficient_of_variation = get_statistical_measures("GBP", AnalysisPeriod.TWO_WEEKS)
    assert median_value == 4.9794
    assert round(mode, 4) == 4.9651
    assert round(standard_deviation, 4) == 0.0155
    assert round(coefficient_of_variation, 4) == 0.0031

    median_value, mode, standard_deviation, coefficient_of_variation = get_statistical_measures("EUR", AnalysisPeriod.MONTH)
    assert median_value == 4.2977
    assert round(mode, 4) == 4.2575
    assert round(standard_deviation, 4) == 0.0280
    assert round(coefficient_of_variation, 4) == 0.0065

    pass

@freeze_time("2024-05-25")
@patch('app.api.requests.get')
def test_no_internet_connection(mock_get):
    """
    Test case for testing function behavior with no internet connection.
    """
    mock_get.side_effect = requests.RequestException("Connection to NBP API not available")
    with pytest.raises(requests.RequestException) as e:
        get_statistical_measures("GBP", AnalysisPeriod.TWO_WEEKS)
    assert str(e.value) == "Connection to NBP API not available"
