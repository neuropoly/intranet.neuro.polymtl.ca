# Apptainer

This page serves as a crash-course for a common use case; creating a Apptainer definition, building the corresponding image, and running a containers using it. If you would like a working example, you can look at the implementation used by [Spinal Cord Toolbox](https://github.com/spinalcordtoolbox/spinalcordtoolbox/tree/master/contrib/apptainer).

If you would like further details or specifics, please refer to the [Apptainer Documentation](https://apptainer.org/docs/user/latest/).

## Creating the Definition

Unlike Docker and Podman, Apptainer's definition files are split into two parts:

### Header

This where you define the "foundation" the container should be built on top of. For those familiar with Docker/PodMan, it can be thought as an extended version of the `FROM` command.

For example, the following header will tell Apptainer to download and use a Docker image of Ubuntu 22.04, obtained from [Docker Hub](https://hub.docker.com/), as the base for images generated using the file:

```bash
# nyan.def
BootStrap: docker
From: ubuntu:22.04
...
```

The **BootStrap** value dictates how the other keys in the header will be interpreted; [`docker`](https://apptainer.org/docs/user/main/appendix.html#build-docker-module) is the most common, but other bootstraps exists. For example, you can use a previously generated image as a starting point with the [`localimage`](https://apptainer.org/docs/user/main/appendix.html#build-localimage) bootstrap:

```bash
# nyan.def
BootStrap: localimage
From: /path/to/image/file.sif
...
```

You can read more about the available bootstraps and their use [here](https://apptainer.org/docs/user/main/definition_files.html#preferred-bootstrap-agents).

## Sections

These are where you define how the image is built, and how containers generated from it should be run. The order of these sections do not matter, though generally you should place sections related to image generation (i.e. `%arguments` and `%post`) above those related to image use (i.e. `%runscript` and `%test`). 

Below is a summary of the common sections you're likely to need in most definitions; for a full list, see the [Apptainer Sections](https://apptainer.org/docs/user/main/definition_files.html#sections) documentation. 

### `%arguments`

Here you can define command line arguments which can be provided by the user when building an image. They should be in `key=value` form, with `value` being the default value for the associated variable `key`. You must _always_ provide a default value for each, which will be used if the user does not provide the argument themselves:

```yaml
# nyan.def
...
%arguments
  NYAN_URL="https://raw.githubusercontent.com/fredred375/nyancat_bash/refs/heads/main/nyancat.sh"
...
```

You can access these arguments in other sections using `{{ variable }}`, replacing `variable` with the key you specified (i.e. `echo {{ MODEL_VERSION }}`).

### `%post`

When an image is built, this script is run before the image is compiled; it is also the **_only time during image construction where you can access the internet!!!_** . As such, this is where you should download any files, install any dependencies, or run any network-dependant scripts/tests. For example:

```bash
# nyan.def
...
%post
  # Install wget
  apt-get update && apt-get install wget
  
  # Download nyancat_bash/nyancat.sh off the internet, save it to 'nyan.sh'
  wget {{ NYAN_URL }} -O nyan.sh
  
  # Mark 'nyan.sh' as a script which has execution permissions
  chmod +x nyan.sh
  
  # Link the script to a file in our local path, so we can call it later
  ln nyan.sh /usr/local/bin/nyan
...
```

### `%runscript` and `%startscript` 

Both of these sections define a script which be run when a container is created from an image. By default, they are run with `bash`/`sh` (depending on the BootStrap used); you can specify a different   

Which of `runscript` or `startscript` is run depends on how the container was created:

* When the image is called as a _script_ (i.e. `./nyan.sif`), the code within `runscript` is used
* When the image is called as an _instance_ (i.e. `apptainer instance start nyan.sif`), the code within `startscript` is used instead.

For our purposes, the former is usually preferred over the latter, as the container will self-terminate after the script is completed:

```bash
# nyan.def
...
%runscript
  # Call the nyan.sh script we downloaded and linked to in %post
  nyan
...
```

## Building an Image

Once you have a definition file, you can request an image be generated from it using `apptainer build {image_file} {definition_file}`. For example, the following command will generate an Apptainer image `nyan.sif` using the specification provided by the definition file `nyan.def`:

```bash
apptainer build nyan.sif nyan.def
```

If you use arguments, you can pass their values in using `--build-arg`; this _must_ be specified before the `{image_file}` and `{definition_file}`:

```bash
apptainer build --build-arg NYAN_URL="https://gist.githubusercontent.com/wting/5278321/raw/327abe259573a59f2e6690972878f976352cbc52/nyan.sh" nyan.sif nyan.def
```

## Running a Container

Once you have a built image, in the form of a `.sif` file, you can start creating containers using it! The "default" way to do so is to run it as a script; you can do so as if it were any other bash script:

```bash
./nyan.sif
```

... or using the `apptainer run` command:

```bash
apptainer run nyan.sif
```

If you would like to run a shell using the container's environment (allowing you to use the tools provided within itself as through they were called on your own computer), you can instead use `apptainer shell`:

```bash
apptainer shell nyan.sif
```

```bash
# Now in Apptainer environment
nyan
```

As with any shell, you can terminate the shell's connection with `CTRL + D` and terminate a running process with `CTRL + C`.  In either case, if you replicate the file above, and have nyan'd, you should see something like this appear on your terminal:

!["Pop tart cat running across the screen, from left to right, with a rainbow training behind it. Nyan Cat is 14 years old at time of writing..."](../../_media/nyan.png)
