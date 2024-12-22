### Examples

#### Hello world!
```
pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello, Jenkins!'
            }
        }
    }
}
```


------
#### Checkout repo
```
pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ramaraja/devops-repo.git'
            }
        }
    }
}
```

-------
#### Parameter example
```
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Git branch to build')
    }
    stages {
        stage('Display Parameters') {
            steps {
                echo "Building branch: ${params.BRANCH_NAME}"
            }
        }
    }
}
```
-------
#### Docker build Image and Pushing to hub
```
pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ramaraja/devops-repo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-app:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh 'echo $DOCKERHUB_TOKEN | docker login -u myuser --password-stdin'
                    sh 'docker push my-app:latest'
                }
            }
        }
    }
}
```
----

# docker build and deploy
```
pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "my-app:latest"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ramaraja/devops-repo.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/ --junitxml=results.xml'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh 'echo $DOCKERHUB_TOKEN | docker login -u myuser --password-stdin'
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'results.xml'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
```
