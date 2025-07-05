from flask import Flask
from prometheus_client import start_http_server, Counter
import random, time

app = Flask(__name__)
REQUESTS = Counter('hello_requests_total', 'Total hello requests')

@app.route('/')
def hello():
    REQUESTS.inc()
    return "Hello from instrumented Flask App!"

if __name__ == '__main__':
    start_http_server(8001)
    app.run(host='0.0.0.0', port=5000)