
### **Step 1: Install Prometheus**
#### **Option 1: Docker (Recommended)**
Run Prometheus as a Docker container:  
```sh
docker run -p 9090:9090 prom/prometheus
```
This starts Prometheus on `http://localhost:9090`.

#### **Option 2: Manual Installation**
1. Download Prometheus:  
   ```sh
   wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-linux-amd64.tar.gz
   ```
2. Extract and run it:  
   ```sh
   tar -xvf prometheus-linux-amd64.tar.gz
   cd prometheus-*
   ./prometheus --config.file=prometheus.yml
   ```

---

### **Step 2: Configure Prometheus**
Edit the `prometheus.yml` file to scrape metrics:
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
```
This configuration makes Prometheus scrape its own metrics.

Restart Prometheus if you modified the config:
```sh
docker restart prometheus
```

---

### **Step 3: Query Metrics**
Visit `http://localhost:9090` and try these example queries:
- **Up status of targets**:  
  ```
  up
  ```
- **CPU usage (example metric for Node Exporter)**:  
  ```
  rate(node_cpu_seconds_total{mode="user"}[5m])
  ```
- **Memory usage**:  
  ```
  node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes
  ```

---

### **Step 4: Add a Node Exporter (for System Metrics)**
To monitor CPU, RAM, and disk usage, run:
```sh
docker run -d -p 9100:9100 prom/node-exporter
```
Then, update `prometheus.yml`:
```yaml
scrape_configs:
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']
```
Restart Prometheus and query system metrics!

---


### **Grafana Setup with Prometheus**

Grafana is a great tool for **visualizing Prometheus metrics** with dashboards.

---

## **Step 1: Install Grafana**
### **Option 1: Docker (Recommended)**
```sh
docker run -d -p 3000:3000 grafana/grafana
```
Now, Grafana is running at `http://localhost:3000` (default login: `admin/admin`).  

