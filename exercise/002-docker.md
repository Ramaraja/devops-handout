
### **1. Getting Started with Docker**
- **Exercise:** Install Docker and run your first container.
  1. Install Docker on your system.
  2. Run the `hello-world` container using `docker run hello-world`.
  3. Inspect the output to understand how Docker works.

---

### **2. Working with Docker Images**
- **Exercise:** Explore Docker Hub and manage images.
  1. Search for an image (e.g., Nginx) on Docker Hub: `docker search nginx`.
  2. Pull the Nginx image: `docker pull nginx`.
  3. List available images: `docker images`.
  4. Remove an image: `docker rmi <image-id>`.

---

### **3. Running Containers**
- **Exercise:** Run a container and explore basic options.
  1. Start an Nginx container: `docker run -d --name my-nginx -p 8080:80 nginx`.
  2. Check running containers: `docker ps`.
  3. Stop and restart the container: `docker stop my-nginx`, `docker start my-nginx`.
  4. Remove the container: `docker rm my-nginx`.

---

### **4. Building Custom Images**
- **Exercise:** Create a custom Docker image.
  1. Create a `Dockerfile` for a simple Python application:
     ```Dockerfile
     FROM python:3.9
     COPY app.py /app.py
     CMD ["python", "/app.py"]
     ```
  2. Write the `app.py` script:
     ```python
     print("Hello, Docker!")
     ```
  3. Build the image: `docker build -t my-python-app .`.
  4. Run the container: `docker run my-python-app`.

---

### **5. Managing Volumes**
- **Exercise:** Use Docker volumes to persist data.
  1. Create a volume: `docker volume create my-volume`.
  2. Run a MySQL container with the volume:
     ```bash
     docker run -d --name my-mysql -e MYSQL_ROOT_PASSWORD=root -v my-volume:/var/lib/mysql mysql
     ```
  3. Inspect the volume: `docker volume inspect my-volume`.
  4. Remove the container and verify the volume persists.

---

### **6. Networking with Docker**
- **Exercise:** Create a custom network and connect containers.
  1. Create a custom network: `docker network create my-network`.
  2. Run two containers on the same network:
     ```bash
     docker run -d --name web1 --network my-network nginx
     docker run -d --name web2 --network my-network nginx
     ```
  3. Use `docker exec` to test connectivity between the containers:
     ```bash
     docker exec -it web1 ping web2
     ```

---
### **7. Custom Image creation**
### **Container Creation**
1. **Run a Container from a Public Image:**
   ```bash
   docker run -d --name my-nginx -p 8080:80 nginx
   ```
   - This runs an Nginx container in detached mode.
   - `-p 8080:80` maps port 8080 on your host to port 80 in the container.

2. **Verify the Container is Running:**
   ```bash
   docker ps
   ```

3. **Access the Container’s Service:**
   - Open a browser and visit `http://localhost:8080` to see the default Nginx page.

4. **Stop the Container:**
   ```bash
   docker stop my-nginx
   ```

5. **Remove the Container:**
   ```bash
   docker rm my-nginx
   ```


### **Create a Custom Docker Image**
1. **Create a Custom HTML File:**
   - Create a directory and navigate into it:
     ```bash
     mkdir custom-nginx && cd custom-nginx
     ```
   - Create an `index.html` file:
     ```html
     echo "<h1>Welcome to My Custom Nginx</h1>" > index.html
     ```

2. **Write a Dockerfile:**
   - Create a `Dockerfile` in the same directory:
     ```Dockerfile
     FROM nginx
     COPY index.html /usr/share/nginx/html/index.html
     ```

3. **Build the Docker Image:**
   ```bash
   docker build -t my-nginx-image .
   ```

4. **Verify the Image:**
   ```bash
   docker images
   ```

5. **Run a Container from the Custom Image:**
   ```bash
   docker run -d --name custom-nginx -p 8080:80 my-nginx-image
   ```

6. **Access the Custom Page:**
   - Visit `http://localhost:8080` in your browser to see the custom HTML page.


### **Push the Image to Docker Hub**
1. **Log in to Docker Hub:**
   ```bash
   docker login
   ```
   - Enter your Docker Hub username and password.

2. **Tag the Image for Docker Hub:**
   ```bash
   docker tag my-nginx-image <your-dockerhub-username>/my-nginx-image:1.0
   ```

