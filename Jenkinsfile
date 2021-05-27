pipeline {
    agent { docker { image 'python:3.5.1' } }
    
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