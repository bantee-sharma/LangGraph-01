from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.graph import MessagesState,StateGraph,END,START

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def add(a:int,b:int)->int:
    '''add a and b
    args:
         a: first number
         b: second number'''
    return a+b

def multiply(a:int,b:int)->int:
    '''multiply a and b
    args:
         a: first number
         b: second number'''
    return a*b

def divide(a:int,b:int)->float:
    '''divide a and b
    args:
         a: first number
         b: second number'''
    return a/b

search = DuckDuckGoSearchRun()

tools = [add, multiply, divide, search]

llm_with_tools = llm.bind_tools(tools=tools)

print(llm_with_tools.invoke("trending news in india"))

system_msg = SystemMessage(content="You are a helpful assistant tasked with using search and performing arithmetic on a set of inputs.")