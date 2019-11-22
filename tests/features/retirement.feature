@retirement-calculator
Feature: Retirement Age Calculator

   The retirement age calculator determines when someone is eligible to receive
   Social Security benefits.  The user enters his/her birth year and month.
   The calculator determines and displays the year and month when the user can
   obtain benefits.

   @valid-years
   Scenario Outline: Determine retirement age
     Given retirement.py has started
     When the birth year "<birth_year>" is entered
     Then the age of retirement is "<age_years>" years and "<age_months>" months

     Examples:
        | birth_year | age_years | age_months |
        | 1925       | 65        | 0          |
        | 1937       | 65        | 0          |
        | 1938       | 65        | 2          |
        | 1939       | 65        | 4          |
        | 1940       | 65        | 6          |
        | 1941       | 65        | 8          |
        | 1942       | 65        | 10         |
        | 1943       | 66        | 0          |
        | 1954       | 66        | 0          |
        | 1955       | 66        | 2          |
        | 1956       | 66        | 4          |
        | 1957       | 66        | 6          |
        | 1958       | 66        | 8          |
        | 1959       | 66        | 10         |
        | 1960       | 67        | 0          |
        | 2000       | 67        | 0          |


   Scenario Outline: Invalid age
     Given retirement.py has started
     When the invalid birth year "<bad_year>" is entered
     Then an error is raised

     Examples:
       | bad_year   |
       | 1899       |
       | -1970      |
       | 1980.5     |
       | s1990      |


