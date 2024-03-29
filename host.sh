#!/bin/bash

# if on linux run using gunicorn, else use waitress
if [ "$(uname)" == "Linux" ]; then
    py -m pip install -r requirements_linux.txt
    py -m gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
else
    py -m pip install -r requirements_windows.txt
    py -c "from waitress import serve; from notetaker import app; serve(app, port=5000)"
fi

# open the server in the browser
start http://localhost:5000