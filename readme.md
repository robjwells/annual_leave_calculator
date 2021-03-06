# Partial-year annual leave calculator

This script calculates how many annual leave days an employee will
accrue for working a portion of a year.

This is helpful for calculating new employees’ leave entitlement, how
much leaving employees will accrue by the day they finish, or how many
days temporary employees are entitled to take.

The actual calculation is simple: the length of the employee’s working
period as a proportion of the length of the leave year.

The ‘Employee finish date’ should either be the annual leave year end
date (for new employees) or the employee’s final day with the company
(and so is included in the leave accrual calculation.)

- `main.DEFAULT_AL_YEAR_START`*: datetime*
  The default first day of the annual leave year (by default January 1
  of the current year).

- `main.DEFAULT_AL`*: Number*
  The default amount of leave (by default 28 days).

  You should probably set it to be the amount of discretionary leave
  that an employee can take, especially if you otherwise include (eg
  in the UK) bank holidays in the annual leave total, as these are
  taken automatically on specific days in the year.

- `main.RESULT_DECIMAL_PLACES`*: int*
  The precision to round the resulting annual leave allowance (by
  default 2 decimal places).
