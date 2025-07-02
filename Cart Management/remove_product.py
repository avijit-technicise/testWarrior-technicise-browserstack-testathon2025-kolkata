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



# Add to cart by specific product name
products = driver.find_elements(By.CLASS_NAME, "shelf-item")
product_found = False
product_name_to_find = "Galaxy Note 20"
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

sleep(5)





# --- Remove a specific item from the cart ---
product_name_to_remove = "Galaxy S20" # <<<--- Specify the product name to remove
print(f"Attempting to remove cart item: {product_name_to_remove}")

try:
    # First, ensure the floating cart is open and visible
    # This is crucial before trying to find items within it
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart--open")))
    print("Floating cart is visible.")

    # Find all items in the cart. You might need to inspect the cart HTML
    # to find the specific class name for individual cart items.
    # Assuming "bag-item" is the class for each item within the cart.
    # From image_19d3df.jpg, the items are under 'float-cart_content' div.
    # Let's assume each item has a class like 'bag-item' or 'cart-item'.
    # If not, you'll need to adjust this XPath/locator.
    cart_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'float-cart__shelf-container')]//div[contains(@class, 'shelf-item')]")
    # OR, if there's a more specific class for items, use that:
    # cart_items = driver.find_elements(By.CLASS_NAME, "bag-item") # Example

    item_removed = False
    if not cart_items:
        print("No items found in the cart to remove.")
    else:
        for item in cart_items:
            # Check if the product name matches within the item's text
            # Assuming the product name is directly in the item's visible text or a specific sub-element.
            if product_name_to_remove in item.text:
                try:
                    # Find the delete button within this specific cart item
                    # The delete button often has a class like 'shelf-item__del' or similar for cart items.
                    # Based on your previous code snippet, 'shelf-item__del' was used.
                    remove_button = item.find_element(By.CLASS_NAME, "shelf-item__del")
                    remove_button.click()
                    print(f"Successfully removed '{product_name_to_remove}' from the cart.")
                    item_removed = True
                    break # Exit loop after finding and removing the item
                except Exception as e:
                    print(f"Found '{product_name_to_remove}' but couldn't click its remove button. Error: {e}")
                    break
        if not item_removed:
            print(f"Product '{product_name_to_remove}' was not found in the cart.")

except Exception as e:
    print(f"Failed during cart item removal process. Error: {e}")

sleep(5) # Give some time for the cart to update after removal


# ==================================================================================================
driver.quit()
