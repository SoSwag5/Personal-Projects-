# Job Scraper - TimesJobs Scraper

## Description:
This project is a Python-based scraper that extracts job listings from the TimesJobs website based on a search keyword (e.g., "Python"). It filters the listings to show jobs posted within the last 3 days. The scraper collects the company name, required skills, and the date of posting.

## Features:
- Scrapes job listings from TimesJobs
- Filters jobs posted within the last 3 days
- Extracts key details such as company name, skills required, and date of posting

## Requirements:
- Python 3.x
- Requests library
- BeautifulSoup4 library (for HTML parsing)
- lxml parser (for more efficient parsing)

## How to Use:
1. Clone this repository or download the script.
2. Install the required Python libraries using pip:
    ```
    pip install requests beautifulsoup4 lxml
    ```
3. Run the script by executing the following in your terminal:
    ```
    python job_scraper.py
    ```
4. The script will display job listings that match the search criteria (e.g., Python jobs) and were posted within the last 3 days.

