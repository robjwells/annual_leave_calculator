"""Partial-year annual leave calculator

This script calculates how many annual leave days an employee will accrue
for working a portion of a year.

This is helpful for calculating new employees’ leave entitlement,
how much leaving employees will accrue by the day they finish,
or how many days temporary employees are entitled to take.

This script currently assumes that the annual leave year matches
the calendar year (and so runs January 1–December 31).

If your leave year starts part-way through the calendar year,
it will need some conditional logic to set the constants
AL_YEAR_START and AL_YEAR_END.

The actual calculation is simple: the length of the employee’s working
period as a proportion of the length of the leave year.

The 'Employee finish date' should either be the annual leave year
end date (for new employees) or the employee’s final day with the
company (and so is included in the leave accrual calculation.)
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
