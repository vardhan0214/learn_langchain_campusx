from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import os 
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen3-Coder-Next",
    task="text-generation",
    max_new_tokens=512,
    do_sample = False,
    provider="auto"
)

model = ChatHuggingFace(llm=llm)
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is missing from your .env file!")

messages = [HumanMessage(content="What is the capital of India?")]
result = model.invoke(messages)

print(result.content)