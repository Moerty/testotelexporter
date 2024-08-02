import os
import requests
import time
import grpc
import logging
from opentelemetry.proto.collector.trace.v1 import trace_service_pb2_grpc
from opentelemetry.proto.collector.trace.v1.trace_service_pb2 import ExportTraceServiceRequest
from opentelemetry.proto.trace.v1.trace_pb2 import ResourceSpans

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Environment variables
TRACE_URL = os.getenv('TRACE_URL', 'https://example.com/traces')
GRPC_SERVER = os.getenv('GRPC_SERVER', 'otel-collector:4317')
FETCH_INTERVAL = int(os.getenv('FETCH_INTERVAL', '60'))

def fetch_and_send_traces():
    while True:
        try:
            response = requests.get(TRACE_URL)
            response.raise_for_status()

            # Assume response content is in the format required
            resource_spans = ResourceSpans()  # Populate with actual trace data

            with grpc.insecure_channel(GRPC_SERVER) as channel:
                stub = trace_service_pb2_grpc.TraceServiceStub(channel)
                request = ExportTraceServiceRequest(resource_spans=[resource_spans])
                stub.Export(request)

            logging.info("Traces sent successfully")
        except requests.RequestException as e:
            logging.error(f"Failed to fetch traces: {e}")
        except grpc.RpcError as e:
            logging.error(f"Failed to send traces: {e}")

        time.sleep(FETCH_INTERVAL)

if __name__ == '__main__':
    fetch_and_send_traces()