# ! python3
# 2048 - automatically plays the 2048 game on https://gabrielecirulli.github.io/2048/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(3)

game = browser.find_element_by_tag_name('html')
while True:
    try:
        game.send_keys(Keys.UP)
        game.send_keys(Keys.RIGHT)
        game.send_keys(Keys.DOWN)
        game.send_keys(Keys.LEFT)
    except Exception:
        break
