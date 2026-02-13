from langchain_community.document_loaders import TextLoader

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

# Text Loader
loader = TextLoader('sample_text.txt', encoding='utf-8')
docs = loader.load()
# print(docs)
# print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)


chain = prompt | model | parser

result = chain.invoke({
    "query": f"Write a summary for the following poem:\n {docs[0].page_content}"
})

print(result)