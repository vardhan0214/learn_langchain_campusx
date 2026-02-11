from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatOllama(model='llama3')

# 1st Prompt >> detailed report 
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic']
)

#  2nd Prompt >> 5 line summary
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text:/n {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)