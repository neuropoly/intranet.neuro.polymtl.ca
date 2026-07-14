# CUDA

## Installation

### Linux

#### CUDA 7.5

1\. Download your relevant CUDA.run file, e.g. `cuda_7.0.28_linux.run`. Note, that once again this install is if you purely want to use your graphics card (Titan X) for GPU/CUDA purposes and not for rendering.

2\. Run:

```bash
sudo apt-get install build-essential
```

3\. No need to create an `xorg.conf` file. If you have one, remove it (assuming you have a fresh OS install): 

```bash
sudo rm /etc/X11/xorg.conf
```

4\. Create the `/etc/modprobe.d/blacklist-nouveau.conf` file with : blacklist nouveau option nouveau modeset=0

Then:

```bash
sudo update-initramfs -u
```

5\. Reboot computer. Nothing should have changed in loading up menu. You should be taken to the login screen. Once there type: `Ctrl + Alt + F1`, and login to your user. 

6\. Go to the directory where you have the CUDA driver, and run:

```
chmod a+x .
```

7\. Now, run $ sudo service lightdm stop The top line is a necessary step for installing the driver. 

8\. Run the CUDA driver run file. \*Notice that I explicitly don't want the OpenGL flags to be installed:

```bash
sudo bash cuda-7.0.28_linux.run –no-opengl-libs
```

9\. During the install:

Accept EULA conditions\
Say YES to installing the NVIDIA driver\
SAY YES to installing CUDA Toolkit + Driver\
Say YES to installing CUDA Samples\
Say NO rebuilding any Xserver configurations with Nvidia.

10\. Installation should be complete. Now to check if device nodes are present, check if `/dev/nvidia*` files exist. If they don't exist:

```bash
sudo modprobe nvidia
```

11\. Set Environment path variables:

```bash
export PATH=/usr/local/cuda-7.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-7.0/lib64:$LD_LIBRARY_PATH
```

\*Change depending on your cuda version.

12\. Verify the driver version: 

```bash
cat /proc/driver/nvidia/version
```

13\. Check CUDA driver version:

```bash
nvcc -V
```

\[Optional] At this point you can switch the `lightdm` back on again by doing: 

```bash
sudo service lightdm start
```

You should be able to login to your session through the GUI without any problems or login-loops.

14\. Create CUDA Samples. Go to your `NVIDIA_CUDA-7.5_Samples` folder and type `make`.

15\. Go to `NVIDIA_CUDA-7.5_Samples/bin/x86_64/linux/release/` for the demos, and do the two standard checks: `./deviceQuery` to see your graphics card specs and `./bandwidthTest` to check if it is operating correctly.

Both tests should output a 'PASS' in your terminal.

16\) Reboot.

## Reference

[https://devtalk.nvidia.com/default/topic/878117/-solved-titan-x-for-cuda-7-5-login-loop-error-ubuntu-14-04-/](https://devtalk.nvidia.com/default/topic/878117/-solved-titan-x-for-cuda-7-5-login-loop-error-ubuntu-14-04-/)​
