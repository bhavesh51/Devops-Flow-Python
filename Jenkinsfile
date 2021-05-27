pipeline {
    agent { docker { image 'python:3.6.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python3 main.py'
      }
    }
  }
}