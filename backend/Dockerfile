FROM python:3.10-slim

# Install system dependencies for Prophet & scikit-learn
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpython3-dev \
    libatlas-base-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Run the app
CMD ["python", "main.py"]
