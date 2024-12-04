# Use an official Python runtime as a parent image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .

# Copiar a pasta pickle para o contêiner
COPY pickle /app/pickle


RUN pip install -r requirements.txt

# Copy the rest of the project code
COPY . .


