import json
from datetime import datetime, timedelta
import re
from dateutil import parser

# Function to parse relative date
def parse_relative_date(date_string):
    """
    Parse relative date strings like "Posted 10 hours ago" into a proper datetime object.
    """
    # Match patterns like 'Posted 10 hours ago', 'Posted 2 days ago'
    match = re.search(r'(\d+)\s+(hour|minute|day)s?\s+ago', date_string)
    
    if match:
        num = int(match.group(1))
        unit = match.group(2)
        
        if unit == 'hour':
            return datetime.now() - timedelta(hours=num)
        elif unit == 'minute':
            return datetime.now() - timedelta(minutes=num)
        elif unit == 'day':
            return datetime.now() - timedelta(days=num)
    
    # If no match, try parsing the date directly with `dateutil.parser`
    try:
        # Attempt to parse common date strings like '2024-12-20 15:30:00'
        return parser.parse(date_string)
    except Exception as e:
        # If parsing fails, return None
        print(f"Error parsing date: {e}")
        return None

# Load the JSON file
input_file = "updated_jobs_data.json"  # Replace with the path to your JSON file
output_file = "updated_jobs.json"  # Output file for updated data

with open(input_file, "r") as file:
    job_data_list = json.load(file)

# Loop through each job in the data and update the `modified_date`
for job_data in job_data_list:
    if "modified_date" in job_data and job_data["modified_date"]:
        # Parse the `modified_date`
        job_data["modified_date"] = parse_relative_date(job_data["modified_date"])

# Save the updated job data to a new file
with open(output_file, "w") as outfile:
    json.dump(job_data_list, outfile, default=str, indent=4)

print(f"Updated job data has been saved to {output_file}")
