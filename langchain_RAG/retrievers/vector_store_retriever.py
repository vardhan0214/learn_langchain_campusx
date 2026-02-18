from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# Step 1: Your Source documents
documents = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models. ")
] 

# Step2 : Initialize Embedding model
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")

# Step3 : Create Chroma vector store in memory
vector_store = Chroma.from_documents(
    documents = documents,
    embedding = embedding_model,
    collection_name = "my_collection"
)

# Step 4: Convert vectorstore into a retriever
retriever = vector_store.as_retriever(search_kwargs={"k":2})

query = "What is Chroma used for?"
results = retriever.invoke( query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1}--- ")
    print(doc.page_content)