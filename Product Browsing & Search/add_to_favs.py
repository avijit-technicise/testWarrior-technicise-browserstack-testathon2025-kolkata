from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from time import sleep

# Configure Chrome options to disable logging
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Initialize the WebDriver
print("Automation testing starts")
driver = webdriver.Chrome(options=options)

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

# ========================= Finding the same product in Favourites list =========================

try:
    # Find all the products in the Favourites page
    fav_products = driver.find_elements(By.CLASS_NAME, "shelf-item") 
    fav_product_found = False
    
    # Look for the product name in the Favourites page
    for fav_product in fav_products:
        if product_name_to_find in fav_product.text:
            print(f"Success: The product '{product_name_to_find}' is found in the Favourites list.")
            fav_product_found = True
            break
    
    if not fav_product_found:
        print(f"Error: The product '{product_name_to_find}' was not found in the Favourites list.")
    
except Exception as e:
    print(f"An error occurred while checking the Favourites list: {e}")


driver.quit()