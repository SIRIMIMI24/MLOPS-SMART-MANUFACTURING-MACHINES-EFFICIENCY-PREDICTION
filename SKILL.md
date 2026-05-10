# SKILL.md

# Smart Manufacturing Machines Efficiency Prediction

# End-to-End Data Science & MLOps Workflow

---

## 1. Purpose

This `SKILL.md` defines the complete end-to-end working standard for the **Smart Manufacturing Machines Efficiency Prediction** project.

The goal of this project is to build a machine learning application that predicts or estimates machine efficiency, starting from notebook experimentation and ending with production-style MLOps deployment.

This skill is designed to guide work across:

- Data Science
- Machine Learning Engineering
- Application Development
- Testing
- Docker Containerization
- Jenkins CI Pipeline
- Kubernetes Deployment
- ArgoCD GitOps Continuous Deployment
- Monitoring and continuous improvement

This file should be used as the project operating standard for humans and AI coding assistants such as ChatGPT, Codex, GitHub Copilot, or other AI coding tools.

---

## 1.1 Current Working Phase

Current phase: **Phase 1 - Notebook-first Experimentation**

The current goal is to create a complete end-to-end modeling notebook before converting logic into production Python scripts.

The AI assistant must follow this phase strictly.

### Allowed in this phase

The assistant may create or modify only the following:

```text
notebooks/01_end_to_end_modeling.ipynb
data/raw/
data/processed/
models/
reports/
README.md
```

Minimal folder creation is allowed only if the folder does not already exist.

### Not allowed in this phase

The assistant must not create or modify the following unless explicitly requested in a later phase:

```text
src/data_processing.py
src/feature_engineering.py
src/train_model.py
src/evaluate_model.py
src/predict.py
Dockerfile
Jenkinsfile
k8s/
argocd/
CI/CD configuration
Kubernetes manifests
ArgoCD manifests
```

### Phase principle

The notebook must prove the data science workflow first.

Productionization will happen only after the notebook logic has been reviewed and approved.

The correct project flow is:

```text
Notebook-first Experimentation
→ Review notebook logic
→ Convert notebook logic into src/*.py
→ Build prediction app
→ Add tests
→ Dockerize
→ Add Jenkins CI
→ Add Kubernetes manifests
→ Add ArgoCD GitOps
→ Add monitoring
```

---

## 1.2 Phase-based Project Roadmap

This project must be developed in phases.

The assistant must not skip phases unless explicitly instructed.

```text
Phase 1: Notebook-first modeling
Phase 2: Convert notebook logic into src/*.py
Phase 3: Add reusable prediction function
Phase 4: Build Flask or FastAPI application
Phase 5: Add unit tests and app tests
Phase 6: Dockerize the application
Phase 7: Add Jenkins CI pipeline
Phase 8: Add Kubernetes manifests
Phase 9: Add ArgoCD GitOps deployment
Phase 10: Add monitoring and continuous improvement
```

Each phase must produce a clear summary:

```text
1. Files created
2. Files modified
3. What was implemented
4. How to run or validate it
5. What should happen in the next phase
```

---

## 2. Project Scope

This project covers the full lifecycle of an MLOps system:

```text
Project Setup
→ Notebook-first Data Science Experiment
→ Data Understanding
→ Data Processing
→ Model Training
→ Model Evaluation
→ Production Code Conversion
→ Prediction Function
→ User App Building
→ Testing
→ Docker Image Build
→ Kubernetes Manifest Creation
→ Jenkins CI Setup
→ GitHub Integration
→ ArgoCD CD Setup
→ Kubernetes Deployment
→ Monitoring & Improvement
```

The project is considered complete only when the trained model can be served through an application and deployed successfully to Kubernetes using Jenkins and ArgoCD.

However, the project must not jump directly to deployment.

The notebook-first phase must be completed before productionization.

---

## 3. Project Architecture

The final target architecture follows a CI/CD and GitOps workflow.

```text
Developer / Data Scientist
        ↓
GitHub Repository
        ↓
Jenkins Continuous Integration
        ↓
Install Dependencies
        ↓
Run Tests
        ↓
Train / Validate Model
        ↓
Build Docker Image
        ↓
Update Kubernetes Manifests
        ↓
GitHub as Source of Truth
        ↓
ArgoCD Continuous Deployment
        ↓
Kubernetes / Minikube
        ↓
Running ML Application
```

Key principle:

```text
GitHub = Source of Truth
Jenkins = CI Engine
ArgoCD = CD / GitOps Engine
Kubernetes = Runtime Environment
Docker = Packaging Layer
```

---

## 4. Main Tools

