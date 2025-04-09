### DockerFile ####

# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file (if you have one) to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY  . .

# Expose the port that Flask will run on
EXPOSE 5000

# Set the environment variable for Flask to run in development mode (optional)
ENV FLASK_ENV=development

# Command to run the Flask application
CMD ["python", "app.py"]

