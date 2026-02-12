from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate
import os 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence

model = ChatOllama(model='gemma3')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Write a LinkedIn post on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Write a post for twitter(X) on {topic}',
    input_variables = {'topic'}
)

parallel_chain = RunnableParallel({
    'linkedin' : RunnableSequence(prompt1, model, parser),
    'tweet': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result)