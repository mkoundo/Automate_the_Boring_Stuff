"""
Ref: Chapter 7 - Regular Expressions
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        michael.koundouros@outlook.com
        July 2020

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
"""


import re


def strong_pass(password):
    matchlower = re.search(r'[a-z]', password)              # Search for a lower case letter
    matchupper = re.search(r'[A_Z]', password)              # Search for an upper case letter
    matchdigit = re.search(r'\d', password)                 # Search for a digit 0-9
    matchlength = re.search(r'[a-zA-Z\d]{8}', password)     # Search for at least 8 characters

    if matchlower is None or matchupper is None or matchdigit is None or matchlength is None:
        print('Invalid Password Format.')
    else:
        print('Password is OK')
    return


password = 'Abcdefg8'  # Valid password
strong_pass(password)

password = 'Abcd8'     # Invalid: Password too short
strong_pass(password)

password = 'abcdefg8'  # Invalid: Password doesn't contain any upper case letters
strong_pass(password)

password = 'ABCDEFG8'  # Invalid: Password doesn't contain any lower case letters
strong_pass(password)

password = 'Abcdefgg'  # Invalid: Password doesn't contain any digits
strong_pass(password)
