"""
Ref: Chapter 7 - Regular Expressions
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are
passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the
string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""


import re


def regex_strip(strings, option):

    optionregex = '[^' + option + ']'
    if option == '':
        stringregex = re.compile(r'(\S+)')
    else:
        stringregex = re.compile(r'' + optionregex + '\S+' + optionregex)

    match = stringregex.search(strings)
    return match.group()


print(regex_strip('    testword   ', ''))
print(regex_strip('....testword....', '.'))
print(regex_strip('ababtestwordababaaab', 'ab'))