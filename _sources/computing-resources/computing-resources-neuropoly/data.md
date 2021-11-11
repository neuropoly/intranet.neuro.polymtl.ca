---
description: This page describes the location of the MRI and histology data at NeuroPoly.
---

# Data

### Duke

This is the data server of **NeuroPoly**. It is backed up nightly at two different locations. Max size ~15TB.

The shared folders \(hosted on **Poly-Grames**\) are:

* **histology** –&gt; Raw histology files
* **mri** –&gt; Raw MRI files \(restricted access\)
* **projects** –&gt; Shared project files \(subfolders containing different projects\)
* **public** –&gt; Contains useful software binaries
* **sct\_testing** –&gt; Data for testing SCT
* **temp** –&gt; Use for temporary files, to share between you. Files are deleted after 15 days.

**NOTE: duke is not accessible when using SSH key login to linux stations.**

#### How to Mount

**Mount from Finder \(OSX only\)**

1. Open Finder
2. CMD+K
3. `afp://duke.neuro.polymtl.ca/`

Note: some root folders are restricted \(e.g. **mri**\), so you need to write the URL to the destination folder you have access to. Example: `duke.neuro.polymtl.ca/mri/unf`

If you get the message “There are no shares available…”, then there might be a bug with the OS. Instead, try to mount on a local folder within the home directory \(to have write permission\).

#### Mount from Terminal


````{tabbed} Mac OSX
Create folder for the mount point on a location \(your home directory\) where you have read and write access:

```bash
mkdir <FOLDER_NAME> # (e.g. <FOLDER_NAME>=sct_testing)
# To mount:
mount -t afp afp://USERNAME:PASSWORD@duke.neuro.polymtl.ca/<FOLDER_NAME> <FOLDER_NAME>
# To unmount:
sudo umount <FOLDER_NAME>/
```
````

````{tabbed} Linux
To mount:

```bash
sudo mount -t cifs //duke.neuro.polymtl.ca/<FOLDER_NAME> /mnt/duke/<FOLDER_NAME> -o username=<GRAMES_USERNAME>,noexec
```
````


#### Mount From Windows \(Win10\)

From Windows explorer, got to This PC - Map network drive.

Under address fill : `\\duke.neuro.polymtl.ca\xxx` and check connect using different credentials.

In the username field enter: `grames\POLYGRAMESUSERNAME` followed by your `POLYGRAMESPASSWORD`.

#### Poly-Grames home/ folder

This is your personal home folder. It is backed-up nightly.

1. Open Finder
2. CMD+K
3. for students:
   1. `smb://hvclusterfs.grames.polymtl.ca/usagers/etudiants/USERNAME`
4. for personnel:
   1. `smb://hvclusterfs.grames.polymtl.ca/usagers/personnels/USERNAME`

### BIDS git-annex server

We have an internal server that hosts BIDS datasets. To access it, visit [this page](https://github.com/neuropoly/data-management/blob/master/internal-server.md#usage). 

### Django

This is our old server. This server is only maintained for old projects. Please **DO NOT** use it if you are starting a new project.

The shared folders \(hosted on **django**\) are:

* **folder\_shared** –&gt; used to shared files, documents, etc. Permission: R+W. Backed-up nightly.
* **matlab\_shared** –&gt; Various MATLAB scripts. Permission: R. Backed-up nightly.
* **data\_processing** –&gt; Used for processing data. **Please clean your files after use!** Permission: R+W. **NOT BACKED-UP**

To access these folders, here's the procedure:

1. CMD+K
2. type: `afp://django.neuro.polymtl.ca`
3. select the mount point \(e.g., data\_shared\)
4. now if you want to make an alias on your desktop, in Finder select the mounted drive and drag/drop it on your Desktop, while pressing keys ALT+CMD

#### VirtualBox

Some VirtualBox machines are accessible under **folder\_shared/virtual\_box** \(this folder is read-only. For adding more, please contact Julien\):

* **WinXP\_IDEA** –&gt; Siemens pulse sequence program environment
* **WinXP\_Terranova** –&gt; Prospa software for Terranova MRI

