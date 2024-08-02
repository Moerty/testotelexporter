# Stage 1: Build the dependencies
FROM python:3.9-slim as builder

# Set environment variables for security
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the final image
FROM python:3.9-slim

# Create a non-root user and switch to it
RUN addgroup --system otel && adduser --system --ingroup otel otel
USER otel

# Set the working directory
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY --chown=otel:otel src /app/src

# Run the application
CMD ["python", "/app/src/custom_scraper/main.py"]