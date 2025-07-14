import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from time import sleep

@pytest.fixture(scope="module")
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("The web browser is opened successfully.")
    yield driver
    
    driver.quit()


@pytest.mark.order(1)
def test_signin (driver):

    print("Automation testing starts")

    wait = WebDriverWait(driver, 20)

    # Step 1: Open the website
    driver.get("https://kolkata.bugbash.live")
    sleep(3)
    print("Website homepage loaded successfully.")

    # Step 2: Click Sign In
    sign_in_button = driver.find_element(By.ID, "Sign In")
    sign_in_button.click()
    sleep(3)
    print("Sign In page displayed.")

    # Step 3: Select Username
    username_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']")))
    username_dropdown.click()
    print("Username dropdown clicked.")
    sleep(1)

    username_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-') and text()='demouser']")))
    username_option.click()
    print("Username 'demouser' selected.")
    sleep(1)

    # Step 4: Select Password
    password_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']")))
    password_dropdown.click()
    print("Password dropdown clicked.")
    sleep(1)

    password_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-') and text()='testingisfun99']")))
    password_option.click()
    print("Password 'testingisfun99' selected.")
    sleep(1)

    # Step 5: Click Login
    login_button = driver.find_element(By.ID, "login-btn")
    login_button.click()
    print("Login button clicked.")
    sleep(5)

    print("Login process completed successfully.")



@pytest.mark.order(2)
def test_empty_cart (driver):
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
    

@pytest.mark.order(3)
def test_add_product (driver):
    
    wait = WebDriverWait(driver, 20)
    
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


@pytest.mark.order(4)
def test_remove_product (driver):
    
    wait = WebDriverWait(driver, 20)
    
    # cart button
    cart_button = driver.find_element(By.CLASS_NAME, "bag__quantity")
    cart_button.click()
    sleep(1)
    print("The cart is opened")

    # --- Remove a specific item from the cart ---
    product_name_to_remove = "Galaxy S20" 
    print(f"Attempting to remove cart item: {product_name_to_remove}")

    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart--open")))
        print("Floating cart is visible.")

        cart_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'float-cart__shelf-container')]//div[contains(@class, 'shelf-item')]")

        item_removed = False
        if not cart_items:
            print("No items found in the cart to remove.")
        else:
            for item in cart_items:
                if product_name_to_remove in item.text:
                    try:
                        remove_button = item.find_element(By.CLASS_NAME, "shelf-item__del")
                        remove_button.click()
                        print(f"Successfully removed '{product_name_to_remove}' from the cart.")
                        item_removed = True
                        break 
                    except Exception as e:
                        print(f"Found '{product_name_to_remove}' but couldn't click its remove button. Error: {e}")
                        break
            if not item_removed:
                print(f"Product '{product_name_to_remove}' was not found in the cart.")

    except Exception as e:
        print(f"Failed during cart item removal process. Error: {e}")

    sleep(3)


@pytest.mark.order(5)
def test_add_product_multiple_times (driver):
    
    wait = WebDriverWait(driver, 20)

    product_1 = "iPhone 12 Mini"

    float_cart_products = driver.find_elements(By.CLASS_NAME, "float-cart__content")
    product_found = False

    for product in float_cart_products:
        # Check if the product name matches
        if product_1 in product.text:
            try:
                # Find the "Add Product" button within that product element
                add_product_button = product.find_element(By.XPATH, ".//button[text()='+']")
                deduct_product_button = product.find_element(By.XPATH, ".//button[text()='-']")
                click_count = 1
                for _ in range(2):
                    add_product_button.click()
                    click_count += 1
                    sleep(2)
                # deduct_product_button.click()
                # sleep(2)
                print(f"Clicked 'Add more Items' {click_count} times for product: {product_1}")
                product_found = True
                break
            except Exception as e:
                print(f"Found product '{product_1}' but couldn't click the button. Error: {e}")
                break

    if not product_found:
        print(f"Product '{product_1}' not found in the cart.")

@pytest.mark.order(6)
def test_appropriate_product_inclusion (driver):
    wait = WebDriverWait(driver, 20)

    # Verify if the product is in the cart
    product_name_to_verify = "iPhone 12 Mini"
    print(f"Verifying if '{product_name_to_verify}' is in the cart...")

    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart--open")))
        print("Floating cart is visible.")

        cart_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'float-cart__shelf-container')]//div[contains(@class, 'shelf-item')]")
        product_found = False

        for item in cart_items:
            if product_name_to_verify in item.text:
                print(f"Product '{product_name_to_verify}' is present in the cart.")
                product_found = True
                break

        if not product_found:
            print(f"Product '{product_name_to_verify}' is NOT present in the cart.")

    except Exception as e:
        print(f"Failed during the verification process. Error: {e}")

    sleep(3)