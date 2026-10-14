---
description: >-
  The Centre de recherche de l'Institut universitaire de gériatrie de Montréal
  (CRIUGM) has computing clusters which members of NeuroPoly Lab have access to.
---

# <span>🖥</span> Computers \@CRIUGM

## Login

To acess CRIUGM computer infrastructure you need a login. Ask Julien and he will redirect you to the right person to get a login.

## VPN

To reach the CRIUGM machines from outside the CRIUGM network, you need to be connected to the CRIUGM VPN (FortiGate SSL VPN). Use your CRIUGM username and password.

| Setting | Value |
| --- | --- |
| VPN server | `206.167.239.2` |
| Port | `443` |
| VPN type | FortiGate (SSL VPN) |
| Trusted certificate (SHA256) | `6864f5458ecef9e9896f8ae6f527681e0a4afc72bcb2c72fbe3feb65b85d85a3` |

```{important}
The gateway uses a self-signed certificate, so you need to pin it as trusted (with the SHA256 above). Do **not** enable "Trust all certs".
```

You can use the official FortiClient VPN, but it asks for your credentials at every login. The open-source [openfortivpn](https://github.com/adrienverge/openfortivpn) is a convenient alternative.

### Linux

Install `openfortivpn` (e.g. `sudo apt install openfortivpn`) and, optionally, the [OpenFortiGUI](https://github.com/theinvisible/openfortigui) front-end, which can store your credentials. In OpenFortiGUI, create a new VPN with the settings in the table above (VPN-Device: `Fortigate`, check "Credentials" and fill your username/password, leave "Trust all Certs" unchecked and paste the SHA256 in "Trusted-Cert").

### macOS

Install from Homebrew:

```bash
brew install openfortivpn
```

For a friendlier GUI, you can try [openfortivpn-connect](https://github.com/walcew/openfortivpn-connect).

### Command line (Linux and macOS)

Create a config file, e.g. `~/.config/openfortivpn/criugm.conf`:

```
host = 206.167.239.2
port = 443
username = <CRIUGM_USERNAME>
trusted-cert = 6864f5458ecef9e9896f8ae6f527681e0a4afc72bcb2c72fbe3feb65b85d85a3
```

Then connect with (you will be prompted for your password):

```bash
sudo openfortivpn -c ~/.config/openfortivpn/criugm.conf
```

Once connected, you can `ssh` to the clusters below.

## CPU Clusters

```bash
elm.criugm.qc.ca (64 cores)
jacaranda.criugm.qc.ca (24 cores)
```

Note: to run your processings, go to `/scratch`, it is a much faster disk than the disk where your home directory is, however it is only used for temp files \(i.e. clean after use\).

## Transferring Data from JACARANDA

When located in your home directory , you can compress a scan \(example myelin\_06\_rescan\) with the following command

```bash
tar -zcvhf myelin_06_rescan.tar.gz /unf/dicoms/by_groups/neuropoly/dev/myelin_mapping/myelin_06_rescan/
```

Once the `.tar.gz` file has been created, you can download it on your computer using scp or using filezilla \(setup connection to sftp server\).

## Using JACARANDA and ELM

JACARANDA and ELM use Sun grid engine.

* Open a Terminal and run: `ssh <username>@jacaranda.criugm.qc.ca`

### **Create Job Script**

```{note}
**Example**

```bash
#!/bin/bash
#$ -V  # To load environment variables
 
cd /scratch/julien
 
echo "Script started at:"
date
 
# Launch script
sct_testing
 
echo "Script ended at:"
date
```
```

* Submit job: `qsub my_job.pbs`
* To see all the jobs currently running type: `qstat`
* use “/scratch” \(faster\)

### Tips & Tricks Elm

Connect to Elm using:

```bash
ssh -Y username@elm.criugm.qc.ca
```

Copy your files using `scp` to Elm from your computer:

```bash
scp -r /src username@elm.criugm.qc.ca:neuropoly/<GE_USERNAME>
```

For a faster processing move your data on elm from home to scratch:

```bash
cp -r source/ /scratch/julien/neuropoly/<GE_USERNAME>
```

Activate MATLAB on elm:

```bash
module load matlab
matlab
```

MATLAB - add to path with subfolders:

```bash
addpath(genpath('/your_path'))
```

