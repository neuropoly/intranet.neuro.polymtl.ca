
(computing-resources-neuropoly)=
# <span>🖥</span> Computers \@NeuroPoly

```{toctree}
:hidden:
cpus
gpus
```

## GE

A [**GE**](https://www.ge.polymtl.ca/compte-informatique/) network account is required to have access to internal computational resources.

You will receive a GE account during your [onboarding](https://github.com/neuropoly/onboarding/issues).

### Password

```{important}
Once in a while, you are requested to change your password. To do so, log onto another machine (eg `bireli`, `joplin`) and use the command `passwd` to change your password. 
```

### Groups

The list of permissions for shared folders on `duke` are available [here](https://docs.google.com/document/d/1ZJUUBpiZPl0wxFsUPxkkR6vXZgfSAd3YBK5vlIpf_aA/edit).

### Connect to Windows Servers

Use Microsoft Remote Desktop Connection on creer51, creer52, creer53.

Computer : creer51.grames.polymtl.ca

Username: grames\your_polygrames_username

Password: your_polygrames_password

## List of Computers at NeuroPoly

Are you new to NeuroPoly and looking for a desk and a station? Please check the [list of Desktop/Server/Clusters computers and Printers](https://docs.google.com/document/d/11GEh5YvYRnWnERv26TezcyvyPF2W5KF0uoI2U6p7XsM/edit) so you can pick one that is free. If you'd like a particular desk and someone else is using a station remotely, please ask the admins to move the station to another location.

If you prefer to work on your laptop, please let the admins know in your [onboarding ticket](https://github.com/neuropoly/onboarding/issues/) and they will find you an available screen you can connect to your laptop.

## VPN

When working remotely from off-campus you need to use the [VPN](http://www.polymtl.ca/si/reseaux/acces-securise-rvp-ou-vpn).

To connect to the VPN, you need to have an account with École Polytechnique, specifically with [CAS](https://cas5.polymtl.ca/cas/login). Students should already have this. Consultants and Research Associates will need to have an account created for them. This should have happened during your onboarding.

You can change your password at [Gestion des Codes](https://codes.si.polymtl.ca/gestion/). Consultants and Research Associates can double-check that they have VPN access by looking for `VPN_EMPLOYEE = Actif` here. Students should have this access by default, although it will not be displayed on the Gestion des Codes page.

_NB: The VPN will not work if you are already accessing wifi on campus via Eduroam, it is typically intended for off-campus use only._

The VPN is a Cisco AnyConnect server. For Linux and macOS you can reach it by first installing a VPN client such as `openconnect` (recommended) or `Cisco AnyConnect Secure Mobility Client` (if `openconnect` is not available for your OS/distro):


::::{tab-set}
:::{tab-item} MacOS
```
brew install openconnect
```

Open your Keychain program and click '+' to add a new item:
- Name: `poly-vpn`
- Account: your `YOUR_CAS_USERNAME`
- Password: enter your password here.

Note: the new item has to be added as an `application password` to your `login` Keychain (i.e., not to your `iCloud` Keychain).

Then, create the following script:
```bash
#!/bin/bash
# vpn.sh

set -eo pipefail

USER="<YOUR_CAS_USERNAME>"
PASS="$(security find-generic-password -a "${USER}" -s poly-vpn -w)"
GROUP=PolySSL # or PolyInvites, depending on your account's status
echo -n "$PASS" | sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin --reconnect-timeout 20 ssl.vpn.polymtl.ca
```

To connect to the VPN, you need to run:
```
./vpn.sh
```
:::

:::{tab-item} Linux
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
echo -n "$PASS" | sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin --reconnect-timeout 20 ssl.vpn.polymtl.ca
```

To connect to the VPN, you need to run:
```
./vpn.sh
```
Depending on your Linux set up, you may also be able to create a graphical interface for your VPN. The following instructions were tested on a system using `NetworkManager` and the GNOME desktop environment:
1. Install the [NetworkManager openconnect plugin](https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/). For example, with: 
```
sudo apt install network-manager-openconnect-gnome
```
2. Under `Settings` go to `Network`.
3. Under `VPN` select `+` to `Add VPN`.
4. Select `Multi-protocol VPN client (openconnect)`.
5. Under `Gateway` put `ssl.vpn.polymtl.ca`.
6. Click `Apply`.
7. Activate the VPN.
8. Under `GROUP:` select `PolySSL`.
9. Under `Username:`  put your CAS username.
10. Under `Password:` put your CAS password.
11. Click `Connect`.
    
:::

:::{tab-item} Windows

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
:::
::::


## Connect to NeuroPoly Computers

### Locally

To log into a desktop station while at NeuroPoly use your GE account.

### SSH (command line)

```{note}
If working off-campus, start your [VPN](#vpn) first.
```

```{note}
If working on-campus using `eduroam` wifi, make sure you are connected to `eduroam` using your Poly credentials. The `ssh` command below will probably not work if you are using `eduroam` credentials from another university. Alternatively, you can use the cable connection.
```

Connect via ssh using the `STATION` you want:

```bash
 ssh <GE_USERNAME>@<STATION>.neuro.polymtl.ca
```

```{note}
Use the password you received by email. Not the password you received on printed paper. To change the password, see the section `Password` above.
```

```{note}
To get ssh on Windows, you can [install Microsoft's ssh package](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse), [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10), [PuTTY](https://www.chiark.greenend.org.uk/\~sgtatham/putty/), or [cmder](https://cmder.net), or [Git-Bash](https://git-scm.com/download/win).
```

Optionally, install this shortcut which allows you to just type `ssh <STATION>`:

```bash
cat >~/.ssh/config_neuropoly <<EOF
Match Host abbey,betty,bireli,coltrane,davis,django,ella,ferguson,jarrett,joplin,kirk,marsalis,mingus,parker,romane,rosenberg,tatum
HostName %h.neuro.polymtl.ca

Match host *.neuro.polymtl.ca
User <GE USERNAME> # fill in your username and remove this comment
# passwords are required to access /mnt/duke: https://github.com/neuropoly/computers/issues/90:
PreferredAuthentications password
EOF

echo 'Include ~/.ssh/config_neuropoly' >> ~/.ssh/config
```

Optionally, add this shortcut which makes simultaneous ssh connections possible without retyping your password:

```
cat >>~/.ssh/config <<EOF
Host *
ControlMaster auto
ControlPath ~/.ssh/%r@%h:%p
ControlPersist 3s
```


### SFTP (Mount a remote station)

`ssh` also allows accessing remote files, via [`sftp`](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol).

The best way to do this is `sshfs`, which makes them appear as if they were a drive on your computer:

Install sshfs, if not yet installed:

::::{tab-set}
:::{tab-item} Linux
```
sudo apt install -y sshfs
```
:::

:::{tab-item} mac (Monterey and after)
Follow [this procedure](https://eengstrom.github.io/musings/install-macfuse-and-sshfs-on-macos-monterey).
:::

:::{tab-item} mac (Before Monterey)
```
brew install --cask osxfuse
brew install sshfs
```
:::
::::

Then mount the folder

```
mkdir cluster_folder
sshfs <USERNAME>@<STATION>: cluster_folder
```

If you use `~` or nothing (as shown) after the `:`, the connection will be relative to to your _remote_ home directory, e.g.

```
sshfs <USERNAME>@<STATION>:~/project1/ cluster_folder
```

will attach the remote `/home/ge.polymtl.ca/$USER/project1/` to the local `./cluster_folder`, and

```
sshfs <USERNAME>@<STATION>:project1/ cluster_folder
```

will do the exact same.

However if you use `/` after the `:`, the mount will be relative to the _remote root directory_, e.g.

```
sshfs <USERNAME>@<STATION>:/tmp/ cluster_folder
```

will attach the remote `/tmp/` to the local `./cluster_folder`


```{note}
If you are experiencing mounting issues on macOs, [this](https://github.com/neuropoly/intranet.neuro.polymtl.ca/issues/57) might help.
```


### VNC (graphical interface)


::::{tab-set}
:::{tab-item} macOS
1. Open Finder
2. Click Cmd+K
3. In the “Server Address”, type (using the `STATION` you want): `vnc://STATION.neuro.polymtl.ca`
4. You can use your local/network account information or the [shared account credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.ckseg5ldklsg)
:::

:::{tab-item} PC/Linux
1. Establish a VNC connection using [vinaigre](https://wiki.gnome.org/Apps/Vinagre/).
2. In the “Server Address”, type (using the `STATION` you want): `vnc://STATION.neuro.polymtl.ca`
3. You can use the password from [shared account credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.ckseg5ldklsg)
:::
::::

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

### Language

The default interface on our systems is français. To use another language, set your `LANG` environment variable:

```
echo 'export LANG=en_CA.UTF-8' >> ~/.profile
```

Logout and back in again and apps should now be in English (or the other language code you chose).



## CPU/GPU Clusters

The following CPU and GPU clusters are available for internal use at **NeuroPoly**.

```{warning}
Please indicate in [NeuroPoly's "Computer resource" calendar](https://calendar.google.com/calendar/u/0/embed?src=4mg6bgd9pv55thf9486t2miht8@group.calendar.google.com) if you plan to launch intensive calculations on a computer. These are shared resources, so it helps to know which computer is being used and by who, in order to prioritize tasks and make the best of our resources. Your calendar entry could span several days, and should specify your name and the ID or number of GPU/CPU used. Example: `julien@rosenberg:gpu[4,5]`, or `naga@joplin:cpu[n=20]` If you don't have writing permission on this calendar please post a request on [the ticket tracker](https://github.com/neuropoly/computers/issues/).
```

```{note}
If you wish to monitor the CPU/GPU/RAM/disk and other aspects of the server you are using, you can use our [monitoring system](https://monitor.neuro.polymtl.ca/v1). You need to be inside the VLAN to see the monitoring system.
```

### rosenberg

| Spec         | Description                  |
| ------------ | ---------------------------- |
| **CPU**      | 2x Intel E5-2630             |
| **GPU**      | 8x P100                      |
| **RAM**      | 16x 32GB DDR4                |
| **Hostname** | `rosenberg.neuro.polymtl.ca` |

* By default, the root (OS and home folder) mount point is on the NVME disk
* Shared **scratch** located under **/scratch**. Please clean the unnecessary data after you finish the processing.
* [How to use GPU Clusters at NeuroPoly](https://intranet.neuro.polymtl.ca/computing-resources/neuropoly/gpus.html)
  * [Video tutorial to get started](https://drive.google.com/file/d/17-eLVBiMNA8bNbfzpD6NLxHApZRDoy1B/view?usp=sharing)

_For system administrators_: Please log all the changes on the station by updating the ansible scripts from [https://github.com/neuropoly/computers](https://github.com/neuropoly/computers).


### romane

| Spec         | Description                  |
| ------------ | ---------------------------- |
| **CPU**      | AMD EPYC 7452 32-Core        |
| **GPU**      | 4x RTX A6000 48GB            |
| **RAM**      | 16x 32GB DDR4                |
| **Hostname** | `romane.neuro.polymtl.ca`    |

* By default, the root (OS and home folder) mount point is on the NVME disk. You can train your model on your /home
* [How to use GPU Clusters at NeuroPoly](https://intranet.neuro.polymtl.ca/computing-resources/neuropoly/gpus.html)
  * [Video tutorial to get started](https://drive.google.com/file/d/17-eLVBiMNA8bNbfzpD6NLxHApZRDoy1B/view?usp=sharing)

_For system administrators_: Please log all the changes on the station by updating the ansible scripts from [https://github.com/neuropoly/computers](https://github.com/neuropoly/computers).


### bireli

| Spec         | Description                |
| ------------ | -------------------------- |
| **CPU**      | i7-5930K 3.5GHz 6 Cores    |
| **GPU**      | 2x GTX Titan X 12GB        |
| **RAM**      | 1x 64GB DDR4               |
| **Hostname** | `bireli.neuro.polymtl.ca`  |

* Add event to the computer calendar
* Use your **GE** account to connect on the machine
* [How to use GPU Clusters at NeuroPoly](https://intranet.neuro.polymtl.ca/computing-resources/computing-resources-neuropoly/gpus)


### joplin

| Spec         | Description                           |
| ------------ | ------------------------------------- |
| **CPU**      | 8x Intel E7-4809v4 8-Core 2.10GHz     |
| **RAM**      | 16x 16GB DDR4                         |
| **Hostname** | `joplin.neuro.polymtl.ca`             |

The server is bound to the GRAMES which is linked to the GE domain.

### abbey

| Spec            | Description                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CPU**         | Xeon 12-core                                                                                                                                                             |
| **OS**          | Ubuntu                                                                                                                                                                   |
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
| **OS** | Windows 10 (⚠️ Connect with Microsoft Remote Desktop) |
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
| **OS** | Windows 10 (⚠️ Connect with Microsoft Remote Desktop) |
| **Hostname**    | `idea7t.neuro.polymtl.ca` |
| **Credentials** | [NeuroPoly Internal Document: Idea7t Remote Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.i6g9qdkw050o) |


### peterson

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA RTX A6000 (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `peterson.grames.polymtl.ca` |
| **Credentials** | <GE_USERNAME>/<GE_PASSWORD> |


### node006 (Poly-Grames)

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA Tesla V100S-PCIE-32GB (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `node006.grames.polymtl.ca` |
| **Credentials** | <GE_USERNAME>/<GE_PASSWORD> |


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

To access software from the department (Matlab, Microsoft Office, etc.), connect to: 
~~~
smb://hcifst.grames.polymtl.ca/tools
~~~

## Scheduled reboots

Each computer has a regular unattended upgrade that forces a reboot once a week. The date and time of the next reboot will be indicated in a message when you log in. Do try and consider this when starting your computations. If you started a long computation that you think will be interupted by the scheduled reboot, you can contact neuropoly-admin@liste.polymtl.ca to request that the reboot be exceptionally delayed.

**Admins**: Documentation on the standard operating procedure for delaying scheduled reboots is described [here](https://github.com/neuropoly/computers/blob/master/docs/unattended-upgrades.md).

## Admin

Technical details about station management and documentation is found on [this repository](https://github.com/neuropoly/computers).
