#! python3
# brute_force.py
# Author: Michael Koundouros
"""
Say you have an encrypted PDF that you have forgotten the password to, but you remember it was a single English
word. Trying to guess your forgotten password is quite a boring task. Instead you can write a program that will
decrypt the PDF by trying every possible English word until it finds one that works. This is called a brute-force
password attack. Download the text file dictionary.txt This dictionary file contains over 44,000 English words with
one word per line.

Using the file-reading skills you learned in Chapter 9, create a list of word strings by reading this file. Then loop
over each word in this list, passing it to the decrypt() method. If this method returns the integer 0, the password was
wrong and your program should continue to the next password. If decrypt() returns 1, then your program should break out
of the loop and print the hacked password. You should try both the uppercase and lowercase form of each word.
usage: python brute_force.py dictionary file
where dictionary is a text file, with one word per line
and file is an encrypted pdf
"""


import sys
import PyPDF2
from pathlib import Path


def brute_force(dictionary, file):
    with open(dictionary, 'r') as dict_file:
        wordlist = dict_file.read().splitlines()

    print('Dictionary read in...')
    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))

    for word in wordlist:
        if pdf_reader.decrypt(word):
            return print(f'Password is: {word}')
        elif pdf_reader.decrypt(word.lower()):
            return print(f'Password is: {word.lower()}')

    return print(f'Password not found.')


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 2:
        print('usage: python brute_force.py dictionary file')
        sys.exit(1)

    brute_force(Path(args[0]), Path(args[1]))
    print('Done!')


if __name__ == '__main__':
    main()
