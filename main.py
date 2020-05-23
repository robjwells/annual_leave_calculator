"""Partial-year annual leave calculator

This script calculates how many annual leave days an employee
will accrue for working a portion of a year.

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

Constants
=========

AL_YEAR_START
-------------

The first day of the annual leave year
(by default January 1 of the current year).

AL_YEAR_END
-----------

The last day of the annual leave year
(by default December 31 of the current year).

STATUTORY_AL
------------

The default amount of leave (by default 28 days,
the current UK statutory minimum annual leave allowance).

You should probably set it to be the amount of discretionary leave
that an employee can take, especially if you otherwise include (eg
in the UK) bank holidays in the annual leave total, as these are
taken automatically on specific days in the year.

RESULT_DECIMAL_PLACES
---------------------

The precision to round the resulting annual leave allowance
(by default 2 decimal places).

"""
from datetime import datetime
from typing import Callable, TypeVar

T = TypeVar("T")
current_year = datetime.now().year

AL_YEAR_START = datetime(current_year, month=1, day=1)
AL_YEAR_END = datetime(current_year, month=12, day=31)
AL_YEAR_LENGTH = (AL_YEAR_END - AL_YEAR_START).days + 1
STATUTORY_AL = 28
RESULT_DECIMAL_PLACES = 2


def main() -> None:
    al_for_full_year = prompt_for_al_amount()
    start_date = prompt_for_date("start", default=AL_YEAR_START)
    end_date = prompt_for_date("finish", default=AL_YEAR_END)

    al_period_length = (end_date - start_date).days + 1
    # +1 as we assume, eg, starting and leaving on Jan 1 accrues
    # 1 day's worth of leave, not zero

    proportion_of_al_year_worked = al_period_length / AL_YEAR_LENGTH
    al_days_available = al_for_full_year * proportion_of_al_year_worked
    print(round(al_days_available, RESULT_DECIMAL_PLACES), "days annual leave")


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


def prompt_for_date(which: str, default: datetime) -> datetime:
    return _prompt_wrapper(
        message=f"Employee {which} date in YYYY-MM-DD format [{default:%Y-%m-%d}]: ",
        default=default,
        constructor=lambda s: datetime.strptime(s, "%Y-%m-%d"),
    )


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()  # Prevent messing up some shells
