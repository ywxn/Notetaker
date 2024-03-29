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

# Open webpage after doing an os check
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open http://localhost:$port
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:$port
elif [[ "$OSTYPE" == "cygwin" ]]; then
    start http://localhost:$port
elif [[ "$OSTYPE" == "msys" ]]; then
    start http://localhost:$port
elif [[ "$OSTYPE" == "win32" ]]; then
    start http://localhost:$port
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    xdg-open http://localhost:$port
else
    echo "Cannot open webpage. Please go to http://localhost:$port"
fi

# Start the server
python3 ./host.py $port