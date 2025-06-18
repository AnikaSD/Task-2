from PIL import Image
import pytesseract
from pdf2image import convert_from_path

pdf_file_path=r'C:\Users\anika\Downloads\Meeting of the Senate_1st to 5th_196808-196307.pdf'
pages=convert_from_path(pdf_file_path)

def text_from_image(image):
    text=pytesseract.image_to_string(image)
    return text

extracted_text=""

for page in pages:
    text=text_from_image(page)
    extracted_text=extracted_text+"\n"+text

print(extracted_text)

