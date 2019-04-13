from flask import Flask, jsonify, request
from joblib import load
import pandas as pd

app = Flask(__name__)
pipeline = load('pipeline.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    X = pd.DataFrame(**request.get_json(force=True))
    y_pred = pipeline.predict(X)
    return jsonify(y_pred.tolist())
