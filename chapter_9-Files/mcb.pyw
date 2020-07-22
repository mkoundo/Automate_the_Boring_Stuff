"""
Ref: Chapter 9 - Reading and Writing Files
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Let’s rewrite the “multi-clipboard” program from Chapter 6 so that it uses the shelve module. The user will now be able
to save new strings to load to the clipboard without having to modify the source code. We’ll name this new
program mcb.pyw (since “mcb” is shorter to type than “multi-clipboard”). The .pyw extension means that Python won’t
show a Terminal window when it runs this program.

The program will save each piece of clipboard text under a keyword. For example, when you run
python mcb.pyw --save spam, the current contents of the clipboard will be saved with the keyword spam. This text can
later be loaded to the clipboard again by running py mcb.pyw spam. If the user forgets what keywords they have, they
can run python mcb.pyw --list to copy a list of all keywords to the clipboard.

Here’s what the program does:

The command line argument for the keyword is checked.
If the argument is --save, then the clipboard contents are saved to the keyword.
If the argument is --list, then all the keywords are copied to the clipboard.
Otherwise, the text for the keyword is copied to the clipboard.
This means the code will need to do the following:

Read the command line arguments from sys.argv.
Read and write to the clipboard.
Save and load to a shelf file.

Usage: python mcb.pyw --save <keyword> - Saves clipboard to shelf file with keyword.
       python mcb.pyw <keyword> - Loads keyword from shelf to clipboard.
       python mcb.pyw --list - Loads all keywords from shelf to clipboard.
       python mcb.pyw --delete <keyword> - deletes keyword from shelf.
       python mcb.pyw --delete - deletes all keywords from shelf.
"""

import sys
import shelve
import pyperclip


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    keywordgiven = True if len(args) > 1 else False

    if not args:
        print('usage: python mcb.pyw [--save | --list | --delete] [keyword]')
        sys.exit(1)

    keyword = sys.argv[-1]
    with shelve.open('mcb') as mcbShelf:
        if args[0] == '--save':
            mcbShelf[keyword] = pyperclip.paste()
        elif args[0] == '--list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif args[0] == '--delete':
            mcbShelf.pop(keyword, '') if keywordgiven else mcbShelf.clear()
        else:
            pyperclip.copy(mcbShelf.get(keyword, ''))


if __name__ == '__main__':
    main()
