"""
Ref: Chapter 6 - Manipulating Strings
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized
table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For
example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""


def printTable(table):
    # determine max column widths from each list item
    max_width = []
    for eachlist in table:
        col_width = 0
        for item in eachlist:
            col_width = max(col_width, len(item))
        max_width.append(col_width)

    # transpose table and print formatted table items
    for col in range(len(table[0])):  # assume that all lists in table are of equal length
        for row in range(len(table)):
            print(table[row][col].rjust(max_width[row] + 1), end='')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
