pipeline {
  agent none
  
  stages {
    stage('build') {
      agent { docker { image 'python:3.6.9' } }
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
      agent { docker { image 'python:3.6.9' } }
      steps {
          withEnv(["HOME=${env.WORKSPACE}"]) {
              sh 'python3 test.py'
          }
      }   
    }

    stage('docker') {
      agent any
      steps {
          sh 'docker version'
          sh 'docker build -t devopsflow51'
          sh 'docker image list'
      }   
    }
    
  }
  post {
        always {
            echo 'Email Notification'
            
            emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}"
            
        }
    }
}