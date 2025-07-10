import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

@pytest.fixture
def driver():
    # Set up Firefox options
    options = FirefoxOptions()

    # Specify Firefox binary location (ensure this path is correct)
    firefox_binary_path = "/usr/bin/firefox"  # Verify the path is correct using `which firefox`
    options.binary_location = firefox_binary_path

    # Specify the path to geckodriver manually if needed
    geckodriver_path = "/snap/bin/geckodriver"  # Ensure this is the correct path
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()

def test_cross_browser(driver):
    # Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The FIREFOX web browser is opened successfully.")

    # Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    time.sleep(3)
    print("The website's homepage loads successfully.")

    # Step 1: Finding the sign-in button
    sign_in_button = driver.find_element(By.ID, "Sign In")
    sign_in_button.click()
    time.sleep(3)
    print("The Sign In page is displayed with fields for username and password.")

    # Step 2: Logging in
    # for username
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']"))).click()
    print("Clicked 'Select Username' dropdown.")
    time.sleep(1)
    username_text = "demouser"
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{username_text}']"))).click()
    print(f"Selected username: {username_text}")
    time.sleep(1)

    # for password section
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']"))).click()
    print("Clicked 'Select Password' dropdown.")
    time.sleep(1)
    password_text = "testingisfun99"
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{password_text}']"))).click()
    print(f"Selected password: {password_text}")
    time.sleep(1)

    # for the login button
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    print("Clicked 'Log In' button.")
    time.sleep(3)

    # Step 3: Finding the "log-out button and clicking"
    log_out_button = driver.find_element(By.ID, "logout")
    print("Found the 'log-out' button")
    log_out_button.click()
    print("The log-out button is clicked and User checked out")
    time.sleep(3)
