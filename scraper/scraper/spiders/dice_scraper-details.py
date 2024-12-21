from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import traceback
import random

# Helper function for random delays
def random_delay():
    time.sleep(random.uniform(2, 5))  # Delay between 2-5 seconds

# Set up ChromeDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30)

# Open the target page
base_job_url = "https://www.dice.com/jobs/job-detail/"
url = "https://www.dice.com/jobs"
driver.get(url)

job_details_list = []

try:
    # Wait for job cards to load
    job_cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card-title-link"))
    )

    for card in job_cards:
        try:
            # Extract job ID
            job_id = card.get_attribute("id")
            if not job_id:
                continue  # Skip if no job ID is found
            
            # Construct job URL dynamically
            job_link = f"{base_job_url}{job_id}"
            job_title_main = card.text

            # Open job details page
            driver.execute_script("window.open(arguments[0]);", job_link)
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the new tab

            # Wait for the job details page to load
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "section.job-description div[data-testid='jobDescription']")
                )
            )

            # Extract job details
            job_description = driver.find_element(
                By.CSS_SELECTOR, "section.job-description div[data-testid='jobDescription']"
            ).text

            job_title_details = driver.find_element(
                By.CSS_SELECTOR, 'h1[data-cy="jobTitle"]'
            ).text

            skills_elements = driver.find_elements(
                By.CSS_SELECTOR, "div[data-cy='skillsList']"
            )
            skills_list = [skill.text for skill in skills_elements]

            compensation = driver.find_element(
                By.CSS_SELECTOR, "div.chip_chip__cYJs6 span[id^='payChip']"
                
            ).text if driver.find_elements(
                By.CSS_SELECTOR, "div.chip_chip__cYJs6 span[id^='payChip']"
            ) else "N/A"

            location_type = driver.find_element(
                By.CSS_SELECTOR, "div.chip_chip__cYJs6 span[id^='location']"
            ).text if driver.find_elements(
                By.CSS_SELECTOR, "div.chip_chip__cYJs6 span[id^='location']"
            ) else "N/A"

            # Append job details to the list
            job_details_list.append(
                {
                    "Job Title (Main Page)": job_title_main,
                    "Job Title (Details Page)": job_title_details,
                    "Job Description": job_description,
                    "Skills": skills_list,
                    "Compensation": compensation,
                    "Location Type": location_type,
                    "Job Link": job_link,
                }
            )

            # Print job details
            print(f"Job Title (Main Page): {job_title_main}")
            print(f"Job Title (Details Page): {job_title_details}")
            print(f"Job Description: {job_description[:100]}...")  # Print a snippet
            print(f"Skills: {', '.join(skills_list)}")
            print(f"Compensation: {compensation}")
            print(f"Location Type: {location_type}")
            print(f"Job Link: {job_link}")
            print("-" * 40)

        except Exception as e:
            print(f"Error scraping job card: {e}")
            traceback.print_exc()

        finally:
            # Close the job details tab and return to the main job listings tab
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])  # Switch back to the main tab

            # Pause to avoid being flagged as a bot
            random_delay()

except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()

finally:
    # Save extracted job details to a JSON file
    with open("job_details.json", "w", encoding="utf-8") as file:
        json.dump(job_details_list, file, ensure_ascii=False, indent=4)

    driver.quit()

print(f"Extracted details for {len(job_details_list)} jobs. Saved to 'job_details.json'.")