| Area | Tools |
|---|---|
| Programming | Python |
| Data Processing | pandas, numpy |
| Machine Learning | scikit-learn, joblib |
| Experiment / Notebook | Jupyter Notebook |
| Web Application | Flask or FastAPI |
| Testing | pytest |
| Containerization | Docker |
| CI | Jenkins |
| Source Control | GitHub |
| Deployment | Kubernetes, Minikube |
| CD / GitOps | ArgoCD |
| Optional Monitoring | Prometheus, Grafana, Evidently AI, MLflow |

---

## 5. Roles and Responsibilities

### 5.1 Data Scientist

Responsible for:

- Understanding the business and machine efficiency problem
- Exploring the dataset
- Cleaning and preparing data
- Creating features
- Training machine learning models
- Evaluating model performance
- Saving model artifacts
- Explaining model results
- Documenting assumptions and limitations

### 5.2 ML Engineer / MLOps Engineer

Responsible for:

- Converting notebook logic into reusable scripts
- Building model training and inference pipeline
- Creating Dockerfile
- Creating Kubernetes manifests
- Setting up Jenkins pipeline
- Setting up ArgoCD deployment
- Ensuring reproducibility
- Troubleshooting deployment issues

### 5.3 Developer

Responsible for:

- Building the prediction application
- Connecting the app to the trained model
- Creating input validation
- Handling errors
- Writing tests
- Maintaining clean code structure

### 5.4 Reviewer

Responsible for:

- Reviewing code quality
- Checking model logic
- Checking data leakage risk
- Checking Docker, Kubernetes, Jenkins, and ArgoCD configuration
- Ensuring tests pass
- Approving pull requests

### 5.5 ChatGPT / Codex / AI Coding Assistant

Used for:

- Breaking down tasks
- Generating code drafts
- Reviewing pull requests
- Fixing review comments
- Improving documentation
- Explaining errors
- Suggesting project structure
- Creating test cases

AI tools must not replace human review before merge or deployment.

---

## 6. Repository Structure

Use this structure as the standard project layout:

```text
smart-manufacturing-mlops/
│
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   └── 01_end_to_end_modeling.ipynb
│
├── config/
│   ├── __init__.py
│   └── data_ingestion_config.py
│
├── src/
│   ├── __init__.py
│   ├── custom_exception.py
│   ├── logger.py
│   ├── data_ingestion.py
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
├── app/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── models/
│   ├── model_pipeline.pkl
│   └── model_metadata.json
│
├── reports/
│   ├── metrics/
│   └── figures/
│
├── tests/
│   ├── test_data_processing.py
│   ├── test_model.py
│   ├── test_predict.py
│   └── test_app.py
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   └── service.yaml
│
├── argocd/
│   └── application.yaml
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
├── SKILL.md
├── .gitignore
├── .dockerignore
└── params.yaml
```

### Folder rules

- Use `notebooks/` for exploration and experiment documentation.
- Use `data/raw/` for original datasets.
- Use `data/processed/` for cleaned and model-ready datasets.
- Use `models/` for trained model artifacts.
- Use `reports/` for metrics, charts, and evaluation outputs.
- Use `src/` for production Python code after Phase 1.
- Use `app/` for web application code.
- Use `tests/` for automated tests.
- Use `k8s/` for Kubernetes manifests.
- Use `argocd/` for GitOps configuration.
- Do not commit secrets, credentials, sensitive data, or large raw datasets.

---

# Phase 1: Notebook-first End-to-End Modeling

## Objective

Create one complete notebook that covers the full machine learning workflow from data loading to model evaluation and model artifact saving.

The notebook is the main deliverable of Phase 1.

## Main deliverable

```text
notebooks/01_end_to_end_modeling.ipynb
```

## Supporting folders

Create these folders only if they do not exist:

```text
data/raw/
data/processed/
models/
reports/
notebooks/
```

## Notebook requirements

The notebook must include the following sections:

```text
1. Project introduction
2. Problem statement
3. Import libraries
4. Define project paths
5. Load dataset from data/raw/
6. Basic data understanding
7. Data shape and column review
8. Data type check
9. Missing value check
10. Duplicate check
11. Basic EDA
12. Target variable inspection
13. Problem type identification
14. Feature and target selection
15. Columns to exclude
16. Train/test split
17. Data cleaning
18. Feature engineering
19. Preprocessing pipeline
20. Baseline model training
21. Candidate model training
22. Model evaluation
23. Error analysis
24. Feature importance or model interpretation if applicable
25. Save model artifact to models/
26. Save metric summary to reports/
27. Summary of findings
28. Next step for converting notebook logic into src/*.py
```

---

## Phase 1 Notebook Quality Standard

The notebook must be readable, reproducible, and suitable for later conversion into production code.

### Notebook quality rules

The notebook must:

