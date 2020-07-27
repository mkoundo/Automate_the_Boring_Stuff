"""
Ref: Chapter 4 - Lists
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items
separated by a comma and a space, with and inserted before the last item. For example, passing
the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your
function should be able to work with any list value passed to it. Be sure to test the case where
an empty list [] is passed to your function.
"""


def comma(mylist):
    try:
        list_to_string = ''
        for items in mylist[:-1]:
            list_to_string += str(items) + ', '
        return list_to_string[:-2] + ' and ' + str(mylist[-1])
    except IndexError:
        print('Error: Empty list entered.')


enteredtList = []
print(comma(enteredtList))
