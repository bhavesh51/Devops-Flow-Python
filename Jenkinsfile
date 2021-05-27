pipeline {
    agent any 
    stages {
        stage("Checkout") {
            steps {
                   echo 'Checkout' 
                   workspace = env.WORKSPACE
                    echo '${workspace}'

                }
            }
        stage("Branch To Build") {
            steps {
                echo 'build'
            }
        }
    }

}