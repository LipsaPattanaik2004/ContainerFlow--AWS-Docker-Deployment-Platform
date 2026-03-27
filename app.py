from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Container Flow Deployment Successful on AWS!"

@app.route('/health')
def health():
    return {"status": "running", "env": os.getenv("ENV", "Not Set")}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
