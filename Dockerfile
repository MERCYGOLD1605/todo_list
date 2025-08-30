# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
