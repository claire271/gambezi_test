#!/bin/bash

sudo echo "Starting server"
sudo `which lwsws` > /dev/null 2>&1 &
sleep 1

echo "Running connect/disconnect tests"
python3 test_a.py &
sleep 12
sudo pkill lwsws
sleep 8
sudo `which lwsws` > /dev/null 2>&1 &

echo "Cleaning up"
sudo pkill lwsws
pkill python3
