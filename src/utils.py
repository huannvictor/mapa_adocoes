# -*- coding: utf-8 -*-
import os
import logging
from datetime import datetime

def setup_logging(log_dir='logs'):
    """
    Sets up logging to both console and file.
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_filename = f"extracao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_path = os.path.join(log_dir, log_filename)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_path, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def get_output_path(input_folder, output_dir='data/output'):
    """
    Generates the output Excel path based on the input folder name.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    folder_name = os.path.basename(os.path.normpath(input_folder))
    return os.path.join(output_dir, f"{folder_name}.xlsx")
