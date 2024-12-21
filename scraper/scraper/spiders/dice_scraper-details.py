import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Base URL for job details
base_url = "https://www.dice.com/job-detail/"

options = Options()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20)

input_csv = "job_details.csv"
output_csv = "enriched_job_details.csv"
output_json = "enriched_job_details.json"

with open(input_csv, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    jobs = list(reader)

enriched_job_details = []

try:
    for job in jobs:
        job_id = job["Job ID"]
        detail_url = f"{base_url}{job_id}" 
        print(f"Scraping details for Job ID: {job_id} from {detail_url}")

        driver.get(detail_url)

        try:
            compensation = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "span[id^='payChip:']")
            )).text
        except:
            compensation = "N/A"

        try:
            skills_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-cy='skillsList'] span[id^='skillChip:']")
            skills = ", ".join([skill.text for skill in skills_elements])
        except:
            skills = "N/A"

        try:
            location_type = driver.find_element(By.CSS_SELECTOR, "span[id^='location:']").text
        except:
            location_type = "N/A"

        try:
            job_description = driver.find_element(By.ID, "jobDescription").text
        except:
            job_description = "N/A"

        job["Compensation"] = compensation
        job["Skills"] = skills
        job["Location Type"] = location_type
        job["Job Description"] = job_description

        enriched_job_details.append(job)

        print(f"Compensation: {compensation}")
        print(f"Skills: {skills}")
        print(f"Location Type: {location_type}")
        print(f"Job Description: {job_description[:100]}...")  
        print("-" * 40)

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()

    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = list(enriched_job_details[0].keys()) 
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enriched_job_details)

    with open(output_json, mode="w", encoding="utf-8") as file:
        json.dump(enriched_job_details, file, ensure_ascii=False, indent=4)

    print(f"Enriched data saved to {output_csv} and {output_json}.")
