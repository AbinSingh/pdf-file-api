pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/AbinSingh/pdf-file-api.git'
        DOCKER_IMAGE = 'abinsr/my-fastapi-app:latest'
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
                    $status = minikube status
                    if ($LASTEXITCODE -ne 0) {
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

                    Write-Host "Fetching Minikube Service URL..."
                    $NODE_PORT = kubectl get svc fastapi-service -n $env:KUBE_NAMESPACE -o=jsonpath="{.spec.ports[0].nodePort}"
                    $MINIKUBE_IP = minikube ip
                    Write-Host "FastAPI Service URL: http://$MINIKUBE_IP`:$NODE_PORT"
                    '''
                }
            }
        }
    }
}
