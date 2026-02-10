from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama 
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(model='llama2', temperature='0.2')

messages = [
    SystemMessage(content='You are a helpful assistant. Answer the user queries in a succinct manner.'),    # This is the system level message that is given in the start to define the role of the chatbot
    HumanMessage(content='Tell me about Langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)