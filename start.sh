#!/bin/bash
# build the docker container 
docker build --no-cache -t sim-checker-flask-app:latest .

# run the docker image 
docker run -d -p 5000:5000 sim-checker-flask-app