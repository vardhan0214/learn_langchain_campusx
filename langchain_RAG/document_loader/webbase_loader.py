from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama 
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model='llama3')

parser = StrOutputParser()

url = 'https://www.freecodecamp.org/news/the-difference-between-a-framework-and-a-library-bd133054023f/'
loader = WebBaseLoader(url)
docs = loader.load()
# print(docs[0].page_content)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional AI Engineer having 15+ years of experience. Use only the provided context."),
    ("human", "Context: {context} \n\n Question:{query}")
])

chain = prompt | model | parser

result = chain.invoke({
    "context": docs[0].page_content,
    "query":"What is this text mainly talking about, and what are the key concepts?"
})

print(result)