from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random as rn,time

browser = webdriver.Firefox()

print(type(browser))

browser.get('https://gabrielecirulli.github.io/2048/')

htmlelement = browser.find_element_by_tag_name('html')

count = 1

t = ['Up', 'Down', 'Left', 'Right']
bla = 0
st = "Keys.ARROW_LEFT"

def send_key(num):
    if num == 0:
        return htmlelement.send_keys(Keys.ARROW_UP)
    elif num == 1 :
        return htmlelement.send_keys(Keys.ARROW_RIGHT)
    elif num == 2:
        return htmlelement.send_keys(Keys.ARROW_LEFT)
    elif num == 3 :
        return htmlelement.send_keys(Keys.ARROW_DOWN)





while count == 1 :
    bla = rn.randint(0,3)# generates a random number
    gg = send_key(bla)
    time.sleep(0.40)  #makes a move every 0.4 seconds
