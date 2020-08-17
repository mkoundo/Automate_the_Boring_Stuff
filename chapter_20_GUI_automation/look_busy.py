#! python3
# look_busy.py
# Author: Michael Koundouros
"""
Write a script to nudge your mouse cursor slightly every 10 seconds. The nudge should be small and infrequent
enough so that it won’t get in the way if you do happen to need to use your computer while the script is running.
"""


import pyautogui
import time

i = 1
while True:
    x_offset = i * 5
    pyautogui.move(x_offset, 0)
    i = -1 * i
    time.sleep(10)
