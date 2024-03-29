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

# Use `python3` instead of `py` to run Python scripts
python3 -c "from waitress import serve; from notetaker import app; serve(app, port=$port)" &

# Wait for the server to start before opening the browser
sleep 5

# Check for the operating system and open the browser accordingly
if [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:5000
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open http://localhost:5000
elif [[ "$OSTYPE" == "msys" ]]; then
    start http://localhost:5000
fi