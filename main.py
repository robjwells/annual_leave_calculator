"""Partial-year annual leave calculator

This calculates how many days of annual leave a new employee can take
for the rest of the year.

This assumes the annual leave year matches the calendar year (Jan 1-Dec 31).

This works by taking the full leave allowance for the year (as if the
employee started on January 1), and keeping a proportion of it that
matches the proportion of days left in the year.

The proportion of the year that remains is worked out by getting the year
length (365 or 366) and dividing the number of days left in the year by it.

The number of days left in the year is calculated by taking the day of the year
(strftime %j) and subtracting it from the year length.

Or in short:

    AL left = year AL allowance * (days left / year length)

"""
from datetime import datetime
from typing import Callable, TypeVar

CURRENT_YEAR = datetime.now().year
AL_YEAR_START = datetime(CURRENT_YEAR, month=1, day=1)
AL_YEAR_END = datetime(CURRENT_YEAR, month=12, day=31)
AL_YEAR_LENGTH = (AL_YEAR_END - AL_YEAR_START).days + 1
STATUTORY_AL = 28
RESULT_DECIMAL_PLACES = 2


def main() -> None:
    al_for_full_year = prompt_for_al_amount()
    start_date = prompt_for_start_date()
    end_date = prompt_for_end_date()

    al_period_length = (end_date - start_date).days + 1
    # +1 as we assume, eg, starting and leaving on Jan 1 accrues
    # 1 day's worth of leave, not zero

    proportion_of_al_year_worked = al_period_length / AL_YEAR_LENGTH
    al_days_available = al_for_full_year * proportion_of_al_year_worked
    print(f"{round(al_days_available, RESULT_DECIMAL_PLACES)} days annual leave")


T = TypeVar("T")


def _prompt_wrapper(message: str, default: T, constructor: Callable[[str], T]) -> T:
    try:
        return constructor(input(message))
    except ValueError:
        return default


def prompt_for_al_amount(default: float = STATUTORY_AL) -> float:
    return _prompt_wrapper(
        message=f"How many days annual leave for the full year? [{default}] ",
        default=default,
        constructor=float,
    )


def prompt_for_start_date(default: datetime = AL_YEAR_START) -> datetime:
    return _prompt_wrapper(
        message=f"Employee start date in YYYY-MM-DD format [{default:%Y-%m-%d}]: ",
        default=default,
        constructor=lambda s: datetime.strptime(s, "%Y-%m-%d"),
    )


def prompt_for_end_date(default: datetime = AL_YEAR_END) -> datetime:
    return _prompt_wrapper(
        message=f"Employee finish date in YYYY-MM-DD format [{default:%Y-%m-%d}]: ",
        default=default,
        constructor=lambda s: datetime.strptime(s, "%Y-%m-%d"),
    )


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()  # Prevent messing up some shells
