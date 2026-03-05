# Lightweight version of python for production, ideal para Hugging Face Spaces
FROM python:3.11-slim

# Do not create .pyc files and ensure output is not buffered (important for logging)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory inside the container
WORKDIR /code

# Install system dependencies (build-essential for any potential compilation, curl for downloading models if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the entire codebase into the container
COPY . /code

# Create a directory for models with appropriate permissions
RUN mkdir -p /code/models && chmod 777 /code/models

# Expose the port that the app will run on (standard for Hugging Face Spaces)
EXPOSE 7860

# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]