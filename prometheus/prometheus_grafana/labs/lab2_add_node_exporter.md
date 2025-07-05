# Lab 2: Add Node Exporter

1. Start Node Exporter:
   ```bash
   docker run -d -p 9100:9100 --name node_exporter prom/node-exporter
   ```

2. Update prometheus.yml with target `localhost:9100` and restart Prometheus.