# Python base image
FROM python:3.10-slim

# System dependencies install karo (gcc, portaudio)
RUN apt-get update && apt-get install -y \
    gcc \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# App directory set karo
WORKDIR /app

# Requirements install karo
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Baaki code copy karo
COPY . .

# Default command
CMD ["python", "main.py"]
