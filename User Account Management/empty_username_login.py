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



# Click the Sign In button
sign_in_button = driver.find_element(By.ID, "Sign In")
sign_in_button.click()
sleep(3)
print("The Sign In page is displayed with fields for username and password.")


# for username
username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
username_dropdown.click()
print("Clicked 'Select Username' dropdown.")
sleep(1)
username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
username_dropdown.click()
print("Clicked 'Select Username' dropdown again.")
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


# ===================== Checking for the Empty Username warning =====================

try:
    # Wait for any error message to become visible
    error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "api-error")))  
    
    # If any error message appears, check if it matches the "Empty Password" message
    if "Empty Username" in error_message.text:
        print("Error: 'Empty Username' warning message is displayed.")
    else:
        print(f"Error: Unexpected message found: {error_message.text}")
        
except:
    print("Error: No error message found at all.")


# Close the driver after testing
driver.quit()