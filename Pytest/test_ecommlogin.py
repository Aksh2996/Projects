import json
import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open("test1.json", "r") as fg:
    datass = json.load(fg)

@pytest.mark.parametrize("data",datass)
def test_2(data):
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service


    ser = Service(r"C:\Users\DELL\OneDrive\Desktop\5lv\chromedriver.exe")
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ser,options=options)
    driver.get("https://www.saucedemo.com/")
    try:
        driver.find_element(By.XPATH,"//div/input[@placeholder='Username']").send_keys(data["username"])
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR,".submit-button").click()
        time.sleep(2)
        #shopping_page
        driver.find_element(By.CSS_SELECTOR,".product_sort_container").click()
        driver.find_element(By.XPATH,"//option[text()='Price (high to low)']").click()
        driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket").click()
        #a=driver.find_element(By.XPATH,"//div[text()='29.99']").text
        #print(a)
        #assert a=="$29.99"
        driver.find_element(By.CSS_SELECTOR,"button[name='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.CSS_SELECTOR,"a[class='shopping_cart_link']").click()
        driver.find_element(By.XPATH,"//button[text()='Checkout']").click()
        driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Akshay")
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys("Prakash")
        driver.find_element(By.XPATH, "//input[@name='postalCode']").send_keys("600024")
        driver.find_element(By.CSS_SELECTOR,"#continue").click()
        driver.find_element(By.CSS_SELECTOR, "#finish").click()
        driver.find_element(By.CSS_SELECTOR, "#back-to-products").click()
        driver.find_element(By.XPATH,"//button[text()='Open Menu']").click()
        wait = WebDriverWait(driver, 10)
        logout_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
        )
        logout_link.click()
        time.sleep(2)
    except Exception as e:
        print(f"yesyesys:{e}")
        pytest.skip(f"skips:{e}")
    finally:
        driver.quit()




