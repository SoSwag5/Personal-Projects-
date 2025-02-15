from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Set up logging to a file
logging.basicConfig(filename="price_scraper.log", level=logging.INFO)

cdp = r"C:\Ethical hacking programs\chromedriver.exe"
service = Service(cdp)

# Initialize the browser in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the page
url = 'https://www.amazon.com/AmazonBasics-Matte-Keyboard-QWERTY-Layout/dp/B07WJ5D3H4'
driver.get(url)

def fetch_price():
    try:
        # Wait for the price element to be visible
        price_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "a-price-whole"))
        )
        price = price_element.text
        print(f"Price: {price}")
        logging.info(f"Price: {price}")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

# Fetch the price every 30 seconds (to avoid overloading the website)
counter = 0
while counter < 10:  # Limit to 10 iterations for example
    fetch_price()
    counter += 1
    time.sleep(30)  # Adjusted sleep time to 30 seconds

driver.quit()
