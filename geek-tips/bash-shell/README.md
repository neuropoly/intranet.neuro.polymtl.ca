# Bash/Shell

```{toctree}
:hidden:
script
```

## Awesome links

* [Bash scripting cheatsheet](https://devhints.io/bash)

## HDD parameters

Check disk space:

```
df -h
```

To list all block devices, run:

```
lsblk
```

To list all partitions, run:

```
 fdisk -l
```

## File/Folders

### Copying

#### **Copy (and synchronize) with rsync**

```bash
rsync -azP <FILE_SRC> <FILE_DEST>
rsync -azP <FOLDER_SOURCE> <FOLDER_DEST>  # will create FOLDER_SOURCE inside FOLDER_DEST (if it does not exist), and will copy the content of FOLDER_SOURCE inside it
rsync -azP <FOLDER_SOURCE>/ <FOLDER_DEST>  # will copy the content of FOLDER_SOURCE inside FOLDER_DEST
# For nii.gz files, no need to further compress so -z can be dropped
```

#### **Copy from remote station via scp**

```bash
scp username@hostname:</PATH_TO_FILE>
```

### Finding

```bash
find . -name "dti*"
```

To be case-insensitive, use:
```bash
find . -iname "dti*"
```

To only look for folders/directories:
```bash
find . -type d -iname "dti*"
```

To only look for files:
```bash
find . -type f -iname "dti*.*"
```


### Deleting

#### **Delete non-empty folder**

```bash
rm -rf <FOLDER>
```

#### **Delete a bunch of files**

```bash
find . -name "dti*" -delete
```

or the more complicated version:

```bash
find . -name "dti*" | while read F; do rm $F; done
```

When you are trying to delete too many files using `rm`, you may get error message: `/bin/rm Argument list too long`. Use `xargs` to avoid this problem.

```bash
find ~ -name ‘*.log’ -print0 | xargs -0 rm -f
```

### Renaming

#### Rename files with a given extension

```bash
ls *.<EXT> | while read F; do mv $F <NEW_FILE_NAME>_$F; done
```

Do it recursively:

```bash
find . -name "t2_seg.nii.gz" -exec bash -c 'mv $(dirname $1)/$(basename $1) $(dirname $1)/t2_seg_manual.nii.gz' -- {} \;
```

**Do something on files modified for the past 10 days**

```bash
find . -type f -name '*.*' -mtime +10 -exec echo "do something on this file: {}" \;
```

**Set created/modification date on a file**

```bash
touch -mt YYYYMMDDhhmm <FILE>
```

On Maverick and later, the creation date is not updated if newer than the existing. So you should use:

```bash
SetFile -d 'DD/MM/YYYY HH:MM:SS' <FILE>
```

#### Size of a disk/folder <a href="size_of_a_diskfolder" id="size_of_a_diskfolder"></a>

```bash
du -sh <FOLDER>
```

or for all folders in the path

```
du -sh *
du -sm * | sort -nr  # in MB and reverse-ordered by size
```

**Get space on a disk**

```
df -h .
```



#### Number of files <a href="number_of_files" id="number_of_files"></a>

\== Get number of files that match a pattern

```
ls -dq *pattern* | wc -l
```

**Get number of files in a folder (recursively)**

```
find .//. ! -name . -print | grep -c //
```

only counts files modified for the past 24h:

```
find .//. ! -name . -mtime -1 -print | grep -c //
```

**List files modified for the past 24h**

```
find . -mtime -1 -print
```

List number of files per folder

```
find . -maxdepth 1 -mindepth 1 -type d -exec sh -c 'echo "{} : $(find "{}" -type f | wc -l)" file\(s\)' \;
```

### Permissions

#### **Change permissions**

```bash
chmod 644  # make a file readable by anyone and writable by the owner only.
chmod 755	 # make a file readable/executable by everyone and writable by the owner only.
chmod 701	 # r/w/x for the owner, no access for everyone
```

#### **Change owner of a file**

```bash
sudo chown <OWNER> <FILE>
```

#### **Look for group owner & permission**

```bash
ls -le@a
```

**Find most recently changed files (less than 1 day ago)**

```
find  -mtime -1 -ls
```

**Search files**

Files with specific string inside:

```
find . -name "string"
```

Files that have been modified for the past 24 hours:

```
find ~/Documents -type f -ctime -0 | more
```

#### Stdout / Stderr <a href="stdoutstderr" id="stdoutstderr"></a>

[https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file)Edit

## Compression/Extraction

### **tar**

compress:

```
tar -czf /path/to/output/folder/filename.tar.gz /path/to/folder
```

extract:

```
tar -zxvf filename.tar.gz
```

### **zip**

compress folder:

```
zip -r archive.zip folder/

# Exclude a sub-folder:
zip -r archive.zip folder/ -x '*subfoldertoexclude*'
```

extract:

```
unzip archive.zip
```

**copie de fichiers ds une directory**

find -name sica\*.png | xargs -t -i /bin/cp ./{} ./imagesEdit

#### Checksum <a href="checksum" id="checksum"></a>

This procedure creates a unique signature for your files and folders. It enables to check for integrity when you share data.


````{tabbed} Linux
```bash
find FOLDER -type f -exec md5sum {} \; | md5sum
```
````

````{tabbed} Mac
```bash
find -s FOLDER -type f -exec shasum {} \; | shasum
find -s FOLDER -type f -exec md5 {} \; | md5
```
````


#### Remove files from tmp <a href="remove_files_from_tmp" id="remove_files_from_tmp"></a>

```bash
find . -name "tmp.*" -type d -print0 | xargs -0 /bin/rm -rf
```

## .bash\_profile

The `.bash_profile` file is launched when you open a new terminal. You can configure your environment variables from there. It is located in your home folder (`$HOME`).

To load it:

```bash
source ~/.bash_profile
```

## Emails

**send email**

```bash
echo "something" | mailx -s "subject" someone@email.com
```

## Processes

### **Check Processes**

```bash
ps aux
```

```
top
```

### **Killing Processes**

#### **kill a process based on PID**

```bash
kill -9 <"PID">
```

#### **kill a process from a user**

```bash
pkill -U <USER> 
```

## Internet / Network

### Download file from internet

```bash
curl -o filename -L <URL>
# Example for OSF file (note the "?action=download" added after the URL):
curl -o data.zip -L https://osf.io/76jkx/?action=download
```

Alternatively:

```bash
wget -O data <URL>
```

### Copying

#### Copy file between computers

* [https://magic-wormhole.readthedocs.io/en/latest/](https://magic-wormhole.readthedocs.io/en/latest/)
* [https://clbin.com/](https://clbin.com) (featuring CLI uploading) ( running [http://github.com/rupa/sprunge](http://github.com/rupa/sprunge) )
* [https://paste.fossdaily.xyz/](https://paste.fossdaily.xyz) (running privatebin)
* [https://paste.tildeverse.org/](https://paste.tildeverse.org) (running privatebin)
* [https://bin.snopyta.org/](https://bin.snopyta.org) (running privatebin)
* [https://pb.envs.net/](https://pb.envs.net) (running privatebin)
* [https://sebsauvage.net/paste/](https://sebsauvage.net/paste/) (running zerobin; an unmaintained forerunner of privatebin)
* [https://0bin.net/](https://0bin.net) (running [https://github.com/sametmax/0bin](https://github.com/sametmax/0bin))
* [https://demo.lufi.io/](https://demo.lufi.io) (running [https://lufi.io](https://lufi.io))
* [https://ybits.io/](https://ybits.io) (closed source but oh well)
* [https://upload.disroot.org/](https://upload.disroot.org) (running [https://lufi.io/](https://lufi.io))
* [https://framadrop.org](https://framadrop.org) (running lufi.io)
* [https://ttm.sh/](https://ttm.sh) (featuring cli uploading) (edited)

Using gist.github.com (only for files <100MB):

```
1. make a new gist
2. note its ID in its URL (something like 3daa207ea45c75722bd0e3bc914dce3a)
3. `git clone git@github.com:3daa207ea45c75722bd0e3bc914dce3a`
4. `cd 3daa207ea45c75722bd0e3bc914dce3a`
5. add your large file;
6. `git add .; git commit; git push`
```

#### **Copy from a remote station**

```bash
scp username@station.domain: </PATH/FILE> . # copy file
scp username@station.domain: </PATH/> . -r # copy folder
```

### Network/DNS

**List all stations on the network (only works on a server)**

```
findsmb
```

**find DNS**

```
cat /etc/resolv.conf
```

**lookup DNS**

```
host HOST_NAME
host IP_ADDRESS
```

**Clear DNS cache (on OSX 10.8 and later)**

```
sudo killall -HUP mDNSResponder
```

**Connect to another station**

```
ssh IP
or:
ssh username@station.domain
```

## Screen (for background processes)

Let's say you connect to a station from your laptop and you wish to launch a script that will run for several hours. If you close your laptop, the remote script will stop. To prevent this, use `screen`. It opens a virtual environment from a remote station, so that any script launched within this environment will continue running even if you close your laptop.

Step-by-step procedure:

1. Connect to a station via `ssh`
2. Launch `screen`. It will create a new screen attached to the station.
3. Do whatever you want (e.g., launch a long process).

Detach from the screen:

```bash
screen -d
# or
CTRL+a d
```

Attach to a detached screen:

```bash
screen -r
```

Attach to a not detached screen. (Multi display mode).

```bash
screen -x
```

List of your screens

```bash
screen -ls
```

Kill a screen

```bash
screen -X kill  # (if you only have one screen running)
screen -X -S [session # you want to kill] kill
```

Give specific name to a screen session

```bash
screen -S <NAME_OF_SESSION>
```

## SSH Public Key

Create key on the client (do this only once):

```bash
ssh-keygen -t rsa
```

Copy key on server:

```bash
ssh-copy-id demo@198.51.100.0
```

## VIM Text Editor

Simple but great editor. Usually installed everywhere.

> :w = save\
> :q = quit\
> :wq = quit and save

Coloured syntax:

```bash
vi ~/.vimrc
add: syntax on
```

