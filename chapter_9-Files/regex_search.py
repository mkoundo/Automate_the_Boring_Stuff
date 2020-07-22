"""
Ref: Chapter 9 - Reading and Writing Files
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular
expression. The results should be printed to the screen.

Usage: python regex_search <directory> "<Regex>"
"""


import re
import sys
from pathlib import Path


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) < 2:
        print('usage: python mad_libs.py <directory> "<regex>"')
        sys.exit(1)
    elif not Path.exists(Path(args[0])):
        print('Directory does not exist')
        sys.exit(1)
    else:
        directory = Path(args[0])
        regex = args[1]

    filelist = list(directory.glob('*.txt'))

    for file in filelist:
        print('\n' + str(file))
        with open(str(file), 'r') as textfile:
            for linenumber, line in enumerate(textfile):
                match = re.search(regex, line)
                if match is not None: print(f'Line: {linenumber+1} found: {match.group()}')


if __name__ == '__main__':
    main()

"""
Some usage examples with output from text*.txt in directory ./text_files

example 1:
python regex_search.py ./text_files "\d+"

text_files\text1.txt

text_files\text2.txt
Line: 3 found: 1

text_files\text3.txt

example 2:
python regex_search.py ./text_files "([0-2][1-9]|[1-3][01])/(0[1-9]|1[0-2])/([12][0-9][0-9][0-9])"

text_files\text1.txt

text_files\text2.txt

text_files\text3.txt
Line: 3 found: 21/02/1998

"""