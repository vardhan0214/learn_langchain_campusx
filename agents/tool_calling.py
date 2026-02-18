from langchain_ollama import ChatOllama 
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests 

#  Step 1 >> create tool 
@tool
def multiply(a : int, b: int) -> int:
    """Given two numbers a and b this tool returns their product"""
    return a*b


# print(multiply.invoke({"a":3,"b":5}))

# Step 2 >> Tool Binding
model = ChatOllama(model= "llama3.1")

llm_with_tools = model.bind_tools([multiply])

query = HumanMessage("can you Multiply 3 with 1000?")

messages = [query]
# Step 3 >> Tool Calling

result = llm_with_tools.invoke(messages)

messages.append(result)
# Step4 >> Tool Execution

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

final_result = llm_with_tools.invoke(messages)

print(final_result.content)