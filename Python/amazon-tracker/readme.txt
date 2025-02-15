# Amazon Price Tracker

## Description:
This project is a Python-based script using Selenium to track the price of an Amazon product in real-time. It uses a headless Chrome browser to open the product page and scrape the price every 5 seconds, printing the current price to the terminal.

## Features:
- Tracks the price of a specified Amazon product
- Uses Selenium to automate the browser in headless mode (no UI)
- Prints the current price every 5 seconds

## Requirements:
- Python 3.x
- Selenium library
- Chrome WebDriver (for automating Chrome)
- Google Chrome browser

## How to Use:
1. Clone this repository or download the script.
2. Install the required Python libraries using pip:
    ```
    pip install selenium
    ```
3. Download the ChromeDriver that matches your version of Google Chrome from: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Replace the `cdp` variable in the script with the path to your downloaded `chromedriver.exe`.
5. Run the script by executing the following in your terminal:
    ```
    python amazon_price_tracker.py
    ```
6. The script will open the specified Amazon product page and track the price, printing the updated price to the terminal every 5 seconds.

