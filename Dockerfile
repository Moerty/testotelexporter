# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY src/ /app/src/

# Set environment variables (can also be overridden by Docker run command or Compose)
ENV TRACE_URL=https://example.com/traces
ENV GRPC_SERVER=otel-collector:4317
ENV FETCH_INTERVAL=60

# Run the Python script
CMD ["python", "/app/src/script.py"]