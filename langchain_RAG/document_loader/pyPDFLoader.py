from langchain_ollama import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader

model = ChatOllama(model='llama3', temperature=0)

parser = StrOutputParser()

loader = PyPDFLoader('Coding Ninjas_Admission Counsellor.pdf')
docs = loader.load()
print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)