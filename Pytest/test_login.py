import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/automation-practice-form")
driver.execute_script("""
    document.querySelectorAll("iframe[id^='google_ads_iframe'], .adsbygoogle").forEach(el => el.remove());
""")
driver.maximize_window()
driver.find_element(By.XPATH,"(//input[@class=' mr-sm-2 form-control'])[1]").send_keys("Akshay")
driver.find_element(By.ID,"lastName").send_keys("Prakash")
wait = WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR,"#subjectsInput").send_keys("maths")
a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".subjects-auto-complete__option")))
driver.execute_script("arguments[0].click();", a)
driver.find_element(By.XPATH,"(//input[@placeholder='name@example.com'])").send_keys("aprakash270@gmail.com")
driver.find_element(By.XPATH,"(//label[@for='gender-radio-1'])").click()
driver.find_element(By.CSS_SELECTOR,"#userNumber").send_keys("8072693473")

# Open the date picker input
date_input = driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput")
driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
driver.execute_script("arguments[0].click();", date_input)  # JS click avoids interception

# Wait for the date picker popup to be visible and clickable
b = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Choose Tuesday, July 1st, 2025']")))

# Scroll to and click the date
driver.execute_script("arguments[0].scrollIntoView(true);", b)
driver.execute_script("arguments[0].click();", b)
hobby_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
driver.execute_script("arguments[0].click();", hobby_checkbox)
p=r"C:\Users\DELL\OneDrive\Documents\Pictures\PHOTO_FOR_ID_CARD.jpg"
driver.find_element(By.CSS_SELECTOR,"#uploadPicture").send_keys(p)
driver.find_element(By.CSS_SELECTOR,"#currentAddress").send_keys("address")
# Click or focus on the State input (this is the actual input field inside the dropdown)
state_input = driver.find_element(By.ID, "react-select-3-input")
state_input.send_keys("NCR")   # Type the visible option
state_input.send_keys(Keys.ENTER)  # Press Enter to select
city_input = driver.find_element(By.ID, "react-select-4-input")
city_input.send_keys("Delhi")
city_input.send_keys(Keys.ENTER)
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
time.sleep(1)  # Optional, helps layout settle
submit_btn.click()
time.sleep(2)
close_button = driver.find_element(By.ID, "closeLargeModal")
driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
driver.execute_script("arguments[0].click();", close_button)
time.sleep(5)


