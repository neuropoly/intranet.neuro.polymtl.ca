# Data Servers

## `data`

`git+ssh://data.neuro.polymtl.ca` has a max size of ~1TB and is [currently not backed up](https://github.com/neuropoly/computers/issues/65).

It supports versioning datasets using [`git-annex`](git-annex.branchable.com/). [Usage instructions](./git-datasets.md).

## `duke`

`{smb,afp}://duke.neuro.polymtl.ca` has a max size of ~15TB and is backed up nightly at two different locations.

The shared folders \(hosted on **Poly-Grames**\) are:

* **histology** –&gt; Raw histology files
* **mri** –&gt; Raw MRI files \(restricted access\)
* **projects** –&gt; Shared project files \(subfolders containing different projects\)
* **public** –&gt; Contains useful software binaries
* **sct\_testing** –&gt; Data for testing SCT
* **temp** –&gt; Use for temporary files, to share between you. Files are deleted after 15 days.



#### How to Mount

`duke` is available over both `smb://` and `afp://`.

{% tabs %}
{% tab title="macOS" %}
1. Open Finder
2. CMD+K
3. `afp://duke.neuro.polymtl.ca/`
{% endtab %}

{% tab title="Linux" %}
1. Open File Browser
2. Menu > Go > Open Network Location 
3. `smb://duke.neuro.polymtl.ca/`
{% endtab %}


{% tab title="Windows 10" %}

1. Open Windows explorer
2. Right click This PC
3. Map Network Drive
4. Address: `\\duke.neuro.polymtl.ca\<FOLDER>`
5. Check "Connect using different credentials".
6. Username: `grames\<POLYGRAMES_USERNAME>`
7. Password: `<POLYGRAMES_PASSWORD>`.

{% endtab %}
{% endtabs %}

Note: some root folders are restricted \(e.g. **mri**\), so that you need to fill in a subfolder you have been granted access to. Example: `duke.neuro.polymtl.ca/mri/unf`

#### Mount from Terminal

{% tabs %}
{% tab title="macOS" %}
Create folder for the mount point on a location \(your home directory\) where you have read and write access:

```bash
mkdir <FOLDER_NAME> # (e.g. <FOLDER_NAME>=sct_testing)
# To mount:
mount -t afp afp://USERNAME:PASSWORD@duke.neuro.polymtl.ca/<FOLDER_NAME> <FOLDER_NAME>
# To unmount:
sudo umount <FOLDER_NAME>/
```
{% endtab %}

{% tab title="Linux" %}
To mount:

```bash
sudo mount -t cifs //duke.neuro.polymtl.ca/<FOLDER_NAME> /mnt/duke/<FOLDER_NAME> -o username=<GRAMES_USERNAME>,noexec
```
{% endtab %}
{% endtabs %}


### Access from stations

When [connecting with `ssh`](TODO), `duke` is available at `~/duke/`:

```
u932945@joplin:~$ ls -l ~/duke
total 36
drwxr-xr-x 2 u108545 domain users  4096 May 13 14:37 histology
drwxr-xr-x 2 u108545 domain users 12288 Jun  7 17:35 mri
drwxr-xr-x 2 u108545 domain users  8192 Jun  8 23:21 projects
drwxr-xr-x 2 u108545 domain users  4096 Mar 11 18:38 public
drwxr-xr-x 2 u108545 domain users  4096 Feb 18 20:45 sct_testing
drwxr-xr-x 2 u108545 domain users  4096 Jun  8 16:44 temp
```

**NOTE: `duke` is [not accessible when using SSH key](https://github.com/neuropoly/computers/issues/90) login. You must log in with your polygrames password.**


### django

`afp://django.neuro.polymtl.ca` is our oldest server. This server is only maintained for old projects. Please **DO NOT** use it if you are starting a new project.

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


### Poly-Grames home folder

This is your personal home folder, managed by [polygrames](https://www.grames.polymtl.ca/facilities/servers-information/). It is backed-up nightly.

1. Open Finder
2. CMD+K
3. for students:
   1. `smb://hvclusterfs.grames.polymtl.ca/usagers/etudiants/USERNAME`
4. for personnel:
   1. `smb://hvclusterfs.grames.polymtl.ca/usagers/personnels/USERNAME`
