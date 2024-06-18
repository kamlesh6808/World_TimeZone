pipeline {
    agent any

    environment {
        // Define the path to the Python executable, if needed
        PYTHON_ENV = '/usr/bin/python3'  // Adjust this path as per your environment
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository
                git 'https://github.com/kamlesh6808/World_TimeZone.git'
            }
        }
        

        stage('Execute Python Script') {
            steps {
                // Execute the Python script
                sh '${PYTHON_ENV} world_timezone.py'
            }
        }
    }
}
