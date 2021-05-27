pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'python3 -V'
      }
    }
    stage('test') {
      steps {
        echo 'Hello'
      }   
    }
  }
  post { 
        always { 
            echo 'I will always say Hello again!'
            
        }
    }
}