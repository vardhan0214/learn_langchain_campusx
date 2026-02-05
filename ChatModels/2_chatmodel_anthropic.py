from langchain_anthropic import ChatAnthropic 
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'Claude2', temperature=0.0, max_tokens = 10)

result = model.invoke("What is the capital of India?")

print(result.content)


#  In Claude instead of max_completion_tokens there is max_tokens
