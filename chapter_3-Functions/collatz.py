"""
Ref: Chapter 3 - Functions
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        michael.koundouros@outlook.com
        July 2020

The Collatz Sequence
Write a function named collatz() that has one parameter named number. If number is even,
then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and
return 3 * number + 1.

Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the
function returns the value 1.
"""


import sys


def collatz(number):
    if number % 2 == 0:
        coll = number // 2
    else:
        coll = (3 * number) + 1
    print(coll)
    return coll


print('Enter a Number: ')

try:
    tmp = int(input())
    while tmp > 1:
        tmp = collatz(tmp)
except ValueError:
    print('Invalid Input')
    sys.exit(1)
