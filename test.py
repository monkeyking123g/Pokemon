from turtle import Turtle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" # google driver
driver = webdriver.Chrome(PATH)

driver.get("https://scrapeme.live/shop/")  # sito per lavoro

def title():
    # ritorna True se title == 'ScrapeMe' else false
    if driver.title == "ScrapeMe":
        return True
    else:
        return False

print(f'Control title: {title()}')
# se vero passa a search e cerchiamo qualsiasi pokemon   
try:
    search = driver.find_element_by_name('s')
    search.send_keys('Metapod')
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.quit()
    
except:
    driver.quit()

