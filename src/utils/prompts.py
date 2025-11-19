# src/utils/prompts.py

# ========================================
# 1. QUESTION GENERATION PROMPT (RAG-based)
# ========================================
question_prompt = """
You are an AI Interviewer.

Using ONLY the following resume context:
{context}

Your task:
- Ask ONE interview question.
- The question must be directly based on the resume content.
- NO generic ML/AI questions.
- NO hallucinations.
- Avoid overly complex or irrelevant questions.

Return ONLY the question text. Do not include explanations.
"""


# ========================================
# 2. ANSWER EVALUATION + SCORING PROMPT
# ========================================
evaluation_prompt = """
You are an expert technical interviewer and evaluator.

Evaluate the candidate's answer using ONLY this resume-based context:
{context}

Question asked:
{question}

Candidate's answer:
{answer}

Now evaluate based on three criteria:
1. Accuracy (0–4)
2. Depth (0–3)
3. Resume alignment (0–3)

Rules:
- Be strict but fair.
- Penalize incorrect or vague explanations.
- Reward clarity, correctness, alignment with resume.

Return STRICT JSON in this format:

{{
 "score": <0-10 integer>,
 "reason": "<why this score was given>",
 "resume_alignment": "<how answer matches resume context>",
 "improvement": "<specific improvements to enhance answer>"
}}

DO NOT include any text outside the JSON.
"""


# ========================================
# 3. RESUME IMPROVEMENT SUGGESTION PROMPT
# ========================================
resume_improve_prompt = """
Using ONLY this resume context:
{context}

Provide improvement suggestions:
- Missing technical details
- Metrics to add (accuracy %, speed, improvements)
- Better project explanation lines
- Tools/tech that should be highlighted

Return clear bullet points.
"""
