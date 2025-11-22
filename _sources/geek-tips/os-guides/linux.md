# Linux

## **Automatic Mount on Startup**

For the following steps you need admin permissions.

1\. Create data_processing & data_shared folders in `/mnt`, type:

```bash
sudo mkdir /mnt/data_processing
sudo mkdir /mnt/data_shared
```

2\. Edit mount table, type : `sudo nano /etc/fstab`

3\. For the following operating systems:


::::{tab-set}
:::{tab-item} Ubuntu 14.04 LTS
Add the following lines at the bottom of the file:

```bash
#data_processing @SERVER
//IP_SERVER/data_processing        /mnt/data_processing    cifs    username=XXX,password=XXX    0       0

#data_shared @SERVER
//IP_SERVER/data_shared        /mnt/data_shared    cifs    username=XXX,password=XXX    0       0
```
:::

:::{tab-item} Debian Wheezy 8
Add the following lines at the bottom of the file:

```bash
#data_processing @SERVER
//IP_SERVER/data_processing    /mnt/data_processing    cifs  nounix,sec=ntlmssp,user=XXX,password=XXX 0 0

#data_shared @SERVER
//IP_SERVER/data_shared    /mnt/data_shared    cifs  nounix,sec=ntlmssp,user=XXX,password=XXX 0 0
```
:::
::::


4\. Remount drives and type: `sudo mount -a`

## CentOS/Fedora/Red Hat

### Ants & c3d

Binaries for debian work well, just make sure the paths are set in the bashrc as follow:

```
PATH=${PATH}:${SCT_DIR}/install/debian/ants

PATH=${PATH}:${SCT_DIR}/install/debian/c3d
```

### FSL

Need `libmng` installed for fslview:

```
~ sudo yum install libmng libpng12
```

Then install FSL with the python script `fslinstaller.py` you'll find there : [http://goo.gl/Tfu1UW](http://goo.gl/Tfu1UW) Make sure the installer set your bash configuration, following lines should be in your bashrc or bash_profile. If not, add it:

```bash
FSLDIR="/usr/local/fsl"
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH
```

### Conda (Miniforge)

```{note}
Due to recent changes in the Terms of Service for the `default` channel in Anaconda, which puts our users at risk of legal action, the instructions below are for installing `miniforge`. This is a fork of `miniconda` that uses the `conda-forge` channel by default instead. It also uses `mamba` as its installer, instead of native `conda` installer; this can greatly speed up environment set-up. See [this SCT issue](https://github.com/spinalcordtoolbox/spinalcordtoolbox/issues/4670) for further details on why you should use `miniforge` instead of `miniconda` for your Python environment management needs.
```

To install `conda` (via `miniforge`) on your computer:

1. Download the `miniforge` installation script for your Linux distribution; you can find their latest release [here](https://conda-forge.org/miniforge/) (if you don't know which file to get, try the `x86_64` release first).

2. Open a new shell, and run the following command:

```bash
bash Miniforge3-*.sh
```
