# Automating the Boring Stuff with Python

By Al Sweigart. Free to read online [here](https://automatetheboringstuff.com/). ![Cover Image](cover.png)

 A collection of mini projects coded in Python3, found in Automating the Boring Stuff with Python.
 
 To install the additional packages required, run:
*pip install -r requirements.txt*
## Chapter 3 - Functions
[collatz.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_3-Functions/collatz.py) - Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return (3 * number) + 1.

## Chapter 4 - Lists
 [coin_flip.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_4-Lists/coin_flip.py) - For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T”. Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
 
[comma_code.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_4-Lists/comma_code.py) - Say you have a list value like this: spam = ['apples', 'bananas', 'tofu', 'cats'].
Write a function that takes a list value as an argument and returns a string with all the items
separated by a comma and a space, with and inserted before the last item. For example, passing
the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your
function should be able to work with any list value passed to it. Be sure to test the case where
an empty list [] is passed to your function.
## Chapter 5 - Dictionaries
[charactercount.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_5-Dictionaries/charactercount.py) - Here is a short program that counts the number of occurrences of each letter in a string.

[inventory.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_5-Dictionaries/inventory.py) - You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory() that would take any possible “inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62

[nested_dictionary.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_5-Dictionaries/nested_dictionary.py) - Here’s a program that uses a dictionary that contains other dictionaries of what items guests are bringing to a picnic. The totalBrought() function can read this data structure and calculate the total number of an item being brought by all the guests.

[chess_validator.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_5-Dictionaries/chess_validator.py) - In this chapter, we used the dictionary value
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn',
'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.
## Chapter 6 - Strings
[mclip.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_6-Strings/mclip.py) - A program with a command line argument provides a short key phrase — for instance, agree or busy. The message associated with that key phrase will be copied to the clipboard so that the user can paste it into an email. This way, the user can have long, detailed messages without having to retype them.

[table_printer.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_6-Strings/table_printer.py) - Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings.
## Chapter 7 - Regular Expressions
[date_detection.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_7-Regex/date_detection.py) - Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero. 

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

[regex_strip.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_7-Regex/regex_strip.py) - Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

[strong_password.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_7-Regex/strong_password.py) - Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

[strong_password_advanced.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_7-Regex/strong_password_advanced.py) - Similar to [strong_password.py](https://github.com/mkoundo/Automate_the_Boring_Stuff/blob/master/chapter_7-Regex/strong_password.py) except uses regex lookaheads.
