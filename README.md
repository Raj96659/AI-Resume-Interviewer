# 🤖 AI Resume Interviewer (RAG + Gemini + LangChain)

An AI-powered interviewer that reads your resume, generates personalized interview questions based on your own projects/skills, evaluates your answers, and gives actionable improvement suggestions.

This project uses **RAG (Retrieval-Augmented Generation)** + **Gemini LLM** to ensure that:
- Questions come ONLY from your resume  
- No hallucinations  
- Accurate evaluation  
- Real interview-like experience  

Perfect for:
- Interview preparation  
- Self-assessment of resume projects  
- HR-tech and AI product portfolios  
- GenAI, RAG, LangChain learning  

---

# 🚀 Features

### ✅ Upload Resume (PDF)
Extracts and cleans the text automatically.

### ✅ Smart Chunking
Splits resume into meaningful sections for RAG.

### ✅ Temporary Vector Store (Per Session)
Creates a fresh FAISS index for each session.  
No data is saved → privacy-safe.

### ✅ RAG-Powered Interview Questions
AI asks relevant questions based ONLY on your resume.

### ✅ Scoring System (0–10)
Evaluates:
- Accuracy  
- Depth  
- Alignment with resume  

### ✅ Improvement Suggestions
AI tells you exactly how to improve your answers.

### ✅ Clean & Simple Streamlit UI
End-to-end workflow for practice and learning.

---

# 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| LLM | Google Gemini 1.5 |
| RAG Framework | LangChain |
| Embeddings | Gemini Embeddings |
| Vector Database | FAISS (in-memory) |
| PDF Parsing | PyPDF2 |
| Environment | venv + .env |
| Deployment | Streamlit Cloud / HuggingFace |

---

# 📁 Project Structure

