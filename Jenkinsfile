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
                sh 'pip install -r requirements.txt'
                sh 'python3 main.py'
            }
        }
    }

}