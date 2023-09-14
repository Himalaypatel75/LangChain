from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import os
from dotenv import load_dotenv

load_dotenv()  # loading environment variable from current dictionary

information = """
lon Reeve Musk (EE-lon; born June 28, 1971) is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$226 billion as of September 2023, according to the Bloomberg Billionaires Index, and $249 billion according to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.[4][5][6]

Musk was born in Pretoria, South Africa, and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University in Kingston, Ontario. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics there. He moved to California in 1995 to attend Stanford University. However, Musk dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and with $12 million of the money he made, that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.

In 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company."""
if __name__ == "__main__":
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #store environment variable in .env file

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

    print(chain.run(information=information))
