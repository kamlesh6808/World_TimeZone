pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository
                git branch: 'main', url: 'https://github.com/kamlesh6808/World_TimeZone.git'
            }
        }

        stage('Execute Python Script') {
            steps {
                // Execute the Python script
                sh 'python3 world_timezone.py'
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
    }
}
