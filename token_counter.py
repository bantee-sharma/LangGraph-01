from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import Graph
from dotenv import load_dotenv

# Load environment variables (e.g., API keys from .env file)
load_dotenv()

# Initialize the Gemini LLM (Google Generative AI)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Node 1: Function to call the Gemini LLM
def llm_func(input1:str) -> str:
    result = llm.invoke(input1)
    return result.content

def token_counter(input):
    token = input.split()
    token = len(token)
    res = f"Total token number is {token}"
    return res

workflow1 = Graph()

workflow1.add_node("func1",llm_func)
workflow1.add_node("func2",token_counter)

workflow1.add_edge("func1","func2")

workflow1.set_entry_point("func1")
workflow1.set_finish_point("func2")

app1 = workflow1.compile()

print(app1.invoke("Who is the pm of india"))

input = "Who is the pm of india"
for output in app1.stream(input):
    for key,value in output.items():
        print(f"This output coming from {key}")
        print("________")
        print(value)
        print("_________")