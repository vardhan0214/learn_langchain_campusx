from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.2, max_completion_tokens = 10 )

result = model.invoke("What is the capital of India?")

# print(result)
print(result.content)


# Roughly for now tokens are equal to words 
#  More on this later 
# max_completion_tokens is very important when working with a paid model 
