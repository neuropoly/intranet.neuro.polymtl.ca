# Software Containers

```{toctree}
:hidden:
:maxdepth: 1
docker
```

## What are Software Containers?

In the context of programming, **Software Containers** are fully isolated, portable software environments which can be run as a standalone process on your machine. You can think of them as a "middle ground" between a [package manager](https://en.wikipedia.org/wiki/Package_manager) (which is not isolated from the rest of the machine) and a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) (where the operating system, and sometimes specific hardware, is emulated as well). You can read more on the difference between containers and virtual machines [here](https://www.ibm.com/think/topics/containers-vs-vms).

## Common Terms

* **Image:**  The precursor to a container; contains all data required to instantiate and run a container, as well as any software managed within them. 
* **Definition:** A file containing the instructions on how to build a container image. Can contain everything from downloading dependencies to setting up file structures to running other software!
* **Client:** A tool which manages how to build, run, and manage images and their associated containers. Usually a command-line interface, though some containerization tools provide GUI clients as well.
* **OCI:** Short for the "[Open Container Initiative](https://opencontainers.org/)", provides a standard for how images and containers should be built and run. If an image is OCI compliant, it can usually be run by any client which is also OCI compliant.

## When to Containerize:

There are a number of reason to "containerize" a piece of software:

1. **Reproducibility:** Once built, an image will always run exactly the same, as all dependencies and environmental settings are ensured to be static and insulated from change.
1. **Portability:** An image can be used to spawn associated containers on (almost) any other machine which has the same container client software, even if that machine does not/cannot install the dependencies required of the software!

A number of drawbacks exist, however:

1. **Heavyweight:** Due to their isolated design, containers won't share their dependencies with one another or try to use those already on your machine. As a result, it is not uncommon to for multiple images to have duplicates of common tools and/or software, which can add up over time.
2. **Security:** As images are immutable and isolated, but still run on your operating system, containerized software often run without the same scrutiny as an "installed" program. While tools exist to check the contents of an image/container, you should generally be wary of running any container you didn't build yourself or get from a trusted source.

## Common Containerization Tools:

Tools used in our research group are all OCI complient. They include:

* [Docker](https://www.docker.com/): Well documented and widely used. Most of NeuroPoly's computing resources support this; however, as it's client is daemon based, it is less secure and not available on many other shared resources.
* [Podman](https://podman.io/): Lightweight and open source. Follows most of the same standards as Docker, but uses a CLI-based client instead; as such, it is what we tend use at NeuroPoly for our shared computing resources.
* [Apptainer](https://apptainer.org/) (Formerly Singularity): Extremely lightweight and, due to its much more stringent definition specification than Docker/Podman, extremely secure. As a result, most high-performance compute clusters (including [Alliance Canada](https://docs.alliancecan.ca/wiki/Apptainer), formerly Compute Canada) only support this containerization tool. Only available for Linux-based operating systems!

You can view further details on each from the sidebar to the left.
