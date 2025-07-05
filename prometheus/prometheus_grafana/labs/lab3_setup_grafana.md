# Lab 3: Setup Grafana

1. Run Grafana:
   ```bash
   docker run -d -p 3000:3000 grafana/grafana
   ```

2. Login with `admin/admin`, connect Prometheus as data source.
3. Import sample dashboard from `grafana/sample_dashboard.json`.