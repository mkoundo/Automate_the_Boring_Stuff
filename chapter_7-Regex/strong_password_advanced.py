"""
Ref: Chapter 7 - Regular Expressions
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
"""


import re


def strong_pass(password):
    passregex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
    '''
    ^ ... $     means the expression applies to the entire string from start^ to end$
    {8,}        means the search string is 8 characters or more in length 
    [a-zA-Z\d]  means each character in the string must match one of the following: a-z, A-Z and 0-9
    (?=...)[]   means look ahead before the match. The order in which the look aheads are done does not matter. 
                Lookarounds stand their ground. They look immediately to the left or right of the engine's current 
                position on the string — but do not alter that position. e.g A(?=5) After the engine matches the A, 
                the lookahead (?=5) asserts that at the current position in the string, what immediately follows is a 5
    (?=.*[a-z]) the look ahead (?=.*[a-z]) asserts that at the current position in the string,
    (?=.*[A-Z]) what follows is zero or more (.*) lower case letters, upper case letters or digits
    (?=.*[\d])  
    
                additional examples of lookaheads
                a(?=a5) applied to aa5 will find the first a
                (?=a5)a applied to aa5 will find the second a           
    '''


    match = passregex.search(password)
    if match is None:
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
