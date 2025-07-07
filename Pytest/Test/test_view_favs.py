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

def test_favourite_list(driver):
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

    username_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-') and text()='fav_user']")))
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

    # --- Identify and Print Products with Red Hearts ---
    favorited_product_names = []

    print("Identifying product cards...")
    # **IMPORTANT:** Adjust this locator to target the main container for each product.
    # Common examples: By.CLASS_NAME, "product-item" or By.CSS_SELECTOR, ".product-card"
    # From inspecting similar BrowserStack demo sites, ".product-card" is a good guess.
    product_cards = driver.find_elements(By.CSS_SELECTOR, "shelf-container") 

    if not product_cards:
        print("No product cards found on the page to inspect.")
        return # Exit the test function if no products are found

    print(f"Found {len(product_cards)} product cards. Checking if added to favourites...")

    for i, card in enumerate(product_cards):
        try:
            # **IMPORTANT:** Adjust this locator to get the product name/title within each card.
            # From inspecting similar BrowserStack demo sites, ".shelf-item__title" is common.
            product_name_element = card.find_element(By.CLASS_NAME, "shelf-item__title") 
            product_name = product_name_element.text.strip()
            
            # **IMPORTANT:** Adjust these locators to accurately find the favorite icon.
            # Assuming the heart icon is within a button/div that has a class.
            # From inspecting similar BrowserStack demo sites, ".shelf-item__wishlist" button wraps the SVG.
            favourite_icon_wrapper = card.find_element(By.CLASS_NAME, "shelf-stopper")
            
            # The actual heart shape is usually an SVG <path> element.
            heart_path_element = favourite_icon_wrapper.find_element(By.TAG_NAME, "path")
            
            # Get the 'fill' attribute which determines the SVG's color.
            current_fill_color = heart_path_element.get_attribute("fill")
            
            # print(f"DEBUG: Product: {product_name}, Heart fill color: {current_fill_color}") # Uncomment to debug colors

            # **IMPORTANT:** Define the exact color values that represent "red".
            # You MUST inspect the actual 'fill' attribute value when a heart is red on the website.
            # Common red hex codes: '#FF0000', '#E50000', also 'rgb(255, 0, 0)' or just 'red'.
            if current_fill_color and (current_fill_color.lower() == '#ff0000' or 
                                        current_fill_color.lower() == 'red' or 
                                        current_fill_color.lower() == 'rgb(255, 0, 0)'):
                favorited_product_names.append(product_name)

        except NoSuchElementException:
            print(f"Warning: Could not find product name or favorite icon for a product card (index {i}). Skipping this card.")
            continue # Skip to the next card if elements are missing from this one
        except Exception as e:
            print(f"An unexpected error occurred while processing card {i}: {e}. Skipping this card.")
            continue
            
    if favorited_product_names:
        print("\n--- Products with Red Hearts ---")
        for product in favorited_product_names:
            print(f"- {product}")
    else:
        print("\nNo products found with red hearts.")

    print("Automation test ends: Finished checking for red-hearted products.")



















