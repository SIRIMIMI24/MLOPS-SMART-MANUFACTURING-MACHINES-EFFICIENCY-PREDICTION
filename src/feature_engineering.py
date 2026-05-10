"""
Feature engineering module for the Smart Manufacturing Efficiency Prediction project.
Handles feature creation and transformation.
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


class FeatureEngineer:
    """Engineer features for machine learning model."""
    
    def __init__(self, df: pd.DataFrame, target_column: str = "Efficiency_Status"):
        """
        Initialize feature engineer.
        
        Args:
            df: Input DataFrame
            target_column: Name of target column
        """
        self.df = df.copy()
        self.target_column = target_column
        self.feature_columns = None
        
    def engineer_timestamp_features(self) -> pd.DataFrame:
        """
        Engineer features from timestamp column.
        Extracts: hour, day_of_week
        
        Returns:
            DataFrame with new timestamp features
        """
        try:
            if "Timestamp" not in self.df.columns:
                logger.warning("Timestamp column not found, skipping timestamp feature engineering")
                return self.df
            
            logger.info("Engineering timestamp features")
            
            # Convert to datetime
            self.df["Timestamp"] = pd.to_datetime(self.df["Timestamp"], errors="coerce")
            
            # Extract hour (0-23)
            self.df["hour"] = self.df["Timestamp"].dt.hour
            logger.info("Created 'hour' feature (0-23)")
            
            # Extract day of week (0-6, where 0=Monday)
            self.df["day_of_week"] = self.df["Timestamp"].dt.dayofweek
            logger.info("Created 'day_of_week' feature (0=Monday, 6=Sunday)")
            
            # Drop original timestamp column
            self.df = self.df.drop(columns=["Timestamp"])
            logger.info("Dropped original Timestamp column")
            
            return self.df
        except Exception as e:
            raise CustomException("Error in timestamp feature engineering", e)
    
    def select_features(self, exclude_columns: list = None) -> tuple:
        """
        Select features for modeling (exclude target and specified columns).
        
        Args:
            exclude_columns: List of columns to exclude
            
        Returns:
            Tuple of (X, y) where X is features and y is target
        """
        try:
            logger.info("Selecting features for modeling")
            
            if exclude_columns is None:
                exclude_columns = []
            
            # Always exclude target column
            exclude_columns.append(self.target_column)
            
            # Select features
            self.feature_columns = [col for col in self.df.columns if col not in exclude_columns]
            
            logger.info(f"Selected {len(self.feature_columns)} features: {self.feature_columns}")
            logger.info(f"Excluded columns: {exclude_columns}")
            
            X = self.df[self.feature_columns]
            y = self.df[self.target_column]
            
            logger.info(f"Feature matrix shape: {X.shape}")
            logger.info(f"Target variable shape: {y.shape}")
            
            return X, y
        except Exception as e:
            raise CustomException("Error in feature selection", e)
    
    def validate_features(self, X: pd.DataFrame) -> dict:
        """
        Validate feature data quality.
        
        Args:
            X: Feature matrix
            
        Returns:
            Dictionary with validation results
        """
        try:
            logger.info("Validating features")
            
            validation_report = {
                "total_features": X.shape[1],
                "total_rows": X.shape[0],
                "numeric_features": len(X.select_dtypes(include=['number']).columns),
                "categorical_features": len(X.select_dtypes(include=['object', 'category']).columns),
                "columns_with_missing": X.columns[X.isna().any()].tolist(),
                "total_missing_values": X.isna().sum().sum()
            }
            
            logger.info(f"Feature validation - Numeric: {validation_report['numeric_features']}, " 
                       f"Categorical: {validation_report['categorical_features']}")
            
            return validation_report
        except Exception as e:
            raise CustomException("Error validating features", e)
    
    def get_feature_info(self) -> dict:
        """
        Get information about engineered features.
        
        Returns:
            Dictionary with feature information
        """
        try:
            logger.info("Collecting feature information")
            
            numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
            categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
            
            if self.target_column in categorical_cols:
                categorical_cols.remove(self.target_column)
            
            feature_info = {
                "all_columns": self.df.columns.tolist(),
                "numeric_features": numeric_cols,
                "categorical_features": categorical_cols,
                "total_features": len(numeric_cols) + len(categorical_cols),
                "feature_list": self.feature_columns if self.feature_columns else []
            }
            
            logger.info(f"Feature info - Total: {feature_info['total_features']}, "
                       f"Numeric: {len(numeric_cols)}, Categorical: {len(categorical_cols)}")
            
            return feature_info
        except Exception as e:
            raise CustomException("Error getting feature information", e)
    
    def engineer(self, exclude_columns: list = None) -> tuple:
        """
        Execute complete feature engineering pipeline.
        
        Args:
            exclude_columns: List of columns to exclude
            
        Returns:
            Tuple of (X, y)
        """
        try:
            self.engineer_timestamp_features()
            X, y = self.select_features(exclude_columns)
            self.validate_features(X)
            
            logger.info("Feature engineering completed successfully")
            return X, y
        except Exception as e:
            raise CustomException("Error in feature engineering pipeline", e)


if __name__ == "__main__":
    """
    Example usage of FeatureEngineer
    """
    try:
        PROJECT_ROOT = Path(__file__).resolve().parents[1]
        PROCESSED_FILE = PROJECT_ROOT / "data" / "processed" / "processed_data.csv"
        
        if PROCESSED_FILE.exists():
            df = pd.read_csv(PROCESSED_FILE)
            engineer = FeatureEngineer(df)
            X, y = engineer.engineer()
            
            logger.info(f"Feature engineering complete: X shape {X.shape}, y shape {y.shape}")
        else:
            logger.warning(f"Processed data file not found: {PROCESSED_FILE}")
            
    except CustomException as ce:
        logger.error(f"Custom Exception: {ce}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
