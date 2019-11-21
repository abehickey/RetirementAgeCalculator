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


@given('retirement.py has started')
def start_retirement():
    pass


@pytest.fixture
@when('the birth year "<birth_year>" is entered')
def birthyear(birth_year):
    # retirement.input = birth_year
    # output = retirement.inputYear()
    # out, err = capsys.readouterr()
    with mock.patch('builtins.input', return_value=birth_year):
        output = retirement.inputYear()
        return output
    #return birth_year


@then('the age of retirement is "<age_years>" years and "<age_months>" months')
def retirement_age(birthyear, age_years, age_months):
    age, mon = getAge(birthyear)
    assert age == age_years and mon == age_months


# @pytest.fixture
# @when('the invalid birth year "<birth_year>" is entered')
# def invalid_year(birth_year):
#     return birth_year
#
# @then('an error is raised')
# def year_error(invalid_year):
#     with pytest.raises(Exception):
#         with mock.patch('builtins.input', return_value=invalid_year):
#             output = retirement.inputYear()




