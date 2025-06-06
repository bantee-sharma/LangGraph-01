from langgraph.graph import Graph
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def llm_func(input:str)->str:
    result = llm.invoke(input=input)
    return result.content

def upper_func(input:str)->str:
    return input.upper()

workflow = Graph()

workflow.add_node("llm_func",llm_func)
workflow.add_node("upper_string",upper_func)
workflow.add_edge("llm_func","upper_string")

workflow.set_entry_point("llm_func")
workflow.set_finish_point("upper_string")

app = workflow.compile()

response = app.invoke("who is pm of india")

#print(app.get_graph().draw_ascii())

query = "What is LangGraph"
for output in app.stream(query):
    for key,value in output.items():
        print(f'this id from {key}')
        print("_"*50)
        print(value)
        print("_"*50)


