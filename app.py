import streamlit as st
import os
from utils.ocr import extract_text_from_file
from utils.gemini import enhance_resume, analyze_jd, client
from utils.ats import check_ats_score
from utils.latex import generate_latex_resume, generate_text_resume
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(
        page_title="AI Resume Enhancer",
        page_icon="📄",
        layout="wide"
    )
    st.title("AI Resume Enhancement Platform")
    page = st.sidebar.selectbox(
        "Choose a feature",
        ["Resume Enhancer", "ATS Score Checker", "JD-Based Generator"]
    )
    if page == "Resume Enhancer":
        resume_enhancer()
    elif page == "ATS Score Checker":
        ats_checker()
    else:
        jd_generator()

def resume_enhancer():
    st.header(" Resume Uploader & Enhancer")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF or Image)",
        type=["pdf", "png", "jpg", "jpeg"]
    )
    if uploaded_file:
        with st.spinner("Extracting text from your resume..."):
            extracted_text = extract_text_from_file(uploaded_file)
        if extracted_text:
            st.subheader("Extracted Resume Text")
            st.text_area("Extracted Text", extracted_text, height=300)
            if st.button("Enhance Resume"):
                with st.spinner("Enhancing your resume..."):
                    enhanced_resume = enhance_resume(extracted_text)
                    latex_resume = generate_latex_resume(enhanced_resume)
                st.subheader("Enhanced Resume Text")
                st.text_area("Enhanced Resume", enhanced_resume, height=300)
                st.subheader("LaTeX Formatted Resume")
                st.text_area("LaTeX Format", latex_resume, height=300)
                st.download_button(
                    label="Download Enhanced Resume (LaTeX)",
                    data=latex_resume,
                    file_name="enhanced_resume.tex",
                    mime="text/x-tex"
                )

def ats_checker():
    st.header("ATS Score Checker")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF or Image) for ATS check",
        type=["pdf", "png", "jpg", "jpeg"],
        key="ats"
    )
    job_description = st.text_area("Paste the Job Description for ATS analysis", height=150)
    if uploaded_file:
        with st.spinner("Extracting text..."):
            extracted_text = extract_text_from_file(uploaded_file)
        if extracted_text:
            st.subheader("Extracted Resume Text")
            st.text_area("Extracted Text", extracted_text, height=300)
            if st.button("Check ATS Compatibility"):
                if not job_description:
                    st.warning("Please provide a Job Description for ATS analysis.")
                else:
                    with st.spinner("Analyzing resume..."):
                        try:
                            ats_result = check_ats_score(extracted_text, job_description)
                            st.subheader("ATS Score and Suggestions")
                            st.metric("Match Percentage", ats_result["percentage_match"])
                            st.subheader("Missing Keywords")
                            if ats_result["missing_keywords"]:
                                for keyword in ats_result["missing_keywords"]:
                                    st.write(f"• {keyword}")
                            else:
                                st.write("No critical keywords missing")
                            st.subheader("Analysis")
                            st.write(ats_result["final_thoughts"])
                        except Exception as e:
                            st.error(f"Error analyzing resume: {str(e)}")

def jd_generator():
    st.header(" JD-Based Resume Enhancer")
    jd_text = st.text_area("Paste the Job Description here", height=250)
    uploaded_file = st.file_uploader(
        "Upload your existing resume (PDF or Image)",
        type=["pdf", "png", "jpg", "jpeg"],
        key="jd"
    )
    if uploaded_file and jd_text:
        with st.spinner("Extracting resume text..."):
            extracted_text = extract_text_from_file(uploaded_file)
        if extracted_text:
            st.subheader("Extracted Resume Text")
            st.text_area("Extracted Text", extracted_text, height=300)
            if st.button("Enhance Resume for JD"):
                with st.spinner("Enhancing for JD..."):
                    enhanced_resume = enhance_resume(extracted_text, jd_context=jd_text)
                    latex_resume = generate_latex_resume(enhanced_resume)
                st.subheader("Enhanced Resume (Based on JD)")
                st.text_area("Enhanced Resume", enhanced_resume, height=300)
                st.subheader("LaTeX Formatted Resume")
                st.text_area("LaTeX Format", latex_resume, height=300)
                with st.expander("View Key Improvements"):
                    improvement_prompt = f"""
                    Analyze the differences between the original and enhanced resume:
                    Original Resume:
                    {extracted_text}
                    Enhanced Resume:
                    {enhanced_resume}
                    Job Description:
                    {jd_text}
                    List the key improvements made to better match the job description.
                    """
                    improvements = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=[improvement_prompt]
                    ).text
                    st.write(improvements)
                st.download_button(
                    label="Download JD-Tailored Resume (LaTeX)",
                    data=latex_resume,
                    file_name="jd_tailored_resume.tex",
                    mime="text/x-tex"
                )

if __name__ == "__main__":
    main()
