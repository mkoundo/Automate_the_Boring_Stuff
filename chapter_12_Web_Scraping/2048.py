#! python3
# 2048.py
# Author: Michael Koundouros
"""
2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. You
can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over
again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right,
down, and left keystrokes to automatically play the game.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

game_board = browser.find_element_by_css_selector('body')

for send_keys in range(120):
    game_board.send_keys(Keys.UP)
    game_board.send_keys(Keys.RIGHT)
    game_board.send_keys(Keys.DOWN)
    game_board.send_keys(Keys.LEFT)

