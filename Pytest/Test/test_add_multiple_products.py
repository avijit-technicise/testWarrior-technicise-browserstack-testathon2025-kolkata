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

def test_add_multiple_products(driver):
    # step 1: Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # step 2: Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")


    # List of product names to test
    product_names = ["iPhone 12", "iPhone 12 Mini", "iPhone 12 Pro Max", "iPhone 12 Pro", "iPhone 11", "iPhone 11 Pro", "iPhone XS", "iPhone XR", "iPhone XS Max", "Galaxy S20", "Galaxy S20+", "Galaxy S20 Ultra", "Galaxy S10", "Galaxy S9", "Galaxy Note 20", "Galaxy Note 20 Ultra", "Pixel 4", "Pixel 3", "Pixel 2", "One Plus 8", "One Plus 8T", "One Plus 8 Pro", "One Plus 7T", "One Plus 7", "One Plus 6T"]

    # Loop through the product names
    for product_name_to_find in product_names:
        print(f"Testing product: {product_name_to_find}")
        
        # Find all products on the page
        products = driver.find_elements(By.CLASS_NAME, "shelf-item")
        sleep(1)
        product_found = False
        
        for product in products:
            if product_name_to_find in product.text:
                try:
                    # Find and click the "Add to Cart" button
                    add_to_cart_button = product.find_element(By.CLASS_NAME, "shelf-item__buy-btn")
                    sleep(1)

                    # Wait for the button to be clickable
                    wait.until(EC.element_to_be_clickable(add_to_cart_button))

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

        # Attempt to close the floating cart 
        print("Attempting to close the floating cart...")
        try:
            float_cart_close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "float-cart__close-btn")))
            float_cart_close_btn.click()
            print("Clicked the exit button of the floating cart.")
            sleep(2)
        except Exception as e:
            print(f"Could not click the floating cart exit button. Error: {e}")

    # Quit the driver at the end of testing
    driver.quit()


