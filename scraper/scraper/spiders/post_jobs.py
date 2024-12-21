import requests
import json

# API endpoint URL
url = "http://127.0.0.1:8000/api/jobs/add/"

# Path to the JSON file
json_file_path = "updated_jobs.json"

try:
    # Load data from the JSON file
    with open(json_file_path, 'r') as file:
        jobs_data = json.load(file)
except FileNotFoundError:
    print(f"Error: File '{json_file_path}' not found.")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Iterate through the jobs and send POST requests
for job in jobs_data:
    try:
        response = requests.post(url, json=job)
        response_data = response.json()  # Parse JSON response

        if response.status_code == 201:
            print(f"Job '{job['title']}' added successfully! Job ID: {response_data.get('job_id')}")
        else:
            print(f"Failed to add job '{job['title']}'. Status code: {response.status_code}")
            print("Response:", response_data)
    except requests.RequestException as e:
        print(f"Network error occurred while adding job '{job['title']}': {e}")
    except ValueError:
        print(f"Error parsing response for job '{job['title']}'. Response text: {response.text}")
