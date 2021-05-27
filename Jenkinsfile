pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
 
    stage('build') {
        steps {
                sh 'virtualenv venv --distribute'
                sh 'source venv/bin/activate '
                sh 'pip install --user -r requirements.txt'
                sh 'python3 test.py'
            }
    }
    stage('test') {
      steps {
        echo 'Hello'
        sh 'python3 test.py'
      }   
    }
  }
  post { 
        always { 
            echo 'I will always say Hello again!'
            
        }
    }
}