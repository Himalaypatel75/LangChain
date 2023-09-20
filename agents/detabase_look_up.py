from langchain.chat_models import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain import PromptTemplate



def lookup(product_detail:str):
    
    template = """
        give me all possible data which contain '{product_detail}' from database either it can be document, content or any other form of information about it"""
        
        
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/openai"

    db = SQLDatabase.from_uri(SQLALCHEMY_DATABASE_URL)
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    toolkit = SQLDatabaseToolkit(db=db, llm = llm)
    
    agent = create_sql_agent(
        llm = llm,
        toolkit=toolkit,
        verbose=True
    )
    
    prompt_template = PromptTemplate(
        input_variables=["product_detail"], template=template
    )

    product_details = agent.run(prompt_template.format_prompt(product_detail=product_detail))
    
    print("---------------------------------Getting Details From Database------------------------------------")
    print(product_details)
    print("---------------------------------Getting Details From Database------------------------------------")
    
    
    return product_details