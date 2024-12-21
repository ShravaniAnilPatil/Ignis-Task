import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

url = "https://www.dice.com/jobs"
driver.get(url)
job_details_list = []

try:
    job_cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card-title-link")))

    for card in job_cards:
        job_title = card.text

        try:
            job_id = card.get_attribute("id")
        except:
            job_id = "N/A"

        try:
            employment_type = card.find_element(By.XPATH, ".//following::span[@data-cy='search-result-employment-type']").text
        except:
            employment_type = "N/A"

        try:
            posted_date = card.find_element(By.XPATH, ".//following::span[@data-cy='card-posted-date']").text
        except:
            posted_date = "N/A"

        try:
            modified_date = card.find_element(By.XPATH, ".//following::span[@data-cy='card-modified-date']").text
        except:
            modified_date = "N/A"
        
        try:
            location = card.find_element(By.XPATH, ".//following::span[@data-cy='search-result-location']").text
        except:
            location = "N/A"

        try:
            company_name = card.find_element(By.XPATH, ".//following::a[contains(@class, 'ng-star-inserted')]").text
        except:
            company_name = "N/A"

        job_details_list.append({
            "Job ID": job_id,
            "Job Title": job_title,
            "Employment Type": employment_type,
            "Location": location,
            "Posted Date": posted_date,
            "Modified Date": modified_date,
            "Company Name": company_name
        })
        print("********************************")

        print(f"Job ID: {job_id}")
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

    csv_file = "job_details.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Job ID", "Job Title", "Employment Type", "Location", "Posted Date", "Modified Date", "Company Name"])
        writer.writeheader()
        writer.writerows(job_details_list)

    json_file = "job_details.json"
    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(job_details_list, file, ensure_ascii=False, indent=4)

    print(f"Data saved to {csv_file} and {json_file}.")
