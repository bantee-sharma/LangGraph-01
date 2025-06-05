from langgraph.graph import Graph

def func1(input1):
    return input1 + "This is from 1st func"

def func2(input2):
    return input2 + "This is from func2"

workflow1 = Graph()

workflow1.add_node("func1",func1)
workflow1.add_node("func2",func2)

workflow1.add_edge("func1","func2")

workflow1.set_entry_point("func1")
workflow1.set_finish_point("func2")

app1 = workflow1.compile()
