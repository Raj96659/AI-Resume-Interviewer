

import os
#from langchain_google_genai import GoogleGenerativeAIEmbeddings
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

def create_vector_db(chunks):
    """
    Creates a temporary in-memory FAISS vector database for the current session.

    Args:
        chunks (List[str]): List of text chunks from resume

    Returns:
        retriever: LangChain retriever for performing similarity search
        vector_db: The FAISS vector store object (stored in session)
    """

    # Initialize HuggingFace Embeddings
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


    # Create FAISS vector store
    vector_db = FAISS.from_texts(chunks, embedding=embeddings)

    # Convert to retriever
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}   # return top 3 most relevant chunks
    )

    return retriever, vector_db
