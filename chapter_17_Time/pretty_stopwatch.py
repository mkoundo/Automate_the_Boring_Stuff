#! python3
# pretty_stopwatch.py
# Author: Michael Koundouros
"""
A stopwatch program that:
1. Tracks the amount of time elapsed between presses of the ENTER key, with each key press starting a new “lap”
   on the timer.
2. Prints the lap number, total time, and lap time.
"""


import time
import pyperclip


# Display the program's instructions.
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()                                                     # press Enter to begin
print('Started.')
startTime = time.time()                                     # get the first lap's start time
lastTime = startTime
lapNum = 1

clipboard = []
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        output_str = f'Lap #{lapNum:2}: {totalTime:5} ({lapTime:5})'
        print(output_str, end='')
        clipboard.append(output_str)
        lapNum += 1
        lastTime = time.time()                              # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    pyperclip.copy('\n'.join(clipboard))
