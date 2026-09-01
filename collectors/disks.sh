#!/bin/bash

echo "======================================"
echo "        StoragePulse - Disks"
echo "======================================"

echo ""
echo "DISKS AND PARTITIONS"
echo "--------------------"

lsblk -o NAME,PATH,SIZE,TYPE,FSTYPE,MOUNTPOINTS
