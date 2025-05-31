## Jenkins Assignments - Easy to Advanced

## Beginner Level

### Task 1: Basic Job Creation
- Create a freestyle job named "hello-world"
- Configure it to echo "Hello Jenkins!" to console
- Run the job and capture the console output

### Task 2: Source Code Integration
- Create a job that pulls code from a public GitHub repository
- Configure Git polling every 5 minutes
- Add a build step to list all files in the workspace

### Task 3: Build Parameters
- Create a parameterized job with:
  - String parameter: `ENVIRONMENT` (default: "dev")
  - Boolean parameter: `DEPLOY` (default: false)
  - Choice parameter: `VERSION` with options: v1.0, v2.0, v3.0
- Use these parameters in build steps

### Task 4: Post-Build Actions
- Create a job that always fails (exit code 1)
- Configure email notification on failure
- Add workspace cleanup as post-build action

### Task 5: Build Artifacts
- Create a job that generates a text file with current timestamp
- Archive this file as a build artifact
- Configure artifact retention for last 5 builds

## INTERMEDIATE LEVEL

### Task 6: Multi-Branch Pipeline
- Set up a multi-branch pipeline for a repository with multiple branches
- Create a basic Jenkinsfile in each branch
- Configure branch discovery and auto-deletion of stale branches

### Task 7: Pipeline with Stages
Create a declarative pipeline with:
```groovy
- Checkout stage
- Build stage (mock compile)
- Test stage (mock unit tests, sonarqube integration)
- Deploy stage (conditional on branch)
```

### Task 8: Agent Management
- Configure a pipeline to run on specific agents
- Use different agents for different stages
- Implement parallel execution on multiple agents

### Task 9: Credentials Management
- Store credentials in Jenkins credential store
- Use credentials in pipeline (API key, database password)
- Implement credential masking in console output

### Task 10: Environment-Specific Deployments
- Create pipeline with environment promotion (dev → staging → prod)
- Implement manual approval for production deployment
- Use different configurations per environment

### Task 11: Docker Integration
- Create pipeline that builds Docker image
- Push image to registry with build number tag
- Run containers for testing
- Clean up containers post-build

### Task 12: Parallel Testing
- Set up pipeline with parallel test execution
- Run unit tests, integration tests, and linting in parallel
- Aggregate and publish test results

