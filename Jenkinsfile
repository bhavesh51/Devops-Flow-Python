pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
    stage('build') {
      steps {
        sh 'python3 -V'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        echo 'Hello'
        sh 'python test.py'
      }   
    }
  }
  post { 
        always { 
            echo 'I will always say Hello again!'
            
        }
    }
}