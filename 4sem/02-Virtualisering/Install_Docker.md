# Install Docker



## Install Docker Engine
Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:

    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io

To install a specific version of Docker Engine, list the available versions in the repo, then select and install:

a. List the versions available in your repo:

    apt-cache madison docker-ce

Install a specific version using the version string from the second column, for example, 5:18.09.1~3-0~ubuntu-xenial

    sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io

Verify that Docker Engine is installed correctly by running the hello-world image.

    sudo docker run hello-world

*This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.*

Docker Engine is installed and running. The docker group is created but no users are added to it. You need to use sudo to run Docker commands.

