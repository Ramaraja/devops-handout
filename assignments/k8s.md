# Kubernetes DevOps Training Tasks

## Prerequisites
- Kubernetes cluster (minikube, kind, or cloud-managed)
- kubectl configured and working
- Metrics server installed for HPA exercises
- Basic understanding of containerization

---

## 1. Pods Tasks

### Task 1.1: Basic Pod Operations
**Objective**: Master basic pod creation and management

**Requirements**:
1. Create a pod named `web-server` using the nginx:1.20 image
2. Create the same pod using both imperative commands and YAML manifest
3. Execute into the pod and create a custom index.html file with your name
4. View the pod logs and describe the pod to understand its configuration
5. Delete the pod and verify it's removed

**Deliverables**:
- Screenshot of pod creation commands
- YAML manifest file for the pod
- Screenshot showing custom webpage content
- Output of `kubectl describe pod` command

### Task 1.2: Multi-Container Pod Challenge
**Objective**: Work with sidecar containers and shared volumes

**Requirements**:
1. Create a pod named `log-processor` with two containers:
   - Main container: nginx serving content
   - Sidecar container: busybox that writes timestamp logs every 5 seconds
2. Use a shared volume so nginx can serve the log files generated by busybox
3. Configure the busybox container to write logs to `/shared/access.log`
4. Configure nginx to serve files from `/usr/share/nginx/html` which should mount the shared volume
5. Access the nginx server and verify you can see the logs

**Deliverables**:
- Complete YAML manifest
- Screenshot of accessing the log file through nginx
- Proof that both containers are running in the same pod

---

## 2. Namespaces Tasks

### Task 2.1: Environment Separation
**Objective**: Organize resources using namespaces

**Requirements**:
1. Create three namespaces: `dev`, `staging`, `prod`
2. Create a deployment named `app-deployment` with 2 replicas of nginx in each namespace
3. Create a service named `app-service` in each namespace to expose the deployment
4. Set your kubectl context to use `dev` namespace as default
5. List all pods across all namespaces
6. Delete all resources in the `staging` namespace

**Deliverables**:
- Commands used to create namespaces
- YAML files for deployments and services
- Screenshot showing resources in different namespaces
- Proof of namespace deletion

### Task 2.2: Cross-Namespace Communication
**Objective**: Understand namespace isolation and communication

**Requirements**:
1. Create a pod named `client` in the `dev` namespace
2. Create a service named `backend-service` in the `prod` namespace
3. From the client pod, try to access the backend service using:
   - Service name only
   - Fully qualified domain name (FQDN)
4. Document which method works and why

**Deliverables**:
- YAML manifests for all resources
- Commands and outputs showing connection attempts
- Explanation of DNS resolution in Kubernetes

---

## 3. Deployments Tasks

### Task 3.1: Deployment Lifecycle Management
**Objective**: Master deployment operations

**Requirements**:
1. Create a deployment named `web-app` with:
   - 4 replicas of nginx:1.19 image
   - Labels: app=web, version=v1
   - Resource requests: 100m CPU, 128Mi memory
2. Scale the deployment to 6 replicas
3. Update the image to nginx:1.20 using rolling update
4. Check the rollout history
5. Rollback to the previous version
6. Pause the deployment, then resume it

**Deliverables**:
- Initial deployment YAML
- Commands used for each operation
- Screenshots of rollout history
- Proof of successful rollback

### Task 3.2: Deployment Strategies
**Objective**: Configure different deployment update strategies

**Requirements**:
1. Create a deployment with `Recreate` strategy
2. Create another deployment with `RollingUpdate` strategy:
   - maxSurge: 25%
   - maxUnavailable: 25%
3. Update both deployments and observe the difference in behavior
4. Simulate a failed deployment by using a non-existent image tag

**Deliverables**:
- YAML files for both deployment strategies
- Documentation of observed differences
- Screenshots showing failed deployment handling

---

## 4. ReplicaSet Tasks

### Task 4.1: ReplicaSet Behavior Analysis
**Objective**: Understand ReplicaSet auto-healing and management

**Requirements**:
1. Create a ReplicaSet named `rs-test` with 3 replicas of nginx
2. Manually delete one of the pods created by the ReplicaSet
3. Observe and document the auto-healing behavior
4. Scale the ReplicaSet to 5 replicas
5. Create a standalone pod with the same labels as the ReplicaSet
6. Observe what happens to the standalone pod

**Deliverables**:
- ReplicaSet YAML manifest
- Screenshots showing auto-healing in action
- Documentation of pod adoption behavior
- Explanation of why certain behaviors occur

### Task 4.2: Orphaned Pods Challenge
**Objective**: Understand pod adoption and orphaning

**Requirements**:
1. Create 2 pods manually with labels `app=test, version=v1`
2. Create a ReplicaSet that selects pods with `app=test, version=v1` and wants 3 replicas
3. Observe how many new pods are created
4. Delete the ReplicaSet (without deleting pods)
5. Check the status of all pods

**Deliverables**:
- All YAML manifests used
- Step-by-step documentation of what happens
- Explanation of pod ownership and adoption

---

## 5. Services Tasks

### Task 5.1: Service Types Exploration
**Objective**: Work with different service types and networking

**Requirements**:
1. Create a deployment with 3 replicas of nginx
2. Create a ClusterIP service to expose the deployment internally
3. Create a NodePort service to expose the deployment externally
4. Test access to both services from inside and outside the cluster
5. If available, create a LoadBalancer service
6. Create a test pod to verify internal service discovery

**Deliverables**:
- Deployment and all service YAML files
- Screenshots of successful access from different locations
- Documentation of service endpoints and ports
- Output of service discovery tests

### Task 5.2: Headless Services
**Objective**: Understand headless services and direct pod access

