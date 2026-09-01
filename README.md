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

## Architecture

1. Disk Inventory:
┌──────────────────┐
│      Linux       │
└────────┬─────────┘
         │
         │ lsblk
         ▼
┌──────────────────┐
│      Bash        │
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

## Features

### Disk Monitoring

### Filesystem Monitoring

### I/O Monitoring

## Technologies

- Linux
- Bash
- Python
- FastAPI
- Streamlit
- Git/GitHub

## How It Works

## Installation

## Usage

## Screenshots

## What I Learned

## Future Improvements

## SUMMARY
Phase 1 - Disk Inventory
 Create project structure
 Configure Git and GitHub
 Configure SSH authentication
 Explore Linux block devices
 Create initial disk collector
