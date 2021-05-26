pipeline {
    agent { any { image 'python:3.6.9' } }
    stages {
        stage("Checkout") {
            steps {
                   echo 'Checkout' 
                }
            }
        stage("Branch To Build") {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                sh "pip install -r requirements.txt --user"
                sh 'python3 main.py'
                }
            }
        }
    }

}