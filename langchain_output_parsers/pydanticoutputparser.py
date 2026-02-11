from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 

model = ChatOllama(model='llama3')

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='City of the person')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Give me a name , age and city of a charcter from Naruto Shippuden.\n{format_instructions}',
    input_variables = [],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({})


print(result)