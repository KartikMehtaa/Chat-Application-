# 🔹 Stage 1: Builder
FROM python:3.10-slim AS builder

WORKDIR /app

# Install dependencies needed for building
RUN apt-get update && apt-get install -y build-essential

# Copy requirements and install into a custom folder
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# 🔹 Stage 2: Final (lightweight image)
FROM python:3.10-slim

WORKDIR /app

# Prevent buffering (important for Jenkins logs)
ENV PYTHONUNBUFFERED=1

# Copy only installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Run app
CMD ["python", "app.py"]