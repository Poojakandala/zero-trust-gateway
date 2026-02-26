# Use a slim version for faster builds and smaller footprint
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for SQLite and networking
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# We will use docker-compose to handle the start commands
