from flask import Flask, request
import os
import time
import socket
from datetime import datetime

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    hostname = socket.gethostname()
    return {
        "message": "ContainerFlow service running",
        "instance": hostname
    }

# Health check route
@app.route('/health')
def health():
    return {
        "status": "running",
        "environment": os.getenv("ENV", "Not Set")
    }

# Load simulation route
@app.route('/load')
def load():
    time.sleep(2)
    return {
        "status": "request processed",
        "note": "simulated delay added"
    }

# Simple request logging
@app.before_request
def log_request():
    print(f"[{datetime.now()}] {request.method} {request.path} request received")

# Entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