- Run from top to bottom after restarting the kernel
- Use relative paths from the project root
- Avoid hardcoded local absolute paths
- Define constants and paths at the top
- Include markdown explanation before each major code section
- Explain what is being checked
- Explain why each step matters
- Explain the finding after each major output
- Avoid over-engineering
- Use simple and stable code first
- Avoid unnecessary complex framework setup
- Avoid Docker, Jenkins, Kubernetes, and ArgoCD in Phase 1

### Notebook writing style

Each major notebook section should follow this pattern:

```text
Markdown explanation
→ Code cell
→ Output
→ Short interpretation
```

Example:

```text
What are we checking?
Why does it matter?
What did we find?
What decision should we make next?
```

---

## Phase 1 Data Contract Requirement

Before training any model, the notebook must document the dataset contract.

The notebook must identify:

```text
Dataset filename
Number of rows
Number of columns
Target column
Problem type: regression or classification
ID columns
Date or timestamp columns
Numerical columns
Categorical columns
Columns excluded from modeling
Missing value strategy
Duplicate handling strategy
Train/test split strategy
Evaluation metric
```

### Target rule

The assistant must not assume the problem type without inspecting the target column.

If the target variable is continuous, use regression modeling and regression metrics.

If the target variable is categorical, use classification modeling and classification metrics.

---

## Phase 1 Data Leakage Rules

The notebook must prevent data leakage.

The assistant must follow these rules:

```text
1. Do not use the target variable as a feature.
2. Do not use future information as a feature.
3. Split train/test before fitting preprocessing logic.
4. Fit imputation only on training data.
5. Fit scaling only on training data.
6. Fit encoding only on training data.
7. Do not use test data during model training.
8. Check duplicate records across train/test if applicable.
9. Document any feature that may cause leakage.
```

Recommended implementation:

Use `Pipeline` and `ColumnTransformer` from scikit-learn where possible.

---

## Phase 1 Preprocessing Standard

The notebook should use a preprocessing pipeline that can later be moved into production code.

Recommended approach:

```text
Numerical features
→ Missing value imputation
→ Scaling if needed

Categorical features
→ Missing value imputation
→ One-hot encoding
```

Recommended tools:

```text
sklearn.pipeline.Pipeline
sklearn.compose.ColumnTransformer
sklearn.impute.SimpleImputer
sklearn.preprocessing.OneHotEncoder
sklearn.preprocessing.StandardScaler
```

The preprocessing logic must be fitted only on the training data.

---

## Phase 1 Baseline Model Standard

The notebook must compare a candidate model against a simple baseline model.

### For regression problems

Minimum models:

```text
DummyRegressor
LinearRegression or RandomForestRegressor
```

Minimum metrics:

```text
MAE
RMSE
R-squared
```

### For classification problems

Minimum models:

```text
DummyClassifier
LogisticRegression or RandomForestClassifier
```

Minimum metrics:

```text
Accuracy
Precision
Recall
F1-score
ROC-AUC if applicable
Confusion matrix
```

A candidate model is useful only if it improves meaningfully over the baseline model.

---

## Phase 1 Evaluation Standard

The notebook must include both technical evaluation and business interpretation.

### For regression

The notebook should include:

```text
MAE
RMSE
R-squared
Actual vs Predicted analysis
Residual analysis
Top error cases
Business interpretation of error size
```

### For classification

The notebook should include:

```text
Accuracy
Precision
Recall
F1-score
ROC-AUC if applicable
Confusion matrix
Classification report
Wrong prediction analysis
Business interpretation of model errors
```

### Business interpretation

The notebook must answer:

```text
Is the model better than baseline?
Is the error acceptable?
Where does the model perform poorly?
What are the possible business risks?
Should this model be converted into production code?
What should be improved next?
```

---

## Phase 1 Model Artifact Standard

The model artifact must be saved in a reproducible format.

Recommended output:

```text
models/
├── model_pipeline.pkl
└── model_metadata.json
```

The saved model pipeline should include both preprocessing and model steps when possible.

The metadata file should include:

```text
model_name
problem_type
target_column
feature_columns
excluded_columns
train_rows
test_rows
train_test_split_ratio
random_state
evaluation_metrics
created_date
limitations
next_steps
```

Example metadata structure:

```json
{
  "model_name": "RandomForestRegressor",
  "problem_type": "regression",
  "target_column": "machine_efficiency",
  "feature_columns": ["feature_1", "feature_2"],
  "excluded_columns": ["machine_id"],
  "train_rows": 1000,
  "test_rows": 250,
  "train_test_split_ratio": 0.2,
  "random_state": 42,
  "evaluation_metrics": {
    "mae": 0.12,
    "rmse": 0.18,
    "r2": 0.86
  },
  "limitations": [
    "Model has not yet been validated in production.",
    "Feature drift has not yet been monitored."
  ],
  "next_steps": [
    "Convert notebook logic into src/data_processing.py",
    "Convert model training logic into src/train_model.py",
    "Create reusable prediction function in src/predict.py"
  ]
}
```

