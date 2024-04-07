# You can can this file from the root directory of the project by running `python -m app.main`
from datetime import date

from .api import get_changes_distribution
from .constans import AnalysisPeriod


def main():
    print(get_changes_distribution("EUR", "USD", date(2023, 9, 9), AnalysisPeriod.QUARTER))


if __name__ == "__main__":
    main()
