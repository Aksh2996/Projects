import pytest
import json

from selenium.webdriver.support.select import Select


def load_data():
    with open("test.json","r") as file:
        return json.load(file)
@pytest.mark.parametrize("data",load_data())
def test_1(driver,data):
    import time
    from selenium.webdriver import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    driver.get("https://demoqa.com/automation-practice-form")
    driver.execute_script("""
        document.querySelectorAll("iframe[id^='google_ads_iframe'], .adsbygoogle").forEach(el => el.remove());
    """)
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//input[@class=' mr-sm-2 form-control'])[1]").send_keys(data["first_name"])
    driver.find_element(By.ID, "lastName").send_keys(data["last_name"])
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys(data["subject"])
    a = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".subjects-auto-complete__option")))
    driver.execute_script("arguments[0].click();", a)
    driver.find_element(By.XPATH, "(//input[@placeholder='name@example.com'])").send_keys(data["email"])
    driver.find_element(By.XPATH, f"(//label[text()='{data['gender']}'])").click()
    #added
    date_input = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
    driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
    date_input.click()
    year_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
    Select(year_dropdown).select_by_value(data["dob_year"])
    month_dropdown = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    Select(month_dropdown).select_by_value(data["dob_month"])
    day_picker = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day--0{int(data['dob_date']):02d}') "  # zero-padded day
            f"and not(contains(@class, 'react-datepicker__day--outside-month'))]"
        ))
    )
    day_picker.click()
    #added
    driver.find_element(By.CSS_SELECTOR, "#userNumber").send_keys(data["phone"])
    hobby_checkbox = driver.find_element(By.XPATH,f"(//label[text()='{data['hobby']}'])")
    driver.execute_script("arguments[0].click();", hobby_checkbox)
    driver.find_element(By.CSS_SELECTOR, "#uploadPicture").send_keys(data["photo_path"])
    driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys(data["address"])
    # Click or focus on the State input (this is the actual input field inside the dropdown)
    state_input = driver.find_element(By.ID, "react-select-3-input")
    state_input.send_keys(data["state"])  # Type the visible option
    state_input.send_keys(Keys.ENTER)  # Press Enter to select
    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys(data["city"])
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


