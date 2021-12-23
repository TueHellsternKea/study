# Creating and Deploying a Flask app with Docker on Azure

## Docker on your local machine and Docker Hub account
You need to have installed Docker on your computer and created a Docker Hub account

## Create your environment with Docker
Create a *empty* directory on your local computer and *add a Dockerfile* to it which specifies the environment you need or pull an image from Docker Hub. 

Then make your **requirements.txt** file and **app.py** file in the same directory. 

### Sample Dockerfile
You can use this *sample Docker* file

    # Use the official Python runtime as a parent image
    FROM python:2.7-slim

    # Set the working directory to /app
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    ADD . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install --trusted-host pypi.python.org -r requirements.txt

    # Make port 80 available to the world outside this container
    EXPOSE 80

    # Define environment variable
    ENV NAME World

    # Run app.py when the container launches
    CMD ["python", "app.py"]

### Sample app.py
You can use this *sample app.py* file

    from flask import Flask
    from redis import Redis, RedisError
    import os
    import socket

    # Connect to Redis
    redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

    app = Flask(__name__)

    @app.route("/")
    def hello():
        try:
            visits = redis.incr("counter")
        except RedisError:
            visits = "<i>cannot connect to Redis, counter disabled</i>"

        html = "<h3>Hello {name}!</h3>" \
            "<b>Hostname:</b> {hostname}<br/>" \
            "<b>Visits:</b> {visits}"
        return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)

### Sample requirements.txt
You can use this *sample requirements.txt* file

    Flask
    Redis

## Build your Docker image and run it
When you have your *three files* in your new directory, you can **build** your Docker image, I called it **keatest**.

Confirm that the app works on your local machine by running the image and navigating to **localhost:4000** in your browser.

    docker build -t keatest .
    docker run -p 4000:80 keatest

## Upload your Dockerfile to to Docker Hub
Create a Docker Hub account if you don’t already have one. 

Create an *empty repo on Docker Hub* to push your image to. 

I called my repo **keatutorial**. 

Once that’s done login with the command below so you can publish from the CLI.

    docker logi

Tag your with your repo info.

    docker tag keatest [your-dockerhub-user]/[repo]:kea

Publish to your repo

    docker push [your-dockerhub-user]/[repo]:kea

## Create your container resource on Azure with your published Docker Hub image
