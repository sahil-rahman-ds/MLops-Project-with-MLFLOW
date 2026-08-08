# 🍷 Wine Quality Prediction using MLOps

An end-to-end Machine Learning Operations (MLOps) project for predicting wine quality using a modular pipeline architecture. The project automates data ingestion, validation, transformation, model training, evaluation, and deployment through a FastAPI web application.

---

## 📌 Project Overview

This project demonstrates the complete lifecycle of a machine learning model following MLOps best practices.

The pipeline includes:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation
- Prediction Pipeline
- FastAPI Deployment
- MLflow Experiment Tracking
- Docker Support

---

## 📂 Project Structure

```
.
├── artifacts/
│   ├── data_ingestion/
│   ├── data_validation/
│   ├── data_transformation/
│   ├── model_trainer/
│   └── model_evaluation/
│
├── config/
│   └── config.yaml
│
├── logs/
├── mlruns/
├── research/
│
├── mlProject/
│   ├── components/
│   ├── config/
│   ├── constants/
│   ├── entity/
│   ├── pipeline/
│   ├── utils/
│   └── __init__.py
│
├── static/
├── templates/
│
├── app.py
├── main.py
├── Dockerfile
├── params.yaml
├── schema.yaml
├── setup.py
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- Modular project architecture
- YAML-based configuration
- Data validation using schema
- Feature engineering
- ElasticNet model training
- MLflow experiment tracking
- FastAPI web interface
- Docker support
- Production-ready prediction pipeline


## ⚙️ Installation

### Clone Repository

```bash
git clone <https://github.com/sahil-rahman-ds/MLops-Project-with-MLFLOW>
```

```bash
cd <MLops-Project-with-MLFLOW>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

Run this in the terminal before running the pipeline:

```bash

$env:MLFLOW_TRACKING_URI="https://dagshub.com/sahil-rahman-ds/MLops-Project-with-MLFLOW.mlflow"

$env:MLFLOW_TRACKING_USERNAME="sahil-rahman-ds" 

$env:MLFLOW_TRACKING_PASSWORD="10d156914dbfaac02412bcf571e182d0cabd7edc"

```
---

## ▶️ Run Training Pipeline

Run the entire ML pipeline

```bash
python main.py
```

This executes:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation

Artifacts are stored inside the **artifacts/** folder.

---

## ▶️ Run FastAPI Application

Start the FastAPI server

```bash
uvicorn app:app --reload
```

Application URL

```
http://127.0.0.1:8000
```

---

## 🌐 API Endpoints

### Home

```
GET /
```

Displays the prediction form.

---

### Train Model

```
GET /train
```

Runs the complete training pipeline.

---

### Predict

```
POST /predict
```

Accepts wine feature values and predicts wine quality.

---

## 📊 MLflow

Launch MLflow UI

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```


## 📁 Configuration Files

### config.yaml

Stores project paths.

### params.yaml

Stores model hyperparameters.

### schema.yaml

Stores dataset schema used for validation.

---

## 🧠 Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Prediction Pipeline
      │
      ▼
FastAPI Web Application
```

---


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## 📦 Artifacts

The project automatically generates:

- Trained Model
- Processed Dataset
- Validation Report
- Evaluation Metrics

inside the **artifacts/** directory.

---

## 📜 License

This project is licensed under the terms of the **[MIT License](LICENSE)** - see the **`LICENSE`** file for details.

---

## 👤 Author

[sahil-rahman-ds](https://github.com/sahil-rahman-ds)
