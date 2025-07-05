# Lab: Kubernetes Monitoring with kube-prometheus-stack

1. Add Prometheus Community Helm repo:
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
   ```

2. Install with values:
   ```bash
   helm install kps prometheus-community/kube-prometheus-stack -f helm-values.yaml
   ```

3. Access:
   - Prometheus: `kubectl port-forward svc/kps-kube-prometheus-stack-prometheus 9090`
   - Grafana: `kubectl port-forward svc/kps-grafana 3000:80`