### **Option 2: Manual Installation**
For Linux:  
```sh
sudo apt update && sudo apt install -y grafana
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```
For other OS, download it from [Grafana Downloads](https://grafana.com/grafana/download).

---

## **Step 2: Connect Grafana to Prometheus**
1. Open `http://localhost:3000`
2. Login with `admin/admin`
3. Go to **"Configuration" → "Data Sources" → "Add data source"**
4. Select **"Prometheus"**
5. Set **URL:** `http://localhost:9090`

---

## **Step 3: Import a Dashboard**
### Option 1: Use a Prebuilt Dashboard
1. Go to **"Dashboards" → "Import"**
2. Enter **Dashboard ID** (e.g., `1860` for Node Exporter)
3. Click **"Load"**, select **Prometheus** as the data source, and click **"Import"**  

### Option 2: Create Your Own Dashboard
1. Go to **"Create" → "Dashboard"**
2. Click **"Add new panel"**
3. Write a PromQL query (e.g., `rate(node_cpu_seconds_total{mode="user"}[5m])`)
4. Select **Graph Visualization** and click **"Save"**

---


## **Exporters**
| **Exporter**         | **Best for Monitoring** |
|----------------------|------------------------|
| **Node Exporter**    | Linux VMs, Servers |
| **Blackbox Exporter** | Websites, APIs, Ping |
| **cAdvisor**         | Docker containers |
| **MySQL Exporter**   | MySQL/MariaDB databases |
| **Postgres Exporter** | PostgreSQL databases |
| **Nginx Exporter**   | Nginx web servers |
| **Windows Exporter** | Windows Servers |
| **SNMP Exporter**    | Network devices |
| **JMX Exporter**     | Java applications |
| **Redis Exporter**   | Redis Cache |

---


### **Adding Alerts in Prometheus and Alertmanager** 

## **Step 1: Define Alerting Rules**  

Create a new file **`alert-rules.yml`**:  

```yaml
groups:
  - name: instance-health
    rules:
      - alert: InstanceDown
        expr: up == 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Instance {{ $labels.instance }} is down"
          description: "Prometheus has detected that instance {{ $labels.instance }} is down for more than 5 minutes."
```

---

## **Step 2: Update `prometheus.yml` to Load Alerts**  

Modify your **prometheus.yml** file to load the alert rules:  

```yaml
global:
  scrape_interval: 15s

rule_files:
  - "alert-rules.yml"

alerting:
  alertmanagers:
    - static_configs:
        - targets: ["alertmanager:9093"]

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

---

## **Step 3: Configure Alertmanager**  

Create a **`alertmanager.yml`** file to send alerts via **Slack, Email, or PagerDuty**:  

```yaml
global:
  resolve_timeout: 5m

route:
  receiver: 'msteams'
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 30m

receivers:
  - name: 'msteams'
    webhook_configs:
      - url: 'https://outlook.office.com/webhook/YOUR-WEBHOOK-URL'
        send_resolved: true
```

---

## **Step 4: Update `docker-compose.yml`**  

Modify your **`docker-compose.yml`** to include Alertmanager:  

```yaml
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alert-rules.yml:/etc/prometheus/alert-rules.yml
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090"

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"

  alertmanager:
    image: prom/alertmanager:latest
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml
    command:
      - '--config.file=/etc/alertmanager/alertmanager.yml'
    ports:
      - "9093:9093"
```

---

## **Step 5: Start the Services**  

Run the updated **Docker Compose** setup:  
```sh
docker-compose up -d
```

Verify that Prometheus has loaded the alert rules:  
```sh
curl http://localhost:9090/api/v1/rules | jq
```

---

## **Step 6: Test Alerts**  
- Stop **node-exporter** to trigger an alert:  
  ```sh
  docker stop node-exporter
  ```
- Go to **Prometheus Alerts**:  
  **http://localhost:9090/alerts**  
- Check Alertmanager:  
  **http://localhost:9093**  


---

### **PromQL (Prometheus Query Language) Examples**  

PromQL is used in Prometheus to **query metrics** for monitoring and alerting. Here are **commonly used queries** for CPU, memory, disk, network, and application monitoring.  


## **1. CPU Metrics Queries**
### **Total CPU Usage (All Cores)**
```promql
rate(node_cpu_seconds_total[5m])
```
Returns **CPU usage** for all cores, including idle, user, system, etc.  

### **User CPU Usage (Last 5 min)**
```promql
rate(node_cpu_seconds_total{mode="user"}[5m])
```
Shows CPU time spent in **user processes**.  

### **CPU Usage % (Excluding Idle)**
```promql
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```
Calculates the **actual CPU usage** by subtracting idle time from 100%.  

### **High CPU Alert (Above 80%)**
```promql
(avg by(instance) (rate(node_cpu_seconds_total{mode="user"}[5m])) * 100) > 80
```
**Triggers an alert** if CPU usage is above **80%** for a specific instance.  

---

## **2. Memory Metrics Queries**
### **Total Available Memory**
```promql
node_memory_MemTotal_bytes
```
Shows **total installed RAM** in bytes.  

### **Used Memory (Excluding Cache & Buffers)**
```promql
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100
```
**Calculates actual memory usage** (excluding buffers/cache).  

### **Memory Usage Above 80% Alert**
```promql
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100 > 80
```
**Triggers an alert** if memory usage goes beyond **80%**.  

---

## **3. Disk Usage Queries**
### **Free Disk Space (Root Partition)**
```promql
node_filesystem_free_bytes{mountpoint="/"}
```
Shows available disk space in bytes for the **root (`/`) partition**.  

### **Disk Usage Percentage**
```promql
(1 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})) * 100
```
Calculates **disk usage as a percentage** for `/`.  

### **Low Disk Space Alert (<10GB Available)**
```promql
node_filesystem_free_bytes{mountpoint="/"} < 10 * 1024 * 1024 * 1024
```
**Triggers an alert** if disk space is **less than 10GB**.  

---

## **4. Network Metrics Queries**
### **Network Traffic (Received)**
```promql
rate(node_network_receive_bytes_total[5m])
```
Shows **bytes received per second** over the last 5 minutes.  

### **Network Traffic (Transmitted)**
```promql
rate(node_network_transmit_bytes_total[5m])
```
Shows **bytes transmitted per second** over the last 5 minutes.  

### **High Network Traffic Alert (Above 100MB/s)**
```promql
rate(node_network_transmit_bytes_total[5m]) > 100 * 1024 * 1024
```
**Triggers an alert** if network traffic exceeds **100MB/s**.  

---

### **5. HTTP Requests Queries**
### **Total HTTP Requests (All Endpoints)**
```promql
sum(rate(http_requests_total[5m]))
```
Shows the **total number of HTTP requests per second**.  

### **HTTP Requests by Status Code**
```promql
sum(rate(http_requests_total[5m])) by (status)
```
Groups HTTP requests by **status code (200, 404, 500, etc.)**.  

### **High 500 Errors Alert**
```promql
sum(rate(http_requests_total{status="500"}[5m])) > 10
```
**Triggers an alert** if there are more than **10 HTTP 500 errors per second**.  

---

## **6. Application-Specific Queries**
### **Active Database Connections (PostgreSQL Example)**
```promql
pg_stat_activity_count
```
Shows the **current number of active connections** to PostgreSQL.  

### **Redis Cache Hit Ratio**
```promql
rate(redis_keyspace_hits[5m]) / (rate(redis_keyspace_hits[5m]) + rate(redis_keyspace_misses[5m]))
```
Measures **how often Redis serves data from cache** instead of querying the database.  

---

### **Instances with High CPU & Memory Usage**
```promql
topk(5, (node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100)
```
Lists the **top 5 instances** with the highest memory usage.  

### **Error Rate for Microservices**
```promql
sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
```
Shows **error rates per microservice** (matching 5xx status codes).  

---