---

## Phase 1 Definition of Done

Phase 1 is complete only when all items below are done.

```text
[ ] notebooks/01_end_to_end_modeling.ipynb exists
[ ] Notebook runs from top to bottom
[ ] Dataset is loaded from data/raw/
[ ] Target variable is identified
[ ] Problem type is identified
[ ] Basic EDA is completed
[ ] Missing values are reviewed
[ ] Duplicates are reviewed
[ ] Data types are reviewed
[ ] Feature columns are selected
[ ] Train/test split is reproducible
[ ] Preprocessing pipeline is created
[ ] Baseline model is trained
[ ] Candidate model is trained
[ ] Evaluation metrics are reported
[ ] Error analysis is included
[ ] Business interpretation is included
[ ] Model artifact is saved under models/
[ ] Model metadata is saved
[ ] Next-step conversion plan is documented
[ ] No Docker/Jenkins/Kubernetes/ArgoCD files are created
```

---

# Phase 2: Convert Notebook Logic into src/*.py

## Objective

Convert the reviewed notebook logic into reusable production Python scripts.

## Expected files

```text
src/data_ingestion.py
src/data_processing.py
src/feature_engineering.py
src/train_model.py
src/evaluate_model.py
src/predict.py
src/logger.py
src/custom_exception.py
```

## Requirements

- Extract data loading logic into `src/data_ingestion.py`
- Extract data cleaning logic into `src/data_processing.py`
- Extract feature engineering logic into `src/feature_engineering.py`
- Extract model training logic into `src/train_model.py`
- Extract evaluation logic into `src/evaluate_model.py`
- Extract prediction logic into `src/predict.py`
- Add logging and custom exception handling if appropriate
- Keep code simple and readable
- Ensure scripts can run independently
- Do not add Docker, Jenkins, Kubernetes, or ArgoCD yet

## Expected commands

```bash
python src/data_ingestion.py
python src/data_processing.py
python src/train_model.py
python src/evaluate_model.py
```

---

# Phase 3: Reusable Prediction Function

## Objective

Create reusable prediction logic that can be called by an application.

## Expected file

```text
src/predict.py
```

## Requirements

- Load the saved model pipeline from `models/model_pipeline.pkl`
- Validate input data
- Convert input dictionary into model-ready format
- Run prediction
- Return a clear prediction response
- Handle errors gracefully
- Do not build the web app yet

## Expected function

```python
def predict_machine_efficiency(input_data: dict) -> dict:
    # Return machine efficiency prediction result.
    pass
```

---

# Phase 4: Build Prediction App

## Objective

Build a simple prediction application using Flask or FastAPI.

## Expected file

```text
app/app.py
```

## Minimum endpoints

```text
GET /health
POST /predict
```

## Requirements

- Create health check endpoint
- Create prediction endpoint
- Reuse `src/predict.py`
- Validate request input
- Return clear JSON response
- Return clear error response for invalid input
- Ensure the app can run locally

## Example command

```bash
python app/app.py
```

---

# Phase 5: Testing

## Objective

Add tests for data processing, model loading, prediction logic, and app endpoints.

## Expected files

```text
tests/test_data_processing.py
tests/test_model.py
tests/test_predict.py
tests/test_app.py
```

## Requirements

- Unit tests must be simple and stable
- Tests must run locally
- App endpoints must be tested
- Prediction function must be tested
- Model loading must be tested

## Expected command

```bash
pytest tests/
```

---

# Phase 6: Docker

## Objective

Dockerize the ML prediction application.

## Expected files

```text
Dockerfile
.dockerignore
```

## Requirements

- Use a stable Python slim base image
- Copy `requirements.txt`
- Install dependencies
- Copy application code
- Ensure model artifact is available in the container
- Expose the correct app port
- Start the app correctly
- Do not hardcode credentials

