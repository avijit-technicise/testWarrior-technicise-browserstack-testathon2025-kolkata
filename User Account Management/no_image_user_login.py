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


# Login with valid details using dropdown
# for username
username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
username_dropdown.click()
print("Clicked 'Select Username' dropdown.")
sleep(1)
username_text = "image_not_loading_user" 
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

# Wait for the images or an element that indicates page is fully loaded
# Adjust the selector to an element that appears after login and image loading
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.shelf-item_thumb img")))

# Find all the image elements inside the 'shelf-item_thumb' div
images = driver.find_elements(By.CSS_SELECTOR, "div.shelf-item_thumb img")

# Iterate through each image
for index, img_element in enumerate(images):
    try:
        # Check if the image is displayed (i.e., visible on the page)
        if img_element.is_displayed():
            print(f"Image {index + 1} is present and visible.")
            
            # Optionally, check if the image is fully loaded
            is_image_loaded = driver.execute_script("""
                var img = arguments[0];
                return img.complete && img.naturalWidth !== 0;
            """, img_element)

            if is_image_loaded:
                print(f"Image {index + 1} is fully loaded.")
            else:
                print(f"Image {index + 1} is not fully loaded.")
        else:
            print(f"Image {index + 1} is present but not visible.")
    
    except Exception as e:
        print(f"Error for Image {index + 1}: {e}")


# Close the browser
driver.quit()