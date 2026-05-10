"""
Data processing module for the Smart Manufacturing Efficiency Prediction project.
Handles data cleaning, missing value handling, and duplicate removal.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)


class DataProcessor:
    """Process raw data for machine learning."""
    
    def __init__(self, data_file: str):
        """
        Initialize data processor.
        
        Args:
            data_file: Path to raw CSV file
        """
        self.data_file = data_file
        self.df = None
        self.target_column = "Efficiency_Status"
        
    def load_data(self) -> pd.DataFrame:
        """
        Load data from CSV file.
        
        Returns:
            DataFrame with raw data
        """
        try:
            logger.info(f"Loading data from {self.data_file}")
            self.df = pd.read_csv(self.data_file)
            logger.info(f"Data loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns")
            return self.df
        except FileNotFoundError:
            raise CustomException(f"Data file not found: {self.data_file}", None)
        except Exception as e:
            raise CustomException("Error loading data", e)
    
    def check_data_quality(self) -> dict:
        """
        Perform data quality checks.
        
        Returns:
            Dictionary with quality metrics
        """
        try:
            logger.info("Performing data quality checks")
            
            quality_report = {
                "total_rows": len(self.df),
                "total_columns": len(self.df.columns),
                "duplicate_rows": self.df.duplicated().sum(),
                "missing_values": self.df.isna().sum().sum(),
                "columns_with_missing": self.df.columns[self.df.isna().any()].tolist(),
                "data_types": self.df.dtypes.to_dict()
            }
            
            logger.info(f"Quality check - Duplicates: {quality_report['duplicate_rows']}")
            logger.info(f"Quality check - Missing values: {quality_report['missing_values']}")
            
            return quality_report
        except Exception as e:
            raise CustomException("Error during data quality check", e)
    
    def remove_duplicates(self) -> pd.DataFrame:
        """
        Remove duplicate rows.
        
        Returns:
            DataFrame without duplicates
        """
        try:
            duplicates_before = self.df.duplicated().sum()
            self.df = self.df.drop_duplicates()
            duplicates_after = self.df.duplicated().sum()
            
            logger.info(f"Removed {duplicates_before - duplicates_after} duplicate rows")
            logger.info(f"Remaining rows: {len(self.df)}")
            
            return self.df
        except Exception as e:
            raise CustomException("Error removing duplicates", e)
    
    def handle_missing_values(self) -> pd.DataFrame:
        """
        Handle missing values in the dataset.
        Numeric columns: median imputation
        Categorical columns: most frequent imputation
        
        Returns:
            DataFrame with missing values handled
        """
        try:
            logger.info("Handling missing values")
            
            numeric_columns = self.df.select_dtypes(include=['number']).columns
            categorical_columns = self.df.select_dtypes(include=['object', 'category']).columns
            
            # Numeric imputation
            for col in numeric_columns:
                if self.df[col].isna().sum() > 0:
                    median_val = self.df[col].median()
                    self.df[col] = self.df[col].fillna(median_val)
                    logger.info(f"Filled {col} with median value: {median_val}")
            
            # Categorical imputation
            for col in categorical_columns:
                if self.df[col].isna().sum() > 0:
                    mode_val = self.df[col].mode()[0] if not self.df[col].mode().empty else "Unknown"
                    self.df[col] = self.df[col].fillna(mode_val)
                    logger.info(f"Filled {col} with mode value: {mode_val}")
            
            logger.info("Missing value handling completed")
            return self.df
        except Exception as e:
            raise CustomException("Error handling missing values", e)
    
    def save_processed_data(self, output_file: str) -> None:
        """
        Save processed data to CSV.
        
        Args:
            output_file: Path to save processed data
        """
        try:
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            self.df.to_csv(output_file, index=False)
            logger.info(f"Processed data saved to {output_file}")
        except Exception as e:
            raise CustomException("Error saving processed data", e)
    
    def process(self, output_file: str = None) -> pd.DataFrame:
        """
        Execute complete data processing pipeline.
        
        Args:
            output_file: Path to save processed data (optional)
            
        Returns:
            Processed DataFrame
        """
        try:
            self.load_data()
            self.check_data_quality()
            self.remove_duplicates()
            self.handle_missing_values()
            
            if output_file:
                self.save_processed_data(output_file)
            
            logger.info("Data processing completed successfully")
            return self.df
        except Exception as e:
            raise CustomException("Error in data processing pipeline", e)


if __name__ == "__main__":
    """
    Example usage of DataProcessor
    """
    try:
        PROJECT_ROOT = Path(__file__).resolve().parents[1]
        DATA_FILE = PROJECT_ROOT / "data" / "raw" / "manufacturing_6G_dataset.csv"
        OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "processed_data.csv"
        
        processor = DataProcessor(str(DATA_FILE))
        processed_df = processor.process(str(OUTPUT_FILE))
        
        logger.info(f"Processing complete: {processed_df.shape[0]} rows, {processed_df.shape[1]} columns")
        
    except CustomException as ce:
        logger.error(f"Custom Exception: {ce}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