## Example Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app/app.py"]
```

## Expected commands

```bash
docker build -t smart-manufacturing-mlops:latest .
docker run -p 5000:5000 smart-manufacturing-mlops:latest
```

---

# Phase 7: Jenkins CI

## Objective

Add Jenkins CI pipeline.

## Expected file

```text
Jenkinsfile
```

## Minimum Jenkins stages

```text
Checkout
Setup Python Environment
Install Dependencies
Run Tests
Build Docker Image
```

## Requirements

- Jenkins must checkout the GitHub repository
- Jenkins must create Python environment
- Jenkins must install dependencies
- Jenkins must run tests
- Jenkins must build Docker image
- Pipeline must fail when tests fail
- Credentials must not be hardcoded

## Example Jenkinsfile

```groovy
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'smart-manufacturing-mlops'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && python -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Please check logs.'
        }
    }
}
```

---

# Phase 8: Kubernetes

## Objective

Create Kubernetes manifests for the ML application.

## Expected files

```text
k8s/namespace.yaml
k8s/deployment.yaml
k8s/service.yaml
```

## Requirements

- Use correct Docker image name
- Use correct container port
- Add resource requests and limits if appropriate
- Add readiness and liveness probes if possible
- Validate YAML with dry-run
- Do not add ArgoCD yet

## Expected commands

```bash
kubectl apply --dry-run=client -f k8s/
kubectl apply -f k8s/
kubectl get pods
kubectl get svc
```

For Minikube:

```bash
minikube service smart-manufacturing-service
```

---

# Phase 9: ArgoCD GitOps

## Objective

Add ArgoCD GitOps configuration.

## Expected file

```text
argocd/application.yaml
```

## Requirements

- Configure ArgoCD to watch the `k8s/` folder
- Use GitHub repository as the source of truth
- Ensure target namespace is correct
- Do not hardcode secrets
- Document how to apply the ArgoCD application

## Expected command

```bash
kubectl apply -f argocd/application.yaml
```

## GitOps deployment flow

```text
Update deployment.yaml
→ Push to GitHub
→ ArgoCD detects change
→ ArgoCD syncs application
→ Kubernetes updates pods
→ New app version runs
```

---

# Phase 10: Monitoring and Continuous Improvement

## Objective

Add basic monitoring and improvement plan for the deployed ML application.

## Minimum monitoring

- Pod status
- Service status
- `/health` endpoint
- `/predict` endpoint
- Application logs
- Failed prediction logs
- Prediction distribution
- Resource usage
- Data drift
- Concept drift
- Model performance decay

## Optional tools

- Prometheus
- Grafana
- Evidently AI
- MLflow

## Useful commands

```bash
kubectl get pods
kubectl get svc
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

---

# Branching Strategy

Use the following branch structure:

```text
main          = stable production-ready branch
dev           = integration branch
feature/*     = new feature
fix/*         = bug fix
ml/*          = model or data science work
ci/*          = Jenkins or CI changes
deploy/*      = Kubernetes or ArgoCD changes
docs/*        = documentation changes
```

Rules:

- Do not commit directly to `main`
- Use pull requests for all changes
- Require review before merge
- Run Jenkins pipeline before merge
- Keep pull requests small and focused

---

# Commit Message Standard

Use clear commit messages.

Format:

```text
<type>: <short description>
```

Examples:

```text
feat: add machine efficiency prediction app
fix: correct missing value handling in data processing
model: add random forest training pipeline
test: add unit test for prediction function
ci: add Jenkins pipeline
deploy: add Kubernetes deployment manifest
docs: update MLOps workflow documentation
```

Common types:

```text
feat     = new feature
fix      = bug fix
model    = model-related change
data     = data processing change
test     = testing change
ci       = CI pipeline change
deploy   = deployment change
docs     = documentation change
refactor = code improvement without behavior change
```

---

# Pull Request Standard

Every PR must include:

- Objective
- Summary of changes
- Files changed
- Testing result
- Risk or limitation
- Screenshots if UI changed
- Deployment note if deployment files changed

PR checklist:

```text
[ ] PR title is clear
[ ] PR description is complete
[ ] Code is scoped to the task
[ ] Tests pass locally
[ ] Jenkins pipeline passes
[ ] Docker build passes if app changed
[ ] Kubernetes dry-run passes if YAML changed
[ ] No secrets are committed
[ ] Documentation is updated
```

---

# Security and Privacy Rules

Do not commit:

- API keys
- GitHub tokens
- Jenkins credentials
- Cloud credentials
- Passwords
- Private keys
- Raw sensitive data
- Customer personal information
- Large raw datasets
- Large model artifacts

Use:

- `.env.example` for sample environment variables
- Jenkins credentials manager for secrets
- Kubernetes secrets for runtime secrets
- `.gitignore` to prevent accidental commits
- Git LFS, DVC, or object storage for large data/model files

Security checklist:

```text
[ ] No secrets in GitHub
[ ] No credentials in Dockerfile
[ ] No credentials in Jenkinsfile
[ ] No sensitive data in logs
[ ] .env is ignored
[ ] .env.example is safe
[ ] Large data/model files are not committed directly
```

---

# Data Leakage Checklist

Before approving model code, check:

```text
[ ] Target variable is not used as feature
[ ] Future information is not used during training
[ ] Train/test split happens before leakage-prone transformations
[ ] Scaling is fit only on training data
[ ] Encoding is fit only on training data
[ ] Imputation is fit only on training data
[ ] Duplicate rows across train/test are reviewed
[ ] Evaluation data is not used during training
[ ] Business logic does not leak the answer
```

---

# Model Reproducibility Checklist