**Requirements**:
1. Create a StatefulSet with 3 replicas
2. Create a headless service (ClusterIP: None) for the StatefulSet
3. Create a test pod and use nslookup to resolve:
   - The headless service name
   - Individual pod names
4. Document the DNS records returned

**Deliverables**:
- StatefulSet and headless service YAML
- nslookup outputs showing DNS resolution
- Explanation of when to use headless services

---

## 6. HPA (Horizontal Pod Autoscaler) Tasks

### Task 6.1: CPU-Based Autoscaling
**Objective**: Implement and test CPU-based horizontal scaling

**Requirements**:
1. Create a deployment with:
   - PHP application that can generate CPU load
   - Resource requests: 200m CPU, 256Mi memory
   - Resource limits: 500m CPU, 512Mi memory
2. Create a service to expose the application
3. Create an HPA that:
   - Scales between 1-5 replicas
   - Targets 50% CPU utilization
4. Generate load on the application and observe scaling behavior
5. Stop the load and observe scale-down behavior

**Deliverables**:
- All YAML manifests (deployment, service, HPA)
- Screenshots showing scaling in action
- Documentation of scaling behavior and timing
- Load generation commands used

### Task 6.2: Multi-Metric Autoscaling
**Objective**: Configure HPA with multiple metrics

**Requirements**:
1. Create an HPA that scales based on both CPU and memory metrics
2. Set different thresholds for each metric
3. Test scaling behavior under different load patterns
4. Create custom metrics if possible (bonus task)

**Deliverables**:
- Multi-metric HPA YAML configuration
- Test results showing scaling based on different metrics
- Analysis of scaling decisions

---

## 7. QoS (Quality of Service) Tasks

### Task 7.1: QoS Classes Implementation
**Objective**: Create pods with different QoS classes

**Requirements**:
1. Create three pods with different QoS classes:
   - **Guaranteed**: requests = limits for both CPU and memory
   - **Burstable**: requests < limits (or only requests specified)
   - **BestEffort**: no requests or limits specified
2. Use `kubectl describe` to verify the QoS class assigned to each pod
3. Run a memory stress test to see eviction behavior
4. Document which pods survive resource pressure

**Deliverables**:
- YAML files for all three pod types
- Screenshots showing QoS class assignment
- Documentation of eviction behavior
- Resource usage monitoring during stress tests

### Task 7.2: Resource Pressure Simulation
**Objective**: Test QoS behavior under resource constraints

**Requirements**:
1. Create multiple pods of each QoS class (3 guaranteed, 3 burstable, 3 best-effort)
2. Simulate memory pressure on your cluster
3. Monitor which pods get evicted first
4. Document the eviction order and reasoning

**Deliverables**:
- All pod manifests used
- Monitoring screenshots during resource pressure
- Eviction logs and analysis
- Recommendations for production workloads

---

## 8. Scheduling Tasks

### Task 8.1: Node Selector Scheduling
**Objective**: Control pod placement using node selectors

**Requirements**:
1. Label your cluster nodes with custom labels:
   - One node: `disktype=ssd`
   - Another node: `disktype=hdd`
2. Create pods that must be scheduled on SSD nodes only
3. Create pods that must be scheduled on HDD nodes only
4. Try to create a pod that requires a non-existent label
5. Document the scheduling behavior

**Deliverables**:
- Node labeling commands
- Pod YAML files with node selectors
- Screenshots showing pod placement
- Analysis of failed scheduling attempts

### Task 8.2: Affinity and Anti-Affinity
**Objective**: Implement advanced scheduling rules

**Requirements**:
1. Create a deployment where pods prefer to be on different nodes (anti-affinity)
2. Create a deployment where pods prefer to be co-located with specific other pods (affinity)
3. Use both hard and soft affinity rules
4. Test scaling behavior and document pod placement

**Deliverables**:
- Deployment YAML files with affinity rules
- Screenshots showing pod distribution
- Documentation of hard vs soft affinity behavior
- Analysis of scheduling decisions

### Task 8.3: Taints and Tolerations
**Objective**: Control scheduling using taints and tolerations

**Requirements**:
1. Taint one node with `role=database:NoSchedule`
2. Create a regular pod (should not schedule on tainted node)
3. Create a pod with toleration for the taint
4. Taint another node with `maintenance=true:NoExecute`
5. Document what happens to existing pods

**Deliverables**:
- Taint application commands
- Pod YAML files with and without tolerations
- Screenshots showing scheduling behavior
- Documentation of NoSchedule vs NoExecute effects

---

## 9. Labeling Tasks

### Task 9.1: Label Strategy Implementation
**Objective**: Develop and implement a comprehensive labeling strategy

**Requirements**:
1. Design a labeling strategy for a multi-tier application with:
   - Frontend tier (React app)
   - Backend tier (API server)
   - Database tier (PostgreSQL)
   - Multiple environments (dev, staging, prod)
2. Create deployments and services for each tier with consistent labeling
3. Demonstrate label-based resource selection and filtering
4. Show bulk operations using label selectors

**Deliverables**:
- Documented labeling strategy
- All resource YAML files with consistent labels
- Commands demonstrating label-based operations
- Examples of bulk operations using selectors

### Task 9.2: Advanced Label Selectors
**Objective**: Master complex label selector queries

**Requirements**:
1. Create 10 different pods with various label combinations
2. Practice complex selector queries:
   - Multiple AND conditions
   - NOT conditions
   - Set-based selectors
   - Existence checks
3. Use label selectors in service and deployment configurations
4. Demonstrate label selector expressions in different contexts

**Deliverables**:
- All pod creation commands with labels
- List of complex selector queries with explanations
- Service/deployment YAML files using advanced selectors
- Documentation of selector syntax and capabilities

---
