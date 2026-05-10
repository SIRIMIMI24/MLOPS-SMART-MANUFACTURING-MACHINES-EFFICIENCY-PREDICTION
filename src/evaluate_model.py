"""
Model evaluation module for the Smart Manufacturing Efficiency Prediction project.
Handles model evaluation and metrics calculation.
"""

import sys
from pathlib import Path
import json
import pandas as pd
import numpy as np
import joblib

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)


class ModelEvaluator:
    """Evaluate machine learning model performance."""
    
    def __init__(self, model, X_test: pd.DataFrame, y_test: pd.Series):
        """
        Initialize model evaluator.
        
        Args:
            model: Trained model pipeline
            X_test: Test features
            y_test: Test target variable
        """
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.y_pred = None
        self.metrics = {}
        
    def make_predictions(self) -> np.ndarray:
        """
        Make predictions on test set.
        
        Returns:
            Array of predictions
        """
        try:
            logger.info("Making predictions on test set")
            self.y_pred = self.model.predict(self.X_test)
            logger.info(f"Predictions shape: {self.y_pred.shape}")
            return self.y_pred
        except Exception as e:
            raise CustomException("Error making predictions", e)
    
    def calculate_metrics(self) -> dict:
        """
        Calculate evaluation metrics.
        
        Returns:
            Dictionary with evaluation metrics
        """
        try:
            if self.y_pred is None:
                self.make_predictions()
            
            logger.info("Calculating evaluation metrics")
            
            # Overall metrics
            accuracy = accuracy_score(self.y_test, self.y_pred)
            macro_f1 = f1_score(self.y_test, self.y_pred, average="macro")
            weighted_f1 = f1_score(self.y_test, self.y_pred, average="weighted")
            
            self.metrics = {
                "accuracy": float(accuracy),
                "macro_f1": float(macro_f1),
                "weighted_f1": float(weighted_f1),
                "test_samples": len(self.y_test)
            }
            
            logger.info(f"Accuracy: {accuracy:.4f}")
            logger.info(f"Macro F1-score: {macro_f1:.4f}")
            logger.info(f"Weighted F1-score: {weighted_f1:.4f}")
            
            return self.metrics
        except Exception as e:
            raise CustomException("Error calculating metrics", e)
    
    def get_classification_report(self) -> str:
        """
        Get detailed classification report.
        
        Returns:
            Classification report as string
        """
        try:
            if self.y_pred is None:
                self.make_predictions()
            
            logger.info("Generating classification report")
            report = classification_report(self.y_test, self.y_pred)
            return report
        except Exception as e:
            raise CustomException("Error generating classification report", e)
    
    def get_confusion_matrix(self) -> np.ndarray:
        """
        Get confusion matrix.
        
        Returns:
            Confusion matrix
        """
        try:
            if self.y_pred is None:
                self.make_predictions()
            
            logger.info("Computing confusion matrix")
            cm = confusion_matrix(self.y_test, self.y_pred)
            return cm
        except Exception as e:
            raise CustomException("Error computing confusion matrix", e)
    
    def per_class_metrics(self) -> pd.DataFrame:
        """
        Calculate per-class metrics.
        
        Returns:
            DataFrame with per-class metrics
        """
        try:
            if self.y_pred is None:
                self.make_predictions()
            
            logger.info("Calculating per-class metrics")
            
            # Get unique classes
            classes = sorted(self.y_test.unique())
            
            per_class = []
            for cls in classes:
                # Binary comparison for each class
                y_test_binary = (self.y_test == cls).astype(int)
                y_pred_binary = (self.y_pred == cls).astype(int)
                
                precision = precision_score(y_test_binary, y_pred_binary, zero_division=0)
                recall = recall_score(y_test_binary, y_pred_binary, zero_division=0)
                f1 = f1_score(y_test_binary, y_pred_binary, zero_division=0)
                
                per_class.append({
                    "class": cls,
                    "precision": float(precision),
                    "recall": float(recall),
                    "f1_score": float(f1)
                })
                
                logger.info(f"Class {cls} - Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}")
            
            return pd.DataFrame(per_class)
        except Exception as e:
            raise CustomException("Error calculating per-class metrics", e)
    
    def error_analysis(self) -> pd.DataFrame:
        """
        Analyze prediction errors.
        
        Returns:
            DataFrame with error information
        """
        try:
            if self.y_pred is None:
                self.make_predictions()
            
            logger.info("Performing error analysis")
            
            error_df = pd.DataFrame({
                "actual": self.y_test.values,
                "predicted": self.y_pred,
                "is_error": self.y_test.values != self.y_pred
            })
            
            error_rate = error_df["is_error"].mean()
            logger.info(f"Overall error rate: {error_rate:.4f}")
            
            # Error rate by actual class
            error_by_class = error_df.groupby("actual")["is_error"].mean()
            logger.info("Error rate by class:")
            for cls, rate in error_by_class.items():
                logger.info(f"  {cls}: {rate:.4f}")
            
            return error_df
        except Exception as e:
            raise CustomException("Error in error analysis", e)
    
    def save_evaluation_report(self, report_path: str) -> None:
        """
        Save comprehensive evaluation report.
        
        Args:
            report_path: Path to save report
        """
        try:
            output_path = Path(report_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            logger.info("Generating evaluation report")
            
            if self.y_pred is None:
                self.make_predictions()
            if not self.metrics:
                self.calculate_metrics()
            
            # Create report
            report_content = f"""# Model Evaluation Report

## Overall Metrics
- Accuracy: {self.metrics.get('accuracy', 'N/A'):.4f}
- Macro F1-score: {self.metrics.get('macro_f1', 'N/A'):.4f}
- Weighted F1-score: {self.metrics.get('weighted_f1', 'N/A'):.4f}
- Test Samples: {self.metrics.get('test_samples', 'N/A')}

## Classification Report
{self.get_classification_report()}

## Confusion Matrix
{self.get_confusion_matrix()}

## Per-Class Metrics
{self.per_class_metrics().to_string(index=False)}
"""
            
            with open(report_path, "w") as f:
                f.write(report_content)
            
            logger.info(f"Evaluation report saved to {report_path}")
        except Exception as e:
            raise CustomException("Error saving evaluation report", e)
    
    def evaluate(self, report_path: str = None) -> dict:
        """
        Execute complete evaluation pipeline.
        
        Args:
            report_path: Path to save report (optional)
            
        Returns:
            Dictionary with all metrics
        """
        try:
            self.make_predictions()
            self.calculate_metrics()
            self.per_class_metrics()
            self.error_analysis()
            
            if report_path:
                self.save_evaluation_report(report_path)
            
            logger.info("Evaluation pipeline completed successfully")
            return self.metrics
        except Exception as e:
            raise CustomException("Error in evaluation pipeline", e)


if __name__ == "__main__":
    """
    Example usage of ModelEvaluator
    """
    try:
        PROJECT_ROOT = Path(__file__).resolve().parents[1]
        MODEL_PATH = PROJECT_ROOT / "models" / "efficiency_model.joblib"
        PROCESSED_FILE = PROJECT_ROOT / "data" / "processed" / "processed_data.csv"
        REPORT_PATH = PROJECT_ROOT / "reports" / "evaluation_report.md"
        
        if MODEL_PATH.exists() and PROCESSED_FILE.exists():
            # Load model and data
            model = joblib.load(MODEL_PATH)
            df = pd.read_csv(PROCESSED_FILE)
            
            # Import feature engineer and trainer
            from src.feature_engineering import FeatureEngineer
            from src.train_model import ModelTrainer
            
            engineer = FeatureEngineer(df)
            X, y = engineer.engineer()
            
            trainer = ModelTrainer(X, y)
            trainer.train_test_split()
            
            # Evaluate model
            evaluator = ModelEvaluator(model, trainer.X_test, trainer.y_test)
            metrics = evaluator.evaluate(str(REPORT_PATH))
            
            logger.info(f"Evaluation complete: Accuracy {metrics['accuracy']:.4f}")
        else:
            logger.warning("Model or processed data not found")
            
    except CustomException as ce:
        logger.error(f"Custom Exception: {ce}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
