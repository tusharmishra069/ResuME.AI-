# utils/gemini.py
from google import genai
import os

# Configure the client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def enhance_resume(text, jd_context=None):
    prompt = f"""
    Improve this resume text with these rules:
    - Keep similar length and format
    - Use professional, ATS-optimized language
    - Do NOT add explanations or improvement notes
    - Output only the improved resume content

    Resume Content:
    {text}

    {"Job Description Context:\n" + jd_context if jd_context else ""}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    return response.text

def analyze_jd(jd_text):
    prompt = f"""
    Extract only important points from this Job Description:
    - Key skills
    - Qualifications
    - Responsibilities
    - Industry keywords
    Output only the list, no extra explanation.

    Job Description:
    {jd_text}
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    return response.text
