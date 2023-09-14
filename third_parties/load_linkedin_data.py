# with the help of nubela we are going to get detail from user linkedin url
import requests
import os
from dotenv import load_dotenv
import json

#THIS IS ONE TIME SCRIPT TO GENERATE JSON FILE.

load_dotenv()
NUBELA_API_KEY = os.getenv("NUBELA_API_KEY")

api_key = NUBELA_API_KEY

if not api_key:
    raise ValueError("NUBELA_API_KEY can't be empty!")

headers = {"Authorization": "Bearer " + api_key}
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {
    "linkedin_profile_url": "https://www.linkedin.com/in/himalay-patel-995499221/"
}
response = requests.get(api_endpoint, params=params, headers=headers)


data = response.json()
json_file_path = "linkedin_profile_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

# Note : this will generate linkedin_profile_data in current dictionary. you have to upload that file into git hub too access it. for saving credit. as only 5 credits are available.
