# Student Exam Performance Indicator - End-to-End Machine Learning Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An end-to-end machine learning web application that predicts a student's **Math Score** based on demographic and academic performance indicators (such as reading score, writing score, gender, race/ethnicity, parental education, lunch type, and test preparation course).

---

## 📌 Project Overview

Understanding the factors that impact student performance helps educators identify areas where additional support is required. This repository contains a production-ready machine learning lifecycle implementation:
- **Data Ingestion & Preprocessing**: Automated train-test splitting, missing value imputation, one-hot encoding, and feature scaling.
- **Model Training & Benchmarking**: Evaluation and hyperparameter tuning across multiple algorithms (Linear Regression, Random Forest, Gradient Boosting, Decision Tree, XGBoost, CatBoost, AdaBoost, KNN) using `GridSearchCV`.
- **Inference Pipeline**: Modular prediction pipeline with cross-version scikit-learn compatibility.
- **Web Interface**: Clean, responsive, and centralized Flask frontend for real-time predictions.

---

## 🏗️ Project Directory Structure

```text
ML_PROJECT/
│
├── artifacts/                  # Persisted artifacts (models, preprocessor, datasets)
│   ├── model.pkl               # Best performing trained regression model
│   ├── preprocessor.pkl        # Fitted ColumnTransformer (scaling & encoding)
│   ├── raw.csv                 # Extracted raw dataset
│   ├── train.csv               # Training split
│   └── test.csv                # Testing split
│
├── notebook/                   # Research & exploratory notebooks
│   ├── data/
│   │   └── stud.csv            # Original student performance dataset
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/                        # Core Python package
│   ├── components/             # ML pipeline components
│   │   ├── data_ingestion.py       # Ingests data and creates train/test splits
│   │   ├── data_transformation.py  # Applies ColumnTransformer preprocessing
│   │   └── model_trainer.py        # Trains & tunes models, exports best model
│   │
│   ├── pipeline/               # Application pipelines
│   │   ├── predict_pipeline.py     # Inference logic with CustomData mapping
│   │   └── train_pipeline.py       # Training orchestration pipeline
│   │
│   ├── exception.py            # Custom exception handling with line/script tracking
│   ├── logger.py               # Timestamped execution logging
│   └── utils.py                # Utilities for serialization and model evaluation
│
├── templates/                  # Frontend HTML templates
│   ├── index.html              # Centralized landing page
│   └── home.html               # Centralized prediction form & result display
│
├── app.py                      # Flask web application entry point
├── requirements.txt            # Project dependencies
├── setup.py                    # Package setup script
└── README.md                   # Project documentation
```

---

## ⚙️ Input Features

The model takes 7 inputs to predict the final **Math Score (0–100)**:

| Feature | Type | Valid Values |
| :--- | :--- | :--- |
| **Gender** | Categorical | `Male`, `Female` |
| **Race / Ethnicity** | Categorical | `Group A`, `Group B`, `Group C`, `Group D`, `Group E` |
| **Parental Education** | Categorical | `Associate's degree`, `Bachelor's degree`, `High school`, `Master's degree`, `Some college`, `Some high school` |
| **Lunch Type** | Categorical | `Standard`, `Free/Reduced` |
| **Test Preparation** | Categorical | `None`, `Completed` |
| **Reading Score** | Numerical | `0` to `100` |
| **Writing Score** | Numerical | `0` to `100` |

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/muhammadbinijaz17/ML_PROJECT.git
cd ML_PROJECT
```

### 2. Set Up a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🌐 Running the Web Application

Launch the Flask development server:

```bash
python app.py
```

Once running, visit in your browser:
- **Landing Page**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Predictor Page**: [http://127.0.0.1:5000/predictdata](http://127.0.0.1:5000/predictdata)

---

## 🔄 Retraining the Model (Optional)

To rerun data ingestion, preprocessing, and model training from scratch:

```bash
python src/components/data_ingestion.py
```

This will automatically:
1. Ingest `notebook/data/stud.csv` and split into `train.csv` and `test.csv`.
2. Fit feature transformations and save `artifacts/preprocessor.pkl`.
3. Benchmark models, pick the best one, and save `artifacts/model.pkl`.

---

## 🧪 Programmatic Inference Example

You can also run predictions directly from Python scripts:

```python
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Prepare input data
data = CustomData(
    gender="female",
    race_ethnicity="group B",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="none",
    reading_score=72.0,
    writing_score=74.0
)

# Convert to DataFrame
df = data.get_data_as_dataframe()

# Run prediction
pipeline = PredictPipeline()
result = pipeline.predict(df)
print(f"Predicted Math Score: {result[0]:.2f}")
```

---

## 🛡️ Robustness & Compatibility

- **Scikit-Learn Version Compatibility**: Features an automatic compatibility layer in `predict_pipeline.py` allowing artifacts to work smoothly across scikit-learn $\ge 1.3$ and modern $1.9+$ environments without attribute errors.
- **Form Validation & Safe Fallback**: Form inputs are validated with friendly error alerts to prevent server crashes.
- **Detailed Logging**: Logs are maintained in `logs/` for tracking and debugging.

---

## 👤 Author

- **Muhammad Bin Ijaz**
- Email: [muhammadbinijaz17@gmail.com](mailto:muhammadbinijaz17@gmail.com)
- GitHub: [@muhammadbinijaz17](https://github.com/muhammadbinijaz17)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).