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


# =============== FOR SAMSUNG PRODUCTS===================
# selecting the Samsung vendor 
print("Filtering by the 'Samsung' vendor type")
try:
    samsung_filter_span = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Samsung']/following-sibling::span[@class='checkmark' and text()='Samsung']")))
    samsung_filter_span.click()
    sleep(3) 
    print("Clicked on 'Samsung' filter.")
except Exception as e:
    print(f"Could not click 'Samsung' filter. Error: {e}")


# Add to cart by specific product name
products = driver.find_elements(By.CLASS_NAME, "shelf-item")
print(type(products))
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


# closing the cart with the exit button
print("Attempting to close the floating cart...")
try:
    # Using By.CLASS_NAME directly for "float-cart_close-btn"
    float_cart_close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "float-cart__close-btn")))
    float_cart_close_btn.click()
    print("Clicked the exit button of the floating cart.")
    sleep(2)
except Exception as e:
    print(f"Could not click the floating cart exit button. Error: {e}")



# ==================================================================================================
driver.quit()
