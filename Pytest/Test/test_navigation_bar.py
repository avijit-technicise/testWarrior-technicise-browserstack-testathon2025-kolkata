import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from time import sleep

@pytest.fixture
def driver():
    # Set up Chrome browser (non-headless, visible)
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navigation_bar_functionality (driver):

    # Initialize the WebDriver
    print("Automation testing starts")

    # Create an explicit wait object
    wait = WebDriverWait(driver, 20)
    print("The web browser is opened successfully.")

    # Navigate to the website
    driver.get("https://kolkata.bugbash.live/")
    sleep(3)
    print("The website's homepage loads successfully.")

    # Step 1: Finding the sign in button
    sign_in_button = driver.find_element(By.ID, "Sign In")
    sign_in_button.click()
    sleep(3)
    print("The Sign In page is displayed with fields for username and password.")



    # Step 2: Logging in
    # for username
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='username']//div[text()='Select Username']"))).click()
    print("Clicked 'Select Username' dropdown.")
    sleep(1)
    username_text = "demouser" 
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{username_text}']"))).click()
    print(f"Selected username: {username_text}")
    sleep(1)

    # for password section
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='password']//div[text()='Select Password']"))).click()
    print("Clicked 'Select Password' dropdown.")
    sleep(1) 
    password_text = "testingisfun99" 
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'css-') and text()='{password_text}']"))).click()
    print(f"Selected password: {password_text}")
    sleep(1)

    # for the login button
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()
    print("Clicked 'Log In' button.")
    sleep(3)


    # Finding and clicking "Offers" button
    try:
        offers_button = driver.find_element(By.ID, "offers")
        offers_button.click()
        sleep(3)
        print("The 'offers' page is displayed")
    except NoSuchElementException:
        print("The 'Offers' button was not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


    # Going back to HOME page clicking the logo
    try:
        logo_button = driver.find_element(By.CLASS_NAME, "Navbar_logo__26S5Y")
        logo_button.click()
        sleep(3)
        print("Went back to HOME page")
    except NoSuchElementException:
        print("The 'BrowserStack logo' was not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



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


    # Going back to HOME page clicking the logo
    try:
        logo_button = driver.find_element(By.CLASS_NAME, "Navbar_logo__26S5Y")
        logo_button.click()
        sleep(3)
        print("Went back to HOME page")
    except NoSuchElementException:
        print("The 'BrowserStack logo' was not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



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



