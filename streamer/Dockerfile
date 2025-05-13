FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (Docker layer caching)
COPY requirements.txt .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your actual app code
COPY stream_server.py .

CMD ["python", "stream_server.py"]

