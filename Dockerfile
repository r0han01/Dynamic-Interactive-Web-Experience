# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to allow access to the Flask app from outside the container
EXPOSE 5000

# Define the environment variable for Flask to run on 0.0.0.0 and port 5000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the Flask application
CMD ["flask", "run"]
