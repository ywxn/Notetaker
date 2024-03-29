#!/bin/bash

# Assuming you are using Python 3, replace `py` with `python3`
python3 -m pip install -r requirements.txt

# check if port 5000 is in use. if so, create a random port
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
    port=$(shuf -i 5001-8888 -n 1)
    echo "Port 5000 is in use. Using port $port instead."
else
    port=5000
fi

# Start the server
python3 ./host.py $port