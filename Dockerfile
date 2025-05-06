# Dockerfile for GenAI Agent Framework
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port for API
EXPOSE 8000

# Default command: run the FastAPI server
CMD ["uvicorn", "app.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
