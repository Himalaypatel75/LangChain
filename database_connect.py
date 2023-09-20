from typing import Tuple
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import random
import os
from dotenv import load_dotenv
import requests
from agents.produt_lookup import lookup as product_lookup_agent
from agents.database_lookup import lookup as database_lookup_agent
from output_parsors import PersonIntel, person_intel_parser
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scraper_user_tweets
from third_parties.twitter_with_stubs import scrape_user_tweets


load_dotenv()  # loading environment variable from current dictionary

def connect_db():
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )  # store environment variable in .env file
    
    database_details = database_lookup_agent(product_detail = "Polyjet")
    product_details = product_lookup_agent(product_descriptions="Polyjet")

    # summary_template = """
    # given the products information from different sources {product_details} and {database_details} about a product I want you to give all list of resources with and also describe resource origin get data from both sources :
    # 1. description
    # 2. name
    # 3. full url of website"""
    
    summary_template = """
    describe what ever you can describe about {database_details} and {product_details} i need description for both with separation"""

    summary_prompt_template = PromptTemplate(
        input_variables=["database_details", "product_details"],
        template=summary_template,
        # partial_variables={
        #     "format_instructions": person_intel_parser.get_format_instructions()
        # },
    )
    
    llm = ChatOpenAI(
        temperature=0, model_name="gpt-3.5-turbo"
    )  # temperature will decide how much llm model can be creative. 0 is less creative. 1 will be creative only 2 values can be

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(
        product_details=product_details,
        database_details = database_details
    )
    
    return result

if __name__ == "__main__":
    result = connect_db()
    print("================Final Description================")
    print(result)
    print("================Final Description================")
    

