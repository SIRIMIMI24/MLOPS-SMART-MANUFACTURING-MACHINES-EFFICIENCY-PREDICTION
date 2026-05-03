import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import kagglehub
import shutil
from src.logger import get_logger
from src.custom_exception import CustomException
from config.data_ingestion_config import * # Calls DATASET_NAME , TARGET_DIR
import zipfile
import json
import json
import pandas as pd

# Before run Clen Cache: pip install kagglehub

logger = get_logger(__name__)

class DataIngestion:

    def __init__(self, dataset_name:str, target_dir:str):
        self.dataset_name = dataset_name
        self.target_dir = target_dir

        # Select data ingestion
        self.required_files = [
            "manufacturing_6G_dataset.csv"
        ]
    
    def create_raw_dir(self):
        raw_dir = os.path.join(self.target_dir, "raw")
        if not os.path.exists(raw_dir):
            try:
                os.makedirs(raw_dir)
                logger.info(f"Created th {raw_dir}")
            except Exception as e:
                logger.error("Error while Creating directory..")
                raise CustomException("Faile to create raw dir", e)
        return raw_dir
    
    def extract_zip(self, path:str) -> str:
        
        if os.path.isdir(path):
            # kagglehub downloads as folder if dataset is small
            logger.info(f"Dataset is already extracted: {path}")
            return path

        if path.endswith(".zip"):
            logger.info(f"Extracting zip file: {path}")
            extract_dir = path.replace(".zip", "")
            try:
                with zipfile.ZipFile(path, "r") as zip_ref:
                    zip_ref.extractall(extract_dir)
                logger.info(f"Extracted zip file to: {extract_dir}")
                return extract_dir
            except Exception as e:
                logger.error("Error while extracting zip file.")
                raise CustomException("Failed to extract zip file", e)
            
        
        raise CustomException("Provided path is neither a directory nor a zip file.")
        
    def extract_dataset_files(self, dataset_root: str, raw_dir: str) -> None:
        try:
            for fname in self.required_files:
                src = os.path.join(dataset_root, fname)
                dst = os.path.join(raw_dir, fname)

                if os.path.exists(src):
                    shutil.copy(src, dst)
                    logger.info(f"Move {src} to {dst}")
                else:
                    logger.warning(f"Required file {fname} not found in dataset.")
        except Exception as e:
            logger.error("Error while extracting required dataset files.")
            raise CustomException("Failed to extract dataset files", e)
    
    def download_data(self, raw_dir: str) -> None:
        try:
            logger.info(f"Downloading dataset: {self.dataset_name}")
            path = kagglehub.dataset_download(self.dataset_name)
            logger.info(f"Downloaded dataset to: {path}")

            dataset_root = self.extract_zip(path)
            self.extract_dataset_files(dataset_root, raw_dir)
        
        except Exception as e:
            logger.error("Error while downloading data.")
            raise CustomException
    
    def initiate_data_ingestion(self) -> None:
        try:
            raw_dir = self.create_raw_dir()
            self.download_data(raw_dir)
            logger.info("Data ingestion completed successfully.")
        except Exception as e :
            logger.error("Error during data ingestion process.")
            raise CustomException("Data ingestion failed", e)

if __name__ == "__main__":
    data_ingestion = DataIngestion(
        dataset_name=DATASET_NAME,
        target_dir=TARGET_DIR
    )
    data_ingestion.initiate_data_ingestion()
