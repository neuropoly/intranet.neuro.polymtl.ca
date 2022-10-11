---
description: >-
  The Centre de recherche de l'Institut universitaire de gériatrie de Montréal
  (CRIUGM) has computing clusters which members of NeuroPoly Lab have access to.
---

# `🖥` Computers \@CRIUGM

## Login

To acess CRIUGM computer infrastructure you need a login. Ask Julien and he will redirect you to the right person to get a login.

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
scp -r /src username@elm.criugm.qc.ca:neuropoly/<GRAMES_USERNAME>
```

For a faster processing move your data on elm from home to scratch:

```bash
cp -r source/ /scratch/julien/neuropoly/<GRAMES_USERNAME>
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

