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

current_year = datetime.now().year
al_year_start = datetime(current_year, month=1, day=1)
al_year_end = datetime(current_year, month=12, day=31)
al_year_length = (al_year_end - al_year_start).days + 1

al_for_full_year = float(input("How many days annual leave for the full year? "))
try:
    start_date = datetime.strptime(
        input(
            f"Employee start date in YYYY-MM-DD format [{al_year_start:%Y-%m-%d}]: "
        ),
        "%Y-%m-%d",
    )
except ValueError:
    start_date = al_year_start
try:
    end_date = datetime.strptime(
        input(
            f"Employee finish date in YYYY-MM-DD format [{al_year_end:%Y-%m-%d}): "
        ),
        "%Y-%m-%d",
    )
except ValueError:
    end_date = al_year_end

al_period_length = (end_date - start_date).days + 1
# +1 as we assume, eg, starting and leaving on Jan 1 accrues
# 1 day's worth of leave, not zero

proportion_of_al_year_worked = al_period_length / al_year_length
al_days_available = al_for_full_year * proportion_of_al_year_worked
print(f"{round(al_days_available, 2)} days annual leave")
