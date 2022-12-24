from flask import Flask
import docker

# a simple Flask web application that talks to the local Docker engine and retrieves a list of running containers

app = Flask(__name__)

@app.route('/containers')
def list_containers():
    # Connect to the Docker daemon
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    # Get a list of running containers
    containers = client.containers.list(filters={'status': 'running'})

    # Build a response with the names of the running containers
    response = '<h1>Running containers:</h1>'
    for container in containers:
        response += '<p>{}</p>'.format(container.name)

    return response

if __name__ == '__main__':
    app.run()
