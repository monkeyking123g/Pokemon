

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" # google driver 
driver = webdriver.Chrome(PATH)

driver.get("https://scrapeme.live/shop/") # sito per lavoro

# Verifichiamo se vero  else quit()
try:
    # clicho su nav bar per passare alla pagina 3 
    driver.find_element_by_xpath("//nav/ul/li[3]/a").click()
    #sulla pagina tre cerco se esiste pokemon Clefairy
    n = driver.find_element_by_xpath("//ul/li/a/h2")

    def verific():
        if n.text == 'Clefairy': 
            return True
        else:
            return False    

    print(f'Verifica: {verific()}')

    time.sleep(5) # tempo prima di chiudersi

    driver.quit()
except:
    driver.quit()


    

