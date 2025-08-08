
# Diabetics Prediction App

A **machine learning web application** that predicts whether an individual is likely to have diabetes based on several health parameters. The app uses the **Pima Indians Diabetes dataset** and provides predictions through a **Flask** web interface.

---

## Overview

This application allows users to input 8 health-related parameters and receive a prediction on diabetes likelihood. It uses a trained ML model with a user-friendly interface.

---

## Objective

* Train a Support Vector Machine model on real-world diabetes data.
* Deploy the model via a lightweight Flask web app.
* Provide an interactive frontend for quick predictions.

---

## Tech Stack

| Component       | Tools / Libraries |
| --------------- | ----------------- |
| Language        | Python            |
| Framework       | Flask             |
| Data Processing | Pandas, NumPy     |
| Model Building  | scikit-learn      |
| Frontend        | HTML, CSS         |

---

## Project Structure

```
Diabeticsapp/
│
├── DiabetesPrediction.ipynb   # Model training and preprocessing
├── app.py                      # Flask application
├── diabetes.csv                # Dataset
├── model.pkl                   # Trained ML model
├── scaler.pkl                  # Feature scaler
├── requirements.txt            # Dependencies
├── templates/
│   └── index.html              # User input form
└── README.md                   # Documentation
```

---

## Dataset

* **Dataset**: Pima Indians Diabetes Dataset
* **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes)
* **Records**: 768
* **Features**: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age.

---

## Model

* **Algorithm**: Support Vector Machine (SVM)
* **Scaler**: StandardScaler
* **Evaluation**: Accuracy, Confusion Matrix
* **Persistence**: joblib (`model.pkl`, `scaler.pkl`)

---

## Installation & Usage

1. Clone the repository

   ```bash
   git clone https://github.com/Mohitderek/Diabeticsapp.git
   cd Diabeticsapp
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app

   ```bash
   python app.py
   ```

4. Open in browser: `http://127.0.0.1:5000`

---

## Future Improvements

* Enhanced UI with Bootstrap/TailwindCSS
* Input validations and tooltips
* Cloud deployment
* User authentication for history tracking

---

## Author

**Mohit Derek**
📧 [mohitsercha5623@gmail.com](mailto:mohitsercha5623@gmail.com)

**License**: MIT License

