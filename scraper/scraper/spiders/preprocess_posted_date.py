import json
from datetime import datetime, timedelta

def parse_posted_date(posted_date):
    # Handle cases like "Posted 11 hours ago" or "Posted 3 days ago"
    if "hours ago" in posted_date:
        hours = int(posted_date.split(" ")[1])
        date = datetime.now() - timedelta(hours=hours)
    elif "days ago" in posted_date:
        days = int(posted_date.split(" ")[1])
        date = datetime.now() - timedelta(days=days)
    else:
        # Default to today's date if format is unexpected
        date = datetime.now()
    return date.strftime("%Y-%m-%d")

# Load your normalized JSON file
with open("normalized_jobs_data.json", "r") as file:
    jobs_data = json.load(file)

# Preprocess the posted_date field
for job in jobs_data:
    if "posted_date" in job and job["posted_date"]:
        job["posted_date"] = parse_posted_date(job["posted_date"])

# Save the updated JSON back to a file
with open("updated_jobs_data.json", "w") as file:
    json.dump(jobs_data, file, indent=4)

print("Updated JSON saved to 'updated_jobs_data.json'.")
