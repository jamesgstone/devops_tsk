pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'my-github-credentials', url: 'https://github.com/my-repo.git']]])
      }
    }
    stage('Build Docker Images') {
      steps {
          sh 'sudo docker-compose build'
     }
    }
    stage('Test') {
                steps {
			    echo "****building containers for testing*****"
                            sh '''
                                sudo docker-compose up -d
                                sudo docker-compose ps
                                '''
			    sh 'sleep 5'
                            sh 'python3 ./unit_tests/website_unittest.py'
      }
	}

    stage('Push Docker Image to Docker Hub') {
      steps {
        withDockerRegistry([credentialsId: 'my-docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
           sh '''
				      docker push my-app-image
              docker push nginx_srv
			    '''
			 
        }
      }
    }
  }
}