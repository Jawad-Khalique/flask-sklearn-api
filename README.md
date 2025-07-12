# 🧠 Flask + scikit-learn API: Iris Classifier (Deployed on AWS EC2 with Docker)

This project is a simple Flask API that serves a machine learning model built using scikit-learn. The model is trained on the classic Iris dataset and predicts the species of iris flower based on sepal and petal measurements.

It demonstrates how to:

- ✅ Build an ML API using Flask
- ✅ Train and serve a scikit-learn model
- ✅ Containerize the app using **Docker**
- ✅ Deploy it on an **AWS EC2** instance
- ✅ Access the API through a **public IP**

---

## 🚀 Features

- ✅ Scikit-learn ML model (Iris classification)
- ✅ Flask-based REST API
- ✅ Containerized with Docker
- ✅ Hosted on AWS EC2 (Ubuntu 20.04 or 24.04)
- ✅ Accessible via `http://<your-ec2-ip>:5000/predict`
- ✅ Includes Bash deployment script

---

## 🔧 Usage

### 1. Clone the repo

```bash
git clone https://github.com/Jawad-Khalique/flask-sklearn-api.git
cd flask-sklearn-api
```

### 2. Build the Docker image

```bash
docker build -t flask-iris-api .
```

### 3. Run the container

```bash
docker run -d -p 5000:5000 flask-iris-api
```

---

## 🌐 Access the API

Once deployed, make a POST request like this:

```bash
curl -X POST http://<your-ec2-ip>:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

---

## 📁 Project Structure

```
flask-sklearn-api/
├── app.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ✍️ Author

**Jawad Khalique**  
Machine Learning & MLOps Enthusiast  
GitHub: [@Jawad-Khalique](https://github.com/Jawad-Khalique)

