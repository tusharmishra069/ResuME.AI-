from google import genai
import os
import base64
import io
from pdf2image import convert_from_bytes
from dotenv import load_dotenv


client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

def get_gemini_response(input_prompt, pdf_content, job_description):
    """
    Sends the input, PDF content, and job description to the Gemini model and retrieves the response.

    Args:
        input_prompt (str): The prompt to guide the AI model.
        pdf_content (str): The processed PDF content as a base64-encoded string.
        job_description (str): The job description text.

    Returns:
        str: The AI model's response.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[input_prompt, pdf_content, job_description]
        )
        return response.text
    except Exception as e:
        print(f"Error during AI model call: {e}")
        return "Error: Unable to process the request with the AI model."

def input_pdf_setup(uploaded_file):
    """
    Processes the uploaded PDF file and converts it to a base64-encoded string.

    Args:
        uploaded_file (UploadedFile): The uploaded PDF file.

    Returns:
        str: The processed PDF content as a base64-encoded string.
    """
    if uploaded_file is not None:
        try: 
            images = convert_from_bytes(uploaded_file.read())
            first_page = images[0]
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format="JPEG")
            img_byte_arr = img_byte_arr.getvalue()

            # Encode the image in base64 and return as a string
            return base64.b64encode(img_byte_arr).decode()
        except Exception as e:
            print(f"Error processing PDF file: {e}")
            raise ValueError("Error processing the uploaded PDF file.")
    else:
        raise FileNotFoundError("No file uploaded.")

def check_ats_score(resume_text, job_description):
    """
    Evaluates the ATS compatibility of a resume based on a job description.
    
    Args:
        resume_text (str): The text content of the resume
        job_description (str): The job description text
        
    Returns:
        dict: A dictionary containing percentage match, missing keywords, and final thoughts
    """
    # Create a clear prompt to get structured output
    prompt = """
    You are an expert ATS (Applicant Tracking System) analyzer. Evaluate the resume against this job description.
    
    Provide your response in the following format:
    Percentage Match: [number]%
    
    Missing Keywords:
    - [keyword 1]
    - [keyword 2]
    (or "No critical keywords missing" if none)
    
    Final Thoughts:
    [Your detailed analysis of the resume's compatibility with the job description]
    
    Resume:
    {}
    
    Job Description:
    {}
    """.format(resume_text, job_description)
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt]
        )
        
        result_text = response.text
        
        ats_result = {
            "percentage_match": "0%",
            "missing_keywords": [],
            "final_thoughts": "Unable to analyze the resume."
        }
      
        if result_text and "Percentage Match:" in result_text:
            match_line = [line for line in result_text.split('\n') if "Percentage Match:" in line][0]
            ats_result["percentage_match"] = match_line.split("Percentage Match:")[1].strip()

        missing_keywords = []
        keyword_section = False
        thoughts_section = False
        
        final_thoughts_lines = []
        
        if result_text is None:
            raise ValueError("The AI model returned no response.")
        
        for line in result_text.split('\n'):
            line = line.strip()
 
            if not line:
                continue
 
            if "Missing Keywords:" in line:
                keyword_section = True
                thoughts_section = False
                continue
            elif "Final Thoughts:" in line:
                keyword_section = False
                thoughts_section = True
                continue

            if keyword_section:
                if line.startswith("- "):
                    missing_keywords.append(line[2:])
                elif line == "No critical keywords missing":
                    pass
            elif thoughts_section:
                final_thoughts_lines.append(line)
        
        # Update the result dictionary
        if missing_keywords:
            ats_result["missing_keywords"] = missing_keywords
        
        if final_thoughts_lines:
            ats_result["final_thoughts"] = " ".join(final_thoughts_lines)
        
        return ats_result
        
    except Exception as e:
        print(f"Error in ATS analysis: {e}")
        return {
            "percentage_match": "0%",
            "missing_keywords": [],
            "final_thoughts": f"Error analyzing resume: {str(e)}"
        }