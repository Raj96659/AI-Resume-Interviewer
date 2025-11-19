import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.utils.prompts import evaluation_prompt

load_dotenv()

def clean_json_response(text: str) -> str:
    """Remove markdown code blocks from Gemini response."""
    text = text.strip()
    
    # Build the marker character by character (backtick = chr(96))
    marker = chr(96) + chr(96) + chr(96)  # This is ```
    
    if text.startswith(marker):
        lines = text.split('\n')
        lines = lines[1:] if len(lines) > 1 else lines
        if lines and lines[-1].strip() == marker:
            lines = lines[:-1]
        text = '\n'.join(lines)
    
    return text.strip()




def evaluate_answer(context, question, user_answer):
    """
    Evaluates the user's interview answer using Gemini.
    
    Inputs:
        context (str): Retrieved resume-based context (RAG)
        question (str): The interview question asked
        user_answer (str): Candidate's response
        
    Returns:
        dict: {
            "score": int (0–10),
            "reason": "Explanation for score",
            "improvement": "Suggestions for better answer",
            "resume_alignment": "How well answer matches resume"
        }
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GEMINI_API_KEY")  # FIXED: Use GOOGLE_API_KEY
    )

    # Create the evaluation prompt
    prompt = evaluation_prompt.format(
        context=context,
        question=question,
        answer=user_answer
    )

    response = llm.invoke(prompt)

    # Parse response - FIXED: strip markdown code blocks
    try:
        data = response.content.strip()
        data = clean_json_response(data)  # Remove markdown if present
        
        print(f"\n=== CLEANED JSON ===\n{data}\n====================\n")
        
    except Exception as e:
        print(f"Error getting response content: {e}")
        return {
            "score": 0,
            "reason": "Evaluation failed",
            "improvement": "Please answer again.",
            "resume_alignment": "Unknown"
        }

    # Parse JSON output from Gemini
    import json
    try:
        result = json.loads(data)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Raw response: {data}")
        # fallback if parsing fails
        result = {
            "score": 0,
            "reason": "Could not parse evaluation",
            "improvement": "Try giving a clearer answer.",
            "resume_alignment": "Unknown"
        }

    return result
