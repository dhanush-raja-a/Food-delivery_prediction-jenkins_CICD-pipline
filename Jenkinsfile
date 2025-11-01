pipeline {
    agent any

    stages {
        stage('Pull from GitHub') {
            steps {
                echo '🔁 Pulling latest code from GitHub...'
                git branch: 'main', url: 'https://github.com/dhanush-raja-a/Food-delivery_prediction-jenkins_CICD-pipline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t food-delivery-ml .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo '🧹 Stopping old container if exists...'
                sh '''
                CONTAINER_ID=$(docker ps -q --filter "publish=5000")
                if [ ! -z "$CONTAINER_ID" ]; then
                    docker stop $CONTAINER_ID && docker rm $CONTAINER_ID
                fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo '🚀 Running new container on port 5000...'
                sh 'docker run -d -p 5000:5000 food-delivery-ml'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful! Visit http:////13.126.159.162:5000'
        }
        failure {
            echo '❌ Build or Deployment Failed. Check logs.'
        }
    }
}