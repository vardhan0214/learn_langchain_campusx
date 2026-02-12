from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda

model = ChatOllama(model= 'gemma3')
parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic']
)

def word_counter(text):
    return len(text.split())

# runnable_word_counter = RunnableLambda(word_counter)

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
print(final_chain.invoke({'topic':'cricket'}))