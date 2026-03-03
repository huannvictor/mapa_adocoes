# -*- coding: utf-8 -*-
import sys
import os
from src.utils import setup_logging, get_output_path
from src.core import run_extraction_pipeline

def main():
    """
    Main entry point for the School Data Extraction RPA.
    """
    if len(sys.argv) < 2:
        print("Usage: python -m src.main <path_to_pdf_folder>")
        sys.exit(1)
        
    input_folder = sys.argv[1]
    
    # Initialize logger
    logger = setup_logging()
    
    # Resolve input and output paths
    # Note: input_folder can be relative to project root or absolute
    if not os.path.exists(input_folder):
        logger.error(f"Provided path '{input_folder}' not found.")
        sys.exit(1)
        
    output_path = get_output_path(input_folder)
    
    logger.info("Initializing RPA process...")
    run_extraction_pipeline(input_folder, output_path)
    logger.info("Process finished.")

if __name__ == "__main__":
    main()
