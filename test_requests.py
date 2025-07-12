import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    'features': [5.1, 3.5, 1.4, 4.2]  # Example Iris flower
}

response = requests.post(url, json=data)
print('Prediction',response.json())