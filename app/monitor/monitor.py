import psutil
from prometheus_client import Gauge
from prometheus_client import Counter
from prometheus_client import Summary
from prometheus_client import start_http_server

cpu_usage = Gauge('cpu_usage', 'CPU usage')
memory_usage = Gauge('memory_usage', 'Memory usage')
error = Counter('error', 'Error count')
request_time = Summary('request_time', 'Request processing time')
endpoint_calls = Counter('endpoint_calls', 'Endpoint calls', ['endpoint'])



def count_endpoint_calls(endpoint):
    endpoint_calls.labels(endpoint).inc(1)

def count_error():
    error.inc(1)

def track_request_time(seconds):
    request_time.observe(seconds)


def track_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU: {cpu}%, Memory: {memory}%")

    cpu_usage.set(cpu)
    memory_usage.set(memory)


def start():
    start_http_server(8001)
