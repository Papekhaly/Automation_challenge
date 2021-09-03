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
