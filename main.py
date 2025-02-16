from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random

# options = Options()

url = "https://docs.google.com/forms/d/e/1FAIpQLSc8fbNlSy8Ov2fDka0fAJZzPpUGkEVH1C5FrCZ1jVUcuouGKg/viewform"

browser = webdriver.Firefox()
browser.get(url)

sleep(3)


lst = browser.find_elements(By.CLASS_NAME, "AB7Lab.Id5V1")
textarea_elements = browser.find_elements(By.XPATH, "//*[@data-initial-dir='auto']")
dct_elements = {'first block' : lst[0:3], 'second block' : lst[3:8], 'third block' : lst[8:12], 'fourth block' : lst[12:14], 'fifth block' : lst[14:22], 'sixth block' : lst[22:]}

print(textarea_elements)

def random_func_radiobuttons():
    for i in dct_elements.keys():
        lst_from_dict = dct_elements[i]
        random.choice(lst_from_dict).click()
        sleep(1)

def random_func_text_areas():
    for j in textarea_elements:
        j.send_keys("96")

random_func_radiobuttons()
random_func_text_areas()


sleep(10)
browser.close()

