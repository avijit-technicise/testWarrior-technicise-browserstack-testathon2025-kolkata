import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_invalid_username(driver):

    # step 1: Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # step 2: Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(2)
    print("The website's homepage loads successfully.")

    # Click the Sign In button
    sign_in_button = driver.find_element(By.ID, "Sign In")
    sign_in_button.click()
    sleep(2)
    print("The Sign In page is displayed with fields for username and password.")

    # ===================== Valid Username =====================

    # for username
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']"))).click()
    print("Clicked 'Select Username' dropdown.")
    sleep(1)
    username_text = "demouser" 
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{username_text}']"))).click()
    print(f"Selected username: {username_text}")
    sleep(1)

    # ===================== Empty Password =====================

    # Clicking the password section and writing an password
    password_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']")))
    password_dropdown.click()  
    sleep(1)  
    password_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']")))
    password_dropdown.click()  
    sleep(1) 
    print("No password is selected")

    # for the login button
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    print("Clicked 'Log In' button.")
    sleep(3)

    # ===================== Checking for the Empty Password warning =====================

    try:
        # Wait for any error message to become visible
        error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "api-error")))  
        
        # If any error message appears, check if it matches the "Empty Password" message
        if "Empty Password" in error_message.text:
            print("Error: 'Empty Password' warning message is displayed.")
        else:
            print(f"Error: Unexpected message found: {error_message.text}")
            
    except:
        print("Error: No error message found at all.")

