---
description: How to use CST Studio on Neuropoly servers
---

# CST Studio

SIMULIA CST is enterprise software some lab members & collaborators use for 3D EM simulation and for coil design.

## Using CST Studio

### Prerequisite

First, check that CST Studio is installed on the server you want to use:

```shell
$ which cst
/usr/local/bin/cst
```

If the output looks like above, you're good to go!

CST Studio 2025 is currently installed on

- tassan

### Running

CST Studio runs in a [Podman](https://podman.io) container under a special user. You can access a shell inside this container using the script `cst`:

```shell
p122326@ge.polymtl.ca@tassan:~$ cst
[cst@tassan CST_Studio_Suite_2025]$
```

Once in the container, you can run CST commands:

```shell
[cst@tassan CST_Studio_Suite_2025]$ ./cst_design_environment
```

### Accessing files from CST container

You can make files available to the podman container by placing them in `/home/cst/files`. The files will then be available inside the container at the path `/files`:
```shell
[cst@tassan CST_Studio_Suite_2025]$ ./cst_design_environment --r --m --hide /files/test_one_port.cst
```

**Note:** since all NeuroPoly members can run commands inside the CST container, it is theoretically possible for any NeuroPoly user to access data in `/files`. If this is unacceptable for PII reasons, please contact an admin or open an issue in the [computers](https://github.com/neuropoly/computers/issues) repo.

#### Space usage

CST Studio files can be very large. Please clean up files once you're done using them.

### Hardware acceleration

CST Studio doesn't [currently support](https://updates.cst.com/downloads/GPU_Computing_Guide.pdf) the NVIDIA Blackwell architecture on tassan. However, you can bypass the standard compatibility checks using the `CST_HWACC_ALLOW_UNVERIFIED_HARDWARE` flag:

```shell
p122326@ge.polymtl.ca@tassan:~$ cst
[cst@tassan CST_Studio_Suite_2025]$ CST_HWACC_ALLOW_UNVERIFIED_HARDWARE=1 ./cst_design_environment
```

To set the flag for the entire session:

```shell
p122326@ge.polymtl.ca@tassan:~$ cst
[cst@tassan CST_Studio_Suite_2025]$ export CST_HWACC_ALLOW_UNVERIFIED_HARDWARE=1
[cst@tassan CST_Studio_Suite_2025]$ ./cst_design_environment --r --m --hide --withgpu=1 /files/test_one_port.cst
```
