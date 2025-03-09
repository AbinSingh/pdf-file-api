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
                    powershell '''
                    if (!(minikube status -ErrorAction SilentlyContinue)) {
                        Write-Host "Minikube is not running. Starting Minikube..."
                        minikube start --driver=docker
                    } else {
                        Write-Host "Minikube is already running."
                    }
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    powershell '''
                    Write-Host "Applying Kubernetes configurations..."
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    powershell '''
                    Write-Host "Fetching pod and service details..."
                    kubectl get pods -n $env:KUBE_NAMESPACE
                    kubectl get svc fastapi-service -n $env:KUBE_NAMESPACE
                    Write-Host "Minikube Service URL:"
                    minikube service fastapi-service --url
                    '''
                }
            }
        }
    }
}
