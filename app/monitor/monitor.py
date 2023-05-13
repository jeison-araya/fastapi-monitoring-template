import psutil
from prometheus_client import Gauge, start_http_server

cpu_usage = Gauge('cpu_usage', 'CPU usage')
memory_usage = Gauge('memory_usage', 'Memory usage')



def track_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"CPU: {cpu}%, Memory: {memory}%")

    cpu_usage.set(cpu)
    memory_usage.set(memory)


def start():
    start_http_server(8001)
