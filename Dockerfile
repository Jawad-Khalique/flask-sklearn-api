# Using official Python base image
FROM python:3.12-slim

# Setting work directory
WORKDIR /app

# Copying everything into the container
COPY . /app

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Exposed the port Flask runs on
EXPOSE 5000

# Set environment variables 
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the app
CMD ["flask", "run", "--port=5000"]
