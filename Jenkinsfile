pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pip install flask'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
      }   
    }
  }
  post { 
        always { 
            echo 'I will always say Hello again!'
            sh 'python3 test.py'
        }
    }
}