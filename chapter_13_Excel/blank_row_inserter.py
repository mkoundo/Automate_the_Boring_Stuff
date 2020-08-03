#! python3
# blank_row_inserter.py
# Author: Michael Koundouros
"""
Create a program blank_row_inserter.py that takes two integers and a filename string as command line arguments.
Let’s call the first integer N and the second integer M. Starting at row N, the program should insert M blank rows
into the spreadsheet.
This solution takes advantage of the built-in insert_rows() method.
usage: python blank_row_inserter.py row blank_rows file
"""


import openpyxl
from pathlib import Path
import sys


def row_insert(n_row, m_blank_rows, file):
    # Function to insert blank rows in excel spreadsheet
    try:
        wb = openpyxl.load_workbook(file)
    except FileNotFoundError:
        print(f'{file} not found!')
        sys.exit(1)

    print(f'Inserting {m_blank_rows} rows at row {n_row}...')
    sheet = wb.active
    sheet.insert_rows(n_row, m_blank_rows)
    wb.save(file)

    return


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 3:
        print('usage: python blank_row_inserter.py row blank_rows file')
        sys.exit(1)
    else:
        filename = Path(args[2])
        try:
            n_integer = int(args[0])
            m_integer = int(args[1])
            openpyxl.load_workbook(filename)
        except ValueError:
            print('Invalid arguments given!')
            sys.exit(1)

    row_insert(n_integer, m_integer, filename)
    print('Done!')


if __name__ == '__main__':
    main()
