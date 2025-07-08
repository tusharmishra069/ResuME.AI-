# AI Resume Enhancement Platform

A modern, AI-powered web application for enhancing resumes, checking ATS (Applicant Tracking System) compatibility, and tailoring resumes to job descriptions. Built with Streamlit and Google Gemini AI, this platform helps users create professional, ATS-optimized resumes with ease.

---

## Features

- **Resume Enhancement**: Upload your resume (PDF or image), extract its content, and enhance it using AI for professional language and ATS optimization.
- **ATS Score Checker**: Analyze your resume against a job description to get an ATS match score, missing keywords, and actionable suggestions.
- **JD-Based Resume Generator**: Tailor your resume to a specific job description, with AI-driven improvements and LaTeX export.
- **LaTeX Export**: Download your enhanced or tailored resume in LaTeX format for high-quality typesetting.

---

## Demo

### Resume Enhancement Interface
![Resume Enhancement](ss/Screenshot%202025-07-09%20013940.png)

### ATS Score Checker
![ATS Score Checker](ss/Screenshot%202025-07-09%20014213.png)

### JD-Based Resume Generator
![JD-Based Resume Generator](ss/Screenshot%202025-07-09%20014244.png)

---

## Getting Started

### Prerequisites
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-resume-enhancer.git
   cd ai-resume-enhancer
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your Google Gemini API key:**
   - Obtain an API key from Google Gemini/Generative AI.
   - Set it as an environment variable:
     ```bash
     # On Windows (PowerShell)
     $env:GOOGLE_API_KEY="your_actual_google_api_key_here"
     # On Mac/Linux
     export GOOGLE_API_KEY=your_actual_google_api_key_here
     ```
   - Or create a `.env` file in the project root:
     ```env
     GOOGLE_API_KEY=your_actual_google_api_key_here
     ```

---

## Usage

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
2. **Open your browser** and go to the local URL provided (usually http://localhost:8501).
3. **Choose a feature** from the sidebar:
   - Resume Enhancer
   - ATS Score Checker
   - JD-Based Generator
4. **Upload your resume** and/or job description as prompted.
5. **Download your enhanced or tailored resume** in LaTeX format if desired.

---

## Project Structure

```
resume-1.2/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .gitignore
├── Readme.md             # Project documentation
├── utils/
│   ├── ocr.py            # OCR and text extraction utilities
│   ├── gemini.py         # Google Gemini AI integration
│   ├── ats.py            # ATS scoring and keyword analysis
│   └── latex.py          # LaTeX resume generation
└── venv/                 # Python virtual environment (not tracked)
```

---

## Key Technologies
- **Streamlit**: Rapid web app development
- **Google Gemini AI**: Resume enhancement and content generation
- **OCR**: Extracts text from PDF and image resumes
- **LaTeX**: High-quality resume export

---

## How It Works

- **Resume Upload**: Users upload a resume (PDF/image). Text is extracted using OCR.
- **Enhancement**: The extracted text is sent to Google Gemini AI for professional, ATS-optimized rewriting.
- **ATS Check**: The resume is compared to a job description, and the app highlights missing keywords and provides a match score.
- **JD Tailoring**: The resume is further enhanced to match a specific job description.
- **Export**: Users can download the improved resume in LaTeX format.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Google Gemini AI](https://ai.google.dev/)
- [spaCy](https://spacy.io/)
- [LaTeX](https://www.latex-project.org/)

---

## Contact

For questions, suggestions, or support, please open an issue or contact the maintainer at [your.email@example.com](mailto:your.email@example.com).

