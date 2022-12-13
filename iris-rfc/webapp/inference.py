import pickle
from flask import Flask, request, jsonify

import numpy as np
import pandas as pd

with open('./rfc-model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h3>Sklearn Prediction Container</h3>"

@app.route('/predict', methods=['POST'])
def predict():

    input_data = pd.DataFrame(request.json)
    prediction = list(model.predict(input_data))

    return jsonify({'prediction': [str(item) for item in prediction]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)