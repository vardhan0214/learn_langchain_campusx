from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Write a 5 pointer summary on the most important points in the following text: \n {text}',
    input_variables=['text']
)

model = ChatOllama(model='gemma3')

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 

result = chain.invoke({'topic' : 'cricket'})

print(result)

chain.get_graph().print_ascii()     # visualize chains