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
    monitor.track_system_usage()
    return await call_next(request)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/error/")
def raise_error():
    raise Exception("Error")

@app.get("/metrics")
def get_metrics():
    return monitor.get_metrics()
