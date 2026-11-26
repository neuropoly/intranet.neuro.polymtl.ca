# Docker for Deep Learning

## Docker Environment <a id="docker_environment"></a>

In this page you'll find information on how to use Docker for Deep Learning. You're of course not required to use Docker, however if you want a different CUDA version or any admin privileges \(root account\) you'll see that Docker will be the best choice.

## NVIDIA Docker

![](../../../.gitbook/assets/docker_arch.png)

Docker alone has no support for NVIDIA GPUs, therefore we use t he [NVIDIA Docker](https://github.com/NVIDIA/nvidia-docker) in order to have access to the host GPUs from the Docker containers.

[![](https://www.neuro.polymtl.ca/_media/internal_resources/deep_learning/docker_arch.png)](https://www.neuro.polymtl.ca/_detail/internal_resources/deep_learning/docker_arch.png?id=internal_resources%3Adeep_learning%3Adocker)As you can see in the image on the left, we have the GPUs and the NVIDIA CUDA Drivers on **the host** \(Ubuntu in our case\), and then you can have different **containers with different CUDA Toolkit versions installed and isolated from the host environment**.

In these containers you have **administrative privileges \(root account\)** where you can do whatever you want and still be able to **access the GPU** from all Deep Learning frameworks.

NVIDIA also provides many images, so you don't even need to install CUDA toolkit or cuDNN by yourself, the list can be [seen here](https://hub.docker.com/r/nvidia/cuda/). You can use Ubuntu 14.04 or Ubuntu 16.04 with CUDA 6.5/7.0/7.5 or 8.0 together with different cuDNN versions.

## Creating Containers

If you want to create containers, you just need to use the `docker run` command. Here is an example on how to start a container with CUDA 8.0 and cuDNN 5:

`nvidia-docker run -it nvidia/cuda:8.0-cudnn5-devel`

After executing this, Docker will download all required images from Docker Hub \(this is done only once, later it is used as a cache\) and it will start the container with the Ubuntu 16.04 with CUDA 8.0 and cuDNN 5 preconfigured.

Please note that after you exit the container, it will stop the container. So if you want to leave a container running you should run it in **detached mode** passing the flag `-d`.

More NVIDIA Images are [available here](https://hub.docker.com/r/nvidia/cuda/).

## Exposing Container Ports

If you want to expose a container port to the host system, you can use the flag `-p`, like in the example below where we use a Tensorflow image with Jupyter:

`nvidia-docker run -it -p 8888:8888 gcr.io/tensorflow/tensorflow:latest-gpu`

The `-p` flag tells two ports, one is from the container and the other is the port that will be opened in the host that will forward to the container. After executing the command above, you'll be able to open a Jupyter notebook from your browser by accessing [`http://localhost:8888`](http://localhost:8888/).

## Accessing Datasets \(external volumes\)

You can mount a host directory inside your Docker container using the following volume parameter:

`docker run -i -t -v [host full path]:[container path] [image] [command]`

Using the `-v` option, allow you to mount the host `[host full path]` directory inside the `[container path]` path of the container.

