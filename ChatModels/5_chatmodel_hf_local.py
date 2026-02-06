from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os 
from langchain_core.messages import HumanMessage

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation',
    pipeline_kwargs = dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
message = [HumanMessage(content="What is the Capital of India?")]
result = model.invoke(message)

print(result.content)