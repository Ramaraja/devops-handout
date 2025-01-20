### Kubernetes Command Cheat Sheet

Here is a quick reference for commonly used Kubernetes (`kubectl`) commands.

---

### **1. General Cluster Commands**
| **Action**                 | **Command**                                                  |
|----------------------------|-------------------------------------------------------------|
| Check cluster information  | `kubectl cluster-info`                                       |
| View cluster nodes         | `kubectl get nodes`                                         |
| Describe a node            | `kubectl describe node <node-name>`                         |
| View API resources         | `kubectl api-resources`                                     |
| View API versions          | `kubectl api-versions`                                      |

---

### **2. Namespace Management**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| List namespaces                      | `kubectl get namespaces`                                      |
| Switch namespace                     | `kubectl config set-context --current --namespace=<namespace>` |
| Create a new namespace               | `kubectl create namespace <namespace>`                       |
| Delete a namespace                   | `kubectl delete namespace <namespace>`                       |

---

### **3. Pod Management**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| List all pods                        | `kubectl get pods`                                            |
| List pods in a namespace             | `kubectl get pods -n <namespace>`                            |
| Describe a specific pod              | `kubectl describe pod <pod-name>`                            |
| Create a pod from a YAML file        | `kubectl apply -f pod.yaml`                                  |
| Delete a pod                         | `kubectl delete pod <pod-name>`                              |
| Exec into a running pod              | `kubectl exec -it <pod-name> -- /bin/bash`                   |
| View logs of a pod                   | `kubectl logs <pod-name>`                                    |
| View logs of a pod's specific container | `kubectl logs <pod-name> -c <container-name>`               |

---

### **4. Deployment Management**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| List all deployments                 | `kubectl get deployments`                                    |
| Describe a deployment                | `kubectl describe deployment <deployment-name>`             |
| Create a deployment                  | `kubectl apply -f deployment.yaml`                          |
| Scale a deployment                   | `kubectl scale deployment <deployment-name> --replicas=<n>` |
| Update a deployment image            | `kubectl set image deployment/<deployment-name> <container-name>=<image>:<tag>` |
| Delete a deployment                  | `kubectl delete deployment <deployment-name>`               |

---

### **5. Service Management**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| List all services                    | `kubectl get services`                                       |
| Describe a service                   | `kubectl describe service <service-name>`                   |
| Create a service                     | `kubectl apply -f service.yaml`                             |
| Delete a service                     | `kubectl delete service <service-name>`                     |

---

### **6. ConfigMap and Secret Management**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| Create a ConfigMap                   | `kubectl create configmap <name> --from-literal=key=value`   |
| Create a ConfigMap from a file       | `kubectl create configmap <name> --from-file=<file-path>`    |
| Get ConfigMaps                       | `kubectl get configmaps`                                     |
| View a ConfigMap                     | `kubectl describe configmap <name>`                         |
| Delete a ConfigMap                   | `kubectl delete configmap <name>`                           |
| Create a Secret                      | `kubectl create secret generic <name> --from-literal=key=value` |
| List all Secrets                     | `kubectl get secrets`                                        |
| View a Secret                        | `kubectl describe secret <name>`                            |

---

### **7. Persistent Volume (PV) and Persistent Volume Claim (PVC)**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| List Persistent Volumes              | `kubectl get pv`                                             |
| List Persistent Volume Claims        | `kubectl get pvc`                                            |
| Create PV or PVC from YAML           | `kubectl apply -f pv.yaml`                                   |
| Describe PV or PVC                   | `kubectl describe pv <pv-name>`                              |
| Delete PV or PVC                     | `kubectl delete pv <pv-name>`                                |

---

### **8. Monitoring and Debugging**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| Check events                         | `kubectl get events`                                         |
| View resource usage (metrics-server) | `kubectl top nodes` / `kubectl top pods`                    |
| Debug a pod                          | `kubectl describe pod <pod-name>`                           |
| Port-forward to a pod                | `kubectl port-forward <pod-name> <local-port>:<pod-port>`   |

---

### **9. YAML Management**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| Export resource YAML                 | `kubectl get <resource> <name> -o yaml`                     |
| Apply a YAML file                    | `kubectl apply -f <file.yaml>`                              |
| Delete using YAML                    | `kubectl delete -f <file.yaml>`                             |

---

### **10. Miscellaneous**
| **Action**                           | **Command**                                                   |
|--------------------------------------|--------------------------------------------------------------|
| Check kubectl config                 | `kubectl config view`                                        |
| Switch Kubernetes context            | `kubectl config use-context <context-name>`                 |
| View resource usage                  | `kubectl top nodes` / `kubectl top pods`                    |
| Dry-run a command                    | `kubectl apply -f <file.yaml> --dry-run=client`             |
| Autoscale deployment                 | `kubectl autoscale deployment <name> --min=<n> --max=<n> --cpu-percent=<value>` |

---

