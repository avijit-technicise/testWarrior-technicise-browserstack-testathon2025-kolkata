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

# ==============================SIGN IN==============================

# Click the Sign In button
sign_in_button = driver.find_element(By.ID, "Sign In")
sign_in_button.click()
sleep(3)
print("The Sign In page is displayed with fields for username and password.")


# Login with valid details using dropdown
# for username
username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
username_dropdown.click()
print("Clicked 'Select Username' dropdown.")
sleep(1)
username_text = "demouser" 
username_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{username_text}']")))
username_option.click()
print(f"Selected username: {username_text}")
sleep(1)

# for password section
password_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']")))
password_dropdown.click()
print("Clicked 'Select Password' dropdown.")
sleep(1) 
password_text = "testingisfun99" 
password_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{password_text}']")))
password_option.click()
print(f"Selected password: {password_text}")
sleep(1)

# for the login button
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
login_button.click()
print("Clicked 'Log In' button.")
sleep(3)


# ==============================CART DISPLAY==============================

# cart button
cart_button = driver.find_element(By.CLASS_NAME, "bag__quantity")
cart_button.click()
sleep(1)
print("The cart is opened")

# ------------------------------------------------------------------------
# Locate the element containing the subtotal 
subtotal_element = driver.find_element(By.CLASS_NAME, "sub-price")
# Extract the text of the subtotal value
subtotal_text = subtotal_element.text.strip()

# Verify if the subtotal is $0.00
if subtotal_text == "$ 0.00":
    print("Subtotal is correctly $ 0.00")
else:
    print(f"Subtotal is incorrect. Found: {subtotal_text}")

#-------------------------------------------------------------------------
buy_button = driver.find_element(By.CLASS_NAME, "buy-btn")
buy_button_text = buy_button.text.strip()

if buy_button_text == "CONTINUE SHOPPING":
    print("The cart is empty: no 'checkout' button available")
else:
    print("Cart has items: Checkout button available")

#-------------------------------------------------------------------------



# step 3: Close the driver after testing
driver.quit()