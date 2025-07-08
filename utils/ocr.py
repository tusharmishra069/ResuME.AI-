import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import io
import PyPDF2
import docx

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text_from_file(uploaded_file):
    file_extension = uploaded_file.name.split(".")[-1].lower()
    
    if file_extension in ["jpg", "jpeg", "png"]:
        image = Image.open(uploaded_file)
        return extract_text_from_image(image)
    
    elif file_extension == "pdf":
        return extract_text_from_pdf(uploaded_file)
    
    elif file_extension == "docx":
        return extract_text_from_docx(uploaded_file)
    
    else:
        return uploaded_file.read().decode("utf-8")

