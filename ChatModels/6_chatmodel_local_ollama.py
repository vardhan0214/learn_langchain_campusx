from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate 
import os 

model = ChatOllama(model = 'llama2',
                 temperature=0.2
                 )


