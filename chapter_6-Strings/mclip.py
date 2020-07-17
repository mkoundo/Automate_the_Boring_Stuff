"""
Ref: Chapter 6 - Manipulating Strings
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        michael.koundouros@outlook.com
        July 2020

A program with a command line argument provides a short key phrase — for instance, agree or busy. The message
associated with that key phrase will be copied to the clipboard so that the user can paste it into an email. This way,
the user can have long, detailed messages without having to retype them.
"""

import sys
import pyperclip


TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [agree | busy | upsell] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
