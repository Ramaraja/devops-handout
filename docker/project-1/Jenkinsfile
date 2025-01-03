pipeline {
    agent { docker { image 'python:3.12.0-alpine3.18' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install pre-reqs') {
            steps {
                sh 'python -m pip install requests'
            }
        }
        stage('Test') {
            steps {
                sh 'python webapp/unit.py'
            }
        }
        stage('Promote') {
            steps {
                sh 'python --version'
            }
        }   
    }
}
