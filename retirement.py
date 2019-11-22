#####################################################
# Programmer: Abe Hickey
# Class: CSC.256.0001
# File: retirement.py
# Description: This program calculates when someone will receive full Social Security Benefits
#####################################################

import retire_calc
import datetime


# Get Birth year from user
def inputYear():
    while True:
        try:
            userInput = int(input("Please enter 4-digit birth year: "))
            if userInput < 1900 or userInput > int(datetime.datetime.now().year):  # if not 1900 to current year print message and ask for input again
                print("Sorry, input must be a 4-digit year between 1900 and the current year")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput


# Get Birth month from user
def inputMonth():
    print("1. January,  2. February,  3. March,  4. April")
    print("5. May,  6. June,  7. July,  8. August")
    print("9. September,  10. October, 11. November, 12. December")
    while True:
        try:
            userInput = int(input("Please the number of the birth month: "))
            if userInput < 1 or userInput > 12:  # if not from 1 to 12 print message and ask for input again
                print("Sorry, input must be a number from 1 to 12.")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput


def main():
    birthYear = inputYear()
    birthMon = inputMonth()
    print()

    age, mon = retire_calc.get_age(birthYear) #Get retirement age and month
    if mon == 0:
        print("Age for obtaining full SSA benefits: ", age)
    else:
        print("Age for obtaining full SSA benefits: ", age, "and", mon, "months")

    ssaYear, ssaMonth = retire_calc.getWhen(birthYear, birthMon, age, mon) #Determine when benefits can be obtained
    print("Full SSA benefits may be obtained " + ssaMonth + " " + str(ssaYear) + ".")


if __name__ == "__main__":
    main()
