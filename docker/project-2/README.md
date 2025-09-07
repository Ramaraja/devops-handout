# Simple Flask Task API

A simple RESTful API built with Flask for managing tasks. This project demonstrates basic CRUD operations, testing, containerization, and CI/CD setup.

## Features

- RESTful API endpoints for tasks (Create, Read, Update, Delete)
- Unit tests with pytest
- Docker containerization
- Multiple CI/CD options (GitHub Actions & Jenkins)
- SonarQube integration for code quality
- Simple in-memory storage

## API Endpoints

- GET `/tasks` - List all tasks
- POST `/tasks` - Create a new task
- PUT `/tasks/<task_id>` - Update a task
- DELETE `/tasks/<task_id>` - Delete a task

## Local Development

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Run tests:
   ```bash
   pytest
   ```

## Docker Usage

You can either pull the image from Docker Hub or build it locally.

### Pull from Docker Hub
```bash
docker pull ramaraja/flask-task-api:latest
docker run -p 8000:8000 ramaraja/flask-task-api:latest
```

### Build Locally
1. Build the Docker image:
   ```bash
   docker build -t ramaraja/flask-task-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 ramaraja/flask-task-api
   ```

The API will be available at `http://localhost:8000`

## Example API Usage

Create a task:
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My first task"}'
```

List all tasks:
```bash
curl http://localhost:8000/tasks
```

## CI/CD

### GitHub Actions
The project includes GitHub Actions workflows that:
1. Run tests on every push and pull request
2. Build Docker image on main branch pushes

### Jenkins Pipeline
A Jenkinsfile is included that provides:
1. Automated build and test execution
2. Code coverage reporting
3. SonarQube analysis
4. Docker image building and deployment

To set up Jenkins pipeline:
1. Install required Jenkins plugins:
   - Pipeline
   - Docker Pipeline
   - SonarQube Scanner
   - Git

2. Configure Jenkins:
   - Add SonarQube server in Jenkins (Manage Jenkins > System)
   - Add SonarQube token in Jenkins credentials
   - Update SonarQube server URL in Jenkinsfile

### SonarQube Integration
The project includes SonarQube configuration for:
- Code quality analysis
- Code coverage tracking
- Security vulnerability scanning
- Technical debt monitoring
- Code smell detection

To set up SonarQube:
1. Run SonarQube server:
   ```bash
   docker run -d --name sonarqube -p 9000:9000 sonarqube
   ```
2. Create a new project with key 'flask-task-api'
3. Generate and configure authentication token

For more information about the quality gates and rules, visit the SonarQube dashboard after setup.
