#with the help of nubela we are going to get detail from user linkedin url
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv() 
NUBELA_API_KEY = os.getenv("NUBELA_API_KEY")

api_key = NUBELA_API_KEY

headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/himalay-patel-995499221/'
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)


data = response.json()
json_file_path = "linkedin_profile_data.json"
with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)