import os
import kagglehub
import shutil
from src.logger import get_logger
from src.exception import CustomException
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
