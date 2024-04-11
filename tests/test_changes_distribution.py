from datetime import date, timedelta

import pytest

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
    assert round(bins[0], 4) == -0.0076
    assert round(bins[-1], 4) == 0.0045
    assert hist[0] == 1
    assert hist[-1] == 1
    assert sum(hist) == 5

    start_date = date.today() - timedelta(days=40)
    hist, bins = get_changes_distribution(
        "EUR", "USD", start_date, AnalysisPeriod.QUARTER
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert round(bins[0], 4) == -0.0076
    assert round(bins[-1], 4) == 0.0082
    assert hist[0] == 1
    assert hist[-1] == 1
    assert sum(hist) == 27

    start_date = date.today() - timedelta(days=110)
    hist, bins = get_changes_distribution(
        "EUR", "USD", start_date, AnalysisPeriod.QUARTER
    )
    assert len(hist) == 14
    assert len(bins) == 15
    assert round(bins[0], 4) == -0.0078
    assert round(bins[-1], 4) == 0.0117
    assert hist[0] == 2
    assert hist[-1] == 1
    assert sum(hist) == 74
