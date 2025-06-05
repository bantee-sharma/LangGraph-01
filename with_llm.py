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


# Node 2: Convert string to uppercase
def upper_string(input2: str) -> str:
    result = input2.upper()
    return result

# Create the LangGraph workflow
workflow = Graph()

# Add nodes to the graph
workflow.add_node("llm",llm_func)
workflow.add_node("upper_string",upper_string)

# Define the edge (connection) between nodes: llm → upper_string
workflow.add_edge("llm","upper_string")

# Set the start and end points of the graph
workflow.set_entry_point("llm")
workflow.set_finish_point("upper_string")

# Compile the graph into an executable app
app = workflow.compile()

# Get user input from the terminal
query = input("Ask: ")

# Try invoking the graph and printing final output
try:
    output = app.invoke(query)
    print("Final Output:\n", output)
except Exception as e:
    print("Error occurred:", e)

# Optional: Print ASCII diagram of the workflow
try:
    print(app.get_graph().draw_ascii())
except Exception as e:
    # This requires some extra dependencies and is optional
    print(e)

# Stream step-by-step output through each node
for output in app.stream(query):
    for key,value in output.items():
        print(f"This is from {key} function")
        print("_"*50)
        print(value)
        print("_"*50)
