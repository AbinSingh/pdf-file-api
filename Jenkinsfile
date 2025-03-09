pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/AbinSingh/pdf-file-api.git' // Replace with your repo URL
        DOCKER_IMAGE = 'abinsr/my-fastapi-app:latest' // Your Docker Hub image
        KUBE_NAMESPACE = 'default'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "$GIT_REPO"
            }
        }

        stage('Start Minikube') {
            steps {
                script {
                    sh "minikube status || minikube start --driver=docker"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "kubectl apply -f k8s/deployment.yaml"
                    sh "kubectl apply -f k8s/service.yaml"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    sh "kubectl get pods -n $KUBE_NAMESPACE"
                    sh "kubectl get svc fastapi-service -n $KUBE_NAMESPACE"
                    sh "minikube service fastapi-service --url"
                }
            }
        }
    }
}
