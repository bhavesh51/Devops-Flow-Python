pipeline {
    agent { docker { image 'python:3.7.2' } }
    
    stages {
        stage("Checkout") {
            steps {
                   echo 'Checkout' 
                }
            }
        stage("Branch To Build") {
            steps {
                echo 'build'
            }
        }
    }

}