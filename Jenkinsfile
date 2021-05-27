pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
 
    stage('build') {
        steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                    sh 'python test.py'
                }
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