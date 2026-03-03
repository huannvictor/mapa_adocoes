import pdfplumber
import sys
import os

def debug_pdf_text(file_path):
    """Extracts text from a PDF and saves it to a file for debugging."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    text_content = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text(x_tolerance=2)
                if page_text:
                    text_content += f"--- PAGE {i+1} ---\n{page_text}\n\n"
        
        output_filename = "debug_output.txt"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(text_content)
        
        print(f"Debug text extracted successfully to '{output_filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debug_pdf.py <path_to_pdf_file>")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    debug_pdf_text(pdf_file)
