import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_order_history(driver):
    print("Automation test starts")
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

    username_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-') and text()='existing_orders_user']")))
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


    # Step 6: Finding and clicking "Orders" button
    try:
        orders_button = driver.find_element(By.ID, "orders")
        orders_button.click()
        sleep(3)
        print("The 'Orders' page is displayed")
    except NoSuchElementException:
        print("The 'Orders' button was not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



    # Step 7: Check if any order is present
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


    