```text
[ ] Random seed is fixed
[ ] Library versions are defined
[ ] Training script can be rerun
[ ] Dataset location is documented
[ ] Parameters are documented
[ ] Model artifact is saved
[ ] Model metadata is saved
[ ] Evaluation metric is reproducible
[ ] Notebook results are converted into scripts after review
```

---

# Local Development Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run notebook:

```bash
jupyter notebook notebooks/01_end_to_end_modeling.ipynb
```

Run data processing:

```bash
python src/data_processing.py
```

Train model:

```bash
python src/train_model.py
```

Evaluate model:

```bash
python src/evaluate_model.py
```

Run app:

```bash
python app/app.py
```

Run tests:

```bash
pytest tests/
```

Build Docker image:

```bash
docker build -t smart-manufacturing-mlops:latest .
```

Run Docker container:

```bash
docker run -p 5000:5000 smart-manufacturing-mlops:latest
```

Validate Kubernetes YAML:

```bash
kubectl apply --dry-run=client -f k8s/
```

Deploy to Kubernetes:

```bash
kubectl apply -f k8s/
```

Check pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get svc
```

---

# Common Issues and Fixes

## Docker Permission Denied

Issue:

```text
permission denied while trying to connect to the Docker daemon socket
```

Fix:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

For Jenkins:

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

## Kubernetes Pod Not Running

Check:

```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

Common causes:

- Wrong Docker image name
- Image pull error
- App port mismatch
- Missing model file
- Python dependency error

---

## ArgoCD OutOfSync

Check:

```bash
argocd app get <app-name>
argocd app sync <app-name>
```

Common causes:

- GitHub manifest changed but not synced
- Invalid Kubernetes YAML
- Wrong ArgoCD path
- Cluster permission issue

---

## App Cannot Load Model

Check:

- Is `models/model_pipeline.pkl` included in Docker image?
- Is the model path correct?
- Is the model trained before app starts?
- Is `joblib` installed?
- Is preprocessing logic included in the saved pipeline?

---

# AI Execution Prompts

## AI Execution Prompt: Phase 1 Notebook-first

Use this prompt when asking ChatGPT, Codex, GitHub Copilot, or any AI coding assistant to start Phase 1.

```text
Please read SKILL.md first and follow the Current Working Phase strictly.

Current task:
Create the Phase 1 notebook-first workflow for the Smart Manufacturing Machines Efficiency Prediction project.

Requirements:
1. Inspect the current repository structure.
2. Do not create production src/*.py modules yet.
3. Do not create Dockerfile.
4. Do not create Jenkinsfile.
5. Do not create Kubernetes manifests.
6. Do not create ArgoCD manifests.
7. Do not add CI/CD configuration yet.
8. Create only the minimal folders needed if missing:
   - notebooks/
   - data/raw/
   - data/processed/
   - models/
   - reports/
9. Create notebooks/01_end_to_end_modeling.ipynb.
10. The notebook must cover:
   - project introduction
   - problem statement
   - import libraries
   - define project paths
   - load dataset from data/raw/
   - data understanding
   - data shape and column review
   - data type check
   - missing value check
   - duplicate check
   - basic EDA
   - target variable inspection
   - problem type identification
   - feature selection
   - columns to exclude
   - train/test split
   - preprocessing pipeline
   - baseline model training
   - candidate model training
   - model evaluation
   - error analysis
   - business interpretation
   - save model artifact to models/
   - save model metadata
   - summary of findings
   - next steps for converting notebook logic into src/*.py
11. Use simple, stable, readable code.
12. Add markdown explanation before every major code section.
13. Make the notebook runnable from top to bottom after restarting the kernel.
14. Use scikit-learn Pipeline and ColumnTransformer where possible.
15. Prevent data leakage by fitting preprocessing only on training data.
16. Do not over-engineer.
17. Keep all changes scoped to Phase 1.

After finishing, summarize:
1. Files created
2. Files modified
3. What the notebook covers
4. How to run the notebook
5. What should be converted into src/*.py in the next phase
```

---

## AI Execution Prompt: Phase 2 Convert Notebook to src

```text
Please read SKILL.md first and follow Phase 2 only.

Current task:
Convert the reviewed notebook logic from notebooks/01_end_to_end_modeling.ipynb into reusable production Python scripts under src/.

Requirements:
1. Do not change the notebook unless necessary.
2. Extract data loading logic into src/data_ingestion.py.
3. Extract data cleaning logic into src/data_processing.py.
4. Extract feature engineering logic into src/feature_engineering.py.
5. Extract model training logic into src/train_model.py.
6. Extract evaluation logic into src/evaluate_model.py.
7. Extract reusable prediction logic into src/predict.py.
8. Add config files if needed.
9. Add logging and custom exception handling if appropriate.
10. Keep the implementation simple and readable.
11. Ensure scripts can run independently.
12. Do not add Docker, Jenkins, Kubernetes, or ArgoCD yet.

Expected commands:
python src/data_ingestion.py
python src/data_processing.py
python src/train_model.py
python src/evaluate_model.py

After finishing, summarize:
1. Files created
2. Files modified
3. Logic converted from notebook
4. How to run each script
5. What should happen in Phase 3
```

