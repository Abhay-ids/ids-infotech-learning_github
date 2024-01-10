
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import json
import os

# Set the Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf_with_images(pdf_file, output_json_file):
    # List to store extracted text organized by trademark
    trademarks_data = []

    # Open the PDF file using PyMuPDF
    pdf_document = fitz.open(pdf_file)

    # Extract text starting from page 4
    for page_num in range(3, pdf_document.page_count):
        # Load the current page
        page = pdf_document.load_page(page_num)

        # Convert the page to a Pixmap
        pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        # Save the Pixmap as a PNG image
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Perform OCR on the image and extract text
        ocr_text = pytesseract.image_to_string(image)

        # Split the text based on newline character
        lines = ocr_text.split('\n')

        # Organize the extracted text into a list with appropriate keys
        current_trademark_data = {"lines": []}

        for line in lines:
            if line.startswith("E-01"):
                # Start a new section with the key "R-01"
                current_trademark_data = {"lines": [line]}
            elif line.startswith("E-") and not line.startswith("E-17"):
                # Append lines to the current section for each occurrence of "R-01" to "R-16"
                current_trademark_data["lines"].append(line)

        # Add the current trademark data to the list
        if current_trademark_data["lines"]:
            trademarks_data.append(current_trademark_data)

    # Save the extracted data to a JSON file
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(trademarks_data, json_file, indent=2, ensure_ascii=False)

# Example usage
pdf_file_path = "AW20221016-10.pdf"
output_json_file_path = "output.json"
extract_text_from_pdf_with_images(pdf_file_path, output_json_file_path)
