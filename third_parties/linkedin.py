import os
import requests
from dotenv import load_dotenv
import json
import random

load_dotenv()
NUBELA_API_KEY = os.getenv("NUBELA_API_KEY")

api_key = NUBELA_API_KEY


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn Profile"""

    profile_url = [
        "https://raw.githubusercontent.com/Himalaypatel75/LangChain/feature/linkedin_intigration/third_parties/himalay_linkedin_data.json",
        "https://raw.githubusercontent.com/Himalaypatel75/LangChain/feature/linkedin_intigration/third_parties/dhaval_linkedin_data.json",
        "https://raw.githubusercontent.com/Himalaypatel75/LangChain/feature/linkedin_intigration/third_parties/nisarg_linkedin_data.json",
    ]

    random_url = random.choice(profile_url)  # this will give random url
    response = requests.get(random_url)

    if response.status_code != 200:
        print("response is not 200 so fetching from scraper")

        try:
            if not api_key:
                raise ValueError("NUBELA_API_KEY can't be empty!")

            api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
            headers = {"Authorization": "Bearer " + api_key}
            params = {"linkedin_profile_url": linkedin_profile_url}
            response = requests.get(api_endpoint, params=params, headers=headers)
            # below code can be used to save data into json file
            # data = response.json()
            # json_file_path = "dhaval_linked_in.json"
            # with open(json_file_path, "w") as json_file:
            #     json.dump(data, json_file, indent=4)
        except Exception as e:
            print(f"exception occured - {e}")

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dic in data.get("groups"):
            group_dic.pop("profile_pic_url")
            # pass

    return data
