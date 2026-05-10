# Smart Manufacturing Machines Efficiency Prediction

This repository is an MLOps project for predicting smart manufacturing machine efficiency.

## Phase 1 Scope

Phase 1 prepares the project structure only. Model training, prediction logic, application endpoints, CI hardening, Kubernetes deployment tuning, and ArgoCD repository configuration will be implemented in later phases.

## Phase 2.1 Notebook Experimentation

The first modeling workflow is documented in `notebooks/01_end_to_end_modeling.ipynb`. This notebook loads the raw dataset from `data/raw/`, performs basic data understanding and EDA, defines `Efficiency_Status` as the target variable, trains a simple baseline classifier, evaluates it, and saves a notebook-phase model artifact to `models/`.

## Project Layout

- `data/raw/`: raw data location; do not commit large datasets.
- `data/processed/`: processed data location; do not commit large generated files.
- `artifacts/raw/`: project-standard raw artifact location from `SKILL.md`.
- `artifacts/processed/`: project-standard processed artifact location from `SKILL.md`.
- `notebooks/`: exploratory notebooks.
- `src/`: production Python modules.
- `app/`: web application code.
- `models/`: model artifacts; do not commit large binary artifacts.
- `tests/`: automated tests.
- `k8s/`: Kubernetes manifests.
- `argocd/`: ArgoCD application manifest.

## Local Setup

```bash
python -m venv venv
pip install -r requirements.txt
```

## Security

Do not commit secrets, credentials, private keys, raw sensitive data, or large generated artifacts.
