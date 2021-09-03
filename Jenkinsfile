pipeline {
    
    stages {
        stage('GITLab Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/Papekhaly/Automation_challenge.git'
            }
        }
        stage('Execute Ansible') {
            steps {
                ansiblePlaybook become: true, colorized: true, credentialsId: 'github', disableHostKeyChecking: true, installation: 'ansible', playbook: 'elk.yml'
            }
        }
        stage('Notify sucess') {
            steps{
                echo("success")               
            }
        }
    
    }

}
