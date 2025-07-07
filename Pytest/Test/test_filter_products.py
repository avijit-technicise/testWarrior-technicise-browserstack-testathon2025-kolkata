import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from time import sleep

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_product_filter(driver):

    # step 1: Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # step 2: Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")


    # --- Filter "Samsung" Products ---
    print("Filtering by the 'Samsung' vendor type")
    try:
        samsung_filter_span = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Samsung']/following-sibling::span[@class='checkmark' and text()='Samsung']")))
        samsung_filter_span.click()
        sleep(3) 
        print("Clicked on 'Samsung' filter.")
    except Exception as e:
        print(f"Could not click 'Samsung' filter. Error: {e}")

    # Unfiltering by clicking the same product tab again
    try:
        samsung_filter_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Samsung']/parent::label")))
        samsung_filter_label.click()
        sleep(3)
        print("Clicked on 'Samsung' filter again (this time, via label).")
    except Exception as e_label:
        print(f"Could not click 'Samsung' filter via label either. Error: {e_label}")



    # --- Filter "Apple" Products ---
    print("Filtering by the 'Apple' vendor type")
    try:
        apple_filter_span = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Apple']/following-sibling::span[@class='checkmark' and text()='Apple']")))
        apple_filter_span.click()
        sleep(3) 
        print("Clicked on 'Apple' filter.")
    except Exception as e:
        print(f"Could not click 'Apple' filter. Error: {e}")

    # Unfiltering by clicking the same product tab again
    try:
        apple_filter_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Apple']/parent::label")))
        apple_filter_label.click()
        sleep(3)
        print("Clicked on 'Apple' filter again (this time, via label).")
    except Exception as e_label:
        print(f"Could not click 'Apple' filter via label either. Error: {e_label}")



    # --- Filter "Google" Products ---
    print("Filtering by the 'Google' vendor type")
    try:
        google_filter_span = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Google']/following-sibling::span[@class='checkmark' and text()='Google']")))
        google_filter_span.click()
        sleep(3) 
        print("Clicked on 'Google' filter.")
    except Exception as e:
        print(f"Could not click 'Google' filter. Error: {e}")

    # Unfiltering by clicking the same product tab again
    try:
        google_filter_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Google']/parent::label")))
        google_filter_label.click()
        sleep(3)
        print("Clicked on 'Google' filter again (this time, via label).")
    except Exception as e_label:
        print(f"Could not click 'Google' filter via label either. Error: {e_label}")


    # --- Filter "OnePlus" Products ---
    print("Filtering by the 'OnePlus' vendor type")
    try:
        oneplus_filter_span = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='OnePlus']/following-sibling::span[@class='checkmark' and text()='OnePlus']")))
        oneplus_filter_span.click()
        sleep(3) 
        print("Clicked on 'OnePlus' filter.")
    except Exception as e:
        print(f"Could not click 'OnePlus' filter. Error: {e}")

    # Unfiltering by clicking the same product tab again
    try:
        oneplus_filter_label = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='OnePlus']/parent::label")))
        oneplus_filter_label.click()
        sleep(3)
        print("Clicked on 'OnePlus' filter again (this time, via label).")
    except Exception as e_label:
        print(f"Could not click 'OnePlus' filter via label either. Error: {e_label}")
