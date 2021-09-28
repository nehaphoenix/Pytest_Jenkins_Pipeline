pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '28e0c8dd-65bb-4a06-a218-0688ed36ef83', url: 'https://github.com/nehaphoenix/Pytest_Jenkins_Pipeline.git']]])
            }
        }
        stage('Build'){
            steps {
                git branch: 'main', credentialsId: '28e0c8dd-65bb-4a06-a218-0688ed36ef83', url: 'https://github.com/nehaphoenix/Pytest_Jenkins_Pipeline.git'
                bat 'pytest test_main.py -v'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing is complete!!'
            }
        }
    }
}
