import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_2():
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    ser = Service(r"C:\Users\DELL\OneDrive\Desktop\5lv\chromedriver.exe")
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ser,options=options)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH,"//div/input[@placeholder='Username']").send_keys("standard_user")
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR,".submit-button").click()
    time.sleep(2)
    #shopping_page
    driver.find_element(By.CSS_SELECTOR,".product_sort_container").click()
    driver.find_element(By.XPATH,"//option[text()='Price (high to low)']").click()
    driver.find_element(By.CSS_SELECTOR,"#add-to-cart-sauce-labs-fleece-jacket").click()
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




