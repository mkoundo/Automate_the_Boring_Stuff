"""
Ref: Chapter 5 - Dictionaries
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        michael.koundouros@outlook.com
        July 2020

Here’s a program that uses a dictionary that contains other dictionaries of what items guests are bringing to a picnic.
The totalBrought() function can read this data structure and calculate the total number of an item being brought by all
the guests.
"""

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalbrought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought += v.get(item, 0)
    return num_brought


print('Number of things being brought:')
print(' - Apples         ' + str(totalbrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalbrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalbrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalbrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalbrought(allGuests, 'apple pies')))
