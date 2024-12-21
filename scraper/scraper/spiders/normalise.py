import json

# Load the original JSON data
with open("enriched_job_details.json", "r") as file:
    jobs_data = json.load(file)

# Define key mapping
key_mapping = {
    "Job ID": "job_id",
    "Job Title": "title",
    "Employment Type": "employment_type",
    "Location": "location",
    "Posted Date": "posted_date",
    "Modified Date": "modified_date",
    "Company Name": "company_name",
    "Compensation": "salary",
    "Skills": "skills",
    "Location Type": "location_type",
    "Job Descrip": "job_description"
}

# Transform keys
normalized_data = [
    {key_mapping.get(k, k): v for k, v in job.items()}
    for job in jobs_data
]

# Save normalized JSON
with open("normalized_jobs_data.json", "w") as file:
    json.dump(normalized_data, file, indent=4)

print("Normalized JSON saved to 'normalized_jobs_data.json'.")
