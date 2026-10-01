# FSLeyes

## Introduction

[FSLeyes](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLeyes), which is part of the [FMRIB Software Library \(FSL\)](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/), is an image viewer for 3D and 4D neuroimages. It is a commonly used package in the field of neuroimaging, and our lab has several plugins that integrate with FSLeyes.

## Installation <a id="install_fsleyes"></a>

The FSLeyes documentation provides two different install options:

1. [Install as part of FSL](https://open.win.ox.ac.uk/pages/fsl/fsleyes/fsleyes/userdoc/install.html#install-as-part-of-fsl-recommended)
2. [Install through conda-forge](https://open.win.ox.ac.uk/pages/fsl/fsleyes/fsleyes/userdoc/install.html#install-from-conda-forge-recommended)

Requirements when running from OSX: XQuartz

Install FSLeyes from `conda-forge` \(this has to be done in a virtual environment\) on the remote host \(rosenberg or joplin\):

```bash
conda create --name <YOUR_ENV>
conda activate <YOUR_ENV>
conda install -c conda-forge fsleyes
```

## Running Remotely

To run FSLeyes remotely, please see the documentation [here](https://open.win.ox.ac.uk/pages/fsl/fsleyes/fsleyes/userdoc/troubleshooting.html#running-fsleyes-remotely).

After installing, do an ssh for X forwarding:

```bash
ssh -X username@remotehost
conda activate <YOUR_ENV>
fsleyes
```

If you have an XQuartz error follow the instructions [here](https://open.win.ox.ac.uk/pages/fsl/fsleyes/fsleyes/userdoc/troubleshooting.html#xquartz-fsleyes-doesn-t-start-and-just-shows-an-error).

## Plugins

We have several different projects with FSLeyes-integrated plugins:

* [Plugin for Spinal Cord Toolbox \(SCT\)](https://spinalcordtoolbox.com/en/latest/user_section/fsleyes.html)
* [Plugin for Shimming Toolbox](https://github.com/shimming-toolbox/fsleyes-plugin-shimming-toolbox)
* [Plugin for AxonDeepSeg \(ADS\)](https://axondeepseg.readthedocs.io/en/latest/documentation.html#graphical-user-interface-gui-optional)

