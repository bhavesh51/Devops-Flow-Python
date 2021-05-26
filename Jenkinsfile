pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                   echo 'Checkout' 
                }
            }
        stage("Branch To Build") {
            steps {
                echo 'build'
                sh 'python3 main.py'
            }
        }
    }

}