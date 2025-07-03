def imageName="football_data"
def dockerPath="mmss/Dockerfile"

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
        stage ('lint/static-analysis'){
            steps {
                script {
                    echo "### STEP: DOCKER-HADOLINT ###"
                    sh "docker run --rm -i hadolint/hadolint < $dockerPath"
                }
            }
        }
        stage ('package-build') {
            steps {
                script {
                    echo "### STEP: DOCKER-BUILD ###"
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