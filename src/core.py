# -*- coding: utf-8 -*-
import os
import re
import logging
import pandas as pd
import pdfplumber
import concurrent.futures
from tqdm import tqdm

# Patterns and Constants
SCHOOL_PATTERN = re.compile(r"^\s*(?:Ficha da Escola\s*)?(.*?)\s*\(?(\d{3}\.\d{3})\)?(?:\s*\|.*)?$", re.MULTILINE)

logger = logging.getLogger(__name__)

def process_single_pdf(file_path):
    """
    Extracts school information from a single PDF file.
    """
    filename = os.path.basename(file_path)
    file_data = []

    try:
        # Extract metadata from filename
        base_name = os.path.splitext(filename)[0]
        parts = base_name.split('-')
        
        if len(parts) < 3:
            logger.warning(f"File '{filename}' does not follow the naming convention and will be skipped.")
            return []

        divulgador = parts[0].capitalize()
        status_raw = '-'.join(parts[1:-1])
        
        if status_raw == "adotante":
            adocao = "ADOTANTE"
        elif status_raw == "nao_adotante":
            adocao = "NÃO ADOTANTE"
        else:
            adocao = "STATUS INDEFINIDO"
            logger.warning(f"Unrecognized adoption status '{status_raw}' in file '{filename}'.")

        # Extract PDF content
        text_content = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text(x_tolerance=2)
                if page_text:
                    text_content += page_text + "\n"
        
        # Apply Regex
        matches = SCHOOL_PATTERN.finditer(text_content)
        
        for match in matches:
            if match.group(1) and match.group(2):
                school_name = match.group(1).strip()
                school_code = match.group(2)
                
                file_data.append({
                    "CÓDIGO": school_code,
                    "ESCOLA": school_name,
                    "DIVULGADOR": divulgador,
                    "ADOÇÃO": adocao
                })

        return file_data

    except Exception as e:
        logger.error(f"Error processing file '{filename}': {e}")
        return []

def run_extraction_pipeline(input_folder, output_path):
    """
    Main pipeline for iterating through files and consolidating results.
    """
    if not os.path.isdir(input_folder):
        logger.error(f"Input folder '{input_folder}' does not exist.")
        return

    pdf_files = [
        os.path.join(input_folder, f)
        for f in os.listdir(input_folder)
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:
        logger.warning(f"No PDF files found in '{input_folder}'.")
        return

    logger.info(f"Starting extraction for {len(pdf_files)} files...")
    all_data = []
    
    # Using ProcessPoolExecutor for parallel processing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_to_file = {executor.submit(process_single_pdf, pdf_path): pdf_path for pdf_path in pdf_files}
        
        # Progression tracking
        for future in tqdm(concurrent.futures.as_completed(future_to_file), total=len(pdf_files), desc="Processing PDFs"):
            results = future.result()
            if results:
                all_data.extend(results)

    if not all_data:
        logger.warning("No data extracted. Excel file will not be created.")
        return

    # Consolidate and Save
    df = pd.DataFrame(all_data)
    df = df[["CÓDIGO", "ESCOLA", "DIVULGADOR", "ADOÇÃO"]]
    
    try:
        df.to_excel(output_path, index=False)
        logger.info(f"Success! '{output_path}' generated with {len(df)} records.")
    except Exception as e:
        logger.error(f"Error saving Excel file: {e}")
