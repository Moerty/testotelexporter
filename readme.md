# OpenTelemetry Custom HTTP Scraper

This repository contains a custom HTTP scraper for collecting traces from a specified URL and forwarding them to an OpenTelemetry Collector.

## Repository Structure

```
otel-custom-scraper/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── custom_scraper/
│       └── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup and Usage

### Prerequisites

- Docker
- Docker Hub account (for pushing images)
- OpenTelemetry Collector

### Building the Docker Image

To build the Docker image, run the following command:

```
docker build -t otel-custom-scraper .
```

### Running the Docker Container

To run the Docker container, use the following command:

```
docker run -d --name otel-custom-scraper otel-custom-scraper
```

### Pushing the Image to Docker Hub

To push the image to Docker Hub, first log in to your Docker Hub account:

```
docker login -u <your-username> -p <your-password>
```

Then tag and push the image:

```
docker tag otel-custom-scraper <your-username>/otel-custom-scraper:latest
docker push <your-username>/otel-custom-scraper:latest
```

### CI/CD Pipeline

This repository includes a GitHub Actions workflow for continuous integration and deployment. The workflow is defined in `.github/workflows/ci.yml` and includes the following steps:

- Checkout code
- Set up Python
- Install dependencies
- Lint code with flake8
- Build Docker image
- Push Docker image to Docker Hub

### Running the Custom Scraper

The custom scraper fetches traces from `https://example.com/traces` every 60 seconds and forwards them to an OpenTelemetry Collector running at `otel-collector:4317`. Make sure to adjust the URL and collector endpoint as needed.

### Security

This setup ensures the following security standards:
- Running the application as a non-root user.
- Using environment variables to avoid writing bytecode and buffering.

## Example Usage

1. Build and run the Docker container:

```
docker build -t otel-custom-scraper .
docker run -d --name otel-custom-scraper otel-custom-scraper
```

2. Monitor the logs to ensure the scraper is working correctly:

```
docker logs -f otel-custom-scraper
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.