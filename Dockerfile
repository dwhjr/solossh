# Use official Python 3.11 image (latest)
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app

# Ensure venv is properly created and activated inside the container
RUN python -m venv /app/venv && \
    /app/venv/bin/python -m ensurepip && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

# Set the virtual environment as default
ENV PATH="/app/venv/bin:$PATH"

# Expose the application port
EXPOSE 5003

# Use an entrypoint script to ensure venv activation
ENTRYPOINT ["/bin/bash", "-c", "source /app/venv/bin/activate && exec python app.py"]






