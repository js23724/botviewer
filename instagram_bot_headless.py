from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set your Instagram Chanel video
instagram_username = 'https://www.instagram.com/reel/DaL4k2RNAfc/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=='

# Configure Chrome to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Runs Chrome in the background
chrome_options.add_argument("--window-size=1920,1080")  # Set a virtual window size so elements layout correctly
chrome_options.add_argument("--disable-gpu")  # Recommended for headless stability

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=chrome_options)

try:
    print("Opening website in headless mode...")
    driver.get('https://leofame.com/free-instagram-views')

    # Set up a max wait time of 15 seconds
    wait = WebDriverWait(driver, 15)

    # 1. Find and fill the link/username input field
    print("Entering username into free_link field...")
    username_input = wait.until(
        EC.presence_of_element_located((By.NAME, 'free_link'))
    )
    # Scroll to the input box to ensure visibility (still good practice in headless)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", username_input)
    time.sleep(0.5)
    
    username_input.clear()  # Ensure the field is clean before typing
    username_input.send_keys(instagram_username)

    # 2. Find and click the submit button
    print("Locating checkout continue button...")
    start_button = wait.until(
        EC.presence_of_element_located((By.ID, 'checkout-continue'))
    )
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", start_button)
    time.sleep(1)

    print("Clicking continue button...")
    driver.execute_script("arguments[0].click();", start_button)

    print("\nSuccessfully clicked! Waiting out the 6-minute timer process in the background...")
    time.sleep(360)

except Exception as e:
    print(f"\nAn error occurred during execution: {e}")

finally:
    print("Closing browser session.")
    driver.quit()
