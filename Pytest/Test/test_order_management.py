import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@pytest.fixture(scope="module")
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("The web browser is opened successfully.")
    yield driver
    driver.quit()

print("Automation testing starts")

@pytest.mark.order(1)
def sign_in (driver):

    # Create an explicit wait object
    # wait = WebDriverWait(driver, 20)
    
    # Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")