---

## AI Execution Prompt: Phase 3 Prediction Function

```text
Please read SKILL.md first and follow Phase 3 only.

Current task:
Create reusable prediction logic that can be called by an application.

Requirements:
1. Create or update src/predict.py.
2. Load the saved model pipeline from models/model_pipeline.pkl.
3. Validate input data.
4. Convert input dictionary into model-ready format.
5. Run prediction.
6. Return a clear prediction response.
7. Handle errors gracefully.
8. Do not build the web app yet.
9. Do not add Docker, Jenkins, Kubernetes, or ArgoCD yet.

Expected function:

def predict_machine_efficiency(input_data: dict) -> dict:
    pass

After finishing, summarize:
1. Files created
2. Files modified
3. How prediction works
4. Example input
5. Example output
6. What should happen in Phase 4
```

---

## AI Execution Prompt: Phase 4 Build App

```text
Please read SKILL.md first and follow Phase 4 only.

Current task:
Build a simple prediction application using Flask or FastAPI.

Requirements:
1. Create app/app.py.
2. Add GET /health endpoint.
3. Add POST /predict endpoint.
4. Reuse src/predict.py for prediction logic.
5. Validate request input.
6. Return clear JSON response.
7. Return clear error response for invalid input.
8. Ensure the app can run locally.
9. Do not add Docker, Jenkins, Kubernetes, or ArgoCD yet.

Expected endpoints:
GET /health
POST /predict

After finishing, summarize:
1. Files created
2. Files modified
3. How to run the app locally
4. Example curl command
5. What should happen in Phase 5
```

---

## AI Execution Prompt: Phase 5 Testing

```text
Please read SKILL.md first and follow Phase 5 only.

Current task:
Add tests for data processing, model loading, prediction logic, and app endpoints.

Requirements:
1. Create tests/ folder if missing.
2. Add test_data_processing.py if applicable.
3. Add test_model.py.
4. Add test_predict.py.
5. Add test_app.py.
6. Ensure pytest can run locally.
7. Keep tests simple and stable.
8. Do not add Docker, Jenkins, Kubernetes, or ArgoCD yet.

Expected command:
pytest tests/

After finishing, summarize:
1. Files created
2. Files modified
3. Tests added
4. How to run tests
5. What should happen in Phase 6
```

---

## AI Execution Prompt: Phase 6 Docker

```text
Please read SKILL.md first and follow Phase 6 only.

Current task:
Dockerize the ML prediction application.

Requirements:
1. Create Dockerfile.
2. Use a stable Python slim base image.
3. Copy requirements.txt.
4. Install dependencies.
5. Copy application code.
6. Ensure model artifact is available in the container.
7. Expose the correct app port.
8. Start the app correctly.
9. Add .dockerignore if needed.
10. Do not add Jenkins, Kubernetes, or ArgoCD yet.

Expected commands:
docker build -t smart-manufacturing-mlops:latest .
docker run -p 5000:5000 smart-manufacturing-mlops:latest

After finishing, summarize:
1. Files created
2. Files modified
3. Docker image build command
4. Docker run command
5. What should happen in Phase 7
```

---

## AI Execution Prompt: Phase 7 Jenkins CI

```text
Please read SKILL.md first and follow Phase 7 only.

Current task:
Add Jenkins CI pipeline.

Requirements:
1. Create Jenkinsfile.
2. Add checkout stage.
3. Add Python environment setup stage.
4. Add dependency installation stage.
5. Add pytest stage.
6. Add Docker build stage.
7. Do not hardcode credentials.
8. Do not add Kubernetes or ArgoCD yet.

Expected Jenkins stages:
Checkout
Setup Python Environment
Install Dependencies
Run Tests
Build Docker Image

After finishing, summarize:
1. Files created
2. Files modified
3. Jenkins stages added
4. Required Jenkins setup
5. What should happen in Phase 8
```

---

## AI Execution Prompt: Phase 8 Kubernetes

```text
Please read SKILL.md first and follow Phase 8 only.

Current task:
Create Kubernetes manifests for the ML application.

Requirements:
1. Create k8s/namespace.yaml.
2. Create k8s/deployment.yaml.
3. Create k8s/service.yaml.
4. Use correct Docker image name.
5. Use correct container port.
6. Add readiness and liveness probes if possible.
7. Add resource requests and limits if appropriate.
8. Validate YAML with kubectl dry-run.
9. Do not add ArgoCD yet.

Expected commands:
kubectl apply --dry-run=client -f k8s/
kubectl apply -f k8s/
kubectl get pods
kubectl get svc

After finishing, summarize:
1. Files created
2. Files modified
3. Kubernetes resources added
4. How to deploy locally
5. What should happen in Phase 9
```

