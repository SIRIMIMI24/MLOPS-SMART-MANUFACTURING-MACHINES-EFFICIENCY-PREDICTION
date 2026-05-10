"""
Pipeline orchestration script for Smart Manufacturing Efficiency Prediction project.
Runs the complete data processing, training, and evaluation pipeline.
"""

import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.logger import get_logger
from src.custom_exception import CustomException
from src.data_processing import DataProcessor
from src.feature_engineering import FeatureEngineer
from src.train_model import ModelTrainer
from src.evaluate_model import ModelEvaluator

logger = get_logger(__name__)


def run_pipeline():
    """Execute complete ML pipeline from data to model evaluation."""
    try:
        # Define paths
        raw_data_file = PROJECT_ROOT / "data" / "raw" / "manufacturing_6G_dataset.csv"
        processed_data_file = PROJECT_ROOT / "data" / "processed" / "processed_data.csv"
        model_path = PROJECT_ROOT / "models" / "efficiency_model.joblib"
        metadata_path = PROJECT_ROOT / "models" / "model_metadata.json"
        evaluation_report = PROJECT_ROOT / "reports" / "evaluation_report.md"
        
        logger.info("="*80)
        logger.info("Starting Smart Manufacturing ML Pipeline")
        logger.info("="*80)
        
        # Step 1: Data Processing
        logger.info("\n[Step 1/4] Data Processing")
        logger.info("-" * 40)
        processor = DataProcessor(str(raw_data_file))
        processed_df = processor.process(str(processed_data_file))
        logger.info(f"✓ Data processed: {processed_df.shape[0]} rows, {processed_df.shape[1]} columns")
        
        # Step 2: Feature Engineering
        logger.info("\n[Step 2/4] Feature Engineering")
        logger.info("-" * 40)
        engineer = FeatureEngineer(processed_df)
        X, y = engineer.engineer()
        logger.info(f"✓ Features engineered: {X.shape[0]} samples, {X.shape[1]} features")
        logger.info(f"✓ Target distribution:\n{y.value_counts()}")
        
        # Step 3: Model Training
        logger.info("\n[Step 3/4] Model Training")
        logger.info("-" * 40)
        trainer = ModelTrainer(X, y)
        model = trainer.train(str(model_path), str(metadata_path))
        logger.info(f"✓ Model trained and saved")
        logger.info(f"  - Train set: {len(trainer.X_train)} samples")
        logger.info(f"  - Test set: {len(trainer.X_test)} samples")
        
        # Step 4: Model Evaluation
        logger.info("\n[Step 4/4] Model Evaluation")
        logger.info("-" * 40)
        evaluator = ModelEvaluator(model, trainer.X_test, trainer.y_test)
        metrics = evaluator.evaluate(str(evaluation_report))
        logger.info(f"✓ Model evaluation complete:")
        logger.info(f"  - Accuracy: {metrics['accuracy']:.4f}")
        logger.info(f"  - Macro F1: {metrics['macro_f1']:.4f}")
        logger.info(f"  - Weighted F1: {metrics['weighted_f1']:.4f}")
        
        logger.info("\n" + "="*80)
        logger.info("Pipeline completed successfully!")
        logger.info("="*80)
        logger.info("\nArtifacts created:")
        logger.info(f"  - Processed data: {processed_data_file}")
        logger.info(f"  - Model: {model_path}")
        logger.info(f"  - Metadata: {metadata_path}")
        logger.info(f"  - Evaluation report: {evaluation_report}")
        logger.info("="*80 + "\n")
        
        return True
        
    except CustomException as ce:
        logger.error(f"Custom Exception: {ce}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
