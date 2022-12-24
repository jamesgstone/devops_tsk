pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'my-github-credentials', url: 'https://github.com/my-repo.git']]])
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t my-app-image .'
      }
    }
    stage('Push Docker Image to Docker Hub') {
      steps {
        withDockerRegistry([credentialsId: 'my-docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
          sh 'docker push my-image'
        }
      }
    }
  }
}