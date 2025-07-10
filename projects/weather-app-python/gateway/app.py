from flask import Flask, jsonify
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return jsonify(message="Welcome to the API Gateway!")

@app.route('/weather')
def proxy_weather():
    res = requests.get("http://weather-service:5000/weather")
    return jsonify(res.json())

@app.route('/alert')
def proxy_alert():
    res = requests.get("http://alert-service:6000/alert")
    return jsonify(res.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)