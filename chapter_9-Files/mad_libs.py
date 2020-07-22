"""
Ref: Chapter 9 - Reading and Writing Files
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE,
NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.
Usage: python mad_libs.py <filename>
"""

import sys
import re

def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    filename = sys.argv[1]

    if not filename:
        print('usage: python mad_libs.py <filename>')
        sys.exit(1)

    with open(filename, 'r') as alltext:
        inputtext = alltext.read()

    # Find searchwords in inputext and list them in the order of occurrence
    searchlist = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB', inputtext)

    # Find and replace searchwords
    for searchword in searchlist:
        inputtext = inputtext.replace(searchword, newword(searchword), 1)
        print(inputtext)

    with open('mad_libs_output.txt', 'w') as writetext:
        writetext.write(inputtext)


def newword(searchword):
    # Function to enter replacement word
    print(f'Enter a {searchword}')
    return input()


if __name__ == '__main__':
    main()
