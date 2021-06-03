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

    stage('docker login'){
      agent any
      steps{
              sh 'docker login -u bhavesh51 -p cb13fa99-aa57-43da-b4ef-f7e7852a2f43'
      }
    }

    stage('docker') {
      agent any
      steps {
        
          sh 'docker version'
          sh 'docker build -t python-docker-demo51 .'
          sh 'docker image list'
          sh 'docker tag python-docker-demo51 bhavesh51/devops_flow:latest'
      }   
    }

    // stage("Docker Push"){
    //   agent any
    //   steps {
    //       sh 'docker push bhavesh51/devops_flow:latest'
    //     }
    // } 
    
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