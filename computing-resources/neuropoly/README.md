# `🖥` Computers \@NeuroPoly

```{toctree}
:hidden:
cpus
gpus
```

## Poly-Grames

### Poly-Grames Network Account

A **Poly-Grames** network account is required to have access to various computation resources available in the laboratory.

In order to request a **Poly-Grames** network account you need to have your Polytechnique ID number, which you get during your [onboarding](https://github.com/neuropoly/onboarding/issues).


```{note}
If you want to find out who is behind u/pXXXXXX Grames account, type this:
~~~
getent passwd <GRAMES_ACCOUNT>
~~~
```


### Home folder

Every GRAMES account has a school-wide personal home folder. It is backed-up nightly.

````{tabbed} macOS
1. Open Finder
2. CMD+K
3. for students:
   1. `smb://hvclusterfs.grames.polymtl.ca/usagers/etudiants/USERNAME`
4. for personnel:
   1. `smb://hvclusterfs.grames.polymtl.ca/usagers/personnels/USERNAME`
````

### Poly-Grames Groups

The list permissions for shared folders on `duke` are available [here](https://docs.google.com/document/d/1ZJUUBpiZPl0wxFsUPxkkR6vXZgfSAd3YBK5vlIpf_aA/edit).

### Connect to Poly-Grames Server

Use Microsoft Remote Desktop Connection on creer51, creer52, creer53.

Computer : creer51.grames.polymtl.ca

Username: grames\your_polygrames_username

Password: your_polygrames_password

## List of Computers at NeuroPoly

Are you new to NeuroPoly and looking for a desk and a station? Please check the [list of Desktop/Server/Clusters computers and Printers](https://docs.google.com/document/d/11GEh5YvYRnWnERv26TezcyvyPF2W5KF0uoI2U6p7XsM/edit) so you can pick one that is free. If you'd like a particular desk and someone else is using a station remotely, please ask the admins to move the station to another location.

If you prefer to work on your laptop, please let the admins know and we will give you a screen you can connect your laptop to.

## VPN

When working remotely from off-campus you need to use the [VPN](http://www.polymtl.ca/si/reseaux/acces-securise-rvp-ou-vpn).

To connect to the VPN, you need to have an account with École Polytechnique, specifically with [CAS](https://cas5.polymtl.ca/cas/login). Students should already have this. Consultants and Research Associates will need to have an account created for them. This should have happened during your onboarding.

You can change your password at [Gestion des Codes](https://codes.si.polymtl.ca/gestion/). Also, you can double-check you have VPN access by looking for `VPN_* = Actif` here.

The VPN is a Cisco AnyConnect server. For Linux and macOS you can reach it by first installing a VPN client such as `openconnect` (recommended) or `Cisco AnyConnect Secure Mobility Client` (if `openconnect` is not available for your OS/distro):


````{tabbed} MacOS
```
brew install openconnect
```

Open your Keychain program and click '+' to add a new password:
- Name: `poly-vpn`
- Account: your `YOUR_CAS_USERNAME` (corresponds to your GRAMES username)
- Password: enter your password here.

Then, create the following script:
```bash
#!/bin/bash
# vpn.sh

set -eo pipefail

USER="<YOUR_CAS_USERNAME>"
PASS="$(security find-generic-password -a "${USER}" -s poly-vpn -w)"
GROUP=PolySSL # or PolyInvites, depending on your account's status
echo -n "$PASS" | sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin --reconnect-timeout 20 --servercert pin-sha256:xpOY2XHGB/dcVtLnGyaZnJfrUsqUbb2e1hhPNzIkmY0= ssl.vpn.polymtl.ca
```

To connect to the VPN, you need to run:
```
./vpn.sh
```

````

````{tabbed} Linux
```
apt install openconnect
```

Then, create the following script:
```bash
#!/bin/bash
# vpn.sh

set -eo pipefail

USER="<YOUR_CAS_USERNAME>"
PASS="<YOUR_CAS_PASSWORD>"
GROUP=PolySSL # or PolyInvites, depending on your account's status
echo -n "$PASS" | sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin ssl.vpn.polymtl.ca
```

To connect to the VPN, you need to run:
```
./vpn.sh
```

````


````{tabbed} Windows

Please follow the official steps from PolyMTL ([French](https://share.polymtl.ca/alfresco/service/api/path/content;cm:content/workspace/SpacesStore/Company%20Home/Sites/rentree/documentLibrary/Aide-m%C3%A9moire%20tutoriels%20A2020/Aide-Memoire_VPN.pdf?a=true&guest=true) or [English](https://share.polymtl.ca/alfresco/service/api/path/content;cm:content/workspace/SpacesStore/Company%20Home/Sites/rentree/documentLibrary/Aide-m%C3%A9moire%20tutoriels%20A2020/Checklist_VPN.pdf?a=true&guest=true).

In case the above links ever break, the steps are:

1. Install "Cisco AnyConnect Secure Mobility Client".
    - NB: This software is licensed to organizations, so the download page will typically be behind some sort of authentication. Right now, you have to download it from the "Utilisation du Service" section of [this page](https://www.polymtl.ca/si/acces-securise-rvp-ou-vpn), which requries you to sign in with your CAS account.
2. Run the newly-installed Cisco AnyConnect Secure Mobility Client program.
3. Configure the VPN:
   * Enter the server address: ssl.vpn.polymtl.ca
   * In the “Group” drop-down list, choose the profile: PolySSL
   * Identify yourself with the username and password of your CAS account (e.g. p123123)
4. Click "Accept". You're connected! :)

````


## Connect to NeuroPoly Computers

### Locally

To log into a local station at NeuroPoly use your GRAMES account.

### SSH (command line)

Once the VPN connection established, connect via ssh using the `STATION` you want:

```bash
 ssh <POLYGRAMES_USERNAME>@<STATION>.neuro.polymtl.ca
```

Note: For Windows systems, you can[ install Microsoft's ssh package](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse), [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10), [PuTTY](https://www.chiark.greenend.org.uk/\~sgtatham/putty/), or [cmder](https://cmder.net).

Optionally, this shortcut. It allows you to just type `ssh <STATION>` and be connected:

```bash
cat >~/.ssh/config_neuropoly <<EOF
# GPU servers
Match Host romane,rosenberg,bireli
HostName %h.neuro.polymtl.ca

# CPU servers
Match Host joplin,abbey,tristano
HostName %h.neuro.polymtl.ca

# Workstations
Match Host ferguson,davis
HostName %h.neuro.polymtl.ca

# data servers
Match Host data
HostName %h.neuro.polymtl.ca

Match Host data.neuro.polymtl.ca
User git
PreferredAuthentications publickey

Match host *.neuro.polymtl.ca
User <POLYGRAMES USERNAME> # fill in your username and remove this comment
# passwords are required to access /mnt/duke: https://github.com/neuropoly/computers/issues/90:
PreferredAuthentications password
EOF

echo 'Include ~/.ssh/config_neuropoly' >> ~/.ssh/config
```

Add this to your `~/.ssh/config` to make multiple ssh connections faster and without retyping your password:

```
Host *
ControlMaster auto
ControlPath ~/.ssh/%r@%h:%p
ControlPersist 3s
```


### SFTP (Mount a remote station)

`ssh` also allows accessing remote files, via [`sftp`](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol).

The best way to do this is `sshfs`, which makes them appear as if they were a drive on your computer:

Install sshfs, if not yet installed:

````{tabbed} Linux
```
sudo apt install -y sshfs
```
````

````{tabbed} mac
```
brew install --cask osxfuse
brew install sshfs
```
````

Then mount the folder

```
mkdir cluster_folder
sshfs <STATION>: cluster_folder
```

If you use `~` or nothing (as shown) after the `:`, the connection will be relative to to your _remote_ home directory, e.g.

```
sshfs <STATION>:~/project1/ cluster_folder
```

will attach the remote `/home/GRAMES.POLYMTL.CA/$USER/project1/` to the local `./cluster_folder`, and

```
sshfs <STATION>:project1/ cluster_folder
```

will do the exact same.

However if you use `/` after the `:`, the mount will be relative to the _remote root directory_, e.g.

```
sshfs <STATION>:/tmp/ cluster_folder
```

will attach the remote `/tmp/` to the local `./cluster_folder`


```{note}
If you are experiencing mounting issues on macOs, [this](https://github.com/neuropoly/intranet.neuro.polymtl.ca/issues/57) might help.
```


### VNC (graphical interface)


````{tabbed} macOS
1. Open Finder
2. Click Cmd+K
3. In the “Server Address”, type (using the `STATION` you want): `vnc://STATION.neuro.polymtl.ca`
4. You can use your local/network account information or the [shared account credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.ckseg5ldklsg)
````

````{tabbed} PC/Linux
1. Establish a VNC connection using [vinaigre](https://wiki.gnome.org/Apps/Vinagre/).
2. In the “Server Address”, type (using the `STATION` you want): `vnc://STATION.neuro.polymtl.ca`
3. You can use the password from [shared account credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.ckseg5ldklsg)
````


#### Linux stations

On Linux targets, a VNC server needs to be started manually before the above instructions will work.

1. Create configuration file under `~/.vnc/xstartup` with the following contents:

```bash
 #!/bin/sh
 # Uncomment the following two lines for normal desktop:
 unset SESSION_MANAGER
 unset DBUS_SESSION_BUS_ADDRESS
 startxfce4 &
 [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
 [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
 xsetroot -solid grey
 vncconfig -iconic &
```

1. Give the right permissions to the file `~/.vnc/xstartup`

```bash
 chmod +x ~/.vnc/xstartup
```

1. Start VNC server

```bash
 vncserver -geometry 1600x1200 :<PORT_NUMBER>
```

**Note:** To list all running vncservers, use: ps -ef | grep vnc\`

After starting the vncserver, connect to it as above.

```{note}
**Note:**

* On the first start of the vncserver, you will have to set a personal password for your vnc session  
* The resolution can be defined by changing the value of the `-geometry` flag.
```

1. Stop VNC server - mandatory at the end of your session

```bash
 vncserver -kill :<PORT_NUMBER>
```


## CPU/GPU Clusters

The following CPU and GPU clusters are available for internal use at **NeuroPoly**.

```{warning}
**IMPORTANT:** Indicate in the calendar below if you plan to launch intensive calculations on a computer (even if it is on your station, in case you leave for holidays but are still using your station). If you don't have writing permission on this calendar please post a request on Slack #computer.
```

[https://calendar.google.com/calendar/u/0/embed?src=4mg6bgd9pv55thf9486t2miht8@group.calendar.google.com](https://calendar.google.com/calendar/u/0/embed?src=4mg6bgd9pv55thf9486t2miht8@group.calendar.google.com)

### rosenberg

| Spec         | Description                  |
| ------------ | ---------------------------- |
| **Model**    | 8 x P100 GPU                 |
| **OS**       | Ubuntu 18.04.2               |
| **Hostname** | `rosenberg.neuro.polymtl.ca` |
| **VNC**      |                              |

* By default, the root (OS and home folder) mount point is on the NVME disk
* Shared **scratch** located under **/scratch**. Please clean the unnecessary data after you finish the processing.
* [How to use GPU Clusters at NeuroPoly](https://intranet.neuro.polymtl.ca/computing-resources/neuropoly/gpus.html)
  * [Video tutorial to get started](https://drive.google.com/file/d/17-eLVBiMNA8bNbfzpD6NLxHApZRDoy1B/view?usp=sharing)

_For system administrators_: Please log all the changes on the station by updating the ansible scripts from [https://github.com/neuropoly/computers](https://github.com/neuropoly/computers).

### bireli

| Spec         | Description                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model**    | 2 x Tesla GPU                                                                                                                                                             |
| **OS**       | Ubuntu 16.04                                                                                                                                                              |
| **Hostname** | `bireli.neuro.polymtl.ca`                                                                                                                                                 |
| **VNC**      | [NeuroPoly Internal Document: Bireli TeamViewer Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.zc65h9q5641z) |

* Add event to the computer calendar
* Use your **Poly-Grames** account to connect on the machine
* [How to use GPU Clusters at NeuroPoly](https://intranet.neuro.polymtl.ca/computing-resources/computing-resources-neuropoly/gpus)

### joplin

| Spec         | Description    |
| ------------ | -------------- |
| **Model**    | 64-core CPU    |
| **OS**       | Ubuntu 20.04.4 |
| **Hostname** |                |
| **VNC**      |                |

The server is bound to the GRAMES domain.

Connect to the server via ssh using the **Poly-Grames** account.

To access the sct_testing_management development webpage use the username: sct_test_user; passwd: management.

For fast I/O, use the NVMe hard drive, which is automatically mounted on your home at: `~/data_nvme_XXX` (XXX being your GRAMES matricule)

### abbey

| Spec            | Description                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Model**       | Xeon 12-core                                                                                                                                                             |
| **OS**          | Ubuntu 20.04.3                                                                                                                                                           |
| **Hostname**    |                                                                                                                                                                          |
| **Credentials** | [NeuroPoly Internal Document: Abbey Teamviewer Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.mtnjvepco2an) |

### fitzgerald

| Spec            | Description                                                                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model**       |                                                                                                                                                                               |
| **OS**          | Windows 7                                                                                                                                                                     |
| **Hostname**    |                                                                                                                                                                               |
| **Credentials** | [NeuroPoly Internal Document: Fitzgerald TeamViewer Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.9kegj6dmbnac) |

### tristano

| Spec            | Description                                                                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model**       | Mac Mini                                                                                                                                                             |
| **OS**          | Ubuntu 16.04                                                                                                                                                         |
| **Hostname**    |                                                                                                                                                                      |
| **Credentials** | [NeuroPoly Internal Document: Tristano VNC Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.wa49ms1v7x01) |

For SCT database interface use: [SCT annotations](http://tristano.neuro.polymtl.ca)

### vnmrj

| Spec            | Description                                                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model**       | PC Intel Duo Quad Core                                                                                                                                            |
| **OS**          | RedHat                                                                                                                                                            |
| **Hostname**    |                                                                                                                                                                   |
| **Credentials** | [NeuroPoly Internal Document: VNMRJ VNC Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.jzew4w9jgpfp) |


### idea3t

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | Programming pulse sequences within the Siemens IDEA environment for VE11C (Prisma) |
| **Model** | PC |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `idea3t.neuro.polymtl.ca` |
| **Credentials** | [NeuroPoly Internal Document: Idea3t Remote Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.d65wz45n6ho7) |

```{warning}
**Possible error:** “The certificate or associated chain is not valid.”\
**Solution:** Install remote Desktop v10 or higher (v8 does not work)
```

### idea7t

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | Programming pulse sequences within the Siemens IDEA environment for VE12U (Terra) |
| **Model** | PC |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `idea7t.neuro.polymtl.ca` |
| **Credentials** | [NeuroPoly Internal Document: Idea7t Remote Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.i6g9qdkw050o) |


### peterson

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA RTX A6000 (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `peterson.grames.polymtl.ca` |
| **Credentials** | <GRAMES_USERNAME>/<GRAMES_PASSWORD> |


### node006 (Poly-Grames)

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA Tesla V100S-PCIE-32GB (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `node006.grames.polymtl.ca` |
| **Credentials** | <GRAMES_USERNAME>/<GRAMES_PASSWORD> |


### node007 (Poly-Grames)

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA Tesla V100S-PCIE-32GB (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `node007.grames.polymtl.ca` |
| **Credentials** | <GRAMES_USERNAME>/<GRAMES_PASSWORD> |


## Connect to the Polytechnique public disk

Finder –> Go –> Connect to server Server address:

```
smb://genie06.polymtl.ca/public
```

Then enter your ID and password at poly.

## Retrieve an old backup

**duke** (/mri, /projects, /sct_testing) is backed up on **grappelli** every evening at 21:00 EST. In order to retrieve old backup you have to contact Jean-Sébastien Décarie.

## Software Installed

### Installed on each station (local)

#### MRI

* FSL
* ANTS
* FreeSurfer
* mricron (for dcm2nii conversion)
* Osirix
* ITKsnap
* MITKworkbench
* Diffusion Toolkit (with quicklook plugin) + Trackvis

#### Programming

* git
* source tree –> visualiser of git
* Xcode (with command line tools)
* PyCharm (Python editor)
* Sublime Text (code editor)

#### Misc

* Google Sketchup
* Google Chrome
* VirtualBox
* Endnote
* Dropbox
* X11 Quartz
* Microsoft suite (Installation kit can be found on the GRAMES server. Please see section below.)
* Matlab (Installation kit can be found on the GRAMES server. Please see section below.)
* Slack
* NDP view
* QuickLook:
  * Nifti viewer
* Tanguy's app to open Nifti files with FSLview

## Admin

Technical details about station management and documentation is found on [this repository](https://github.com/neuropoly/computers).
