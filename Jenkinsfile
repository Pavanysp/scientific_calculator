pipeline { 
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url:'https://github.com/Pavanysp/scientific_calculator.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt || echo "No dependencies to install"'
            }
        }

        stage('Build Project') {
            steps {
                sh 'chmod u+x calculator.py'
                sh 'python3 calculator.py --auto'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
            chmod u+x test_calculator.py
            pip3 install --upgrade pip
            pip3 install pytest
            export PATH=$HOME/.local/bin:$PATH  # Add pytest to PATH
            pytest --maxfail=1 --disable-warnings --tb=short
        '''
    }
}


       
    }
}
