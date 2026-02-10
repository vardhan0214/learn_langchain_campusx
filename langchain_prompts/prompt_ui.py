import streamlit as st
# from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv

load_dotenv()


# llm = HuggingFacePipeline.from_model_id(
#     model_id = "meta-llama/Llama-3.1-8B-Instruct",
#     task = "text-generation",
#     pipeline_kwargs = dict(
#         temperature = 0.5,
#         max_new_tokens = 100
#     )
# )

# model = ChatHuggingFace(llm = llm)

model = ChatOllama(model = "llama2", temperature=0.2)


paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

st.header('Research Tool')

# Template
template = load_prompt('template.json')


# Fill the place holders
# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

# user_input = st.text_input('Enter your Prompt')

if st.button('Summarize'):
    # result = model.invoke(prompt)
    # st.write(result.content)


    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)