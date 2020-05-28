pipeline{
    // tools {
    //     maven "Maven 3.6.1"
    // }
    agent {
        docker {
            image 'sibh8/ubuntu-java'
            args '--user root'
        }
    }
    stages{
        stage("Build"){
            // when{
            //     changeset "**/vote/**"
            // }
            steps{
                echo "Compiling fibonacci"
                dir("vote") {
                    sh "pip install -r requirements.txt";
                }
            }
        }
        stage("Test"){
            // when{
            //     changeset "**/vote/**"
            // }
            steps{
                echo "Testing vote"
                dir("vote") {
                    sh "nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml";
                }
            }
        }
        stage('Sonarqube') {
            // when {
            //      branch 'master'
            // }
            environment{
              sonarpath = tool 'SonarScanner'
            }
            steps {
                echo 'Running Sonarqube Analysis..'
                  withSonarQubeEnv('sonar') {
                    sh "${sonarpath}/bin/sonar-scanner -Dproject.settings=vote/sonar-project.properties"
                  }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            slackSend(channel:"python-sample-app",color: "#15A339", message:"*Build Success*  \n\n Job Name : ${env.JOB_BASE_NAME} \n Build Number: ${env.BUILD_NUMBER} \n Branch: ${env.BRANCH_NAME} \n Build URL: (<${env.BUILD_URL} | Open>)")
        }
        failure{
            slackSend(channel:"python-sample-app",color: "#F00A21", message:"*Build Failed* \n\n Job Name : ${env.JOB_BASE_NAME} \n Build Number: ${env.BUILD_NUMBER} \n Branch: ${env.BRANCH_NAME} \n Build URL: (<${env.BUILD_URL} | Open>)")
        }
    }
}