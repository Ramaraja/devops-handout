# Lab: Setup Blackbox Exporter

1. Run blackbox exporter:
   ```bash
   docker run -d --name=blackbox -p 9115:9115 -v $(pwd)/blackbox.yml:/etc/blackbox_exporter/config.yml prom/blackbox-exporter
   ```

2. Add job to prometheus.yml:
   ```yaml
   - job_name: 'blackbox'
     metrics_path: /probe
     params:
       module: [http_2xx]
     static_configs:
       - targets:
         - https://example.com
     relabel_configs:
       - source_labels: [__address__]
         target_label: __param_target
       - source_labels: [__param_target]
         target_label: instance
       - target_label: __address__
         replacement: 127.0.0.1:9115
   ```

3. Reload Prometheus and test.