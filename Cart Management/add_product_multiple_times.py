from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from time import sleep

# Configure Chrome options to disable logging
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# step 1: Initialize the WebDriver
print("Automation testing starts")
driver = webdriver.Chrome(options=options)

# Create an explicit wait object
wait = WebDriverWait(driver, 20)
print("The web browser is opened successfully.")

# step 2: Navigate to the website
driver.get("https://kolkata.bugbash.live/")
sleep(3)
print("The website's homepage loads successfully.")

# ======================================================================================================

# Add to cart by specific product name
# Finding all the products
products = driver.find_elements(By.CLASS_NAME, "shelf-item")
product_found = False

product_1 = "Galaxy S20"
for product in products:
    # Check if the product name matches
    if product_1 in product.text:
        try:
            # Find the "Add to Cart" button within that product element
            add_to_cart_button = product.find_element(By.CLASS_NAME, "shelf-item__buy-btn")
            add_to_cart_button.click()
            print(f"Clicked 'Add to Cart' for product: {product_1}")
            product_found = True
            break
        except Exception as e:
            print(f"Found product '{product_1}' but couldn't click the button. Error: {e}")
            break

if not product_found:
    print(f"Product '{product_1}' not found on the page.")

sleep(3)

product_2 = "iPhone 12"
for product in products:
    # Check if the product name matches
    if product_1 in product.text:
        try:
            # Find the "Add to Cart" button within that product element
            add_to_cart_button = product.find_element(By.CLASS_NAME, "shelf-item__buy-btn")
            add_to_cart_button.click()
            print(f"Clicked 'Add to Cart' for product: {product_2}")
            product_found = True
            break
        except Exception as e:
            print(f"Found product '{product_2}' but couldn't click the button. Error: {e}")
            break

if not product_found:
    print(f"Product '{product_2}' not found on the page.")

sleep(3)


# ============================== Multiplying one product ==============================

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


driver.quit()