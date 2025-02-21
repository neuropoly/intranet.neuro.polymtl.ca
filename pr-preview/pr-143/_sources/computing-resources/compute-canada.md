# <span>🖥</span> Compute Canada

## Create Account

Register here: [https://ccdb.computecanada.ca/account\_application](https://ccdb.computecanada.ca/account_application). Members of the NeuroPoly lab can use [the sponsor number of their supervisor](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.g1khl9eioopm). Please use the following information - Home institution: Polytechnique Montreal ; Department: Electrical Engineering.

Links to Compute Canada:

* [List of available clusters](https://docs.computecanada.ca/wiki/National_systems)
  * [Niagara](https://docs.computecanada.ca/wiki/Niagara_Quickstart)
  * [Graham](https://docs.computecanada.ca/wiki/Graham)
* [Compute Canada Documentation](https://docs.computecanada.ca/wiki/Compute_Canada_Documentation)
* [Compute Canada available resources](https://www.computecanada.ca/research-portal/accessing-resources/available-resources/)
* [CC documentation \(from Mila\)](https://docs.mila.quebec/compute-canada-cluster/index.html)

Useful resources:

* [High Performance Computing \(HPC\) Tutorials](https://ulhpc-tutorials.readthedocs.io/en/latest/)

## Getting Started

You can find the [Resource Allocation Project Identifier \(RAPI\)](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.g1khl9eioopm) here.

### **Transfer Files**

```bash
scp <username>@guillimin.clumeq.ca:<PATH/TO/FILE>
```

### **Environment Variables**

You have a `.bash_profile` and `.bashrc` on the server. Use `.bahsrc` rather than `.bash_profile`.

```bash
PATH=${PATH}:/gs/project/<RAPI>/bin/ants/bin
export ANTSPATH=/gs/project/<RAPI>/bin/ants/bin/
```

### **Modules**

There are pre-installed modules that you'll need to load in order to use \(e.g. `cmake`\). To see all modules available:

```bash
module avail
```

To load module \(you can put this in your `.bashrc` if you need the module all the time\):

```bash
module load <module_name>
```

```{note}
**Example**: Check if git is available and load it

```bash
module avail git
module load apps/git/2.13.0
```
```

You have to build everything from source because you don't have root permission to install anything yourself. You can send an email to `guillimin "at" calculquebec "dot" ca` if you need them to install something on your session. They are quite responsive.

### **Disk Space**

You have:

1. home folder `/home/<username>` → 10GB
2. project space `/gs/project/<id>` id is the one shared by all the people in the group \(login to calculquebec website and you’ll find it\) → 1TB

To check how much space you have left:

```bash
serveur-info
```

The folder common to the lab \(where you need to work\) is:

```bash
/gs/project/<RAPI>
```

### **Create job script**

```{note}
**Example**

```bash
#!/bin/bash
#PBS -l nodes=1:ppn=16,pmem=31700m,walltime=48:00:00
#PBS -A <RAPI>
#PBS -o output.txt
#PBS -e error.txt
#PBS -V
#PBS -N build_template
cd /gs/project/<RAPI>/final_data_T2
bash buildtemplateparallel.sh -d 3 -o AVT -n 0 -c 2 -j 16 *.nii.gz
```
```

### **Submit job**

```bash
qsub my_job.sh
  -p  Defines the  priority of the job.  The priority argument must be a integer between -1024 and +1023 inclusive.  The default is  no  priority which is equivalent to a priority of zero.
  -m be  sends email when job begins and terminates
  -z  Directs  that  the qsub command is not to write the job identifier assigned to the job to the command’s standard output.
```

### **Check jobs**

```bash
qstat -u $USER
  S: Q (queue), R (running)
checkjob JobID (only the number!) [-v] [-v]
```

```bash
# Once running:
showq -r -u $USER
```

### **Kill job**

```text
qdel JobID
```

## Tips and Tricks

Use `$SCRATCH` disk to run your scripts, because `$SCRATCH` is much faster than `$HOME`. 

### Python

[Compute Canada: Python](https://docs.computecanada.ca/wiki/Python) 

```bash
# activate python
module load python/3.6
# create virtual environment
virtualenv <VENV_NAME>
# activate it
source <VENV_NAME>/bin/activate
# deactivate
deactivate
```

## List of Servers

[Compute Canada: Running jobs](https://docs.computecanada.ca/wiki/Running_jobs)

### Cedar \(CC\)

**Server**: `cedar.computecanada.ca`  
**Documentation**: [Compute Canada: Cedar](https://docs.computecanada.ca/wiki/Cedar)

* Some tricks on how to use GPUs on Cedar: [Cedar Tricks](https://www.neuro.polymtl.ca/internal_resources/list_of_computers/cedartricks)
* [Graham and Cedar Announcement \(WestGrid News\)](https://www.westgrid.ca/westgrid_news/new_compute_canada_national_systems_now_available)

```{note}
**Example**: Run SCT on Cedar

256 CPUS  
1GB of memory per process  
default lab account \(def-jcohen\)  
slurm queueing system

```bash
#!/bin/bash
#SBATCH --account=def-jcohen
#SBATCH --ntasks=256            # number of MPI processes (1 for the main process and 255 for the workers)
#SBATCH --mem-per-cpu=1024M     # memory; default unit is megabytes
#SBATCH --time=0-03:00          # time (DD-HH:MM)
 
# cd to a scratch space where outputs will be saved
cd /scratch/$USER/workdir
 
DATA_PATH=</PATH/TO/SUBJECTS/DATA/>
 
</PATH/TO/SCT_PIPELINE> --nb-cup 255 -f sct_propseg -d </PATH/TO/BIG_DATASET>  -p  \"-i t2s/t2s.nii.gz  -c t2s\"    # run propseg on 255 workers
```

You can then submit the job with `sbatch`:

```bash
chmod 750 my_sct_script.sh # make sure the script is executable
sbatch my_sct_script.sh # submit the job
squeue -u $UID # check that the job is in the slurm queue
```

One can also do interactive testing with MPI. We recommend using this method to run SCT on a smaller scale. For example, here we run on 16 cores:

```bash
salloc --time=0-03:00 --ntasks=16 --mem-per-cpu=1024M  --account=def-jcohen
# [wait for cedar to give you a session, bigger are ntasks and mem-per-cpu, longer is that time]
```

Then run `sct_pipeline`. The 16 cores will be accessible via the MPI interface:

```bash
<PATH/TO/SCT>/bin/sct_pipeline -cpu-nb 16  -f sct_propseg -d /home/poq/small -p \" -i  t2s/t2s.nii.gz  -c t2s \"
```
```

### Colosse \(CQ/Laval\)

**Server**: `colosse.calculquebec.ca`  
**Documentation**: [https://wiki.calculquebec.ca/w/Colosse](https://wiki.calculquebec.ca/w/Colosse)

### Guillimin \(CQ/McGill\)

**Server**: `guillimin.clumeq.ca`  
**Documentation**: 

### Briaree \(CQ/UdeM\)

**Server**: `briaree.calculquebec.ca`

### Graham \(CC\)

**Server**: `graham.computecanada.ca`  
**Documentation**: [Compute Canada: Graham Server](https://docs.computecanada.ca/wiki/Graham)

[https://ccdb.computecanada.ca/resources/graham-compute](https://ccdb.computecanada.ca/resources/graham-compute)

To run the SCT on Graham, follow the same procedure as describe in the Cedar section.

### Mammoth \(CQ/Sherbrooke\)

**Server**: `jcohen-mp2.ccs.usherbrooke.ca`

### HELIOS \(Quebec, GPU\)

Make sure that the version you need has already been compiled:

```bash
ls /software/gpu/apps/python/wheelhouse/tensorflow-0.*
```

Load the required modules. For example:

```bash
module load compilers/gcc/4.8.5 cuda/7.5 libs/cuDNN/5
```

Load the correct Python module:

```text
module load apps/python/3.6.0
```

Create a virtual environment and activate it:

```bash
virtualenv <ENV_NAME>
source <ENV_NAME>/bin/activate
```

Install `tensorflow`. If you need a version other than the latest version, you can specify the version number.

```bash
pip install tensorflow==<VERSION_NUMBER>+helios
```

The addition of `+helios` after the version number isn't necessary, but it ensures that `pip` doesn't download a version from the internet, and instead uses the version you have compiled for Helios. 

Submitting a script \(use MOAB\):

```bash
(name@server) $ msub [options] script.pbs
```

## Cloud Account

There is the possibility to host processes on the cloud for public access. To do so, each PI needs to open a specific account to allocate cloud resource at: [Compute Canada: Cloud](https://docs.computecanada.ca/wiki/Cloud).

See: [https://github.com/spinalcordmri/spinalcordmri.github.io\#set-up-compute-canada-instance](https://github.com/spinalcordmri/spinalcordmri.github.io#set-up-compute-canada-instance)

