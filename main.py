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

CURRENT_YEAR = datetime.now().year
AL_YEAR_START = datetime(CURRENT_YEAR, month=1, day=1)
AL_YEAR_END = datetime(CURRENT_YEAR, month=12, day=31)
AL_YEAR_LENGTH = (AL_YEAR_END - AL_YEAR_START).days + 1
STATUTORY_AL = 28


def main():

    try:
        al_for_full_year = float(
            input(f"How many days annual leave for the full year? [{STATUTORY_AL}] ")
        )
    except ValueError:
        al_for_full_year = STATUTORY_AL
    try:
        start_date = datetime.strptime(
            input(
                f"Employee start date in YYYY-MM-DD format [{AL_YEAR_START:%Y-%m-%d}]: "
            ),
            "%Y-%m-%d",
        )
    except ValueError:
        start_date = AL_YEAR_START
    try:
        end_date = datetime.strptime(
            input(
                f"Employee finish date in YYYY-MM-DD format [{AL_YEAR_END:%Y-%m-%d}): "
            ),
            "%Y-%m-%d",
        )
    except ValueError:
        end_date = AL_YEAR_END

    al_period_length = (end_date - start_date).days + 1
    # +1 as we assume, eg, starting and leaving on Jan 1 accrues
    # 1 day's worth of leave, not zero

    proportion_of_al_year_worked = al_period_length / AL_YEAR_LENGTH
    al_days_available = al_for_full_year * proportion_of_al_year_worked
    print(f"{round(al_days_available, 2)} days annual leave")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()  # Prevent messing up some shells
