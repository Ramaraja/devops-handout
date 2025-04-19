**Most important and commonly used blocks** in a Jenkins Pipeline:

---

#### 1. `pipeline` – Root Block
The top-level block that defines the entire pipeline.
```groovy
pipeline {
    agent any
    stages {
        // your pipeline stages 
    }
}
```

---

#### 2. `agent` – Where to Run the Pipeline
Defines where the pipeline or a specific stage should run.

```groovy
agent any         // run on any available agent
agent none        // don’t assign a global agent
agent { label 'linux' } // run on a node labeled 'linux'
```

Can also be declared **per stage** for more control.

---

#### 3. `stages` and `stage` – Grouping of Build Steps
Defines a sequence of steps in the pipeline.

```groovy
stages {
    stage('Build') {
        steps {
            echo 'Building...'
        }
    }

    stage('Test') {
        steps {
            echo 'Testing...'
        }
    }
}
```

---

#### 4. `steps` – Actions to Run in a Stage
The actual commands or tasks Jenkins executes.

```groovy
steps {
    sh 'npm install'
    echo 'Build complete'
}
```

---

#### 5. `script` – Write Groovy Code / Logic
Use this when you need more complex logic (e.g. `if-else`, loops, variables).

```groovy
script {
    def version = '1.0.0'
    if (version == '1.0.0') {
        echo "Stable version"
    }
}
```

---

#### 6. `when` – Conditional Stage Execution
Runs a stage only if certain conditions are met.

```groovy
stage('Deploy to Prod') {
    when {
        branch 'main'
    }
    steps {
        echo 'Deploying to production'
    }
}
```

---

#### 7. `environment` – Define Environment Variables
Set env variables available to steps.

```groovy
environment {
    APP_ENV = 'dev'
    API_KEY = credentials('api-key-id')
}
```

---

#### 8. `post` – Actions After Pipeline or Stage
Run actions after success, failure, or always.

```groovy
post {
    success {
        echo 'Pipeline succeeded!'
    }
    failure {
        echo 'Pipeline failed!'
    }
    always {
        echo 'Runs every time'
    }
}
```

---

#### `parameters` – For User Input Before Build
Allow parameters to be passed into the build.

```groovy
parameters {
    string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
    booleanParam(name: 'DEPLOY', defaultValue: true, description: 'Deploy after build?')
}
```

---


