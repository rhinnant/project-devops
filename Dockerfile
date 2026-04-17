# Use official Python slim image
FROM python:3.11-slim

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project code
COPY . /app/

# Expose Django port
EXPOSE 8080

# Run migrations and start Django server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "3"]
