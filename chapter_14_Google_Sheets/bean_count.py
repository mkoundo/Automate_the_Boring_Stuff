#! python3
# bean_count.py
# Author: Michael Koundouros
"""
https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit#gid=289119951
The columns of the first sheet in this spreadsheet are “Beans per Jar,” “Jars,” and “Total Beans.” The “Total
Beans” column is the product of the numbers in the “Beans per Jar” and “Jars” columns. However, there is a mistake in
one of the 15,000 rows in this sheet. That’s too many rows to check by hand. Luckily, you can write a script that
checks the totals.

As a hint, you can access the individual cells in a row with ss[0].getRow(rowNum), where ss is the Spreadsheet object
and rowNum is the row number. Remember that row numbers in Google Sheets begin at 1, not 0. The cell values will be
strings, so you’ll need to convert them to integers so your program can work with them. The expression int(ss[
0].getRow(2)[0]) * int(ss[0].getRow(2)[1]) == int(ss[0].getRow(2)[2]) evaluates to True if the row has the correct
total. Put this code in a loop to identify which row in the sheet has the incorrect total.
"""


import ezsheets


ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]
all_cells = sheet.getRows()

for index, row in enumerate(all_cells):
    beans, jars, totals, *_ = row                             # Unpack first three columns into variables.
    try:                                                      # Use try/except to ignore heading row & blank rows.
        if int(beans) * int(jars) != int(totals):
            print(f'Duff row at {index+1}')
    except ValueError:
        pass

print('Done!')
