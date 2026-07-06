import os
from dotenv import load_dotenv
from pypdf import PdfReader
import google.generativeai as genai

# ---------------------------------
# Load Environment Variables
# ---------------------------------
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


# ---------------------------------
# Extract Text from Resume PDF
# ---------------------------------
def extract_text_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# ---------------------------------
# Resume Analysis
# ---------------------------------
def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an Expert ATS Resume Reviewer.

Analyze the following resume according to the given Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:

1. Resume Summary

2. ATS Score (/100)

3. Skills Match

4. Missing Skills

5. Strengths

6. Weaknesses

7. Suggestions to Improve Resume

Give the answer in a professional format.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"


# ---------------------------------
# Mock Interview Questions
# ---------------------------------
def generate_interview_questions(job_description):

    prompt = f"""
You are a Senior Technical Interviewer.

Based on the Job Description below, generate:

• 5 HR Interview Questions

• 5 Technical Interview Questions

Job Description:

{job_description}

Format:

## HR Questions

1.
2.
3.
4.
5.

## Technical Questions

1.
2.
3.
4.
5.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"


# ---------------------------------
# Cover Letter Generator
# ---------------------------------
def generate_cover_letter(resume_text, job_description):

    prompt = f"""
You are a professional career coach.

Write a professional and personalized cover letter based on the candidate's resume and the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

Requirements:
- Professional tone
- Around 300-400 words
- Highlight relevant skills and experience
- Explain why the candidate is a strong fit
- End with a professional closing paragraph.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"