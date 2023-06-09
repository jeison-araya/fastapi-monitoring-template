import random
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.monitor import monitor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    monitor.start()


@app.middleware("http")
async def monitor_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    monitor.track_request_time(process_time)
    monitor.track_system_usage()
    if request.url.path:
        monitor.count_endpoint_calls(request.url.path)

    return response


@app.exception_handler(Exception)
async def error_handler(request, exc):
    monitor.count_error()
    return {"Error": f"{exc}"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/error/")
def raise_error():
    raise Exception("Error")


@app.get('/delay/')
def random_delay():
    process_time = random.randint(2, 5)
    time.sleep(process_time)
    return {"Response time": f'{process_time} seconds'}
