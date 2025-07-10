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

def test_fav_user_login(driver):
    # step 1: Initialize the WebDriver
    print("Automation testing starts")

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
    username_text = "fav_user" 
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


    # ===================== Checking for the Locked User warning =====================

    try:
        # Wait for the "Favourites" button to become visible
        fav_button = wait.until(EC.visibility_of_element_located((By.ID, "favourites")))
        fav_button.click()
        print("The 'Favourites' button is found and clicked.")
        
    except Exception as e:
        print(f"Error: 'Favourites' button not found or could not be clicked. Details: {e}")

    sleep(3)


    # Locate all the products in the Favourites page
    fav_products = driver.find_elements(By.CLASS_NAME, "shelf-item")  

    if fav_products:
        print(f"Success: {len(fav_products)} product(s) found in Favourites.")
        for product in fav_products:
            try:
                product_title = product.find_element(By.CLASS_NAME, "shelf-item__title").text  
                print(f"Product found: {product_title}")
            except Exception as e:
                print(f"Error: Could not find the title for one of the products. Details: {e}") 
    else:
        print("No products found in the Favourites list.")


