# PromQL for SLA/SLO

- Total requests:
  ```promql
  sum(rate(http_requests_total[1m]))
  ```

- Error rate (5xx):
  ```promql
  sum(rate(http_requests_total{status=~"5.."}[1m])) / sum(rate(http_requests_total[1m]))
  ```

- Uptime of endpoints:
  ```promql
  probe_success{instance=~".*example.com.*"}
  ```