from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser



#  Step 1 >> Ask user for a prompt
prompt = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

# Step 2 >> Share this prompt to LLM 
model = ChatOllama(model='llama3')
parser = StrOutputParser()

#  Step 3 >> LLM Response display 
chain = prompt | model | parser 

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()     # visualize chains 