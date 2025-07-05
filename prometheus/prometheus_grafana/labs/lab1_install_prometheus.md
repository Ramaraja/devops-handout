# Lab 1: Install Prometheus

1. Run Prometheus using Docker:
   ```bash
   docker run -d -p 9090:9090 --name prometheus -v $(pwd)/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
   ```

2. Access it via http://localhost:9090