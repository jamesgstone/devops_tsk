pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
                git url: 'https://github.com/jamesgstone/devops_tsk'
            }
    }
    stage('Prune agent data')  {
                steps {			
                           sh 'sudo docker system prune -a -f'
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
  
    post {
	    always {
                         sh 'sudo docker-compose down --remove-orphans -v'
                         sh 'echo "removed all containers and images"'
			 deleteDir()
            }

            success {    
                         slackSend channel: '#succeeded-build',
                         color: 'good',
                         message: "${currentBuild.fullDisplayName} completed successfully."
            }       
                            
            failure {
                         slackSend channel: '#devops-alerts',
                         color: 'danger',
                         message: "${currentBuild.fullDisplayName} FAILED"
            }
    }   
}