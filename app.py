from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form[key]) for key in [
        'pregnancies', 'glucose', 'bloodPressure', 'skinThickness',
        'insulin', 'bmi', 'dpf', 'age'
    ]]

    scaled_input = scaler.transform([features])
    prediction = model.predict(scaled_input)[0]

    return render_template('index.html', prediction=int(prediction))

if __name__ == '__main__':
    app.run(debug=True)
