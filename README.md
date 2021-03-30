
# An attempt at a scalable and reliable Node API
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Node.js_logo.svg/1280px-Node.js_logo.svg.png" height="100px" />
<img src="https://jolicode.com/media/original/2013/10/homepage-docker-logo.png" height="100px" />
<img src="https://miro.medium.com/max/400/0*KzqL3xqmXzV5PPjX.png" height="100px" />
</p>

### INTRODUCTION

Following an introduction to **distributed systems**, I had to try to build a system using the above tools. I ended up putting together a dummy **Node** API, and **dockerized** it in order to deploy it through **Minikube** (a lightweight kubernetes).

### RUN IN NODE

> for this, make sure you have **Node** installed on your device

To run this app as a bare node server, just follow these steps.
- Clone this repository with `git clone https://github.com/Faber-smythe/k8s-docker-node`
- Install the dependencies with `npm install`
- Run the server with `node server`

You should see a log showing the local port where the API is running.
For more information, see the **[Node.js documentation](https://nodejs.org/en/docs/)**

### RUN IN DOCKER

> for this, make sure you have **Docker** installed on your device

To run this app in a Docker container, you have two choices. Either :
- Build your own Docker image
- Pull the existing image from my DockerHub repository

1. Build your image
    - Follow the steps from the <i>RUN AS NODE</i> section in order to clone the node project
    - Edit the project as you wish. For example change the API's endpoints, or the port on which it will run. If you know what you're doing, you can also modify the Dockerfile.
    - Run `docker build -t [my_custom_image] .` at the root of the node project. You should see the new image among the list given by `docker images`.
    - Run `docker run -dp 8080:8080 [my_custom_image]` to start the container. `d` flag is to detach the container from the terminal, so that it will run in the background. `p` flag allows to map the 8080 port from the container (or whatever port you picked in case you modified `server.js` file) to your machine's 8080 port.
2.  Pull the existing image as is
    - Run `docker pull fabersmythe/k8s-docker-node` to clone the image
    - Run `docker run -dp 8080:8080 [my_custom_image]` to start the container. `d` flag is to detach the container from the terminal, so that it will run in the background. `p` flag allows to map the 8080 port from the container to your machine's 8080 port. 

Your container should be running. You can check if he is with `docker ps`. 
For more information, see the **[Docker documentation](https://docs.docker.com/)**

### RUN IN MINIKUBE
> for this, make sure you have **Minikube**  AND **kubectl** installed on your device

To deploy this app through Minikube, you will first need to get the Docker image. The easiest way is described in the "**2. Pull the existing image as is**" part from the previous section. Use `docker images` to make sure the image you need is in the list. Then, follow these steps :
- Run Minikube with `minikube start`
- Deploy the app with `kubectl create deployment [my_app] --image=fabersmythe/test`
- Expose the running app to browser requests with `kubectl expose deployment faberapp --type=NodePort --port=8080`
- In order to know where to access you app within the distributed system, use `minikube service [my_app] --url`

You should see a log with the url you need. Just enter it in your favourite browser and **TADAM**, here is the API !

For more information, see the **[Minikube documentation](https://kubernetes.io/fr/docs/setup/learning-environment/minikube/)**


<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/Logo-pole-leonard-vinci-n.png" height="100px" />
<img src="https://s3-eu-west-1.amazonaws.com/assets.atout-on-line.com/images/commerce/Logos_Ecoles/2018_2020/iim_250.jpg" height="100px" />
<img src="https://media-exp1.licdn.com/dms/image/C560BAQEyc5wzxsB0cw/company-logo_200_200/0/1570453944259?e=2159024400&v=beta&t=x8rq23AoxqG6nrJRTOLEliIlcptOBGDT4M_5XCL8SC8" height="100px" />
</p>
