#! python3
# form_data.py
# Author: Michael Koundouros
"""
Google Forms allows you to create simple online forms that make it easy to collect information from people. The
information they enter into the form is stored in a Google Sheet. For this project, write a program that can
automatically download the form information that users have submitted. Go to https://docs.google.com/forms/ and
start a new form; it will be blank. Add fields to the form that ask the user for a name and email address. Then
click the Send button in the upper right to get a link to your new form, such as
https://goo.gl/forms/QZsq5sC2Qe4fYO592/. Try to enter a few example responses into this form.

On the “Responses” tab of your form, click the green Create Spreadsheet button to create a Google Sheets spreadsheet
that will hold the responses that users submit. You should see your example responses in the first rows of this
spreadsheet. Then write a Python script using EZSheets to collect a list of the email addresses on this spreadsheet.
"""


import ezsheets


ss = ezsheets.Spreadsheet('1u4r2ErwZK61uF5K20fg5MPf6uhd7sHndaCQjKTba8PM')

first_sheet = ss[0]
print(first_sheet.title)

emails = first_sheet.getColumn(2)

for email in emails:
    if email != '':
        print(email)
