#! python3
# clipboard_text.py
# Author: Michael Koundouros
"""
Write a program that copies the text from a window’s text fields. Use pyautogui.getWindowsWithTitle('Notepad')
(or whichever text editor you choose) to obtain a Window object. The top and left attributes of this Window object can
tell you where this window is, while the activate() method will ensure it is at the front of the screen. You can then
click the main text field of the text editor by adding, say, 100 or 200 pixels to the top and left attribute values
with pyautogui.click() to put the keyboard focus there. Call pyautogui.hotkey('ctrl', 'a') and
pyautogui.hotkey('ctrl', 'c') to select all the text and copy it to the clipboard.

Finally, call pyperclip.paste() to retrieve the text from the clipboard and paste it into your Python program. From
there, you can use this string however you want, but just pass it to print() for now.
"""


import pyautogui
import pyperclip

# Get window object with specified title
window_list = pyautogui.getWindowsWithTitle('Notepad')

for window in window_list:
    # Activate editor window
    print(window.title)
    window.restore()
    window.activate()
    corner = window.topleft
    pyautogui.click(corner.x+200, corner.y+200)

    # Select all text and copy
    pyautogui.hotkey('ctrl', 'a')                           # select all text
    pyautogui.hotkey('ctrl', 'c', interval=0.25)            # copy selected text

    text_retrieved = pyperclip.paste()
    print(text_retrieved)
