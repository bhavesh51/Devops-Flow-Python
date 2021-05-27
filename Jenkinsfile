pipeline {
  agent { docker { image 'python:3.6.9' } }
  stages {
 
        stage('build') {
        steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
            sh script:'''
                            #/bin/bash
                            echo "PATH is: $PATH"
                              python --version
                              python -m pip install --upgrade pip --user
                              ls
                              pip install --user -r requirements.txt
                              export PATH="$WORKSPACE/.local/bin:$PATH"
                                '''
            }
        }
    }
    stage('run') {
      steps {
        echo 'Hello'
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