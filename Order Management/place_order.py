from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException

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

driver.quit()