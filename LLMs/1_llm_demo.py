from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0)

result = llm.invoke("What is the capital of India?")

print(result)


# This is the older version, when LLM's were used, now no one uses LLM's, ChatModels are being used now and recommended
