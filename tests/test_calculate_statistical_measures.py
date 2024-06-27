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

@freeze_time("2024-06-27")
def test_get_statistical_measures():
    """
    Test of determine median, dominant, standard deviation or
    coefficient of variation for the last 1 week, 2 weeks, 1 month, 1 quarter,
    half a year and 1 year for the currency selected by the user using the
    program option

    """
    stats_month = get_statistical_measures('GBP', AnalysisPeriod.MONTH)
    assert isinstance(stats_month, tuple)
    assert len(stats_month) == 4
    assert all(isinstance(s, float) for s in stats_month)
    assert stats_month == (5.1033, 5.0055, 0.05363146908476847, 0.010524513828495183)

    stats_half_year = get_statistical_measures('CHF', AnalysisPeriod.HALF_YEAR)
    assert isinstance(stats_half_year, tuple)
    assert len(stats_half_year) == 4
    assert all(isinstance(s, float) for s in stats_half_year)
    assert stats_half_year == (4.47955, 4.3072, 0.11234511930955293, 0.024995720277755262)

    stats_week = get_statistical_measures('GBP', AnalysisPeriod.WEEK)
    assert isinstance(stats_week, tuple)
    assert len(stats_week) == 4
    assert all(isinstance(s, float) for s in stats_week)
    assert stats_week == (5.1027, 5.0774, 0.018802739162154112, 0.003685900966066053)

    stats_two_weeks = get_statistical_measures('GBP', AnalysisPeriod.TWO_WEEKS)
    assert isinstance(stats_two_weeks, tuple)
    assert len(stats_two_weeks) == 4
    assert all(isinstance(s, float) for s in stats_two_weeks)
    assert stats_two_weeks == (5.12575, 5.0774, 0.033071982099656505, 0.006451760442691923)

    stats_quarter = get_statistical_measures('GBP', AnalysisPeriod.QUARTER)
    assert isinstance(stats_quarter, tuple)
    assert len(stats_quarter) == 4
    assert all(isinstance(s, float) for s in stats_quarter)
    assert stats_quarter == (5.0233, 4.9651, 0.0567011293094921, 0.011245891574738985)

    stats_year = get_statistical_measures('GBP', AnalysisPeriod.YEAR)
    assert isinstance(stats_year, tuple)
    assert len(stats_year) == 4
    assert all(isinstance(s, float) for s in stats_year)
    assert stats_year == (5.0785, 5.0117, 0.10438009921555647, 0.02042470518293572)

    pass