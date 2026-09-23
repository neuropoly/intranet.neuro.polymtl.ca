# `django`

```{important}
This server is only maintained for old projects. Please **DO NOT** use it if you are starting a new project.
```

Full address: `{smb,afp}://django.neuro.polymtl.ca`. 

The shared folders \(hosted on **django**\) are:

* **folder\_shared** –&gt; used to shared files, documents, etc. Permission: R+W. Backed-up nightly.
* **matlab\_shared** –&gt; Various MATLAB scripts. Permission: R. Backed-up nightly.
* **data\_processing** –&gt; Used for processing data. **Please clean your files after use!** Permission: R+W. **NOT BACKED-UP**

To access these folders, here's the procedure:

1. CMD+K
2. type: `afp://django.neuro.polymtl.ca`
3. select the mount point \(e.g., data\_shared\)
4. now if you want to make an alias on your desktop, in Finder select the mounted drive and drag/drop it on your Desktop, while pressing keys ALT+CMD

## VirtualBox

Some VirtualBox machines are accessible under **folder\_shared/virtual\_box** \(this folder is read-only. For adding more, please contact Julien\):

* **WinXP\_IDEA** –&gt; Siemens pulse sequence program environment
* **WinXP\_Terranova** –&gt; Prospa software for Terranova MRI
