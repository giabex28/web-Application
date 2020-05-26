This repo contains files needed to create a web application using Python and Flask, which shows the line "Hello World" and counts webpage hits. The application web server used is nginx, in combination with uwsgi a software application used for serving Python web applications in conjunction with a nginx web server. The backend database used is Redis. The Flask web application, the web server nginx and the database redis are developed as docker containers that operate all togheter.


### Details
The app is written in Python, using Flask framework

 - `app.py` is the actual app code
 - `requirements.txt` are the dependencies required to run the app
 - `Dockerfile` is used to build docker container
 - `app.ini` is used to set up uwsgi apllication framework.

The following docker containers are run:
   - flask container
   - nginx web server container
   - redis container

### Building/testing steps
Download/pull this repository:

Go to the newly created directory:
cd appication

Build the docker images:
docker-compose build

Run the docker containers:
docker-compose up -d

### additional reqiurements(not implemented)
In order to perform the buiid of the application container at every commit(continous integration) the following steps can be performed:
 - create a GitHub repository of the project
 - integrate the repository with Jenkins, so for each code commit to the repository Jenkins performs Continous integration and deployment. 
 - Jenkins create a docker image and it puts its into Docker Hub. 
