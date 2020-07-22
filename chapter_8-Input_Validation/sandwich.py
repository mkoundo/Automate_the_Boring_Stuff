"""
Ref: Chapter 8 - Input Validation
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they
enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their
selection.
"""


import pyinputplus as pyip

order = []

# Input order options into a list
breadselection = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
order.append(breadselection)
meatselection = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
order.append(meatselection)

prompt = 'Would you like cheese with that?\n'
cheesechoice = pyip.inputYesNo(prompt)
if cheesechoice == 'yes':
    cheeseselection = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
    order.append(cheeseselection)

prompt = 'Would you like any condiments?\n'
extraschoice = pyip.inputYesNo(prompt)
if extraschoice == 'yes':
    extrasselection = pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'], numbered=True)
    order.append(extrasselection)

sandwiches = pyip.inputInt('How many sandwiches would you like?\n', min=1)

menu = {'wheat': 1.10, 'white': 0.90, 'sourdough': 1.20, 'chicken': 1.20, 'turkey': 1.05, 'ham': 1.15,
        'tofu': 1.35, 'cheddar': 0.80, 'swiss': 0.90, 'mozzarella': 1.10, 'mayo': 0.30, 'mustard': 0.20,
        'lettuce': 0.10, 'tomato': 0.15}

total = 0

# Print order summary and total
print('Order Summary')
for orderitem in order:
    print(f'{orderitem.ljust(20)} {menu[orderitem.lower()]:0.2f}')
    total = total + menu[orderitem.lower()]

print(f'\n{"Sandwiches:".ljust(20)} {sandwiches}')
print(f'{"Total:".ljust(20)} {total*sandwiches:0.2f}')
