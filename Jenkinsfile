def imageRegistry="192.168.89.150:5000"
def imageName="football_stats"
def imageTag="test"
def fullimageName="$imageRegistry/$imageName:$imageTag" 
def dockerfilePath="mmss/Dockerfile"
def srccodePath="mmss/app"
def lintvenvPath="/opt/python-lint/bin/activate"

pipeline {
    agent {
        label 'agent'
    }
    stages {
        stage('source-code-retrieve') { 
            steps { // PASSED
                checkout scm //Repo configured in the job definition
             //   sh "ls -la" // File debug
            }
        }
        stage ('lint/static-analysis'){
            steps {
                script { // PASSED
                    echo "### STEP: DOCKER-HADOLINT ###"
                    sh "docker run --rm -i hadolint/hadolint < $dockerfilePath"
                }
                script{ // PASSED
                    echo "### STEP: DOCKER-TRIVY-CONFIG ###"
                    sh "trivy fs --security-checks vuln,secret,config $dockerfilePath"  
                }
                script { // PASSED
                    echo "### STEP: PYTHON-BLACK ###"
                    sh ". $lintvenvPath" // . in sh is equal to source in bash
                    sh "black $srccodePath"
                }
                script { // PASSED
                    echo "### STEP: PYTHON-RUFF ###"
                    sh ". $lintvenvPath && ruff check --fix $srccodePath"
                }
            }
            }
        }
        stage ('package-build') {
            steps { // PASSED
                script {
                    echo "### STEP: DOCKER-BUILD ###"
                    sh "cd mmss && docker build -t $fullimageName ."
                    // applicationImage = docker.build( //To be included with docker workflow plugin
                    //     "$imageName:$dockerTag",
                    //     "-f $dockerPath .")
                }
            }
        }
        stage ('security-scan'){
            steps {
                script{
                    sh "trivy image $fullimageName"
                }
            }
        }
        stage ('package-publish') {
            steps {  // PASSED
                script{
                    echo "### STEP: DOCKER-PUBLISH ###"
                    sh "docker push $fullimageName"
                    echo "### CHECK IMAGE PRESENCE IN REGISTRY"
                    sh "curl http://$imageRegistry/v2/$imageName/tags/list"
                }
            }
        }    

        
    }
}