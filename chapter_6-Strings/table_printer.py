"""
Ref: Chapter 6 - Manipulating Strings
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        michael.koundouros@outlook.com
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
    # determine max column widths
    max_width = []
    for eachlist in table:
        col_width = 0
        list_length = len(eachlist)  # to be used in transpose table
        for item in eachlist:
            col_width = max(col_width, len(item))
        max_width.append(col_width)

    # transpose table
    transpose_table = []
    for listindex in range(list_length):
        item_list = []
        for tableindex, eachlist in enumerate(table):
            item_list.append(table[tableindex][listindex])
        transpose_table.append(item_list)

    # print out formatted transpose table
    for eachlist in transpose_table:
        for index, item in enumerate(eachlist):
            print(item.rjust(max_width[index] + 1), end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
