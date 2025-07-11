import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# By setting scope="module", this fixture will create ONE browser instance
# that will be shared by all tests in this file.
@pytest.fixture(scope="module")
def driver():
    # Set up Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("\n----------- BROWSER SESSION STARTED -----------")
    
    yield driver # The driver is now passed to all tests
    
    # This will run only ONCE after all tests in the file are done
    driver.quit()
    print("\n----------- BROWSER SESSION CLOSED -----------")

# Order 1: The first test to run
@pytest.mark.order(1)
def test_open_website(driver):
    print("\n[Test 1] Opening the website...")
    driver.get("https://kolkata.bugbash.live/")
    # Wait until the filter sidebar is visible to confirm page load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filters"))
    )
    assert "StackDemo" in driver.title
    print("-> Website's homepage loaded successfully.")

# Order 2: The second test to run, using the SAME browser
@pytest.mark.order(2)
def test_filtering(driver):
    print("\n[Test 2] Filtering by vendor...")
    wait = WebDriverWait(driver, 20)
    try:
        # CORRECTED XPATH: Find the clickable span for 'Google'
        google_filter = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@value='Google']/following-sibling::span")
        ))
        google_filter.click()
        sleep(3) # Let filter apply
        print("-> Clicked on 'Google' filter.")
    except Exception as e:
        pytest.fail(f"Could not click 'Google' filter. Error: {e}")

# Order 3: The third test, continuing from where the last one left off
@pytest.mark.order(3)
def test_cart_addition(driver):
    print("\n[Test 3] Adding product to cart...")
    wait = WebDriverWait(driver, 20)
    # CORRECTED Product Name: Must be a Google product to be found
    product_name_to_find = "Pixel 4"
    product_found = False

    products = driver.find_elements(By.CLASS_NAME, "shelf-item")
    for product in products:
        if product_name_to_find in product.text:
            product.find_element(By.CLASS_NAME, "shelf-item__buy-btn").click()
            print(f"-> Clicked 'Add to Cart' for product: {product_name_to_find}")
            product_found = True
            break
            
    if not product_found:
        pytest.fail(f"Product '{product_name_to_find}' not found after filtering.")

    # Close the cart to finish the test
    print("Closing the floating cart...")
    try:
        close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "float-cart__close-btn")))
        close_button.click()
        print("-> Floating cart closed successfully.")
        sleep(2)
    except Exception as e:
        pytest.fail(f"Could not close the floating cart. Error: {e}")