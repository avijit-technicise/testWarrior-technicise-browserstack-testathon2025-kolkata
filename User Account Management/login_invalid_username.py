from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
sleep(2)
print("The website's homepage loads successfully.")

# Click the Sign In button
sign_in_button = driver.find_element(By.ID, "Sign In")
sign_in_button.click()
sleep(2)
print("The Sign In page is displayed with fields for username and password.")

# ===================== Invalid Username =====================

# Clicking the username section and writing an username
username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
username_dropdown.click()  
sleep(1)  

username_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-2-input']")))
username_input.send_keys("random_username")
username_input.send_keys(Keys.ENTER)
print(f"Enterted username: {username_input}")
sleep(1)

# ===================== Valid Password =====================

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
wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
print("Clicked 'Log In' button.")
sleep(3)

# ===================== Checking for the Invalid Username warning =====================

try:
    # Wait for the error message to be visible
    error_message = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "api-error")))  
    print("Error: Invalid Username message is displayed.")
except:
    print("No 'Invalid Username' message found.")


driver.quit()