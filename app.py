import streamlit as st
from dotenv import load_dotenv
import os

# Import our custom modules
from src.pdf_parser import extract_text_from_pdf
from src.text_splitter import chunk_text
from src.rag_builder import create_vector_db
from src.interview_agent import ask_question
from src.evaluator import evaluate_answer

load_dotenv()

# -------------------------
# COOL MODERN UI STYLING
# -------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Animated gradient background */
    .main {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Title animation */
    h1 {
        color: white !important;
        font-size: 3.5rem !important;
        font-weight: 700 !important;
        text-align: center;
        text-shadow: 0 0 20px rgba(0,0,0,0.3);
        animation: fadeInDown 0.8s ease-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Subtitle */
    .subtitle {
        color: white;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 400;
        margin-bottom: 2rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Glass card effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin: 1.5rem 0;
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* White content card */
    .content-card {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        margin: 1.5rem 0;
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Section headers */
    h2, h3 {
        color: white !important;
        font-weight: 600 !important;
    }
    
    .content-card h3 {
        color: #e73c7e !important;
        border-bottom: 3px solid #e73c7e;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    /* Question card - cool gradient */
    .question-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        font-size: 1.2rem;
        font-weight: 500;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        margin: 1.5rem 0;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    /* Score card - neon effect */
    .score-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 0 40px rgba(245, 87, 108, 0.6);
        margin: 1.5rem 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .score-box .score-number {
        font-size: 4rem;
        font-weight: 700;
        text-shadow: 0 0 20px rgba(255,255,255,0.5);
    }
    
    /* Buttons - modern style */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.8rem 2.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* File uploader - glass effect */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        border: 2px dashed #667eea;
    }
    
    /* Fix uploaded file name visibility */
    [data-testid="stFileUploader"] section small {
        color: #1f2937 !important;
    }

    
    /* Text area - modern style */
    .stTextArea textarea {
        border: 2px solid #e73c7e;
        border-radius: 15px;
        padding: 1rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
    }
    
    /* Success/Info boxes */
    .stSuccess, .stInfo {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px !important;
        border-left: 5px solid #23d5ab !important;
        color: #065f46 !important;
    }
    
    .stInfo {
        border-left-color: #3b82f6 !important;
        color: #1e3a8a !important;
    }
    
    /* Feedback sections */
    .feedback-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
    
    .feedback-title {
        color: #667eea;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border-radius: 10px;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
        margin: 2rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: white;
        font-size: 1rem;
        padding: 2rem;
        margin-top: 3rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
</style>
""", unsafe_allow_html=True)

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="AI Resume Interviewer",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# HEADER
# -------------------------
st.markdown("# 🤖 AI Resume Interviewer")
st.markdown('<p class="subtitle">✨ Practice tailored interview questions powered by AI ✨</p>', unsafe_allow_html=True)

# -------------------------
# SESSION STATE
# -------------------------
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "current_question" not in st.session_state:
    st.session_state.current_question = ""
if "context" not in st.session_state:
    st.session_state.context = ""

# -------------------------
# UPLOAD SECTION
# -------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 📄 Upload Your Resume")
uploaded_file = st.file_uploader("Drag and drop or browse", type=["pdf"], label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    with st.spinner("🔄 Processing your resume..."):
        text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(text)
        retriever, vector_db = create_vector_db(chunks)
        
        st.session_state.vector_db = vector_db
        st.session_state.retriever = retriever
    
    st.success("✅ Resume processed successfully! Ready to start.")

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------
# QUESTION GENERATION
# -------------------------
if st.session_state.retriever:
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.button("🎯 Generate Interview Question"):
            with st.spinner("🤔 Generating question..."):
                question, context = ask_question(st.session_state.retriever)
                st.session_state.current_question = question
                st.session_state.context = context

# -------------------------
# QUESTION & ANSWER
# -------------------------
    if st.session_state.current_question:
        
        st.markdown(f"""
        <div class="question-box">
            <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.8rem;">❓ Interview Question</div>
            <div style="font-size: 1.3rem; line-height: 1.6;">{st.session_state.current_question}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("### ✏️ Your Answer")
        user_ans = st.text_area("Type your answer here...", height=200, label_visibility="collapsed")
        
        col_a, col_b, col_c = st.columns([1, 2, 1])
        with col_b:
            if st.button("📊 Evaluate My Answer"):
                if len(user_ans.strip()) < 5:
                    st.warning("⚠️ Please provide a meaningful answer")
                else:
                    with st.spinner("🔍 Analyzing your answer..."):
                        result = evaluate_answer(
                            context=st.session_state.context,
                            question=st.session_state.current_question,
                            user_answer=user_ans
                        )
                    
                    st.markdown("<hr>", unsafe_allow_html=True)
                    
                    # Score display
                    st.markdown(f"""
                    <div class="score-box">
                        <div class="score-number">{result.get("score", 0)}<span style="font-size: 2rem;">/10</span></div>
                        <div style="font-size: 1.2rem; margin-top: 0.5rem;">Your Score</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Feedback
                    with st.expander("📝 Detailed Reasoning", expanded=True):
                        st.write(result.get("reason", "No feedback"))
                    
                    with st.expander("🎯 Resume Alignment", expanded=True):
                        st.write(result.get("resume_alignment", "No info"))
                    
                    with st.expander("🔧 Improvement Suggestions", expanded=True):
                        st.write(result.get("improvement", "No suggestions"))
        
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    Made by Raj • Powered by Gemini 2.5 Flash
</div>
""", unsafe_allow_html=True)
