# Partial-year annual leave calculator

This script calculates how many annual leave days an employee will
accrue for working a portion of a year.

This is helpful for calculating new employees’ leave entitlement, how
much leaving employees will accrue by the day they finish, or how many
days temporary employees are entitled to take.

This script currently assumes that the annual leave year matches the
calendar year (and so runs January 1–December 31).

If your leave year starts part-way through the calendar year, it will
need some conditional logic to set the constants `AL_YEAR_START` and
`AL_YEAR_END`.

The actual calculation is simple: the length of the employee’s working
period as a proportion of the length of the leave year.

The ‘Employee finish date’ should either be the annual leave year end
date (for new employees) or the employee’s final day with the company
(and so is included in the leave accrual calculation.)

- `main.AL_YEAR_START`*: datetime*
  The first day of the annual leave year (by default January 1 of the
  current year).

- `main.AL_YEAR_END`*: datetime*
  The last day of the annual leave year (by default December 31 of the
  current year).

- `main.STATUTORY_AL`*: Number*
  The default amount of leave (by default 28 days, the current UK
  statutory minimum annual leave allowance).

  You should probably set it to be the amount of discretionary leave
  that an employee can take, especially if you otherwise include (eg
  in the UK) bank holidays in the annual leave total, as these are
  taken automatically on specific days in the year.

- `main.RESULT_DECIMAL_PLACES`*: int*
  The precision to round the resulting annual leave allowance (by
  default 2 decimal places).
