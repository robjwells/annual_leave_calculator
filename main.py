"""Partial-year annual leave calculator

This script calculates how many annual leave days an employee
will accrue for working a portion of a year.

This is helpful for calculating new employees’ leave entitlement,
how much leaving employees will accrue by the day they finish,
or how many days temporary employees are entitled to take.

The actual calculation is simple: the length of the employee’s working
period as a proportion of the length of the leave year.

The 'Employee finish date' should either be the annual leave year
end date (for new employees) or the employee’s final day with the
company (and so is included in the leave accrual calculation.)

Constants
=========

AL_YEAR_START
-------------

The default first day of the annual leave year
(by default January 1 of the current year).

DEFAULT AL
----------

The default amount of leave (by default 28 days).

RESULT_DECIMAL_PLACES
---------------------

The precision to round the resulting annual leave allowance
(by default 2 decimal places).

"""
from datetime import datetime, timedelta
from typing import Callable, TypeVar

T = TypeVar("T")
current_year = datetime.now().year

# Modify these constants to suit your circumstances
DEFAULT_AL_YEAR_START = datetime(current_year, month=1, day=1)
DEFAULT_AL = 28
RESULT_DECIMAL_PLACES = 2


def main() -> None:
    al_for_full_year = prompt_for_al_amount()

    al_year_start = prompt_for_date("Leave year start", default=DEFAULT_AL_YEAR_START)
    al_year_end = al_year_start.replace(year=al_year_start.year + 1) - timedelta(days=1)

    start_date = prompt_for_date("Employee start", default=al_year_start)
    end_date = prompt_for_date("Employee finish", default=al_year_end)

    al_year_days = (al_year_end - al_year_start).days + 1
    employed_days = (end_date - start_date).days + 1
    # +1 as we assume, eg, starting and leaving on Jan 1 accrues
    # 1 day's worth of leave, not zero

    proportion_of_al_year_worked = employed_days / al_year_days
    al_days_available = al_for_full_year * proportion_of_al_year_worked
    print(round(al_days_available, RESULT_DECIMAL_PLACES), "days annual leave")


def _prompt_wrapper(message: str, default: T, constructor: Callable[[str], T]) -> T:
    try:
        return constructor(input(message))
    except ValueError:
        return default


def prompt_for_al_amount(default: float = DEFAULT_AL) -> float:
    return _prompt_wrapper(
        message=f"How many days annual leave for the full year? [{default}] ",
        default=default,
        constructor=float,
    )


def prompt_for_date(which: str, default: datetime) -> datetime:
    return _prompt_wrapper(
        message=f"{which} date [{default:%Y-%m-%d}]: ",
        default=default,
        constructor=lambda s: datetime.strptime(s, "%Y-%m-%d"),
    )


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()  # Prevent messing up some shells
