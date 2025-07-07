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

def test_checkout(driver):

    # step 1: Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # step 2: Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")


    # Sign in 
    # Locate the button by its ID attribute
    sign_in_button = driver.find_element(By.ID, "Sign In")
    sign_in_button.click()
    sleep(3)
    print("The Sign In page is displayed with fields for username and password.")



    username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
    username_dropdown.click()
    print("Clicked 'Select Username' dropdown.")
    sleep(1)
    username_text = "demouser" 
    username_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{username_text}']")))
    username_option.click()
    print(f"Selected username: {username_text}")
    sleep(1)

    password_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']")))
    password_dropdown.click()
    print("Clicked 'Select Password' dropdown.")
    sleep(1) 
    password_text = "testingisfun99" 
    password_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{password_text}']")))
    password_option.click()
    print(f"Selected password: {password_text}")
    sleep(1)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
    login_button.click()
    print("Clicked 'Log In' button.")
    sleep(3)



    # Add to cart by specific product name
    products = driver.find_elements(By.CLASS_NAME, "shelf-item")
    product_found = False
    product_name_to_find = "Galaxy S20"
    for product in products:
        # Check if the product name matches
        if product_name_to_find in product.text:
            try:
                # Find the "Add to Cart" button within that product element
                add_to_cart_button = product.find_element(By.CLASS_NAME, "shelf-item__buy-btn")
                add_to_cart_button.click()
                print(f"Clicked 'Add to Cart' for product: {product_name_to_find}")
                product_found = True
                break
            except Exception as e:
                print(f"Found product '{product_name_to_find}' but couldn't click the button. Error: {e}")
                break

    if not product_found:
        print(f"Product '{product_name_to_find}' not found on the page.")

    sleep(3)

    # ========================================= MAIN SECTION =========================================
    #-----------------Checking out the items in the cart-----------------
    print("Trying to check out the items in the cart")
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart--open")))
        print("Floating cart is visible.")
        cart_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'float-cart__shelf-container')]//div[contains(@class, 'shelf-item')]")
        checkout_clicked = False
        if not cart_items:
            print("No items found in the cart to remove.")
        else:
            try:
                checkout_button = driver.find_element(By.CLASS_NAME, "buy-btn")
                checkout_button.click()
                print(f"Successfully clicked on the checkout button")
                checkout_clicked = True
            except Exception as e:
                print(f"Found checkout button but couldn't click its remove button. Error: {e}")

    except Exception as e:
        print(f"Failed during the checkout process. Error: {e}")

    sleep(5) # Give some time 




