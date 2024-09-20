from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = Options()
options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # Update this path if necessary

service = Service(executable_path="geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.youtube.com/")
WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)

input_element = driver.find_element(By.NAME, "search_query")
input_element.clear()
action = ActionChains(driver)
action.click(on_element=input_element)
action.perform()
input_element.send_keys("markiplier" + Keys.ENTER)

time.sleep(2)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "CLICKOLDING")
link.click()

time.sleep(7)
skipadd = driver.find_element(By.ID, "skip-button:3")
skipadd.click()


while True:
    choice = random.randint(1, 10)
    time.sleep(10)
    link = driver.find_element(By.ID and By.PARTIAL_LINK_TEXT, "thumbnail" and str(choice))
    link.click()
    time.sleep(10)
    choice = random.randint(1, 10)
    link2 = driver.find_element(By.ID and By.PARTIAL_LINK_TEXT, "thumbnail" and str(choice))
    if link2 == link:
        choice = random.randint(1, 10)
        link = driver.find_element(By.ID and By.PARTIAL_LINK_TEXT, "thumbnail" and str(choice))
        link.click()
    else:
        link2.click()




driver.quit()
