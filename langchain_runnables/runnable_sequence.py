from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import os 
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence

model = ChatOllama(model = 'gpt-oss')

prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain in simple words what is the following joke: \n {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic': 'AI'}))