from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/alert')
def get_alert():
    temp = 35  # Simulated temp
    if temp > 30:
        return jsonify(alert="Heat alert!"), 200
    return jsonify(alert="Normal"), 200

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)