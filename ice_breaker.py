from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import random
import os
from dotenv import load_dotenv
import requests

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()  # loading environment variable from current dictionary


if __name__ == "__main__":
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )  # store environment variable in .env file

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo"
    )  # temperature will decide how much llm model can be creative. 0 is less creative. 1 will be creative only 2 values can be

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/himalay-patel-995499221/"
    )

    print(chain.run(information=linkedin_data))
