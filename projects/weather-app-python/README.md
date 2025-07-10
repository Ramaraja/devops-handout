
## DevOps Project: **“Weather & Alerts Microservices Platform”**

### **Project Overview**

The idea is to build a CI/CD for **Python-based microservices platform** that fetches weather data and generates alerts. The application should be containerized, deployed to a local Kubernetes cluster (Minikube), monitored using Prometheus and Grafana, and delivered via an automated Jenkins CI/CD pipeline.

---

## Problem Statement

### Goal:

> **Design, build, deploy, monitor, and automate a multi-container Python microservices platform using DevOps tools.**

---

## Requirements

### 1. **Application**

Provided a simple Python application to fetch the weather information from OpenWeatherMap API **three Python Flask microservices**:
Download the app and use your github personal account to do the exercise and share the repo url as end outcome.

| Service Name      | Port | Role                                           |
| ----------------- | ---- | ---------------------------------------------- |
| `gateway`         | 4000 | Entry point, routes API calls                  |
| `weather-service` | 5000 | Fetches live weather data (OpenWeatherMap API) |
| `alert-service`   | 6000 | Generates alerts based on weather data         |

* Each service should expose `/health` and `/metrics` endpoints.
* All APIs return JSON responses.
* All services should be containerized using Docker.

---

### 2. **Dockerization**

* Create a `Dockerfile` for each service.
* Images must be tagged properly (`gateway:latest`, `weather-service:latest`, etc.)
* Containers must run using port as defined above.

---

### 3. **Kubernetes Deployment**

Deploy each microservice to Kubernetes (Minikube) using raw **YAML manifests**.

* Create a Deployment and Service for each microservice.
* Expose `gateway` via `NodePort` so it’s accessible on your browser.
* Make sure services can **talk to each other** using service DNS (e.g., `http://alert-service:6000/alert`).

---

### 4. **CI/CD with Jenkins**

Set up a Jenkins pipeline that automates the following:

* Checkout code from your local GitHub repo
* Build Docker images for all services
* Deploy services to Kubernetes using `kubectl apply`
* Include basic health checks using `curl`


---

### 5. **Monitoring with Prometheus + Grafana**

* Integrate `prometheus_flask_exporter` into each service
* Each service must expose `/metrics`
* Deploy Prometheus to Kubernetes to scrape metrics
* Deploy Grafana and create dashboards to visualize:

  * API response time
  * Alert count
  * Error rate
  * CPU/memory usage (node-exporter)

---

### 6. **Infrastructure Setup**

Provision your laptop with the necessary tools using:

* **Ansible** to install:

  * Docker
  * Minikube
  * Kubectl
  * Jenkins


---
