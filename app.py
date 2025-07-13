import joblib
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return 'Iris Classifier API is running'

@app.route('/predict',methods=['Post'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1,-1)
        prediction = model.predict(features)
        iris_classes = ['setosa', 'versicolor', 'virginica']
        predicted_class = iris_classes[int(prediction[0])]
        return jsonify({'prediction':predicted_class})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
