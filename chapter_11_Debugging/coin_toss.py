#! python3
# coin_toss.py
# Author: Michael Koundouros
"""
The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy
game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep
the program from working correctly.
"""

import random


guess = ''
options = ['heads', 'tails']

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads

if options[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if options[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
