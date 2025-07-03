def imageName="football_data"
def dockerPath="most_matches_single_season/Dockerfile"

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
                    sh "cd mmss && docker build -t $imageName:$dockerTag ."
                    // applicationImage = docker.build( //To be included with docker workflow plugin
                    //     "$imageName:$dockerTag",
                    //     "-f $dockerPath .")
                }
            }

        }
    }
}