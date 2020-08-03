#! python3
# txt_2_xl.py
# Author: Michael Koundouros
"""
Write a program to read in the contents of several text files (you can make the text files yourself) and insert
those contents into a spreadsheet, with one line of text per row. The lines of the first text file will be in the
cells of column A, the lines of the second text file will be in the cells of column B, and so on.

Use the readlines() File object method to return a list of strings, one string per line in the file. For the first
file, output the first line to column 1, row 1. The second line should be written to column 1, row 2, and so on. The
next file that is read with readlines() will be written to column 2, the next file to column 3, and so on.
usage: python txt_2_xl.py file1 file2 file3 ...
where filen are text files
"""

import openpyxl
from pathlib import Path
import sys


def import_txt(files):
    # Function to import text files into excel. Each file is written to a column.
    new_wb = openpyxl.Workbook()
    new_sheet = new_wb.active

    for cols, file in enumerate(files):
        with open(Path(file), 'r') as tmpfile:
            textlines = tmpfile.read().splitlines()                     # Read each line into a list without newline \n
            print(f'Importing file {file}...')
            for rows, textline in enumerate(textlines):
                new_sheet.cell(row=rows+1, column=cols+1).value = textline

    new_wb.save('imported_text.xlsx')
    return


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) < 1:
        print('usage: python txt_2_xl.py file1 file2 file3 ...')
        sys.exit(1)

    # Check that files exist
    for file in args:
        if not Path(file).is_file():
            print(f'{file} not found!')
            sys.exit(1)

    import_txt(args)
    print('Done!')


if __name__ == '__main__':
    main()
