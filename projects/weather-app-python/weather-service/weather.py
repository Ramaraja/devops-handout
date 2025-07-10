from flask import Flask, jsonify
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/weather')
def get_weather():
    res = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=demo")
    data = res.json()
    return jsonify({
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"]
    })

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)