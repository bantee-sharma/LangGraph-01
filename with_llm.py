from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import Graph
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def llm_func(input1):
    result = llm.invoke(input1)
    return result.content

def upper_string(input2):
    result = input2.upper()
    return result

workflow = Graph()

workflow.add_node("llm",llm_func)
workflow.add_node("upper_string",upper_string)
workflow.add_edge("llm","upper_string")

workflow.set_entry_point("llm")
workflow.set_finish_point("upper_string")

app = workflow.compile()

query = "Who is the PM of india"
print(app.invoke(query))

try:
    print(app.get_graph().draw_ascii())
except Exception as e:
    # This requires some extra dependencies and is optional
    print(e)

input = "who is the pm of india"

for output in app.stream(input):
    for key,value in output.items():
        print(f"This is from {key} function")
        print("_"*50)
        print(value)
        print("_"*50)
