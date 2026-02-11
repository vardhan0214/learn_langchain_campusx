from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel 

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate important short and simple notes from the following text: \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Generate a 5 questions quiz on the following text: \n {text}',
    input_variables = ['text']
)

prompt4 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables = ['notes', 'quiz']
)

model1 = ChatOllama(model='gemma3')
model2 = ChatOllama(model='llama3')

parser = StrOutputParser()

text_chain = prompt1 | model1 | parser 

parallel_chain =  RunnableParallel({
    'notes': prompt2 | model1 | parser,
    'quiz' : prompt3 | model2 | parser
})

merge_chain = prompt4 | model1 | parser

chain = text_chain |parallel_chain | merge_chain

result = chain.invoke({'topic': 'Generative AI'})

print(result)

chain.get_graph().print_ascii()     # visualize chains