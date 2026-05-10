# Phase 2 Quick Reference Guide

## 📁 Files Created

```
src/
├── logger.py                    ✅ Logging configuration
├── custom_exception.py          ✅ Error handling
├── data_ingestion.py            ✅ Data download (existing)
├── data_processing.py           ✅ NEW - Data cleaning & validation
├── feature_engineering.py       ✅ NEW - Feature creation
├── train_model.py              ✅ NEW - Model training
├── evaluate_model.py           ✅ NEW - Model evaluation
├── predict.py                  ✅ NEW - Prediction engine
└── pipeline.py                 ✅ NEW - Orchestration script
```

---

## 🚀 Quick Start

### Run Complete Pipeline
```bash
cd <project-root>
python src/pipeline.py
```

### Run Individual Steps
```bash
# Step 1: Process data
python src/data_processing.py
# Output: data/processed/processed_data.csv

# Step 2: Train model
python src/train_model.py
# Output: models/efficiency_model.joblib

# Step 3: Evaluate model
python src/evaluate_model.py
# Output: reports/evaluation_report.md

# Step 4: Make predictions
python src/predict.py
```

---

## 💻 Usage Examples

### 1. Data Processing
```python
from src.data_processing import DataProcessor

processor = DataProcessor("data/raw/manufacturing_6G_dataset.csv")
df = processor.process("data/processed/processed_data.csv")
```

### 2. Feature Engineering
```python
from src.feature_engineering import FeatureEngineer
import pandas as pd

df = pd.read_csv("data/processed/processed_data.csv")
engineer = FeatureEngineer(df)
X, y = engineer.engineer()
```

### 3. Model Training
```python
from src.train_model import ModelTrainer

trainer = ModelTrainer(X, y)
model = trainer.train(
    "models/efficiency_model.joblib",
    "models/model_metadata.json"
)
```

### 4. Model Evaluation
```python
from src.evaluate_model import ModelEvaluator

evaluator = ModelEvaluator(model, trainer.X_test, trainer.y_test)
metrics = evaluator.evaluate("reports/evaluation_report.md")
```

### 5. Make Predictions
```python
from src.predict import predict_machine_efficiency

input_data = {
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

result = predict_machine_efficiency(input_data)
print(result['prediction'])        # "Low", "Medium", or "High"
print(result['probabilities'])     # Class probabilities
```

---

## 📊 Data Flow

```
Raw Data (100K rows × 13 columns)
    ↓
DataProcessor (remove duplicates, handle missing values)
    ↓
Processed Data (100K rows × 13 columns)
    ↓
FeatureEngineer (extract timestamp features, select features)
    ↓
Feature Matrix (80K train × 13 features) + Target
    ↓
ModelTrainer (split, preprocess, train)
    ↓
Trained Model + Metadata
    ↓
ModelEvaluator (evaluate on 20K test samples)
    ↓
Metrics Report (Accuracy: 88.63%, F1: 0.823)
```

---

## 🔑 Key Features

### DataProcessor
- Loads CSV data
- Quality checks (shape, types, missing values)
- Removes duplicates (19 rows)
- Handles missing values (numeric: median, categorical: mode)
- Saves processed data

### FeatureEngineer
- Engineers timestamp features (hour, day_of_week)
- Selects features for modeling
- Validates feature data quality
- Returns feature matrix and target

### ModelTrainer
- Stratified train-test split (80/20)
- Numeric preprocessing: imputation + scaling
- Categorical preprocessing: imputation + one-hot encoding
- Trains LogisticRegression with balanced weights
- Saves model and metadata

### ModelEvaluator
- Computes overall metrics
- Per-class evaluation
- Error analysis
- Confusion matrix
- Classification report
- Saves evaluation report

### PredictionEngine
- Loads model
- Validates input
- Prepares data (feature engineering)
- Makes predictions with probabilities
- Supports batch predictions

---

## 📋 Expected Artifacts

After running Phase 2 pipeline:

```
data/
├── raw/
│   └── manufacturing_6G_dataset.csv    (100K rows)
└── processed/
    └── processed_data.csv              (99,981 rows, duplicates removed)

models/
├── efficiency_model.joblib             (trained pipeline)
└── model_metadata.json                 (model config & metrics)

reports/
└── evaluation_report.md                (evaluation results)

logs/
└── log_2025-05-10.log                 (execution logs)
```

---

## ✅ Verification Checklist

Run these to verify Phase 2:

```bash
# Check files exist
ls -la src/data_processing.py
ls -la src/feature_engineering.py
ls -la src/train_model.py
ls -la src/evaluate_model.py
ls -la src/predict.py

# Check they're importable
python -c "from src.data_processing import DataProcessor; print('✓ DataProcessor')"
python -c "from src.feature_engineering import FeatureEngineer; print('✓ FeatureEngineer')"
python -c "from src.train_model import ModelTrainer; print('✓ ModelTrainer')"
python -c "from src.evaluate_model import ModelEvaluator; print('✓ ModelEvaluator')"
python -c "from src.predict import predict_machine_efficiency; print('✓ PredictionEngine')"

# Run pipeline
python src/pipeline.py
```

---

## 🔍 What Each Module Does

| Module | Input | Process | Output |
|--------|-------|---------|--------|
| DataProcessor | CSV file | Clean, validate | Processed CSV |
| FeatureEngineer | DataFrame | Engineer features | X, y matrices |
| ModelTrainer | X, y data | Train model | Joblib model + JSON metadata |
| ModelEvaluator | Model + test set | Evaluate | Metrics + report |
| PredictionEngine | Model + input dict | Predict | Prediction + probabilities |

---

## 🎯 Next Phase (Phase 3)

Next: Create Flask/FastAPI application that uses these modules to serve predictions as a web API.

Files to create in Phase 3:
- `app/app.py` - Flask/FastAPI application
- `app/requirements.txt` - App dependencies
- Health check endpoint (`GET /health`)
- Prediction endpoint (`POST /predict`)

---

## 📚 Documentation Files

- `PHASE1_COMPLETION_REPORT.md` - Phase 1 summary
- `PHASE2_COMPLETION_REPORT.md` - This phase's detailed report
- `reports/metrics_summary.md` - Model metrics
- `models/model_metadata.json` - Model configuration

---

**Status**: ✅ Phase 2 Complete | Ready for Phase 3  
**Date**: May 10, 2025  
