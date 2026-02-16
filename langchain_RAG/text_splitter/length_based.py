from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:\\Users\\hs901\\Desktop\\langchain_practice_and_learning\\youtube channel\\campusx\\langchain_RAG\\document_loader\\books\\_OceanofPDF.com_learning_langchain_-_mayo_oshin.pdf')

docs = loader.load()

# text = """
# LangChain's text splitters are components designed to break large documents into smaller, manageable chunks that fit within the context windows of large language models (LLMs). This process, often called chunking, is crucial for maintaining semantic meaning, improving retrieval accuracy in Retrieval-Augmented Generation (RAG) systems, and managing processing costs and constraints. 
# LangChain's text splitters are components designed to break large documents into smaller, manageable chunks that fit within the context windows of large language models (LLMs). This process, often called chunking, is crucial for maintaining semantic meaning, improving retrieval accuracy in Retrieval-Augmented Generation (RAG) systems, and managing processing costs and constraints. 
# LangChain's text splitters are components designed to break large documents into smaller, manageable chunks that fit within the context windows of large language models (LLMs). This process, often called chunking, is crucial for maintaining semantic meaning, improving retrieval accuracy in Retrieval-Augmented Generation (RAG) systems, and managing processing costs and constraints. 
# """

splitter = CharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 0,
    separator=''
)

# result = splitter.split_text(text)

result = splitter.split_documents(docs)

print(result[0].page_content)

