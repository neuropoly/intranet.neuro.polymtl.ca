
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

### Home folder

Your home folder at GE is here: `smb://hvclusterfs.grames.polymtl.ca/usagers/personnels`


## List of Computers at NeuroPoly

Are you new to NeuroPoly and looking for a desk and a station? Please check the [list of Desktop/Server/Clusters computers and Printers](https://docs.google.com/document/d/11GEh5YvYRnWnERv26TezcyvyPF2W5KF0uoI2U6p7XsM/edit) so you can pick one that is free. If you'd like a particular desk and someone else is using a station remotely, please ask the admins to move the station to another location.

If you prefer to work on your laptop, please let the admins know in your [onboarding ticket](https://github.com/neuropoly/onboarding/issues/) and they will find you an available screen you can connect to your laptop.

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
  * romane has a [special system for sharing CPU/RAM](./gpus.md#running-memory-and-cpu-intensive-tasks)

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
| **Credentials** | Username: "GRAMES\\\*\*\*" (***: Your GE username, eg: p101317) | Password: Your GE password |


### node006 (Poly-Grames)

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA Tesla V100S-PCIE-32GB (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `node006.grames.polymtl.ca` |
| **Credentials** | Username: "GRAMES\\\*\*\*" (***: Your GE username, eg: p101317) | Password: Your GE password |


### node007 (Poly-Grames)

| Spec | Description |
| --------------- | -------------- |
| **Purpose** | EM simulation with CST |
| **Model** | PC, NVIDIA Tesla V100S-PCIE-32GB (1x) |
| **OS** | Windows 10 (Connect with Microsoft Remote Desktop) |
| **Hostname**    | `node007.grames.polymtl.ca` |
| **Credentials** | Username: "GRAMES\\\*\*\*" (***: Your GE username, eg: p101317) | Password: Your GE password |

## VPN

When working remotely from off-campus you need to use the [VPN](http://www.polymtl.ca/si/reseaux/acces-securise-rvp-ou-vpn).

To connect to the VPN, you must have an account with École Polytechnique, specifically with [CAS](https://cas5.polymtl.ca/cas/login). **Students** should already have this. **Consultants**, **Research Professionals**, and sometimes **Interns** will need to have an account created for them. This should have happened during your onboarding.

You can change your CAS password at [Gestion des Codes](https://codes.si.polymtl.ca/gestion/).

The VPN uses the `Cisco AnyConnect` protocol, and to use it, you must first install a compatible VPN client.

```{important}
Depending on your status at Polytechnique, you will be assigned to a different VPN group. Your assigned group will determine how authentication will work for you, as well as which VPN clients will be compatible.

Instructions for different user scenarios are provided below.
```

```{note}
For the purposes of this documentation, the most reliable indicator of official Polytechnique status is the type of matricule (ID number) one is assigned:
- **[Students](#students)** typically have an ID number _without_ any letters at the start.
- **[Staff](#polytechnique-staff)** will have a `pMatricule` (an ID number preceded by a `p`).
- **Consultants** and [certain others](#other-members) will have a `uMatricule` (an ID number preceded by a `u`).
```

```{note}
The VPN will not work if you are already accessing wifi on campus via `eduroam`, it is typically intended for off-campus use only.
```

### Background on VPN changes

In September 2024, Polytechnique reconfigured their VPN management strategy.

Previously, VPN authentication worked similarly for all Neuropoly members. `Linux` and `macOS` users wishing to avoid installing proprietary `Cisco AnyConnect` software could follow the instruction provided for students (below).

Because of the changes implemented by Polytechnique, these instructions **no longer work for non-students.**

If you are not a student, please follow the instructions provided for your specific use case.

### Students

Students should be approved for VPN access by default. They are assigned to the `PolySSL` group.

For `Linux` and `macOS` users, `openconnect` is the recommended VPN client.

`Windows` users should typically follow the official Polytechnique instructions. Advanced users concerned about the monitoring capabilities of the `Cisco AnyConnect` client might consider adapting the instructions for a VM-based workaround documented under `Polytechnique Staff` to their needs.

::::{tab-set}
:::{tab-item} MacOS

**Install OpenConnect:**
```
brew install openconnect
```

**Add your password to Keychain:**
Open your Keychain program and click '+' to add a new item:
- Name: `poly-vpn`
- Account: your `YOUR_CAS_USERNAME`
- Password: enter your password here.
```{note}
The new item has to be added as an `application password` to your `login` Keychain (i.e., not to your `iCloud` Keychain).
```

**Automate connection with a script:**
_**Set up a shell script**_
```{note}
If you're not sure where to put your shell script, we recommend storing shell scripts under `~/bin`. You can modify the path in the following instructions if you prefer a different location.
```

Create a directory for shell scripts, and `cd` into it. E.g.:
```
mkdir ~/bin && cd ~/bin
```

Create a file called `vpn.sh` and add the following:
```bash
#!/bin/bash
# vpn.sh

set -eo pipefail

USER="<YOUR_CAS_USERNAME>"
PASS="$(security find-generic-password -a "${USER}" -s poly-vpn -w)"
GROUP=PolySSL # or PolyInvites, depending on your account's status
echo -n "$PASS" | sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin --reconnect-timeout 20 ssl.vpn.polymtl.ca
```

Make your script executable:
```
chmod 755 vpn.sh
```

To connect to the VPN, you need to run:
```
~/bin/vpn.sh
```

Or, from _within_ the same directory as your script:
```
./vpn.sh
```

_**Optional: Create an alias for your script**_
```{note}
For `macOS`, we assume you are using `zsh`, if you are using bash instead, replace `.zshrc` with `.bashrc` in the instructions. If the relevant file does not already exist, you should create it. 
```

Add the following to `~/.zshrc`:
```
alias vpn='~/bin/vpn.sh'
```

Source your shell to make the new alias available:
```
source ~/.zshrc
```

To start your vpn:
```
vpn
```
:::

:::{tab-item} Linux
**Install OpenConnect:**
```
sudo apt install openconnect
```

**Automate connection with a script:**
_**Set up a shell script**_
```{note}
If you're not sure where to put your shell script, we recommend storing shell scripts under `~/bin`. You can modify the path in the following instructions if you prefer a different location.
```

Create a directory for shell scripts, and `cd` into it. E.g.:
```
mkdir ~/bin && cd ~/bin
```

Create a file called `vpn.sh` and add one of the following:

_Option 1_
```bash
#!/bin/bash
# vpn.sh

set -eo pipefail

USER="<YOUR_CAS_USERNAME>"
PASS="<YOUR_CAS_PASSWORD>"
GROUP=PolySSL # or PolyInvites, depending on your account's status
sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin --reconnect-timeout 20 ssl.vpn.polymtl.ca
```

_Option 2_
```bash
#!/bin/bash
# vpn.sh

set -eo pipefail

USER="<YOUR_CAS_USERNAME>"
PASS="<YOUR_CAS_PASSWORD>"
GROUP=PolySSL # or PolyInvites, depending on your account's status
echo -n "$PASS" | sudo openconnect -u "$USER" --authgroup "$GROUP" --passwd-on-stdin --reconnect-timeout 20 ssl.vpn.polymtl.ca
```

```{warning}
_Option 2_ avoids a password prompt each time the script is invoked, **however** it also hardcodes your password, which is insecure and not recommended. We thus prefer _Option 1_. 
```

Make your script executable:
```
chmod 755 vpn.sh
```

To connect to the VPN, you need to run:
```
~/bin/vpn.sh
```

Or, from _within_ the same directory as your script:
```
./vpn.sh
```

_**Optional: Create an alias for your script**_
```{note}
If you are using `zsh` instead of `bash`, replace `.bashrc` with `.zshrc` in the instructions. If the relevant file does not already exist, you should create it. 
```

Add the following to `~/.bashrc`:
```
alias vpn='~/bin/vpn.sh'
```

Source your shell to make the new alias available:
```
source ~/.bashrc
```

To start your vpn:
```
vpn
```

**Alternative: Graphical OpenConnect:**

Depending on your Linux set up, you may be able to create a graphical interface for your VPN. 
```{note}
The following instructions were tested on a system using `NetworkManager` and the `GNOME` desktop environment.
```

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

Please follow the official steps from PolyMTL ([French](https://share.polymtl.ca/alfresco/service/api/path/content;cm:content/workspace/SpacesStore/Company%20Home/Sites/rentree/documentLibrary/Aide-m%C3%A9moire%20tutoriels%20A2020/Aide-Memoire_VPN.pdf?a=true&guest=true) or [English](https://share.polymtl.ca/alfresco/service/api/path/content;cm:content/workspace/SpacesStore/Company%20Home/Sites/rentree/documentLibrary/Aide-m%C3%A9moire%20tutoriels%20A2020/Checklist_VPN.pdf?a=true&guest=true)).

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

### Polytechnique Staff

Polytechnique staff (including **Professors**, **Research Associates**, **Postdoctoral Researchers**, and sometimes **Interns**) are those with a `pMatricule`. Polytechnique members with a `pMatricule` are assigned to the `PolyQuartz` group.

The `PolyQuartz` group relies on an authentication flow that makes use of your `Okta` account. The authentication flow is _not natively supported by the `openconnect` client_.

Users wishing to avoid installing the officially provisioned `Cisco AnyConnect` client can consider several known workarounds.

`Linux` and `macOS` users can use a workaround involving the `openconnect` client and manual cookie extraction.

All users can implement a workaround involving running the `Cisco AnyConnect` client inside a Virtual Machine.

_Instructions for each of these options are as follows:_

::::{tab-set}
:::{tab-item} Openconnect with cookie extraction

This workaround allows you to complete the `Okta`-based authentication flow while using the `openconnect` client.

It should be effective for `Linux` and `macOS` users.

1. Ensure that the `openconnect` client is installed on your computer.
2. Visit https://ssl.vpn.polymtl.ca in a browser
3. Select `PolyQuartz` and press `Logon`
4. Logon with your `Okta` credentials
5. On the `Cisco Secure Client Download` page, open your browser's `DevTools`.
6. Find the `webvpn` cookie and copy its value.
7. Pass this value to the following command on stdin (either by typing it, or piping to it):
```bash
sudo openconnect --protocol=anyconnect --authgroup=PolyQuartz --cookie-on-stdin https://ssl.vpn.polymtl.ca/
```

```{note}
A script to automate this process can be [found here](https://github.com/SomeoneInParticular/AutoPolyVPN).
```

:::

:::{tab-item} Cisco AnyConnect in a VM

This workaround allows you to isolate the `Cisco AnyConnect` client in a virtual machine. Additionally it allows you to determine which traffic you send through the VPN.

It should be effective for `Linux`, `macOS` and `Windows` users.

It is recommended for advanced users.

1. Create an `Ubuntu` virtual machine using your preferred Virtual Machine Manager (these instructions were tested with QEMU-KVM, but other VMMs should work fine as well).
2. Under network settings, your VM should be set to use `NAT`.
3. Inside your new VM, follow [the official Polytechnique instructions](https://www.polymtl.ca/si/acces-securise-rvp-ou-vpn) to install the `Cisco AnyConnect` client.
4. Set up your VM as an `SSH server`.
```bash
sudo apt install openssh-server
```
```bash
sudo systemctl enable ssh
```
```bash
sudo systemctl start ssh
```
5. Get the ip address of your VM (`ip a`) and write it down.
6. On the host, generate an SSH key pair, (or select an existing key pair to use) then transfer the public key to your VM using `ssh-copy-id`. You can **modify** the following commands with the correct info to do this:
```bash
ssh-keygen -t ed25519 -C "<VM_USER>@<VM_NAME>" -f ~/.ssh/<VM_USER>_ed25519
```
```bash
ssh-copy-id -i ~/.ssh/<VM_USER>_ed25519.pub -o PreferredAuthentications=password <VM_USER>@<VM_IP>
```
7. Test that you can successfully SSH into the VM.
8. In your SSH config file (`~/.ssh/config`) configure your VM as a proxy jump for traffic directed to NeuroPoly servers. You can **modify** the following config for your purposes:
```bash
# Needed for proxy jump with AnyConnect vm

# Replace the HostName with your VM's IP
# Replace the User with the username on your VM
# Replace the IdentityFile with the correct path to the relevant SSH key
Host jumpvm
    HostName <VM_IP>
    User <VM_USER>
    IdentityFile ~/.ssh/<VM_USER>_ed25519

# This allows you to proxy ssh traffic to NeuroPoly servers
Host *.neuro.polymtl.ca 132.207.*
    ProxyJump jumpvm

# Needed to use git with data

# Replace the IdentityFile with the correct path to the SSH key you use on data
Host data.neuro.polymtl.ca
    User git
    IdentityFile ~/.ssh/<KEY_FILE>
```

```{note}
If you sometimes work on campus, this config will interfere with your onsite access if not disabled. If you want to make it easier to manage alternate ssh config settings, you can create a different config file that includes these settings, and then point to it with the `ssh -F` option.
```

Once you have finished with configuration, you can test your set up. For it to work, you will need to first start your VM and enable the VPN connection using the `Cisco AnyConnect` client inside your VM.

You will then be able to proxy NeuroPoly-destined ssh traffic from your main host through your VM, which will make it easier to connect to NeuroPoly resources without significantly altering your workflow. You can test making an ssh connection to a NeuroPoly server to confirm that this works.

```{note}
You can use port forwarding to form other kinds of connections through your VM. (e.g. for `RDP` connections, to access `duke` or to access `data` in your browser). Examples follow.
```

**To connect to a station using `RDP`**
```bash
ssh -NL 3389:localhost:3389 <GE_USERNAME@<STATION>.neuro.polymtl.ca
```
Then in your `RDP` client put `localhost:3389` for the server.

**To connect to `duke`**
```bash
ssh -NL 1445:duke.neuro.polymtl.ca:445 <VM_USER>@jumpvm
```
Then follow standard instructions for `duke` but replace `duke.neuro.polymtl.ca` with `localhost:1445` (e.g. `smb://localhost:1445/<FOLDER>`).

**To access `data` in your browser**
```bash
ssh -NL 3000:localhost:3000 <GE_USERNAME>@data.neuro.polymtl.ca
```
Then in your browser go to: `http://localhost:3000`

:::

:::{tab-item} Official instructions

The official Polytechnique instructions for configuring the `Cisco AnyConnect` client [can be found here](https://www.polymtl.ca/si/acces-securise-rvp-ou-vpn).
:::
::::

### Other Members

This section applies to users who have been assigned a `uMatricule`. Typically, this means **Consultants**, some **Interns**, and anyone else considered an **"Invité"** by Polytechnique. Users in this category are **not** granted VPN access by default. A specific request must be submitted to [DGE IT](mailto:dge.informatique@polymtl.ca) to give you VPN access. (Normally, someone on the admin team should help you with this during your onboarding).

Once you are approved for VPN access, DGE IT will provide personalized instructions for your specific use case. Most likely, you will be be added to the `PolyPhoton` group. Like `PolyQuartz`, this group uses `Okta` for authentication.

```{note}
If you do not wish to use the official `Cisco AnyConnect` client, you may be able to adapt the instructions under the `Polytechnique Staff` section for your purposes. However, please note that the workarounds described for `PolyQuartz` users have not been adequately tested for `PolyPhoton` users.
```

```{warning}
DGE IT's protocols for integration of VPN users with an **"Invité"** status are currently under development, so at the moment we cannot provide much assurance that alternative VPN configurations will work for these users. The most reliable option is to follow the official instructions provided by DGE IT [and Polytechnique](https://www.polymtl.ca/si/acces-securise-rvp-ou-vpn).
```

## Connect to NeuroPoly Computers

### Locally

To log into a desktop station while at NeuroPoly, use your GE account.

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
Follow [this procedure](https://www.petergirnus.com/blog/how-to-use-sshfs-on-macos).
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

As part of regularly scheduled system upgrades, all NeuroPoly stations will automatically reboot once a week. These reboots are critical to system health, which is why they are configured to run automatically. In exceptional circumstances, scheduled reboots can be manually postponed by admins.


### How do I know when a station will reboot?

When you first login to a station, you will see a message called the `Message Of The Day` (`MOTD`).

This message includes a notice about the reboot schedule for the machine you are using. It will look something like this:
```
This system may reboot to install upgrades Mondays at 02:00am.
```

There is also a convenience script which will display the date of the next system update:
```
$ unattended-upgrades-date
Mon Aug  4 04:04:38 EDT 2025
```

### How can I request that a scheduled reboot is postponed?

If you started or will start a long computation that you think will be interrupted by the scheduled reboot, you can [use the `Reboot Postponement Request` issue template](https://github.com/neuropoly/computers/issues/new?template=reboot-postponement-req.md) to request a postponement.

More detailed instructions are included in the template.

```{important}
Please try to give admins a working day's notice for postponement requests.
```

**Admins:** The standard operating procedure for postponing scheduled reboots, along with more details on how automatic reboots work at NeuroPoly is all documented
[on the wiki](https://github.com/neuropoly/computers/wiki/Administering-stations#unattended-upgrades).

## Admin

Technical details about station management and documentation is found on [this repository](https://github.com/neuropoly/computers).
