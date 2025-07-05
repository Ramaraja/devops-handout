# PromQL Cheatsheet

- All targets: `up`
- CPU usage: `rate(node_cpu_seconds_total{mode!="idle"}[5m])`
- Memory: `node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes`

- CPU %: `100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`
- memeory %: `100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))`