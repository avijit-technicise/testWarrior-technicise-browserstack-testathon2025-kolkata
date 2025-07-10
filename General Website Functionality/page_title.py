from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait

# Enable logging in ChromeOptions
from selenium.webdriver.chrome.options import Options


# Configure Chrome options to disable logging
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Initialize the WebDriver
print("Automation testing starts")
driver = webdriver.Chrome(options=options)

# Create an explicit wait object
wait = WebDriverWait(driver, 20)
print("The web browser is opened successfully.")


# Initialize WebDriver
driver.get("https://kolkata.bugbash.live/")  

print("Title:", driver.title)

try:
    assert "StackDemo" in driver.title
except AssertionError:
    print("Title mismatch!")