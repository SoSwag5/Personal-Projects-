from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the URL
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_text = response.text  # To display the text results or textify the URL

    # Parse the HTML content using BeautifulSoup with lxml parser
    soup = BeautifulSoup(html_text, 'lxml')  # Just memorize the stuff inside

    # Find all job listings
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Iterate over each job listing
    for job in jobs:
        date = job.find('span', class_='sim-posted')
        if date:
            date = date.span.text.strip() if date.span else "N/A"  # Handle missing date

        if 'Posted 3 days ago' in date:  # Filter jobs posted 3 days ago
            company_name = job.find('h3', class_='joblist-comp-name')
            company_name = company_name.text.strip() if company_name else "N/A"  # Handle missing company name

            skills = job.find('span', class_='srp-skills')
            skills = skills.text.strip() if skills else "N/A"  # Handle missing skills

            # Print job details
            print(f"Company Name: {company_name}")
            print(f"Skills Required: {skills}")
            print(f"Posted: {date}")
            print('___' * 20)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
