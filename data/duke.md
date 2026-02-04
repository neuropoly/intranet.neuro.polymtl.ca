# `duke`

This server includes a variety of data: raw MRI and histology data, project data (processed and non-processed), temporary data to share with colleagues.

`{smb,afp}://duke.neuro.polymtl.ca` has a max size of ~15TB and is backed up nightly at two different locations.

The shared folders are:

| Folder Name     | Description                                   |
|-----------------|-----------------------------------------------|
| `histology`       | Raw histology files                           |
| `mri`             | Raw MRI files (restricted access)             |
| `projects`        | Various active projects. In general, we only keep files that are processed in their final form, and that have been used for journal publications or for conferences. Avoid keeping large temporary that are not an absolute necessity. Also, please **do not** put any files that are versioned with git or git annex. |
| `public`          | Contains useful software binaries             |
| `temp`            | Use for temporary files, to share between you. Please clean up your files regularly. Files not used for a certain amount of time will be deleted. |
| `sct_testing`     | Data for testing SCT                          |
| `archives`        | Terminated projects are archived here (restricted access). |

```{warning}
Please do not run processing scripts or `git annex` inside `duke`.
(It is fine if your input data is in `duke`, but not the script and not the output.)

This is because, inside `duke`, every file has permissions `-rw-r--r--` and every directory has permissions `drwxr-xr-x`
(even if you try to change them with `chmod`), so scripts will not be executable (including the git hooks used by git-annex).
```

```{note}
`duke` is not accessible when using SSH key login to linux stations.
```


## Access from stations

When [connecting with `ssh`](../computing-resources/neuropoly/README.md#ssh-command-line), `duke` is available at `/mnt/duke/`, e.g.:

```
u932945@joplin:~$ ls -l /mnt/duke
total 36
drwxr-xr-x 2 u108545 domain users  4096 May 13 14:37 histology
drwxr-xr-x 2 u108545 domain users 12288 Jun  7 17:35 mri
drwxr-xr-x 2 u108545 domain users  8192 Jun  8 23:21 projects
drwxr-xr-x 2 u108545 domain users  4096 Mar 11 18:38 public
drwxr-xr-x 2 u108545 domain users  4096 Feb 18 20:45 sct_testing
drwxr-xr-x 2 u108545 domain users  4096 Jun  8 16:44 temp
```


## Mount with GUI

When working on campus or [over the VPN](../computing-resources/neuropoly/README.md#vpn), you can connect your computer to `duke`:

::::{tab-set}
:::{tab-item} macOS
1. Open Finder
2. CMD+K
3. <details><summary>Enter <code>afp://duke.neuro.polymtl.ca/</code></summary>

    ![Screenshot of Connect to Server dialog](./duke-macOS-01.png)
    
    </details>
4. <details><summary>Enter your <a href="./computing-resources/neuropoly/README.md#ge">GE</a> username and password</summary>
    
    ![Screenshot of password dialog](./duke-macOS-02.png)
    
    </details>
    
5. <details><summary>Pick the top-level folder to access</summary>

    ![Screenshot of volume selector dialog](./duke-macOS-03.png)
    
    </details>
    
6. <details><summary>Finder should open with the chosen folder</summary>

    ![Screenshot of Finder with mounted volume](./duke-macOS-04.png)
    
    </details>
:::

:::{tab-item} Linux
1. Open File Browser
2. Menu > Go > Open Network Location 
3. `smb://duke.neuro.polymtl.ca/`
:::

:::{tab-item} Windows 10
1. Open Windows explorer
2. Right click This PC
3. Map Network Drive
4. Address: `\\duke.neuro.polymtl.ca\<FOLDER>`
5. Check "Connect using different credentials".
6. Username: `GE\<GE_USERNAME>`
7. Password: `<GE_PASSWORD>`.
:::
::::

```{note}
Some root folders are restricted \(e.g. **mri**\), so you need to write the URL to the destination folder you have access to. Example: `duke.neuro.polymtl.ca/mri/unf`
```

```{note}
If you get the message “There are no shares available…”, then there might be a bug with the OS. Instead, try to mount on a local folder within the home directory \(to have write permission\).
```

## Mount with Terminal

You can also connect your computer from the CLI, or with a script, which might be more efficient in the long run:

::::{tab-set}
:::{tab-item} Mac OSX
Create folder for the mount point on a location \(your home directory\) where you have read and write access:

```bash
mkdir <FOLDER_NAME> # (e.g. <FOLDER_NAME>=sct_testing)
# To mount:
mount -t afp afp://USERNAME:PASSWORD@duke.neuro.polymtl.ca/<FOLDER_NAME> <FOLDER_NAME>
# To unmount:
sudo umount <FOLDER_NAME>/
```
:::

:::{tab-item} Linux
To mount:

```bash
sudo mount -t cifs //duke.neuro.polymtl.ca/<FOLDER_NAME> /mnt/duke/<FOLDER_NAME> -o username=<GE_USERNAME>,noexec
```
:::
::::

## Retrieve an old backup

`duke` (`/mri`, `/projects`, `/sct_testing`) is backed up on **grappelli** every evening at 21:00 EST. In order to retrieve old backup you have to contact Jean-Sébastien Décarie.
