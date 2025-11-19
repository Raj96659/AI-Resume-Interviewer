import PyPDF2
from src.utils.cleaning import clean_text

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from uploaded PDF file.

    Args:
        pdf_file: Uploaded PDF file from Streamlit (BytesIO object)

    Returns:
        str: Cleaned text extracted from the PDF.
    """

    reader = PyPDF2.PdfReader(pdf_file)
    raw_text = ""

    # Loop through each page and extract text
    for page in reader.pages:
        text = page.extract_text()
        if text:
            raw_text += text + "\n"

    # Clean unwanted spacing, newlines, symbols etc.
    cleaned = clean_text(raw_text)

    return cleaned
