# devops_tsk
This Jenkinsfile assumes that you have already configured your Jenkins instance with the necessary plugins (e.g. the Jenkins Pipeline plugin and the Docker plugin), and that you have created credentials for your GitHub repository and Docker Hub account.
# app
a simple Flask web application that talks to the local Docker engine and retrieves a list of running containers
This application defines a single route, /containers, that returns a list of the names of the running containers when accessed through a web browser.

To use this application, you will need to have the Docker Python module installed.
# unit test 
sends a simple http request

# post
added success/failure slack notifications - * Slack Notification plugin is necessary and credentials + channels must be configured 