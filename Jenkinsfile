pipeline {
    agent any
 
    options {
        skipDefaultCheckout(true)
    }
 
    stages {
        stage('Git') {
            steps {
                echo '> Checking out the Git version control ...'
                checkout scm
            }
        }
        stage('test ansible node'){
           steps {
               echo '> Checking ansible node version ...'
               sh 'py.test -v tests/host_test.py'
           }
        }

       stage('Sonarqube') {
             environment {
                 scannerHome = tool 'SonarQubeScanner'
             }
             steps {
                  withSonarQubeEnv('sonarqube') {
                      sh "${scannerHome}/bin/sonar-scanner"
                  }
                  timeout(time: 10, unit: 'MINUTES') {
                      waitForQualityGate abortPipeline: true
                  }
             }
        } 
        stage('Deploy ELK stack') {
            steps {
                echo '> Deploying ELK stack ...'
                ansiblePlaybook(
                    vaultCredentialsId: 'AnsibleVault',
                    inventory: 'inventory',
                    playbook: 'elk.yml'
                )
            }
        }
        stage('Test elasticsearch connection'){
           steps {
               echo '> Test elastic container connection...'
               sh 'py.test -v tests/test_elasticsearch.py'
               }
        }
        stage('Deploy heartbeat') {
            steps {
                echo '> Deploying heartbeat ...'
                ansiblePlaybook(
                    vaultCredentialsId: 'AnsibleVault',
                    inventory: 'inventory',
                    playbook: 'elk-heartbeat.yml'
                )
            }
        }
     
    }

}
