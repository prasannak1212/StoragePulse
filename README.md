# StoragePulse

Linux Storage & Filesystem Monitoring Dashboard

## Overview

StoragePulse is a Linux storage and filesystem monitoring dashboard built using Bash, Python, FastAPI and Streamlit.

The goal is to monitor and analyze:

- Disks
- Partitions
- Filesystems
- Filesystem utilization
- Disk I/O
- Storage growth
- Storage-related alerts

## Project Structure

storagepulse/
├── collectors/
│   ├── disks.sh
│   ├── filesystems.sh
│   └── io.sh
│
├── app/
│   ├── main.py
│   └── analyzer.py
│
├── data/
├── logs/
├── scripts/
└── README.md

## Technologies

- Linux
- Bash
- Python
- FastAPI
- Streamlit
- Git/GitHub

## Phases

### Phase - 1. Disk Inventory:

## Architecture
┌──────────────────┐
│      Linux       │
└────────┬─────────┘
         │
         │ Bash Commands (lsblk)
         ▼
┌──────────────────┐
│   Bash Script    │
│  disks.sh        │
└────────┬─────────┘
         │
         │ JSON
         ▼
┌──────────────────┐
│     FastAPI      │
│     /disks       │
└────────┬─────────┘
         │
         │ HTTP
         ▼
┌──────────────────┐
│    Streamlit     │
│    Dashboard     │
└──────────────────┘

## Workflow

Step - 1: Choose appropriate bash command to get JSON output for all disks.
Step - 2: Write Bash Script disks.sh (storagepulse/collectors/disks.sh) to save the JSON file in disks.json (storagepulse/collectors/disks.json).
Step - 3: Create FastAPI GET API Endpoint "/disks" to expose the API.
Step - 4: Call the Endpoint from streamlit and display as dashboard.

### Disk Monitoring

### Filesystem Monitoring

### I/O Monitoring





