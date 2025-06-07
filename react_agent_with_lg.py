from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.graph import MessagesState,StateGraph,END,START
from langgraph.prebuilt import ToolNode,tools_condition

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

def reasoner(state: MessagesState):
    messages = [system_msg] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": state["messages"] + [response]}

builder = StateGraph(MessagesState)
builder.add_node("reasoner",reasoner)
builder.add_node("tools",ToolNode(tools))
builder.add_edge(START,"reasoner")
builder.add_conditional_edges("reasoner",tools_condition)
builder.add_edge("tools","reasoner")
react_graph = builder.compile()
    
#print(react_graph.get_graph().draw_ascii())

query = [HumanMessage(content="What is 2 times of naranger modi age?")]
res = react_graph.invoke({"messages":query})

for i in res["messages"]:
    i.pretty_print()
