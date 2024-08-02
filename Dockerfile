# Use a minimal base image with Python
FROM python:3.9-slim

# Set environment variables for security
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create a non-root user and switch to it
RUN addgroup --system otel && adduser --system --ingroup otel otel
USER otel

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY --chown=otel:otel requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY --chown=otel:otel src /app/src

# Run the application
CMD ["python", "/app/src/custom_scraper/main.py"]