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
          //sh 'docker build --tag python-docker .'
          sh 'docker image list'
          //sh 'docker rmi $(docker images --filter "dangling=true" -q --no-trunc)'
         // sh 'docker tag python-docker-demo51 bhavesh51/devops_flow:latest'
      }   
    }

    stage("Automate"){
      agent any
      steps {
          sh 'ansible-playbook automation.yaml'
        }
    }

    // stage("Deployment"){
    //   agent any
    //   steps {
    //       sh 'eval $(minikube docker-env)'
    //       sh 'kubectl config get-contexts'
    //       sh 'kubectl cluster-info'
    //       sh 'kubectl apply -f deployment.yaml'
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