"""
Model training module for the Smart Manufacturing Efficiency Prediction project.
Handles model training and artifact saving.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)


class ModelTrainer:
    """Train machine learning models."""
    
    def __init__(self, X: pd.DataFrame, y: pd.Series, random_state: int = 42):
        """
        Initialize model trainer.
        
        Args:
            X: Feature matrix
            y: Target variable
            random_state: Random seed for reproducibility
        """
        self.X = X
        self.y = y
        self.random_state = random_state
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.preprocessor = None
        
    def train_test_split(self, test_size: float = 0.2) -> None:
        """
        Split data into train and test sets.
        Uses stratification to preserve class distribution.
        
        Args:
            test_size: Fraction of data for testing
        """
        try:
            logger.info(f"Splitting data: test_size={test_size}")
            
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.X,
                self.y,
                test_size=test_size,
                random_state=self.random_state,
                stratify=self.y
            )
            
            logger.info(f"Train set: {self.X_train.shape[0]} samples")
            logger.info(f"Test set: {self.X_test.shape[0]} samples")
            logger.info(f"Train/test ratio: {len(self.X_train)/len(self.X_test):.2f}")
            
        except Exception as e:
            raise CustomException("Error in train-test split", e)
    
    def create_preprocessing_pipeline(self) -> ColumnTransformer:
        """
        Create preprocessing pipeline for numeric and categorical features.
        
        Returns:
            ColumnTransformer object
        """
        try:
            logger.info("Creating preprocessing pipeline")
            
            # Identify feature types
            numeric_features = self.X_train.select_dtypes(include=['number']).columns.tolist()
            categorical_features = self.X_train.select_dtypes(include=['object', 'category']).columns.tolist()
            
            logger.info(f"Numeric features: {len(numeric_features)} - {numeric_features}")
            logger.info(f"Categorical features: {len(categorical_features)} - {categorical_features}")
            
            # Numeric pipeline
            numeric_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])
            
            # Categorical pipeline
            categorical_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
            ])
            
            # Combine pipelines
            self.preprocessor = ColumnTransformer(transformers=[
                ("numeric", numeric_pipeline, numeric_features),
                ("categorical", categorical_pipeline, categorical_features)
            ])
            
            logger.info("Preprocessing pipeline created successfully")
            return self.preprocessor
        except Exception as e:
            raise CustomException("Error creating preprocessing pipeline", e)
    
    def train_model(self) -> Pipeline:
        """
        Train the baseline logistic regression model.
        
        Returns:
            Trained model pipeline
        """
        try:
            logger.info("Training baseline model (LogisticRegression)")
            
            if self.preprocessor is None:
                self.create_preprocessing_pipeline()
            
            # Create pipeline
            self.model = Pipeline(steps=[
                ("preprocessor", self.preprocessor),
                ("model", LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=self.random_state
                ))
            ])
            
            # Train model
            logger.info("Fitting model on training data")
            self.model.fit(self.X_train, self.y_train)
            
            logger.info("Model training completed successfully")
            return self.model
        except Exception as e:
            raise CustomException("Error in model training", e)
    
    def save_model(self, model_path: str) -> None:
        """
        Save trained model to file.
        
        Args:
            model_path: Path to save model
        """
        try:
            if self.model is None:
                raise CustomException("Model not trained yet", None)
            
            output_path = Path(model_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            joblib.dump(self.model, model_path)
            logger.info(f"Model saved to {model_path}")
        except Exception as e:
            raise CustomException("Error saving model", e)
    
    def save_metadata(self, metadata_path: str, metrics: dict = None) -> None:
        """
        Save model metadata.
        
        Args:
            metadata_path: Path to save metadata
            metrics: Dictionary of evaluation metrics
        """
        try:
            import json
            
            output_path = Path(metadata_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            numeric_features = self.X_train.select_dtypes(include=['number']).columns.tolist()
            categorical_features = self.X_train.select_dtypes(include=['object', 'category']).columns.tolist()
            
            metadata = {
                "model_name": "LogisticRegression",
                "problem_type": "multi-class classification",
                "target_column": "Efficiency_Status",
                "feature_columns": self.X.columns.tolist(),
                "numeric_features": numeric_features,
                "categorical_features": categorical_features,
                "train_rows": len(self.X_train),
                "test_rows": len(self.X_test),
                "train_test_split_ratio": 0.2,
                "random_state": self.random_state,
                "evaluation_metrics": metrics if metrics else {},
                "created_date": datetime.now().isoformat(),
                "model_parameters": {
                    "max_iter": 1000,
                    "class_weight": "balanced"
                }
            }
            
            with open(metadata_path, "w") as f:
                json.dump(metadata, f, indent=2)
            
            logger.info(f"Metadata saved to {metadata_path}")
        except Exception as e:
            raise CustomException("Error saving metadata", e)
    
    def train(self, model_path: str, metadata_path: str = None) -> Pipeline:
        """
        Execute complete training pipeline.
        
        Args:
            model_path: Path to save model
            metadata_path: Path to save metadata
            
        Returns:
            Trained model
        """
        try:
            self.train_test_split()
            self.create_preprocessing_pipeline()
            self.train_model()
            self.save_model(model_path)
            
            if metadata_path:
                self.save_metadata(metadata_path)
            
            logger.info("Training pipeline completed successfully")
            return self.model
        except Exception as e:
            raise CustomException("Error in training pipeline", e)


if __name__ == "__main__":
    """
    Example usage of ModelTrainer
    """
    try:
        PROJECT_ROOT = Path(__file__).resolve().parents[1]
        PROCESSED_FILE = PROJECT_ROOT / "data" / "processed" / "processed_data.csv"
        MODEL_PATH = PROJECT_ROOT / "models" / "efficiency_model.joblib"
        METADATA_PATH = PROJECT_ROOT / "models" / "model_metadata.json"
        
        if PROCESSED_FILE.exists():
            # Load processed data
            df = pd.read_csv(PROCESSED_FILE)
            
            # Import feature engineer
            from src.feature_engineering import FeatureEngineer
            
            engineer = FeatureEngineer(df)
            X, y = engineer.engineer()
            
            # Train model
            trainer = ModelTrainer(X, y)
            model = trainer.train(str(MODEL_PATH), str(METADATA_PATH))
            
            logger.info("Model training complete")
        else:
            logger.warning(f"Processed data not found: {PROCESSED_FILE}")
            
    except CustomException as ce:
        logger.error(f"Custom Exception: {ce}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
