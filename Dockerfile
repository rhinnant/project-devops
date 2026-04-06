# Dockerfile (corrected)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire project
COPY . .

# Expose port
EXPOSE 8000

# Run server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
