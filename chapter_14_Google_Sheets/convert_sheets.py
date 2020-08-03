#! python3
# convert_sheets.py
# Author: Michael Koundouros
"""
You can use Google Sheets to convert a spreadsheet file into other formats. Write a script that passes a submitted
file to upload(). Once the spreadsheet has uploaded to Google Sheets, download it using downloadAsExcel(),
downloadAsODS(), and other such functions to create a copy of the spreadsheet in these other formats.
usage: convert_sheets.py file
"""


import sys
import ezsheets
from pathlib import Path


def convert_xlsx(file):
    # Function converts excel spreadsheets to ods, csv, tsv & pdf formats
    # formats csv, tsv & pdf are applicable to the first sheet only.

    sheet = ezsheets.upload(str(file))

    sheet.downloadAsExcel(f'{file.stem}.xlsx')
    sheet.downloadAsODS(f'{file.stem}.ods')
    sheet.downloadAsCSV(f'{file.stem}.csv')
    sheet.downloadAsTSV(f'{file.stem}.tsv')
    sheet.downloadAsPDF(f'{file.stem}.pdf')

    return


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 1:
        print('usage: convert_sheets.py file')
        sys.exit(1)
    else:
        file = Path(args[0])

    print(f'Converting file {file}')
    convert_xlsx(file)
    print('Done!')


if __name__ == '__main__':
    main()
