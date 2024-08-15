from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST', 'GET'])
def predict_data():
    if request.method == 'POST':
        temperature = float(request.form.get('Temperature'))
        rh = float(request.form.get('RH'))
        ws = float(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes'))
        region = float(request.form.get('Region'))

        features = [[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]]
        scaled_features = standard_scaler.transform(features)
        
        result = ridge_model.predict(scaled_features)
        
        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
