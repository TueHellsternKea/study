# Creating and Deploying a Flask app with Docker on Azure
This demo builds a simple Python web application running on Docker Compose. 

The application uses the Flask framework and maintains a hit counter in Redis.

## Docker on your local machine and Docker Hub account
You need to have installed Docker on your computer and created a Docker Hub account

## Create your environment with Docker
Create a *empty* directory on your local computer.

    mkdir keadockerdemo
    cd keadockerdemo

Then make 4 files in the same directory

- app.py
- requirements.txt
- Dockerfile
- docker-compose.yml

### Sample app.py
You can use this sample *app.py* file

    import time
    import redis
    from flask import Flask

    app = Flask(__name__)
    cache = redis.Redis(host='redis', port=6379)

    def get_hit_count():
        retries = 5
        while True:
            try:
                return cache.incr('hits')
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    raise exc
                retries -= 1
                time.sleep(0.5)

    @app.route('/')
    def hello():
        count = get_hit_count()
        return 'Hello World! I have been seen {} times.\n'.format(count)

In this example, **redis** is the hostname of the **redis container** on the application’s network. 

Use the default port for Redis, **6379**.

### Sample requirements.txt
Create another file called **requirements.txt** in your project directory and paste this in:

    flask
    redis

## Create a Dockerfile
Create a Dockerfile that builds the Docker image. The image contains all the dependencies the Python application requires, including Python itself.

In your project directory, create a file named **Dockerfile** and paste the following:

    # syntax=docker/dockerfile:1
    FROM python:3
    WORKDIR /code
    ENV FLASK_APP=app.py
    ENV FLASK_RUN_HOST=0.0.0.0
    RUN apk add --no-cache gcc musl-dev linux-headers
    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt
    EXPOSE 5000
    COPY . .
    CMD ["flask", "run"]

This tells *Docker* to:

- Build an image starting with the Python 3.7 image.
- Set the working directory to **/code**
- Set *environment variables* used by the flask command.
- Install gcc and other dependencies
- Copy *requirements.txt* and install the Python dependencies.
- Add metadata to the image to describe that the container is listening on port *5000*
- Copy the current directory **.** in the project to the workdir **.** in the image.
- Set the default command for the container to **flask run**

## Define services in a Compose file
Create a file called **docker-compose.yml** in your project directory and paste the following:

    version: "3.9"
    services:
    web:
        build: .
        ports:
          - "5000:5000"
    redis:
        image: "redis:alpine"

This Compose file defines two services: **web** and **redis**

### Web service
The web service uses an image that’s built from the **Dockerfile** in the current directory. It then binds the container and the host machine to the exposed port, **5000**. This example service uses the default port for the Flask web server, **5000**.

### Redis service
The **redis** service uses a **public Redis image** pulled from the Docker Hub registry.

## Build and run your app with Compose
From your project directory, start up your application by running **docker-compose up** - *Make sure that Docker is running on your computer!*

    docker-compose up

Compose pulls a Redis image, builds an image for your code, and starts the services you defined. In this case, the code is statically copied into the image at build time.

Enter **http://localhost:5000/** in a browser to see the application running.

If this doesn’t resolve, you can also try **http://127.0.0.1:5000**

Switch to another terminal window, and type **docker image ls** to list local images.

Listing images at this point should return **redis** and **web**.

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
