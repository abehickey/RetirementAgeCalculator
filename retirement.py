# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------

import calendar
import datetime


# ----------------------------------------------------------------------
# Calculation Functions
# ----------------------------------------------------------------------

def calculate_retirement_age(birth_year):
  if birth_year <= 1937:
    return 65, 0
  elif birth_year == 1938:
    return 65, 2
  elif birth_year == 1939:
    return 65, 4
  elif birth_year == 1940:
    return 65, 6
  elif birth_year == 1941:
    return 65, 8
  elif birth_year == 1942:
    return 65, 10
  elif 1943 <= birth_year <= 1954:
    return 66, 0
  elif birth_year == 1955:
    return 66, 2
  elif birth_year == 1956:
    return 66, 4
  elif birth_year == 1957:
    return 66, 6
  elif birth_year == 1958:
    return 66, 8
  elif birth_year == 1959:
    return 66, 10
  else:
    return 67, 0


def calculate_retirement_date(birth_year, birth_month, age_years, age_months):
  year = birth_year + age_years
  month = birth_month + age_months

  if month > 12:
    year += 1
    month -= 12
  
  return year, month
