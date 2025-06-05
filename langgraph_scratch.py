from langgraph.graph import Graph
from IPython.display import Image, display

def func3(input3):
    return input3

def func1(input1):
    return input1 + " This is from 1st func"

def func2(input2):
    output = "this is from func3"
    return input2 + output + " sharma This is from func2"

workflow1 = Graph()

workflow1.add_node("func1",func1)
workflow1.add_node("func2",func2)

workflow1.add_edge("func1","func2")

workflow1.set_entry_point("func1")
workflow1.set_finish_point("func2")

app1 = workflow1.compile()

'''try:
    print(app1.get_graph().draw_ascii())
except Exception as e:
    # This requires some extra dependencies and is optional
    print(e)'''

print(app1.invoke("Hii this is bantee"))

input = "hii this is bantee"

'''for output in app1.stream(input):
    for key,value in output.items():
        print(f"This output coming from {key}")
        print("________")
        print(value)
        print("_________")'''
    
