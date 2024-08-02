import requests
import time
import grpc
from opentelemetry.proto.collector.trace.v1 import trace_service_pb2_grpc
from opentelemetry.proto.collector.trace.v1.trace_service_pb2 import (
    ExportTraceServiceRequest,
)
from opentelemetry.proto.trace.v1.trace_pb2 import ResourceSpans


def fetch_and_send_traces():
    while True:
        try:
            response = requests.get('https://example.com/traces')
            response.raise_for_status()

            # Assume response content is in the format required
            resource_spans = ResourceSpans()  # Populate with actual trace data

            with grpc.insecure_channel('otel-collector:4317') as channel:
                stub = trace_service_pb2_grpc.TraceServiceStub(channel)
                request = ExportTraceServiceRequest(
                    resource_spans=[resource_spans]
                )
                stub.Export(request)

            print("Traces sent successfully")
        except requests.RequestException as e:
            print(f"Failed to fetch traces: {e}")
        except grpc.RpcError as e:
            print(f"Failed to send traces: {e}")

        time.sleep(60)


if __name__ == '__main__':
    fetch_and_send_traces()