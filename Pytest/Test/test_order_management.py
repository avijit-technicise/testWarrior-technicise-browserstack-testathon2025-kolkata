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
from selenium.common.exceptions import TimeoutException


@pytest.fixture(scope="module")
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("The web browser is opened successfully.")
    yield driver
    driver.quit()

print("Automation testing starts")

@pytest.mark.order(1)
def sign_in (driver):

    # Create an explicit wait object
    # wait = WebDriverWait(driver, 20)
    
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
def test_place_order (driver):

    wait = WebDriverWait(driver, 20)

    # =========================Add to cart=================================

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

    # =========================Checkout================================

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

    sleep(3) 

    # ================================Shipping Address Submission===========================

    try:
        first_name = "Harry"
        first_name_element = driver.find_element(By.ID, "firstNameInput")
        first_name_element.send_keys(first_name);
        print(f"Successfully typed the first name: {first_name}")
        sleep(1)
    except Exception as e:
        print(f"An error occurred typing first name: {e}")

    try:
        last_name = driver.find_element(By.ID, "lastNameInput")
        last_name.send_keys("Potter");
        print(f"Successfully typed the last name: {last_name}")
        sleep(1)
    except Exception as e:
        print(f"An error occurred typing last name: {e}")


    try:
        address = driver.find_element(By.ID, "addressLine1Input")
        address.send_keys("UK");
        print(f"Successfully typed the address: {address}")
        sleep(1)
    except Exception as e:
        print(f"An error occured typing the address: {e}")


    try:
        province = driver.find_element(By.ID, "provinceInput")
        province.send_keys("London");
        print(f"Successfully typed the province name: {province}")
        sleep(1)
    except Exception as e:
        print(f"An error occured typing province name: {e}")

    try:
        postal_code = driver.find_element(By.ID, "postCodeInput")
        postal_code.send_keys("456");
        print(f"Successfully typed the posatl code: {postal_code}")
        sleep(1)
    except Exception as e:
        print(f"An error occured while typing postal code: {e}")

    try:
        submit_button = driver.find_element(By.ID, "checkout-shipping-continue")
        submit_button.click()
        print("Form submitted successfully!")
        sleep(1) 
    except Exception as e:
        print(f"An error occurred: {e}")

    sleep(5)


@pytest.mark.order(3)
def test_order_verification (driver):
    wait = WebDriverWait(driver, 20)
    try:
    # Wait up to 10 seconds for the product name to be visible in the order summary
    # This XPath looks for any element containing the product name inside the order summary section.
    # You may need to adjust the locator based on your actual HTML structure.
    product_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), 'Order Summary')]/following-sibling::div//p[contains(text(), '{product_to_find}')]"))
    )
    
    # Assert that the element's text contains the product name
    assert product_to_find in product_element.text
    
    print(f"✅ Success: Found '{product_element.text}' in the order summary.")

    except TimeoutException:
        print(f"❌ Failure: Product '{product_to_find}' was not found in the order summary within the time limit.")
    except AssertionError:
        print(f"❌ Failure: Element found, but text did not match '{product_to_find}'




@pytest.mark.order(4)
def view_order_history (driver):
    wait = WebDriverWait(driver, 20)

    # Finding and clicking "Orders" button
    try:
        orders_button = driver.find_element(By.ID, "orders")
        orders_button.click()
        sleep(3)
        print("The 'Orders' page is displayed")
    except NoSuchElementException:
        print("The 'Orders' button was not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



    # Check if any order is present
    print("Checking for orders on the page.")

    order_items = driver.find_elements(By.ID, "1") 

    if order_items:
        print(f"Found {len(order_items)} orders on the page.")
        assert len(order_items) > 0, "Assertion Failed: Expected orders to be present, but none were found."
        print("Test Passed: Orders are present on the page.")
    else:
        print("No orders found on the page.")
        assert False, "Assertion Failed: No orders found on the order history page for 'existing_orders_user'."

    print("Automation test ends")