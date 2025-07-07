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

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_add_to_fav(driver):
    # Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")


    # ================Sign In===========
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


    # Add to cart by specific product name
    products = driver.find_elements(By.CLASS_NAME, "shelf-item")
    product_found = False
    product_name_to_find = "iPhone 12 Mini"
    for product in products:
        # Check if the product name matches
        if product_name_to_find in product.text:
            try:
                # Find the "Add to Cart" button within that product element
                add_to_fav_button = product.find_element(By.CLASS_NAME, "shelf-stopper")
                add_to_fav_button.click()
                print(f"Clicked 'Add to Favourites' for product: {product_name_to_find}")
                product_found = True
                break
            except Exception as e:
                print(f"Found product '{product_name_to_find}' but couldn't click the button. Error: {e}")
                break

    if not product_found:
        print(f"Product '{product_name_to_find}' not found on the page.")

    sleep(3)

    # Finding and clicking "Favourites" button
    try:
        fav_button = driver.find_element(By.ID, "favourites")
        fav_button.click()
        sleep(3)
        print("The 'Favourites' page is displayed")
    except NoSuchElementException:
        print("The 'Favourites' button was not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")