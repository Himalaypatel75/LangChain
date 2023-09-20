from tools.tools import get_profile_url

from langchain import PromptTemplate

from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI


def lookup(product_descriptions: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # template = """
    #     give me product detail for {product_description} I want you to find product image link, name and short description give me 5 details"""
        
    template = """
        find what ever you can find for {product_descriptions}"""
        
    tools_for_agent_product = [
        Tool(
            name="Crawl Google 4 Online Buying Websites",
            func=get_profile_url,
            description="useful for when you need get the Product Detail",
        ),
    ]

    agent = initialize_agent(
        tools_for_agent_product,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        # max_iterations=2,
    )
    prompt_template = PromptTemplate(
        input_variables=["product_descriptions"], template=template
    )

    product_details = agent.run(prompt_template.format_prompt(product_descriptions=product_descriptions))
    print("****************************Using Google Search Engine****************************")
    print(product_details)
    print("****************************Using Google Search Engine****************************")
    return product_details
