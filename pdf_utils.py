import pdfplumber

def is_pdf(input_data):
    # Accepts a file path or file-like object
    if isinstance(input_data, str) and input_data.lower().endswith('.pdf'):
        return True
    return False

def extract_pdf_text(pdf_path: str) -> str:
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() or '' for page in pdf.pages)
        return text
    except Exception as e:
        return f"[PDF extraction error: {e}]"
