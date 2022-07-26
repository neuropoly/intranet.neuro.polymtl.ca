# VirtualBox

## Import a .ova file <a href="import_a_ova_file" id="import_a_ova_file"></a>

If you have a Virtual Machine (VM) that has a .ova extension here's what to do to use it with Virtualbox

* Install virtualbox [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
* Open Virtualbox, then go to file –> Import appliance –> Open appliance and select your .ova file
* Then click Continue then Import
* It may take several minutes to import
* Once it's done just select your machine and click on Show to run it

## Shared folder <a href="shared_folder" id="shared_folder"></a>

### Using Guest Additions (recommended) <a href="using_guest_additions_recommended" id="using_guest_additions_recommended"></a>

[https://www.virtualbox.org/manual/ch04.html#idp91444064](https://www.virtualbox.org/manual/ch04.html#idp91444064)

On Linux: once you ran all the instructions here, a CD-ROM will be mounted on the guest. Then, go to /mnt/ and run the file ./VBoxLinuxAdditions.run in a terminal.

### Manual method <a href="manual_method" id="manual_method"></a>

[https://www.virtualbox.org/manual/ch04.html#idp91444064](https://www.virtualbox.org/manual/ch04.html#idp91444064) If you want to transfer files between your computer (host) and your Virtual Machine (guest) you'll need a shared folder.

* Create a folder on your computer that will be your shared folder e.g. /home/user/VM_shared
* Go to VirtualBox and open the Settings of your VM
* On the Shared Folders section, click on Add a folder
* Enter the path to your folder AND give it a different name e.g **VBShared**.
* Now, start your VM and create a folder e.g /home/user/Shared_Folder
* Now you need to edit the file `/etc/rc.local` and add this above the “exit 0 ” line: `mount -t vboxsf -o `_`username=uid, groupname=gid`_` `**`VBShared`**` /home/user/Shared_Folder`
  * In order to get _username/uid/groupname/gid_. Open a terminal:
    * Get _username_ –> `whoami`. Get _groupname_ –> `groups` (uid and gid respectively) to assign the permissions to the Shared folder
    * gid: `getent group `_`groupname`_ (e.g. groupename = NeuroPoly, the command will give NeuroPoly:x:1000 where the 3rd argument is the gid)
    * uid: `id -u `_`username`_
  * For admin rights use `sudo vi /etc/rc.local`. Or `su root`. Then `vi /etc/rc.local` You need the admin password.
* Now reboot your VM.
* Make the change permanent: Go to VirtualBox–>settings–>foldershared–>double click–>'Make Permanent' option

If that didn't work it could be because the VBoxGuestAdditions are not installed on your VM. If so, follow those next step :

* In the Storage section of Settings of your VM add the VBoxGuestAdditions.iso file that you'll find in ( _C:\Program Files\Oracle\VirtualBox_ for Windows or _/Applications/VirtualBox.app/Contents/MacOS_ for Mac )
* In your VM open a terminal and run (for Linux-based VM e.g. Linux,Debian,Ubuntu):
* `cd /media/cdrom`
* `sudo bash VBoxLinuxAdditions.run`
* Reboot your VM

### Create a Virtual Machine (VM) with Debian <a href="create_a_virtual_machine_vm_with_debian" id="create_a_virtual_machine_vm_with_debian"></a>

To create a Virtual Machine with Debian, you can follow this excellent tutorial: [http://www.brianlinkletter.com/installing-debian-linux-in-a-virtualbox-virtual-machine/](http://www.brianlinkletter.com/installing-debian-linux-in-a-virtualbox-virtual-machine/).

**RAM**

Don't give to your VM more than the half of your system RAM. You need to keep memory for your own system.

### Reduce the size of the VM <a href="reduce_the_size_of_the_vm" id="reduce_the_size_of_the_vm"></a>

Run defrag in the guest (Windows only)

Nullify free space:

**With a Linux Guest run this:**

```
sudo dd if=/dev/zero of=/bigemptyfile bs=4096k
sudo rm -rf /bigemptyfile
```

**With a Windows Guest, download SDelete and run this:**

```
sdelete –z
```

Shutdown the guest VM

Now run VBoxManage's modifyhd command with the –compact option:

**With a Linux Host run this:**

```
vboxmanage modifyhd /path/to/thedisk.vdi --compact
```

**With a Windows Host run this:**

```
VBoxManage.exe modifyhd c:\path\to\thedisk.vdi --compact
```

**With a Mac Host run this:**

```
VBoxManage modifyhd /path/to/thedisk.vdi --compact
```

This reduces the vdi size.

Source:

* [http://www.maketecheasier.com/shrink-your-virtualbox-vm/](http://www.maketecheasier.com/shrink-your-virtualbox-vm/)
* [http://www.thelinuxdaily.com/2010/02/shrinking-a-dynamic-virtualbox-disk-image/](http://www.thelinuxdaily.com/2010/02/shrinking-a-dynamic-virtualbox-disk-image/)
* [http://jurajsplayground.com/2012/05/20/shrinking-a-dynamic-virtualbox-hard-disk-on-ubuntu/](http://jurajsplayground.com/2012/05/20/shrinking-a-dynamic-virtualbox-hard-disk-on-ubuntu/)
* [http://crysol.github.io/recipe/2013-10-15/virtualbox-compact-vmdk-images/#.U8LWqY1dUkg](http://crysol.github.io/recipe/2013-10-15/virtualbox-compact-vmdk-images/#.U8LWqY1dUkg)

### Install guest additions <a href="install_guest_additions" id="install_guest_additions"></a>

#### Ubuntu 14.04 <a href="ubuntu_1404" id="ubuntu_1404"></a>

```
sudo apt-get update
sudo apt-get install virtualbox-guest-additions-iso
```

Once installed, click on **Devices > Insert Guest Additions CD Image…**, then reload VM.
