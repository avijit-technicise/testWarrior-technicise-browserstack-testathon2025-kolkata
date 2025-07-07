import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from time import sleep

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_incorrect_details(driver):

    # step 1: Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # step 2: Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")

    # Sign in 
    # Locate the button by its ID attribute
    sign_in_button = driver.find_element(By.ID, "Sign In")
    sign_in_button.click()
    sleep(3)
    print("The Sign In page is displayed with fields for username and password.")

    username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
    username_dropdown.click()
    print("Clicked 'Select Username' dropdown.")
    sleep(3)

    # --- NEW CODE TO TYPE SOMETHING AND PRESS ENTER ---

    # IMPORTANT: You need to inspect the HTML after clicking the "Select Username" dropdown.
    # Look for the input field that appears. It might be:
    # - an <input> tag with a specific ID, name, or class.
    # - a <div> or <span contenteditable="true"> element.

    # Here are some common examples for locating the input field.
    # You will need to uncomment and adjust one based on your website's HTML.

    # Example 1: If the input field has a unique ID (very common for search/filter inputs)
    # search_input_field = wait.until(EC.presence_of_element_located((By.ID, "react-select-2-input"))) # Example ID for a React Select search input
    # print("Found search input field by ID.")

    # Example 2: If the input field has a specific role or placeholder text
    # search_input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@role='combobox' and @aria-autocomplete='list']")))
    # print("Found search input field by XPATH (role combobox).")
    
    # Example 3: If it's an input inside a specific parent structure
    # You might need to be more specific based on the dropdown library used (e.g., react-select, select2)
    # This XPath tries to find an input element that is typically used for typing in a dropdown.
    # It specifically targets the input field that appears after clicking the dropdown.
    # search_input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
    # print("Found search input field by common CSS-based XPATH for a combobox input.")


    # Text you want to type
    text_to_type = "IncorrectUser" # Example: an incorrect username to test

    # Type the text into the input field
    username_dropdown.send_keys(text_to_type)
    print(f"Typed '{text_to_type}' into the input field.")

    # Press Enter
    username_dropdown.send_keys(Keys.ENTER)
    print("Pressed Enter after typing.")

    sleep(3) # Give time for the action to process (e.g., selection or error message)

    # --- End of NEW CODE ---