import pytesseract
from PIL import Image
import PyPDF2

def extract_text_from_image(image_path: str) -> str:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
    img = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text

def extract_text_from_pdf(pdf: str) -> str:
    text = ""
    with open(f'{pdf}','rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text
