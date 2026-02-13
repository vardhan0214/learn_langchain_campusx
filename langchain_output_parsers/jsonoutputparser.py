from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(model='llama3')

parser = JsonOutputParser()

template = PromptTemplate(
    template = ' Give me a name , age and city of a charcter from Naruto Shippuden.\n {format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
    
chain = template | model | parser 

result = chain.invoke({})
print(result)