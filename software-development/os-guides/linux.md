# Linux

## **Automatic** M**ount on Startup**

For the following steps you need admin permissions.

1. Create data\_processing & data\_shared folders in `/mnt`, type:

```bash
sudo mkdir /mnt/data_processing
sudo mkdir /mnt/data_shared
```

2. Edit mount table, type : `sudo nano /etc/fstab`

3. For the following operating systems:

{% tabs %}
{% tab title="Ubuntu 14.04 LTS" %}
Add the following lines at the bottom of the file:

```bash
#data_processing @SERVER
//IP_SERVER/data_processing        /mnt/data_processing    cifs    username=XXX,password=XXX    0       0

#data_shared @SERVER
//IP_SERVER/data_shared        /mnt/data_shared    cifs    username=XXX,password=XXX    0       0
```
{% endtab %}

{% tab title="Debian Wheezy 8" %}
Add the following lines at the bottom of the file:

```bash
#data_processing @SERVER
//IP_SERVER/data_processing    /mnt/data_processing    cifs  nounix,sec=ntlmssp,user=XXX,password=XXX 0 0

#data_shared @SERVER
//IP_SERVER/data_shared    /mnt/data_shared    cifs  nounix,sec=ntlmssp,user=XXX,password=XXX 0 0
```
{% endtab %}
{% endtabs %}

4. Remount drives and type: `sudo mount -a`

## CentOS/Fedora/Red Hat

### Ants & c3d

Binaries for debian work well, just make sure the paths are set in the bashrc as follow:

```text
PATH=${PATH}:${SCT_DIR}/install/debian/ants

PATH=${PATH}:${SCT_DIR}/install/debian/c3d
```

### FSL

Need `libmng` installed for fslview:

```text
~ sudo yum install libmng libpng12
```

Then install FSL with the python script `fslinstaller.py` you'll find there : [http://goo.gl/Tfu1UW](http://goo.gl/Tfu1UW) Make sure the installer set your bash configuration, following lines should be in your bashrc or bash\_profile. If not, add it:

```bash
FSLDIR="/usr/local/fsl"
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH
```

### Miniconda

Run the miniconda installer shell script for linux you can get there [http://conda.pydata.org/miniconda.html](http://conda.pydata.org/miniconda.html)

```bash
~ bash Miniconda-*.sh
```

Then, in the SCT repo, type:

```text
~ bash ./requirements/requirements.sh
```

