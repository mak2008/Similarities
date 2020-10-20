FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# install all requirements like flask
RUN pip install -r requirements.txt

# copy the app file 
COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]