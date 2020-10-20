# pre-requisites:
# install and login to docker 

# first run the start.sh


# renaming the docker image as per convention
# create tag to push image to docker hub
docker tag sim-checker-flask-app mak2008/sim-checker-flask-app:1.0

# pushing the docker image to docker public hub
# docker push command
docker push mak2008/sim-checker-flask-app:1.0


# This is for pulling and running the docker file 
# pull the docker image 
docker pull mak2008/sim-checker-flask-app:1.0

# run the docker image 
docker run -d -p 5000:5000 mak2008/sim-checker-flask-app:1.0
