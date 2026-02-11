from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_output_parsers import structuredoutputparser, ResponseSchema

StructuredOutputParser = structuredoutputparser.StructuredOutputParser

model = ChatOllama(model='llama3')

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 3 facts about {topic}.\n{format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'black hole'})
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

final_result = chain.invoke({'topic': 'black hole'})


print(final_result)
