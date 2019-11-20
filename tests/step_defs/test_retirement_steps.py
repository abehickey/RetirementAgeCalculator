from unittest import mock
import pytest

from pytest_bdd import scenarios, given, when, then


import retirement
from retireCalc import getAge


EXTRA_TYPES = {
    'Number': int,
}


CONVERTERS = {
    'birth_year': int,
    'age_years': int,
    'age_months': int,
}


scenarios('../features/retirement.feature', example_converters=CONVERTERS)

@given('retirment.py has started')
def start_retirement():
    pass


@when('the birth year "<birth_year>" is entered')
def birthyear(birth_year, capsys):
    # retirement.input = birth_year
    # output = retirement.inputYear()
    # out, err = capsys.readouterr()
    with mock.patch('builtins.input', return_value=birth_year):
        output = retirement.inputYear()
        return output

@then('the age of retirement is "<age_years>" years and "<age_months>" months')
def retirement_age(birthyear, age_years, age_months):
    age, mon = getAge(birthyear)
    assert age == age_years and mon == age_months



