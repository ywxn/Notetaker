#!/bin/bash

# Assuming you are using Python 3, replace `py` with `python3`
python3 -m pip install -r requirements.txt

# Use `python3` instead of `py` to run Python scripts
python3 -c "from waitress import serve; from notetaker import app; serve(app, port=5000)" &

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