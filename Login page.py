import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrom=Options()
chrom.add_argument("--incognito")
pat=Service(r"C:\Users\DELL\OneDrive\Desktop\5lv\chromedriver.exe")
driver=webdriver.Chrome(service=pat,options=chrom)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("tomsmith")
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR,".fa").click()
driver.find_element(By.CLASS_NAME,"icon-2x").click()
time.sleep(3)


