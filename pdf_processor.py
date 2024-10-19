# 2. Handles PDF processing
import PyPDF2
from io import BytesIO
from utils import calculate_word_lengths


async def process_pdf(file):
    # Read the uploaded PDF
    pdf_reader = PyPDF2.PdfReader(BytesIO(await file.read()))

    # Extract text from the first page
    if len(pdf_reader.pages) > 0:
        first_page = pdf_reader.pages[0]
        text = first_page.extract_text()

        if text:
            word_lengths = calculate_word_lengths(text)
            return word_lengths
        else:
            raise Exception("No text found on the first page.")
    else:
        raise Exception("Empty PDF.")
