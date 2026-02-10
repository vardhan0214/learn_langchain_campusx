from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os 

model = ChatOllama(model = 'llama2',
                   temperature = 0.2)

chat_history = [
    SystemMessage(content='You are a helpful assistant. Answer the user queries in a succinct manner.'),
]
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'quit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

# print(chat_history)