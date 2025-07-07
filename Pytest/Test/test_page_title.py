import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Enable logging in ChromeOptions
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_page_title (driver):
    # Initialize WebDriver
    driver.get("https://kolkata.bugbash.live/")  

    print("Title:", driver.title)

    try:
        assert "StackDemo" in driver.title
    except AssertionError:
        print("Title mismatch!")



