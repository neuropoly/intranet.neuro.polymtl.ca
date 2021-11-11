# Unix Shell \(bash\)



## Awesome links

* [Bash scripting cheatsheet](https://devhints.io/bash)

## HDD parameters

To list all block devices, run:

```text
lsblk
```

To list all partitions, run:

```text
 fdisk -l
```

### Linux Hard Disk Format Command

**Partition the new disk using fdisk command**

Fist list all partitions, run:

```text
 fdisk -l
```

To partition the disk – /dev/sda, enter:

```text
 fdisk /dev/sda  
```

Then select to create a new partition:

```text
 n
```

Select partition type:

```text
 p   
```

Set the desired partition number \(be careful not to overlap with previous partitions\) and the size.

At the end write the new partition table:

```text
 w   
```

**Format the new disk using mkfs.ext4 command**

To format Linux partitions using ext4fs on the new disk:

```text
 mkfs.ext4 /dev/sda1   
```

**Mount the new disk using mount command**

First create a mount point /mnt/extradisk1 and use mount command to mount /dev/sda1, enter:

```text
 mkdir /mnt/extradisk1
 mount /dev/sda1 /mnt/extradisk1
 df -H      
```

**Update /etc/fstab file**

Open /etc/fstab file, enter:

```text
 vi /etc/fstab
```

Append as follows:

```text
 /dev/sda1               /mnt/extradisk1           ext4    defaults        1 2
```



