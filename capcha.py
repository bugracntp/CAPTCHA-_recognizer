from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

import pytesseract

import time


browser = webdriver.Chrome("chromedriver.exe")


browser.get("https://uyg.sgk.gov.tr/vizite/welcome.do")
text_box = browser.find_element(By.XPATH,"/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[4]/td[3]/input")
picture=browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[5]/td[3]/img')
with open('key.png','wb') as file:
    file.write(picture.screenshot_as_png)
# Adding custom options
text = pytesseract.image_to_string(Image.open('key.png'))
print(text)
time.sleep(2)
text_box.send_keys(text)

time.sleep(2)
browser.close()