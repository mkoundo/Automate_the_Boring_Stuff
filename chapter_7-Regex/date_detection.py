"""
Ref: Chapter 7 - Regular Expressions
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31,
the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit,
it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent
dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write
additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has
28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly
divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how
this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
"""


import re


def test_date(date):
    match = re.search(r'([0-2][1-9]|[1-3][01])/(0[1-9]|1[0-2])/([12][0-9][0-9][0-9])', date)
    '''
    Regex to search for date in format DD/MM/YYYY
    groups are enclosed in (), character class in [] and | is the OR operator
    DD
    first group: [0-2][1-9]|[1-3][01])  match first digit as 0-2 AND second digit as 1-9 OR
                                        match first digit as 1-3 AND second digit as 0 or 1
                 /
    MM
    second group: 0[1-9]|1[0-2]         match third digit a 0 and fourth digit as 1-9 OR
                                        match third digit a 1 and fourth digit as 0-2
                 /
    YYYY
    third group: [12][0-9][0-9][0-9]    match fifth digit as 1 or 2
                                        match sixth digit as 1-9
                                        match seventh digit as 1-9
                                        match eighth digit as 1-9
    '''

    # Assign date search match to variables
    if match is None:
        print('No date found!')
    else:
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))

    # Check if days in month are valid
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leapyeardays = 29
    else:
        leapyeardays = 28

    daysinmonth = {1: 31, 2: leapyeardays, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if day <= daysinmonth[month]:
        print('Valid Date')
    else:
        print('Date is not valid')

    return

date_string = 'Test if 29/02/2000 is a valid date'  # leap year because 1900 % 4 =0 AND 1900 % 400 = 0
print(date_string)
test_date(date_string)
date_string = 'Test if 29/02/1900 is a valid date'  # not a leap year because 1900 % 400 > 0
print(date_string)
test_date(date_string)
date_string = 'Test if 29/02/2020 is a valid date'    # leap year beacause 1900 % 4 =0 AND 1900 % 400 = 0
print(date_string)
test_date(date_string)
