# Docker

```{toctree}
:hidden:
docker-for-deep-learning
```

## Docker Terminology

**Images** - The blueprints of our application which form the basis of containers.

**Containers** - Created from Docker images and run the actual application. A list of running containers can be seen using the docker ps command. **Docker Daemon** - The background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system to which clients talk to.

**Docker Client** - The command line tool that allows the user to interact with the daemon.

**Docker Hub** - A registry of Docker images. You can think of the registry as a directory of all available Docker images. If required, one can host their own Docker registries and can use them for pulling images.

## Using Docker

### Search for remote image

```text
docker search ubuntu  # will search for ubuntu distrib
```

[List of Ubuntu images](https://hub.docker.com/_/ubuntu)

### Install & Run Linux distribution <a id="install_run_linux_distribution"></a>

```text
docker pull debian  # will install debian
docker pull ubuntu:16.04
docker pull centos
```

### List local Docker images <a id="list_local_docker_images"></a>

```text
docker images
```

### Run Docker image <a id="run_docker_image"></a>

To run in interactive mode, use flag `-i`

```bash
docker run -it IMAGE /bin/bash
docker run -it ubuntu:trusty /bin/bash
docker run -it ubuntu:16.04
```

### Remove Docker image or containers \(force deletion\) <a id="remove_docker_image_or_containers_force_deletion"></a>

```text
docker rmi -f IMAGE_ID
docker rmi $(docker images -a -q)  # WARNING!!! This will remove all images
docker rm $(docker ps -a -f status=exited -q)  # WARNING!!! This will remove all containers
```

### Save a Docker image <a id="save_a_docker_image"></a>

The example below shows how to install useful items on a standard ubuntu image, and then save the image locally.

```text
# launch docker
docker pull ubuntu:16.04
docker run ubuntu:16.04
# inside image
apt-get update
yes | apt install git curl bzip2
# open another Terminal
# list current docker images
docker ps -a
# save container as new image
docker commit <container_id> your_name/ubuntu:16.04
```

### Build Docker container from Dockerfile <a id="build_docker_container_from_dockerfile"></a>

1. Create a Dockerfile by running \`touch Dockerfile\`
2. Inside the Dockerfile write the following \(items below are just given as an example\):

```yaml
FROM centos:latest
```

```text
RUN yum -y update \
&& yum -y install git bzip2 gcc wget which mesa-libGL unzip \
&& yum clean all 
```

```text
# Fetch SCT from source and install (at root directory)
RUN git clone https://github.com/neuropoly/spinalcordtoolbox.git sct; \
  cd sct; \
  yes | ./install_sct
```

```text
# Add SCT executable to the system env 
ENV PATH "/sct/bin:${PATH}"
```

1. Build docker image: \`docker build -t &lt;container\_id&gt; .\`
2. Run it: \`docker run -it &lt;container\_id&gt;\`

### Run with DISPLAY redirection <a id="run_with_display_redirection"></a>

In order to run scripts with GUI you need to allow X11 redirection:

1. Install XQuartz X11 server and run it.
2. In preferences, check ‘Allow connections from network clientsoption inXQuartz\` settings.
3. Quit and restart XQuartz.
4. In XQuartz window xhost + 127.0.0.1
5. In your other Terminal window, run:
   1. On OSX: \`docker run -e DISPLAY=host.docker.internal:0 -it &lt;CONTAINER\_ID&gt;\`
   2. On Linux: \`docker run -ti –rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix &lt;CONTAINER\_ID&gt;\`

### Copy file into container <a id="copy_file_into_container"></a>

```bash
# list container
docker ps
# copy file
docker cp <file> <CONTAINER ID>:<PATH_DEST>/<file>
```

Examples of Docker builder:

1. [https://github.com/neuropoly/docker](https://github.com/neuropoly/docker)

