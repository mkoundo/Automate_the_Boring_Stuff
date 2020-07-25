#! python3
# fill_gaps.py
# Author: Michael Koundouros
"""
Ref: Chapter 10 - Organising Files
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019

Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single
folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

Usage: python fill_gaps.py {--fill | --insert} file

Options:
--fill - files are renamed to remove any gaps in numbering
--insert - files are renamed to create a gap for a new file
At least one option must be specified.
When used with option --fill, file is any file in the sequence to be filled e.g. spam003.txt
When used with option --insert, file is the name of the file to be inserted.
"""


import sys
import re
import shutil
from pathlib import Path


def fill_gaps(file):
    # Function renames files to file001.txt, file002.txt, file003.txt ... removing any gaps.
    file_name, files, _ = get_files(file)
    counter = 1
    files_renamed = 0
    for file_item in files:
        testfile = f'{file_name}{counter:03}{file.suffix}'
        if testfile != file_item.name:
            newfile = file_item.parent / testfile
            shutil.move(file_item, newfile)
            print(newfile)
            files_renamed += 1
        counter += 1
    print(f'{files_renamed} files renamed.')
    return


def insert_gap(file):
    # Function inserts gap into sequence file001.txt, file002.txt, file003.txt ... as per given file argument.
    # e.g: given file003.txt the files will be renamed to  file001.txt, file002.txt, file004.txt, file005.txt ...
    file_name, files, file_digits = get_files(file)
    files_renamed = 0
    for file_num in range(len(files), int(file_digits) - 1, -1):
        newfile = file.parent / f'{file_name}{file_num+1:03}{file.suffix}'
        oldfile = file.parent / f'{file_name}{file_num:03}{file.suffix}'
        shutil.move(oldfile, newfile)
        print(newfile)
        files_renamed += 1
    print(f'{files_renamed} files renamed.')


# ========================================UTILITIES ===============================================================
def get_files(file):
    # Extract filename without last 3 digits  eg file001 -> file. Filename can contain any alphanumeric characters.
    # Assume file suffix is always 3 digits 001, 002 , 003 ...
    # Function returns the extracted filename, last 3 digits and a list of all files inc. path
    match_name = re.search(r'(\w+)(?=[\d]{3}$)', file.stem)
    ''' (\w+)    matches any alphanumeric character as long as the lookahead is satisfied
        (?=...)  positive lookahead: (\w+) must be followed by the following:
        [\d]{3}$ last 3 charctaers of the string must be digits.
    '''
    match_digits = re.search(r'[\d]{3}$', file.stem)
    file_name = match_name.group()
    file_digits = match_digits.group()
    files = list(file.parent.glob(f'{file_name}???{file.suffix}'))
    return file_name, files, file_digits
# ================================================================================================================


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) < 2:
        print('usage: python fill_gaps.py {--fill | --insert} file')
        sys.exit(1)
    elif not Path.is_file(Path(args[1])):
        print('File not found!')
        sys.exit(1)
    else:
        option = args[0]
        file = Path(args[1])

    if option == '--fill':
        fill_gaps(file)
    elif option == '--insert':
        insert_gap(file)
    else:
        print('Options are --fill or --insert')
        sys.exit(1)


if __name__ == '__main__':
    main()
