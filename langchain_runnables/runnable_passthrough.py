from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel

model = ChatOllama(model='gemma3')
parser = StrOutputParser()

# passthrough = RunnablePassthrough()
# print(passthrough.invoke(2))

prompt1 = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Write a short exlanation of the following joke: \n {topic}',
    input_variables = ['topic']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic': 'cricket'}))