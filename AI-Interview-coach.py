import streamlit as st
from utils import (
    extract_text_from_pdf,
    analyze_resume,
    generate_interview_questions,
    generate_cover_letter,
)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🤖 AI Interview Coach")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Resume Analysis",
        "Mock Interview",
        "Cover Letter",
        "About"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------
if page == "Dashboard":

    st.title("🤖 AI Interview Coach")
    st.write("Welcome! This AI application will help you prepare for interviews.")

    col1, col2 = st.columns(2)

    with col1:
        resume = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"]
        )

    with col2:
        job_description = st.text_area(
            "Paste Job Description",
            height=250
        )

    if st.button("🚀 Analyze Resume", use_container_width=True):

        if resume is None:
            st.warning("Please upload your resume.")

        elif job_description.strip() == "":
            st.warning("Please paste the Job Description.")

        else:

            with st.spinner("Analyzing Resume..."):

                resume_text = extract_text_from_pdf(resume)

                result = analyze_resume(
                    resume_text,
                    job_description
                )

            st.success("✅ Analysis Completed!")
            st.markdown("## 📊 Resume Analysis")
            st.write(result)

# -----------------------------
# Resume Analysis
# -----------------------------
elif page == "Resume Analysis":

    st.title("📄 Resume Analysis")
    st.info("Please use the Dashboard to analyze your resume.")

# -----------------------------
# Mock Interview
# -----------------------------
elif page == "Mock Interview":

    st.title("🎤 AI Mock Interview")

    job_description = st.text_area(
        "Paste Job Description",
        height=250,
        key="interview_jd"
    )

    if st.button(
        "🎯 Generate Interview Questions",
        key="generate_interview_btn"
    ):

        if job_description.strip() == "":
            st.warning("Please paste the Job Description.")

        else:

            with st.spinner("Generating Interview Questions..."):

                try:

                    questions = generate_interview_questions(
                        job_description
                    )

                    st.success("✅ Interview Questions Generated!")

                    st.markdown("## 🎤 Interview Questions")
                    st.markdown(questions)

                except Exception as e:

                    st.error(f"❌ Error: {e}")

# -----------------------------
# Cover Letter
# -----------------------------
elif page == "Cover Letter":

    st.title("📝 AI Cover Letter Generator")

    resume = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        key="cover_resume"
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=250,
        key="cover_jd"
    )

    if st.button(
        "📝 Generate Cover Letter",
        key="generate_cover_letter_btn"
    ):

        if resume is None:
            st.warning("Please upload your resume.")

        elif job_description.strip() == "":
            st.warning("Please paste the Job Description.")

        else:

            with st.spinner("Generating Cover Letter..."):

                try:

                    resume_text = extract_text_from_pdf(resume)

                    cover_letter = generate_cover_letter(
                        resume_text,
                        job_description
                    )

                    st.success("✅ Cover Letter Generated!")

                    st.markdown("## 📄 Cover Letter")
                    st.markdown(cover_letter)

                except Exception as e:

                    st.error(f"❌ Error: {e}")

# -----------------------------
# About
# -----------------------------
elif page == "About":

    st.title("ℹ️ About")

    st.write("""
This project is built using:

- Streamlit
- Google Gemini AI
- PyPDF
- Python

Developed by Shahzaib Ali
""")