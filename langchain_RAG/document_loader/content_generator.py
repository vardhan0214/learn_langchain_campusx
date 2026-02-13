from langchain_ollama import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

model = ChatOllama(model='llama2', temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional poet with 15+ years of experience."),
    ("human", "{query}")
])

parser = StrOutputParser()


chain = prompt | model | parser

content_to_export = chain.invoke({
    "query" : "Write me a long poem on Cricket"
})


# Saving the text into a new file 
file_path = "sample_text.txt"
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content_to_export)
    print(f"Successfully exported to '{file_path}'")
except IOError as e:
    print(f"An error occurred while exporting to '{file_path}': {e}")

