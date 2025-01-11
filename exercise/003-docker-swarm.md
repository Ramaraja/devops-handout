**Docker Swarm command examples** to help you manage Swarm clusters, services, and deployments.


### **1. Swarm Initialization and Setup**

#### **Initialize a Docker Swarm**
```bash
docker swarm init
```
- Outputs the manager token to add worker nodes.

#### **Join a Worker Node to the Swarm**
On the worker node, use the token provided during initialization:
```bash
docker swarm join --token <worker-token> <manager-ip>:2377
```

#### **Join a Manager Node to the Swarm**
Use the manager token:
```bash
docker swarm join --token <manager-token> <manager-ip>:2377
```

#### **Leave the Swarm**
```bash
docker swarm leave
```
- Use `--force` to remove a manager node.


### **2. Node Management**

#### **List Nodes in the Swarm**
```bash
docker node ls
```

#### **Inspect a Node**
```bash
docker node inspect <node-id> --pretty
```

#### **Promote a Node to Manager**
```bash
docker node promote <node-id>
```

#### **Demote a Manager to Worker**
```bash
docker node demote <node-id>
```

#### **Remove a Node**
```bash
docker node rm <node-id>
```


### **3. Service Management**

#### **Deploy a Service**
```bash
docker service create --name web --replicas 3 -p 8080:80 nginx
```

#### **List Services**
```bash
docker service ls
```

#### **Inspect a Service**
```bash
docker service inspect <service-name> --pretty
```

#### **Scale a Service**
```bash
docker service scale web=5
```

#### **Update a Service**
```bash
docker service update --image nginx:latest web
```

#### **Remove a Service**
```bash
docker service rm <service-name>
```


### **4. Stack Management**
(Refer the example of dc-project-2 under docker folder)
#### **Deploy a Stack**
```bash
docker stack deploy -c docker-compose.yml webapp
```

#### **List Stacks**
```bash
docker stack ls
```

#### **Inspect a Stack**
```bash
docker stack ps webapp
```

#### **Remove a Stack**
```bash
docker stack rm webapp
```


### **5. Task Management**

#### **List Tasks in a Service**
```bash
docker service ps <service-name>
```

#### **Inspect a Task**
```bash
docker inspect <task-id>
```


### **6. Logs and Monitoring**

#### **View Service Logs**
```bash
docker service logs <service-name>
```
- Tail logs:
  ```bash
  docker service logs -f <service-name>
  ```

#### **List Swarm Events**
```bash
docker events
```


### **7. Swarm Tokens**

#### **View Manager and Worker Tokens**
```bash
docker swarm join-token manager
docker swarm join-token worker
```

#### **Rotate Tokens**
```bash
docker swarm join-token --rotate manager
docker swarm join-token --rotate worker
```


### **8. Drain, Pause, and Activate Nodes**

#### **Drain a Node**
- Stops scheduling new tasks on the node:
  ```bash
  docker node update --availability drain <node-id>
  ```

#### **Pause Scheduling on a Node**
- Maintains running tasks but prevents scheduling new ones:
  ```bash
  docker node update --availability pause <node-id>
  ```

#### **Activate a Node**
- Allows task scheduling:
  ```bash
  docker node update --availability active <node-id>
  ```


### **9. Troubleshooting and Debugging**

#### **Check Swarm Status**
```bash
docker info | grep Swarm
```

#### **Debug Tasks**
Inspect task logs:
```bash
docker logs <task-id>
```

