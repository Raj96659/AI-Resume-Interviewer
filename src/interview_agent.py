# src/interview_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.utils.prompts import question_prompt

load_dotenv()

def ask_question(retriever):
    """
    Generates a resume-based interview question using RAG and Gemini.

    Args:
        retriever: LangChain retriever (FAISS-based)

    Returns:
        question (str): Generated interview question
        context (str): Retrieved resume text used to form the question
    """

    # Query retriever to get relevant text
    # Query is generic because we want a random meaningful chunk
    docs = retriever.invoke("generate interview question")


    # Combine retrieved chunks into a single context string
    context = "\n".join([d.page_content for d in docs])

    # Prepare LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.3,   # Slight randomness for variety
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    # Fill prompt
    prompt = question_prompt.format(context=context)

    # Call LLM
    response = llm.invoke(prompt)

    # Extract question text
    try:
        question = response.content.strip()  # Modern LangChain format
    except Exception as e:
        print(f"Error extracting question: {e}")
        question = "Could not generate question. Please try again."
    
    return question, context
