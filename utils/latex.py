def generate_latex_resume(content):
    """
    Generate a professionally formatted LaTeX resume with proper styling and structure.
    """
    latex_template = r"""
    \documentclass[11pt,a4paper]{article}
    
    % Essential packages
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \usepackage{lmodern}
    \usepackage[margin=0.75in]{geometry}
    \usepackage{hyperref}
    \usepackage{fontawesome}
    \usepackage{titlesec}
    \usepackage{enumitem}
    \usepackage{xcolor}
    \usepackage{tabularx}
    \usepackage{ragged2e}
    
    % Custom colors
    \definecolor{primary}{RGB}{0, 79, 159}
    \definecolor{secondary}{RGB}{100, 100, 100}
    
    % Hyperlink styling
    \hypersetup{
        colorlinks=true,
        linkcolor=primary,
        urlcolor=primary
    }
    
    % Custom section styling
    \titleformat{\section}
        {\Large\bfseries\color{primary}}
        {}{0em}
        {}[\titlerule]
    
    % Custom spacing
    \setlength{\parindent}{0pt}
    \setlength{\parskip}{8pt}
    
    % Custom list styling
    \setlist[itemize]{leftmargin=*}
    \setlist[enumerate]{leftmargin=*}
    
    \begin{document}
    
    % Content will be inserted here
    $CONTENT
    
    \end{document}
    """
    
    def clean_content(text):
        """Clean and format the content for LaTeX."""
        text = text.replace('*', '')
        latex_special_chars = {
            '_': r'\_',
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}'
        }
        for char, replacement in latex_special_chars.items():
            text = text.replace(char, replacement)
        text = text.replace('**', r'\textbf{').replace('__', '}')
        text = text.replace('---', r'\hrule')
        return text
    
    formatted_content = clean_content(content)
    return latex_template.replace("$CONTENT", formatted_content)

def generate_text_resume(content):
    """
    Generate a plain text version of the resume with the same structure as the LaTeX resume.
    """
    def clean_content(text):
        """Clean and format the content for plain text."""
        text = text.replace('*', '')
        text = text.replace('**', '').replace('__', '')
        text = text.replace('---', '--------------------')
        return text

    formatted_content = clean_content(content)
    return formatted_content

def format_section(title, content):
    """Helper function to format a resume section."""
    return f"""
    {title.upper()}
    {content}
    """

def format_contact_info(name, email, phone, linkedin):
    """Helper function to format contact information."""
    return f"""
    {name}
    Email: {email}
    Phone: {phone}
    LinkedIn: {linkedin}
    """