3. **Push the Image to Docker Hub:**
   ```bash
   docker push <your-dockerhub-username>/my-nginx-image:1.0
   ```

4. **Verify the Image on Docker Hub:**
   - Log in to your Docker Hub account and check the repository to see the uploaded image.


### **Pull and Run the Pushed Image**
1. **Pull the Image from Docker Hub:**
   ```bash
   docker pull <your-dockerhub-username>/my-nginx-image:1.0
   ```

2. **Run the Pulled Image:**
   ```bash
   docker run -d --name pulled-nginx -p 8081:80 <your-dockerhub-username>/my-nginx-image:1.0
   ```

3. **Access the Running Container:**
   - Visit `http://localhost:8081` to confirm the custom HTML page is served.

---

### **8. Multi-Container Applications with Docker Compose**
- **Exercise:** Deploy a web application with Docker Compose.
  1. Create a `docker-compose.yml` file for a simple WordPress setup:
     ```yaml
     version: '3.7'
     services:
       db:
         image: mysql:5.7
         environment:
           MYSQL_ROOT_PASSWORD: root
           MYSQL_DATABASE: wordpress
       wordpress:
         image: wordpress
         ports:
           - "8080:80"
         environment:
           WORDPRESS_DB_HOST: db
           WORDPRESS_DB_PASSWORD: root
     ```
  2. Start the application: `docker-compose up`.
  3. Access the WordPress site at `http://localhost:8080`.

---

### **9. Inspecting and Debugging Containers**
- **Exercise:** Use Docker commands to inspect and debug.
  1. Inspect a container’s metadata: `docker inspect <container-id>`.
  2. Check container logs: `docker logs <container-id>`.
  3. Access a running container’s shell: `docker exec -it <container-id> bash`.

---

### **10. Scaling with Docker Compose**
- **Exercise:** Scale a service using Docker Compose.
  1. Modify the `docker-compose.yml` file to add `replicas`.
  2. Scale up a service: `docker-compose up --scale web=3`.
  3. Verify running containers: `docker ps`.

---

### **11. Deploying with Docker Swarm**
- **Exercise:** Set up and manage a Docker Swarm cluster.
  1. Initialize a Docker Swarm: `docker swarm init`.
  2. Deploy a service to the swarm:
     ```bash
     docker service create --name web-service -p 8080:80 nginx
     ```
  3. Scale the service: `docker service scale web-service=5`.
  4. Check the service status: `docker service ls`.

---

### **12. Docker Security**
- **Exercise:** Explore security features in Docker.
  1. Scan a Docker image for vulnerabilities: `docker scan <image-name>`.
  2. Run a container with limited permissions: `docker run --read-only nginx`.
  3. Configure secrets management using `docker secret`.

---

**Docker Compose** example to demonstrate how to define and run multiple services using a `docker-compose.yml` file.

### **1. Example Use Case**
A simple application with:
1. A **web service** running an Nginx server.
2. A **database service** using MySQL.


### **2. `docker-compose.yml` File**

```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    container_name: web-container
    ports:
      - "8080:80" # Map localhost:8080 to container's port 80
    volumes:
      - ./html:/usr/share/nginx/html # Mount local directory for web content
    depends_on:
      - db

  db:
    image: mysql:8.0
    container_name: db-container
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: mydatabase
      MYSQL_USER: myuser
      MYSQL_PASSWORD: mypassword
    ports:
      - "3306:3306" # Map MySQL's default port
    volumes:
      - db-data:/var/lib/mysql # Persist MySQL data

volumes:
  db-data:
```


### **3. Directory Structure**
```
project/
├── docker-compose.yml
├── html/
│   └── index.html
```

- `html/index.html`: Your website content. Example:
  ```html
  <html>
    <head>
      <title>Welcome</title>
    </head>
    <body>
      <h1>Hello from Nginx!</h1>
    </body>
  </html>
  ```


### **4. Commands to Run**
1. **Start Services:**
   ```bash
   docker-compose up
   ```
   - Adds `-d` to run in detached mode:
     ```bash
     docker-compose up -d
     ```

2. **Stop Services:**
   ```bash
   docker-compose down
   ```

3. **List Running Containers:**
   ```bash
   docker-compose ps
   ```

4. **Rebuild Services:**
   If you've updated the configuration:
   ```bash
   docker-compose up --build
   ```


