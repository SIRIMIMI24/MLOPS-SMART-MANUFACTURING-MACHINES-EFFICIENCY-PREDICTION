"""
Prediction module for the Smart Manufacturing Efficiency Prediction project.
Provides reusable prediction functionality.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
from typing import Dict, List, Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)


class PredictionEngine:
    """Make predictions using trained model."""
    
    def __init__(self, model_path: str):
        """
        Initialize prediction engine.
        
        Args:
            model_path: Path to saved model
        """
        self.model_path = model_path
        self.model = None
        self.load_model()
        
    def load_model(self) -> None:
        """Load trained model from file."""
        try:
            if not Path(self.model_path).exists():
                raise CustomException(f"Model file not found: {self.model_path}", None)
            
            self.model = joblib.load(self.model_path)
            logger.info(f"Model loaded from {self.model_path}")
        except Exception as e:
            raise CustomException("Error loading model", e)
    
    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        """
        Validate input data format.
        
        Args:
            input_data: Input features as dictionary
            
        Returns:
            True if valid, raises exception otherwise
        """
        try:
            if not isinstance(input_data, dict):
                raise CustomException("Input must be a dictionary", None)
            
            if len(input_data) == 0:
                raise CustomException("Input dictionary is empty", None)
            
            logger.info(f"Input validated: {len(input_data)} features")
            return True
        except Exception as e:
            raise CustomException("Input validation failed", e)
    
    def prepare_input(self, input_data: Dict[str, Any]) -> pd.DataFrame:
        """
        Convert input dictionary to DataFrame for model prediction.
        
        Args:
            input_data: Input features as dictionary
            
        Returns:
            DataFrame ready for prediction
        """
        try:
            logger.info("Preparing input data")
            
            # Convert to DataFrame
            input_df = pd.DataFrame([input_data])
            
            # Handle Timestamp if present
            if "Timestamp" in input_df.columns:
                logger.info("Processing Timestamp feature")
                input_df["Timestamp"] = pd.to_datetime(input_df["Timestamp"], errors="coerce")
                input_df["hour"] = input_df["Timestamp"].dt.hour
                input_df["day_of_week"] = input_df["Timestamp"].dt.dayofweek
                input_df = input_df.drop(columns=["Timestamp"])
                logger.info("Timestamp features engineered")
            
            logger.info(f"Prepared input shape: {input_df.shape}")
            return input_df
        except Exception as e:
            raise CustomException("Error preparing input data", e)
    
    def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make prediction on input data.
        
        Args:
            input_data: Dictionary with feature values
            
        Returns:
            Dictionary with prediction results
        """
        try:
            logger.info("Making prediction")
            
            # Validate input
            self.validate_input(input_data)
            
            # Prepare input
            input_df = self.prepare_input(input_data)
            
            # Make prediction
            prediction = self.model.predict(input_df)[0]
            
            # Get prediction probability if available
            try:
                probabilities = self.model.predict_proba(input_df)[0]
                classes = self.model.named_steps['model'].classes_
                prob_dict = {str(cls): float(prob) for cls, prob in zip(classes, probabilities)}
            except:
                prob_dict = {}
            
            result = {
                "prediction": str(prediction),
                "probabilities": prob_dict,
                "input_features": input_data
            }
            
            logger.info(f"Prediction complete: {prediction}")
            return result
        except CustomException:
            raise
        except Exception as e:
            raise CustomException("Error in prediction", e)
    
    def batch_predict(self, input_data_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Make predictions on multiple samples.
        
        Args:
            input_data_list: List of input feature dictionaries
            
        Returns:
            List of prediction results
        """
        try:
            logger.info(f"Making batch predictions for {len(input_data_list)} samples")
            
            results = []
            for i, input_data in enumerate(input_data_list):
                try:
                    result = self.predict(input_data)
                    results.append(result)
                except Exception as e:
                    logger.warning(f"Prediction failed for sample {i}: {e}")
                    results.append({"error": str(e), "input_features": input_data})
            
            logger.info(f"Batch prediction complete: {len(results)} results")
            return results
        except Exception as e:
            raise CustomException("Error in batch prediction", e)


def predict_machine_efficiency(input_data: Dict[str, Any], model_path: str = None) -> Dict[str, Any]:
    """
    Reusable prediction function.
    
    Args:
        input_data: Dictionary with feature values
        model_path: Path to saved model (default: PROJECT_ROOT/models/baseline_efficiency_status_model.joblib)
        
    Returns:
        Dictionary with prediction results
        
    Example:
        >>> input_data = {
        ...     "Machine_ID": 10,
        ...     "Operation_Mode": "active",
        ...     "Temperature_C": 75.5,
        ...     "Vibration_Hz": 2.3,
        ...     "Power_Consumption_kW": 45.2,
        ...     "Network_Latency_ms": 15,
        ...     "Packet_Loss_%": 0.5,
        ...     "Quality_Control_Defect_Rate_%": 0.1,
        ...     "Production_Speed_units_per_hr": 500,
        ...     "Predictive_Maintenance_Score": 0.8,
        ...     "Error_Rate_%": 2.1,
        ...     "Timestamp": "2025-05-10 14:30:00"
        ... }
        >>> result = predict_machine_efficiency(input_data)
        >>> print(result['prediction'])
    """
    try:
        if model_path is None:
            model_path = str(PROJECT_ROOT / "models" / "baseline_efficiency_status_model.joblib")
        
        engine = PredictionEngine(model_path)
        result = engine.predict(input_data)
        
        return result
    except CustomException:
        raise
    except Exception as e:
        raise CustomException("Error in prediction function", e)


if __name__ == "__main__":
    """
    Example usage of prediction engine
    """
    try:
        PROJECT_ROOT_PATH = Path(__file__).resolve().parents[1]
        MODEL_FILE = PROJECT_ROOT_PATH / "models" / "baseline_efficiency_status_model.joblib"
        
        if MODEL_FILE.exists():
            # Example input
            example_input = {
                "Machine_ID": 10,
                "Operation_Mode": "active",
                "Temperature_C": 75.5,
                "Vibration_Hz": 2.3,
                "Power_Consumption_kW": 45.2,
                "Network_Latency_ms": 15,
                "Packet_Loss_%": 0.5,
                "Quality_Control_Defect_Rate_%": 0.1,
                "Production_Speed_units_per_hr": 500,
                "Predictive_Maintenance_Score": 0.8,
                "Error_Rate_%": 2.1,
                "Timestamp": "2025-05-10 14:30:00"
            }
            
            # Make prediction
            result = predict_machine_efficiency(example_input, str(MODEL_FILE))
            
            logger.info(f"Prediction: {result['prediction']}")
            logger.info(f"Probabilities: {result['probabilities']}")
        else:
            logger.warning(f"Model not found: {MODEL_FILE}")
            
    except CustomException as ce:
        logger.error(f"Custom Exception: {ce}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
