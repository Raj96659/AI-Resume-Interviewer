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

```
ai_resume_interviewer/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
├── README.md                   # Documentation
│
├── data/
│   └── sample_resumes/        # Sample PDFs for testing
│
├── src/
│   ├── __init__.py
│   ├── pdf_parser.py          # PDF text extraction
│   ├── text_splitter.py       # Text chunking
│   ├── rag_builder.py         # FAISS vector database
│   ├── interview_agent.py     # Question generation
│   ├── evaluator.py           # Answer evaluation
│   │
│   └── utils/
│       ├── __init__.py
│       ├── cleaning.py        # Text preprocessing
│       ├── prompts.py         # Prompt templates
│       └── session_handler.py # Session state
│
└── static/
    └── style.css              # Custom styling
```
# 🧪 How It Works (Architecture)

```
User uploads PDF
        │
        ▼
PDF Parser → Extracts & cleans text
        │
        ▼
Text Splitter → Creates semantic chunks
        │
        ▼
RAG Builder → Embeddings + FAISS Vector DB (session-based)
        │
        ▼
Interview Agent → Generates resume-based questions
        │
        ▼
User Answers
        │
        ▼
Evaluator → Scores answers + gives improvement tips

Privacy-first:
✔ Every session creates a new FAISS DB
✔ Nothing saved after refresh
```
# 🎥 Demo Screenshot

### Application Interface
![App Interface](https://github.com/Raj96659/AI-Resume-Interviewer/blob/main/Screenshoots/1.png)

### Question Generation
![Question Generation](https://github.com/Raj96659/AI-Resume-Interviewer/blob/main/Screenshoots/2.png)

### Evaluation Results
![Evaluation Results](https://github.com/Raj96659/AI-Resume-Interviewer/blob/main/Screenshoots/3.png)

### LLM Suggestions
![Demo](./screenshots/demo.gif)

# 💡 Why This Project Is Unique
```
Most ML/AI interview tools ask generic questions.
This one interviews you strictly on your own resume — a real HR-tech use case.

Hiring managers love candidates who:

Build useful AI tools

Understand RAG properly

Can deploy real applications

Demonstrate end-to-end GenAI skills

This is a high-impact portfolio project.
```
