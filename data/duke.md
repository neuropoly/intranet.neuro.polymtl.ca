# `duke`

This server includes a variety of data: raw MRI and histology data, project data (processed and non-processed), temporary data to share with colleagues.

`{smb,afp}://duke.neuro.polymtl.ca` has a max size of ~15TB and is backed up nightly at two different locations.

The shared folders are:

* **histology** –&gt; Raw histology files
* **mri** –&gt; Raw MRI files \(restricted access\)
* **projects** –&gt; Shared project files \(subfolders containing different projects\)
* **public** –&gt; Contains useful software binaries
* **sct\_testing** –&gt; Data for testing SCT
* **temp** –&gt; Use for temporary files, to share between you. Files are deleted after 15 days.

```{note}
`duke` is not accessible when using SSH key login to linux stations.
```


## Access from stations

When [connecting with `ssh`](../../#ssh-command-line), `duke` is available at `/mnt/duke/`, e.g.:

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

```{warning}
Don't run processing scripts or `git annex` inside `duke`.
(It's fine if your input data is in `duke`, but not the script and not the output.)

This is because, inside `duke`, every file has permissions `-rw-r--r--` and every directory has permissions `drwxr-xr-x`
(even if you try to change them with `chmod`), so scripts will not be executable (including the git hooks used by git-annex).
```


## Mount with GUI

When working on campus or [over the VPN](../../#vpn), you can connect your computer to `duke`:

````{tabbed} macOS
1. Open Finder
2. CMD+K
3. <details><summary>Enter <code>afp://duke.neuro.polymtl.ca/</code></summary>

    ![Screenshot of Connect to Server dialog](./duke-macOS-01.png)
    
    </details>
4. <details><summary>Enter your <em>GRAMES</em> username and password</summary>

    ![Screenshot of password dialog](./duke-macOS-02.png)
    
    </details>
    
5. <details><summary>Pick the top-level folder to access</summary>

    ![Screenshot of volume selector dialog](./duke-macOS-03.png)
    
    </details>
    
6. <details><summary>Finder should open with the chosen folder</summary>

    ![Screenshot of Finder with mounted volume](./duke-macOS-04.png)
    
    </details>
````

````{tabbed} Linux
1. Open File Browser
2. Menu > Go > Open Network Location 
3. `smb://duke.neuro.polymtl.ca/`
````

````{tabbed} Windows 10

1. Open Windows explorer
2. Right click This PC
3. Map Network Drive
4. Address: `\\duke.neuro.polymtl.ca\<FOLDER>`
5. Check "Connect using different credentials".
6. Username: `grames\<POLYGRAMES_USERNAME>`
7. Password: `<POLYGRAMES_PASSWORD>`.
````

```{note}
Some root folders are restricted \(e.g. **mri**\), so you need to write the URL to the destination folder you have access to. Example: `duke.neuro.polymtl.ca/mri/unf`
```

```{note}
If you get the message “There are no shares available…”, then there might be a bug with the OS. Instead, try to mount on a local folder within the home directory \(to have write permission\).
```

## Mount with Terminal

You can also connect your computer from the CLI, or with a script, which might be more efficient in the long run:

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
