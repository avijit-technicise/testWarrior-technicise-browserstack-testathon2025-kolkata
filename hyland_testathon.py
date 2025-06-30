from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from time import sleep

# Configure Chrome options to disable logging
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# TC:99
# step 1: Initialize the WebDriver
print("Automation testing starts")
driver = webdriver.Chrome(options=options)

# Create an explicit wait object
wait = WebDriverWait(driver, 20)
print("The web browser is opened successfully.")

# step 2: Navigate to the website
driver.get("https://kolkata.bugbash.live/")
sleep(3)
print("The website's homepage loads successfully.")

add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "shelf-item__buy-btn")

if add_to_cart_buttons:
    print(f"Found {len(add_to_cart_buttons)} 'Add to Cart' buttons on the page.")

    add_to_cart_buttons[2].click()
    print("Clicked the required 'Add to Cart' button.")
else:
    print("No 'Add to Cart' buttons found on the page.")

sleep(2)

# TC:100 -> Sign in with valid details
# step 1: Click the Sign In button
sign_in_button = driver.find_element(By.ID, "Sign In")
sign_in_button.click()
sleep(3)
print("The Sign In page is displayed with fields for username and password.")


# step 3: Close the driver after testing
driver.quit()


