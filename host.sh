#!/bin/bash

# Run wsgi.py using gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app