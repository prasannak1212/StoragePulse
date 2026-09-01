import json
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(
    title="StoragePulse",
    description="Linux Storage Monitoring API",
    version="0.1.0"
)

PROJECT_DIR = Path(__file__).resolve().parent.parent
DISK_DATA_FILE = PROJECT_DIR / "data" / "disks.json"


@app.get("/")
def root():
    return {
        "application": "StoragePulse",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/disks")
def get_disks():

    with open(DISK_DATA_FILE, "r") as file:
        data = json.load(file)

    return data