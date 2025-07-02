def imageName="football_data"

pipeline {
    agent {
        label 'agent'
    }
    stages {
        stage('Get Code') {
            steps {
                checkout scm //Repo configured in the job definition
            }
        }

        stage ('Build Docker image') {
            steps {
                script {
                    dockerTag = "test"
                    applicationImage = docker.build("$imageName:$dockerTag", ".")
                }
            }

        }
    }
}