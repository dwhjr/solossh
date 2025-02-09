FROM python:3.11

WORKDIR /app

# Install system dependencies including NGINX
RUN apt-get update && apt-get install -y \
    nginx \
    bash \
    libssl-dev \
    libffi-dev \
    build-essential \
    python3-dev \
    python3-pip \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for web access
EXPOSE 80

# Start NGINX and the Python app
ENTRYPOINT ["bash", "-c", "service nginx start && python3 /app/app.py"]
