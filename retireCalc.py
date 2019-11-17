#####################################################
# Programmer: Abe Hickey
# Class: CSC.256.0001
# File: retireCalc.py
# Description: Calculation module for FullRetirementAge.py
#####################################################


import calendar


# Returns retirement age and month for full SSA benefits based on birth year
def getAge(yr):

                # Dictionary of year born with age and month for full SSA benefits
    ageDict = {1:{"year": 1938, "age": 65, "month": 2},
               2:{"year": 1939, "age": 65, "month": 4},
               3:{"year": 1940, "age": 65, "month": 6},
               4:{"year": 1941, "age": 65, "month": 8},
               5:{"year": 1942, "age": 65, "month": 10},
               6:{"year": 1955, "age": 66, "month": 2},
               7:{"year": 1956, "age": 66, "month": 4},
               8:{"year": 1957, "age": 66, "month": 6},
               9:{"year": 1958, "age": 66, "month": 8},
               10:{"year": 1959, "age": 66, "month": 10}
               }

    if yr <= 1937:   # Birth year of 1937 or before returns retirement age of 65 years and 0 months
        return 65, 0
    elif yr >= 1960:   # Birth year of 1960 or after returns retirement age of 67 years and 0 months
        return 67, 0
    elif yr >= 1943 and yr <= 1954:  # Birth year of 1943 to 1954 returns retirement age of 66 years and 0 months
        return 66, 0
    else:   # Use Dictionary to return retirement age and month
        for k in ageDict:
            if ageDict[k]["year"] == yr:
                return ageDict[k].get("age"), ageDict[k].get("month")


# Returns month and year when full SSA benefits may be obtained
def getWhen(byr, bm, ra, rm):
    year = byr + ra #birth year + retirement age
    month = bm + rm #birth month + retirement month
    if month > 12: # Determine if retirement month pushes into the next year
        year = year + 1
        month = month - 12

    return year, calendar.month_name[month]