### **5. Explanation**
- **Services:**
  - `web`: Runs an Nginx server.
  - `db`: Runs a MySQL database.
- **Volumes:**
  - Ensures MySQL data persists even after the container is stopped.
- **Ports:**
  - Maps host ports to container ports for external access.
- **Dependencies:**
  - `depends_on`: Ensures `db` service starts before `web`.


### **6. Extending the Example**
- Add an **application service** (e.g., a Python Flask app):
  ```yaml
  app:
    build:
      context: ./app
    container_name: app-container
    ports:
      - "5000:5000"
    depends_on:
      - db
  ```
  - Create a Dockerfile in the `./app` directory for your Flask app.

---


### **Docker Network Overview**
Docker networking allows containers to communicate with each other and the outside world. Docker provides several networking modes, including:

1. **Bridge Network (default):**
   - Containers communicate with each other using their internal IPs.
   - Containers can access the host system and external networks via NAT.

2. **Host Network:**
   - The container shares the host machine's network stack.
   - No isolation from the host.

3. **None Network:**
   - No network for the container. Fully isolated.

4. **Overlay Network:**
   - Allows containers on different hosts to communicate securely.
   - Used in Docker Swarm or Kubernetes.

5. **Macvlan Network:**
   - Assigns a MAC address to containers, making them appear as physical devices on the network.

---

### **Docker Network Commands**

1. **List Networks:**
   ```bash
   docker network ls
   ```

2. **Inspect a Network:**
   ```bash
   docker network inspect <network_name>
   ```

3. **Create a Network:**
   ```bash
   docker network create my-network
   ```

4. **Remove a Network:**
   ```bash
   docker network rm my-network
   ```

5. **Connect a Container to a Network:**
   ```bash
   docker network connect my-network my-container
   ```

6. **Disconnect a Container from a Network:**
   ```bash
   docker network disconnect my-network my-container
   ```

---

### **Docker Network**

#### **1. Default Bridge Network**
1. Start two containers without specifying a network:
   ```bash
   docker run -d --name container1 alpine sleep 1000
   docker run -d --name container2 alpine sleep 1000
   ```

2. Test connectivity:
   ```bash
   docker exec container1 ping -c 2 container2
   ```
   - **Expected result:** Fails because default bridge network does not allow automatic name resolution.

3. Connect both containers to a user-defined bridge:
   ```bash
   docker network create my-bridge
   docker network connect my-bridge container1
   docker network connect my-bridge container2
   ```

4. Test connectivity again:
   ```bash
   docker exec container1 ping -c 2 container2
   ```
   - **Expected result:** Success.

---

#### **2. Host Network**
1. Run a container with the host network:
   ```bash
   docker run --rm --network host -d nginx
   ```

2. Access the service:
   - Open a browser and navigate to `http://localhost` to see the Nginx default page.

3. Check container processes on the host:
   ```bash
   netstat -tuln
   ```

---

#### **3. Overlay Network (Docker Swarm)**
1. Enable Docker Swarm:
   ```bash
   docker swarm init
   ```

2. Create an overlay network:
   ```bash
   docker network create -d overlay my-overlay
   ```

3. Deploy a service to the overlay network:
   ```bash
   docker service create --name my-service --network my-overlay -p 8080:80 nginx
   ```

4. Verify:
   ```bash
   docker network inspect my-overlay
   ```

---

#### **4. Macvlan Network**
1. Create a Macvlan network:
   ```bash
   docker network create -d macvlan \
       --subnet=192.168.1.0/24 \
       --gateway=192.168.1.1 \
       -o parent=eth0 my-macvlan
   ```

2. Run a container on the Macvlan network:
   ```bash
   docker run --rm --net my-macvlan --ip 192.168.1.100 -it alpine ash
   ```

3. Test connectivity:
   - Ping other devices on the same subnet.

---

#### **5. Docker Compose with Custom Network**
Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  app:
    image: nginx
    networks:
      - my-custom-network

  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
    networks:
      - my-custom-network

networks:
  my-custom-network:
    driver: bridge
```

Run the setup:
```bash
docker-compose up
```

Inspect the network:
```bash
docker network inspect my-custom-network
```


### **Key Commands Cheat Sheet**
- **Create Network:** `docker network create <name>`
- **Inspect Network:** `docker network inspect <name>`
- **Delete Network:** `docker network rm <name>`
- **List Networks:** `docker network ls`

---
