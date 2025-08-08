Diabetics Prediction App
A machine learning-based web application that predicts whether a person is likely to have diabetes based on several health parameters. This project uses the Pima Indians Diabetes Dataset and provides predictions through a Flask-based web interface.

Overview
Early detection of diabetes can help prevent severe health complications. This application allows users to input health parameters and receive an instant prediction using a trained ML model.

Objective
Train a machine learning model using Support Vector Machine on real-world diabetes data.

Deploy the model using Flask for real-time predictions.

Provide a simple web interface for easy use.

Tech Stack
Component	Tools / Libraries
Language	Python
Framework	Flask
Data Processing	Pandas, NumPy
Model Building	Scikit-learn
Frontend	HTML, CSS
Deployment	Localhost

Project Structure
bash
Copy
Edit
Diabeticsapp/
│
├── DiabetesPrediction.ipynb   # Model training and preprocessing
├── app.py                     # Flask application
├── diabetes.csv               # Dataset
├── model.pkl                  # Trained ML model
├── scaler.pkl                 # Feature scaler
├── requirements.txt           # Required Python packages
├── templates/
│   └── index.html             # Web interface
└── README.md                  # Documentation
Dataset Information
Dataset: Pima Indians Diabetes Dataset

Source: UCI Machine Learning Repository

Records: 768 samples

Features:

Pregnancies

Glucose Level

Blood Pressure

Skin Thickness

Insulin Level

BMI

Diabetes Pedigree Function

Age

Machine Learning Model
Algorithm: Logistic Regression, Support Vector Machine

Scaler: StandardScaler

Evaluation: Accuracy, Confusion Matrix

Model Persistence: Saved using joblib

Installation & Usage
Clone the Repository

bash
Copy
Edit
git clone https://github.com/Mohitderek/Diabeticsapp.git
cd Diabeticsapp
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Application

bash
Copy
Edit
python app.py
Open in Browser

cpp
Copy
Edit
http://127.0.0.1:5000
Future Improvements
Enhance UI using Bootstrap or TailwindCSS

Add input validation

Deploy on cloud platforms

Implement user authentication to store history

Author
Mohit Derek
Email: [mohitsercha5623@gmail.com]

