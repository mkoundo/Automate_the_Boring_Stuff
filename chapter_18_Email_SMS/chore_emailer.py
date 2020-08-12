#! python3
# chore_emailer.py
# Author: Michael Koundouros
"""
Write a program that takes a list of people’s email addresses and a list of chores that need to be done and
randomly assigns chores to people. Email each person their assigned chores. If you’re feeling ambitious,
keep a record of each person’s previously assigned chores so that you can make sure the program avoids assigning
anyone the same chore they did last time. For another possible feature, schedule the program to run once a week
automatically.
"""

import ezgmail
import random
import shelve
from pathlib import Path


chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
emails = ['legowaj684@mailvk.net', 'name@email.com', 'name2@email.com', 'name3@email.com']

chore_history = Path('oldchores.dat')

# Read in previous chore assignments from shelf file
shelf_file = shelve.open('oldchores')
chore_dict = shelf_file['chore_dict']

# Assume each person must have a different chore
# Each person must not repeat last chore assignment
new_chore_dict = {}
tmp_set = set()
for email in emails:
    selection_pool = set(chores)
    selection_pool.remove(chore_dict[email])                # exclude previous chore assignment
    selection_pool.difference_update(tmp_set)               # exclude chores already assigned
    random_chore = random.choice(list(selection_pool))
    tmp_set.add(random_chore)                               # chores already assigned
    new_chore_dict[email] = random_chore                    # dictionary of current chore assignments

    print(f'Emailing: {email}, with chore: {random_chore}')
    ezgmail.send(email, 'Re: Chores', f'Your chore for today is: {random_chore}')

# Write current chore assignments to shelf file
shelf_file['chore_dict'] = new_chore_dict
shelf_file.close()

# Program scheduled to run weekly using Windows Task Scheduler