---

## AI Execution Prompt: Phase 9 ArgoCD

```text
Please read SKILL.md first and follow Phase 9 only.

Current task:
Add ArgoCD GitOps configuration.

Requirements:
1. Create argocd/application.yaml.
2. Configure ArgoCD to watch the k8s/ folder.
3. Use GitHub repository as the source of truth.
4. Ensure target namespace is correct.
5. Do not hardcode secrets.
6. Document how to apply the ArgoCD application.

Expected command:
kubectl apply -f argocd/application.yaml

After finishing, summarize:
1. Files created
2. Files modified
3. ArgoCD application configuration
4. How GitOps deployment works
5. What should happen in Phase 10
```

---

## AI Execution Prompt: Phase 10 Monitoring

```text
Please read SKILL.md first and follow Phase 10 only.

Current task:
Add basic monitoring and improvement plan for the deployed ML application.

Requirements:
1. Document minimum monitoring checks.
2. Add health check validation.
3. Add prediction logging recommendation.
4. Add model drift monitoring recommendation.
5. Add retraining trigger recommendation.
6. Add troubleshooting commands.
7. Keep implementation simple.

Minimum monitoring:
- Pod status
- Service status
- /health endpoint
- /predict endpoint
- Application logs
- Failed prediction logs
- Prediction distribution
- Resource usage

After finishing, summarize:
1. Files created
2. Files modified
3. Monitoring plan
4. Troubleshooting commands
5. Future improvement plan
```

---

# Final Definition of Done

The full project is done only when all items below are completed.

## Data Science Done

```text
[ ] Dataset is understood
[ ] Notebook-first experiment is completed
[ ] Data processing script works
[ ] Feature engineering script works
[ ] Model training script works
[ ] Model evaluation script works
[ ] Model artifact is saved
[ ] Model metadata is saved
[ ] Prediction function works
```

## Application Done

```text
[ ] App starts locally
[ ] Health endpoint works
[ ] Prediction endpoint works
[ ] Invalid input is handled
[ ] Model loads correctly
[ ] App returns prediction result
```

## Testing Done

```text
[ ] Unit tests exist
[ ] pytest passes
[ ] Model loading test passes
[ ] Prediction test passes
[ ] App endpoint test passes
[ ] Docker build test passes
```

## Docker Done

```text
[ ] Dockerfile exists
[ ] Docker image builds successfully
[ ] Docker container runs successfully
[ ] App is accessible in container
```

## Kubernetes Done

```text
[ ] Deployment YAML exists
[ ] Service YAML exists
[ ] Namespace YAML exists
[ ] YAML dry-run passes
[ ] App runs on Kubernetes / Minikube
[ ] Service is accessible
```

## Jenkins Done

```text
[ ] Jenkinsfile exists
[ ] Jenkins can checkout GitHub repo
[ ] Jenkins installs dependencies
[ ] Jenkins runs tests
[ ] Jenkins builds Docker image
[ ] CI pipeline passes
```

## ArgoCD Done

```text
[ ] ArgoCD is installed
[ ] ArgoCD can access GitHub repo
[ ] ArgoCD Application exists
[ ] ArgoCD syncs successfully
[ ] ArgoCD status is Healthy
[ ] App is deployed through GitOps flow
```

## Documentation Done

```text
[ ] README.md is updated
[ ] SKILL.md is updated
[ ] Setup steps are documented
[ ] Run commands are documented
[ ] Deployment steps are documented
[ ] Troubleshooting steps are documented
```

---

# Final Workflow Summary

The complete project workflow is:

```text
1. Setup project structure
2. Create notebook-first end-to-end modeling workflow
3. Understand dataset
4. Process data
5. Train baseline and candidate models
6. Evaluate model
7. Save model artifact and metadata
8. Convert notebook logic into src/*.py
9. Build reusable prediction function
10. Build prediction app
11. Write tests
12. Build Docker image
13. Create Jenkins CI pipeline
14. Create Kubernetes manifests
15. Setup ArgoCD GitOps
16. Deploy app to Kubernetes
17. Monitor app
18. Improve model and pipeline continuously
```

Core principle:

```text
Plan → Notebook → Review → Script → Test → Package → Deploy → Monitor → Improve
```

This project should not be treated as only a machine learning notebook project.

It should be treated as a production-style MLOps project where model, code, container, CI/CD, GitOps, and deployment are managed together.

However, the project must always start with notebook-first experimentation before productionization.
