from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode for debugging
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

# Open the target page
url = "https://www.dice.com/jobs"
driver.get(url)

try:
    # Wait for job cards to load
    job_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card-title-link")))

    for card in job_cards:
        # Extract Job Title
        job_title = card.text

        # Try to locate employment type
        try:
            employment_type = card.find_element(By.XPATH, ".//following::span[@data-cy='search-result-employment-type']").text
        except:
            employment_type = "N/A"

        # Try to locate Posted Date
        try:
            posted_date = card.find_element(By.XPATH, ".//following::span[@data-cy='card-posted-date']").text
        except:
            posted_date = "N/A"

        # Try to locate Modified Date
        try:
            modified_date = card.find_element(By.XPATH, ".//following::span[@data-cy='card-modified-date']").text
        except:
            modified_date = "N/A"
        
        try:
            location = card.find_element(By.XPATH, ".//following::span[@data-cy='search-result-location']").text
        except:
            location = "N/A"

        # Try to locate Company Name
        try:
            company_name = card.find_element(By.XPATH, ".//following::a[contains(@class, 'ng-star-inserted')]").text
        except:
            company_name = "N/A"

        # Print Job Details
        print(f"Job Title: {job_title}")
        print(f"Employment Type: {employment_type}")
        print(f"Location: {location}")
        print(f"Posted Date: {posted_date}")
        print(f"Modified Date: {modified_date}")
        print(f"Company Name: {company_name}")
        print("-" * 40)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
