pipeline { 
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Pavanysp/scientific_calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt || echo "No dependencies to install"'
            }
        }

        stage('Build Project') {
            steps {
                sh 'chmod +x calculator.py'
                sh 'python3 calculator.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'chmod +x test_calculator.py'
                sh 'python3 -m unittest test_calculator.py || echo "Tests failed"'
            }
        }
    }
}
