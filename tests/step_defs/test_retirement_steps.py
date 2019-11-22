import pytest
from pytest_bdd import scenarios, given, when, then
from retire_calc import get_age


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
    return birth_year


@then('the age of retirement is "<age_years>" years and "<age_months>" months')
def retirement_age(birthyear, age_years, age_months):
    age, mon = get_age(birthyear)
    assert age == age_years and mon == age_months


@pytest.fixture
@when('the invalid birth year "<bad_year>" is entered')
def invalid_year(bad_year):
    return bad_year


@then('an error is raised')
def year_error(invalid_year):
    try:
        assert int(invalid_year) < 1900
    except:
        with pytest.raises(Exception):
            assert int(invalid_year) < 1900





