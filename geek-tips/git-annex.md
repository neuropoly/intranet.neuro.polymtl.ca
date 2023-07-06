# git-annex

[`git annex`](https://git-annex.branchable.com/) is an extension to git that lets it handle large repos spread in pieces across multiple servers/disks/accounts.

We are using it because

1. We have datasets we need to trace but they are too large for plain git to handle them well
1. It is compatible with [`datalad`](https://datalad.org) which gaining popularity in the neuroimaging community

It has about a thousand variants and options. This covers only the parts we use.

`git-annex` brings with it all the power of `git`. You should be somewhat familiar with branches, tags,. Please read [the git book](https://git-scm.com/book/en/v2). The [datalad handbook](https://handbook.datalad.org/) also has useful perspective, though not all of it is relevant to how we do things.

## Installation

You must have a unix OS. `git-annex` is simply not compatible with anything else.

::::{tab-set}
:::{tab-item} Linux
* **Arch**: `pacman -Sy git-annex`
* **Fedora/RedHat/CentOS**: `dnf install git-annex`
* **Debian/Ubuntu**: `apt-get install git-annex`
* **[ComputeCanada](https://docs.computecanada.ca/)**, a supercomputer we have accounts on: `module load StdEnv/2020  && module load git-annex` *in [every session or batch job](https://docs.alliancecan.ca/wiki/Utiliser_des_modules/en#Loading_modules_automatically)*
* if on an older system and can't upgrade, you can try [installing `conda`](https://docs.conda.io/en/latest/miniconda.html) (or [miniforge](https://github.com/conda-forge/miniforge/#miniforge3) or [mambaforge](https://github.com/conda-forge/miniforge/#mambaforge)) and then using `conda install -f conda-forge git-annex` (or `mamba install -f conda-forge git-annex).
:::

:::{tab-item} macOS
```
brew install git-annex
```
:::

:::{tab-item} Windows 10 (via WSL)
Install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10), pick a distro, and then run one of:

* **[Ubuntu-20.04](https://www.microsoft.com/store/apps/9n6svws3rx71)**: `apt install git-annex`
* **[Debian](https://www.microsoft.com/store/apps/9MSVKQC78PK6)**: `apt install git-annex`
* The [other distros](https://docs.microsoft.com/en-us/windows/wsl/install-manual#downloading-distributions) are supported.
:::

:::{tab-item} Windows 10 (via VirtualBox)
Install [VirtualBox](https://virtualbox.org/), install a Linux distro inside of it, and then follow the Linux instructions.
:::
::::


````{warning}
Check that `git annex version` reports **version 8** or higher! It should look like:

```
$ git annex version
git-annex version: 8.20210310-ga343ea76c8
build flags: Assistant Webapp Pairing Inotify DBus DesktopNotify TorrentParser MagicMime Feeds Testsuite S3 WebDAV
dependency versions: aws-0.22 bloomfilter-2.0.1.0 cryptonite-0.28 DAV-1.3.4 feed-1.3.2.0 ghc-8.10.4 http-client-0.7.6 persistent-sqlite-2.11.1.0 torrent-10000.1.1 uuid-1.3.14 yesod-1.6.1.0
key/value backends: SHA256E SHA256 SHA512E SHA512 SHA224E SHA224 SHA384E SHA384 SHA3_256E SHA3_256 SHA3_512E SHA3_512 SHA3_224E SHA3_224 SHA3_384E SHA3_384 SKEIN256E SKEIN256 SKEIN512E SKEIN512 BLAKE2B256E BLAKE2B256 BLAKE2B512E BLAKE2B512 BLAKE2B160E BLAKE2B160 BLAKE2B224E BLAKE2B224 BLAKE2B384E BLAKE2B384 BLAKE2BP512E BLAKE2BP512 BLAKE2S256E BLAKE2S256 BLAKE2S160E BLAKE2S160 BLAKE2S224E BLAKE2S224 BLAKE2SP256E BLAKE2SP256 BLAKE2SP224E BLAKE2SP224 SHA1E SHA1 MD5E MD5 WORM URL X*
remote types: git gcrypt p2p S3 bup directory rsync web bittorrent webdav adb tahoe glacier ddar git-lfs httpalso borg hook external
operating system: linux x86_64
supported repository versions: 8
upgrade supported from repository versions: 0 1 2 3 4 5 6 7
```
````

### Global `git` config

For smooth operation, everyone should do on all of their machines:

```
git config --global push.default current
```

And specifically for `git-annex`:

```
git config --global annex.thin true # save disk space by de-duplicating checked out and annexed copies
git config --global annex.private true # prevent attempting to share your local copy of the annex, which is impossible when working in a team
```

See [below](#annexthin-hardlinks) to understand what this setting offers.

## New repo

There is a template repository on our [internal server](../data/git-datasets.md) at git+ssh://data.neuro.polymtl.ca/datasets/template.

The key is to ensure each filetype has a line added to `.gitattributes` like

```
echo '*.nii.gz      filter=annex annex.largefiles=anything' >> .gitattributes
```

If you are working on a private, internal dataset, you can use [this script](../data/git-datasets.md#new-repository).

## `annex.thin` Hardlinks <a id="hardlinks">

`annex.thin` saves a lot of space by deduplicating file content via [hard links](https://wiki.debian.org/ln):
the files your checkout `repo/` will be physically the same content as their sources in `repo/.git/annex/objects/`, instead of copies.

To confirm this is working, you can compare the size of the content with the annex.
They should be roughly the same size, **even though one is contained in the other**:

```
~/datasets/uk-biobank-processed$ du -hs uk-biobank-processed/
81G	uk-biobank-processed/
nguenther@data:~/datasets/uk-biobank-processed$ du -hs uk-biobank-processed/.git/annex/
81G	uk-biobank-processed/.git/annex/
```


You can confirm it another way by looking at the link count on a file, e.g.
 
```
$ stat derivatives/labels/sub-1140317/anat/sub-1140317_T1w_seg-manual.nii.gz
   File: derivatives/labels/sub-1140317/anat/sub-1140317_T1w_seg-manual.nii.gz
   Size: 28305     	Blocks: 56         IO Block: 4096   regular file
 Device: 802h/2050d	Inode: 1319996     Links: 2
 Access: (0644/-rw-r--r--)  Uid: ( 1001/zamboni)   Gid: ( 1001/zamboni)
 Access: 2021-06-28 17:19:15.321874946 -0400
 Modify: 2021-06-28 16:00:45.261893952 -0400
 Change: 2021-06-28 17:19:15.161873978 -0400
  Birth: 2021-06-28 16:00:45.261893952 -0400
```
> 
(macOS uses a different format for `stat(1)`, but all the same information is there)
 
This shows that the link count is 2, which should be the case for "thinly" annexed files (unless they are duplicated elsewhere in the dataset, in which case the link count could be 3, 4, or higher).

You can find where such a file is in the annex by searching for its inode number:

```
$ find . -inum 1319996
 ./derivatives/labels/sub-1140317/anat/sub-1140317_T1w_seg-manual.nii.gz
 ./.git/annex/objects/6V/X3/SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz/SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz
```


## Troubleshooting

### version problems

If you have any error at all, the first thing to check is that you have `git-annex` version 8, [as explained above](#installation).

### checking annex file locations

The content of annexed files that have been downloaded locally is stored under `repo/.git/annex/objects/`. You can find which specific file corresponds to by using `git show` or `git log -p` to see the content that `git` has recorded for the file -- which will be a string giving the "annex pointer":

```
$ git show HEAD:derivatives/labels/sub-1140317/anat/sub-1140317_T1w_seg-manual.nii.gz
/annex/objects/SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz
```

and then locating a file with this name in `.git/annex/objects/`; however, it is not as simple as just combining the two together, git-annex prepends extra filenames, so you need to use `find(1)` to locate the file:

```
$ find .git/annex/objects/ -name "SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz"
.git/annex/objects/6V/X3/SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz
.git/annex/objects/6V/X3/SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz/SHA256E-s28305--3f309650bbc2d5146d9e1d1e24c7b17ee82c9da2fb609030ee83f3c1f2d74acb.nii.gz
```

### "a cosmetic problem affecting git status"

Sometimes the `git-annex` filter will glitch, particularly during long uploads or downloads.
It will usually -- but not always -- give you a warning in these cases saying "a cosmetic problem affecting git status".
Despite the innocuous sounded warning, this glitch prevents git operating.
A symptom of this glitch is that `git status` reports many, many "modified" files that shouldn't be.

The fix is:

```
git status | sed -n 's/modified://p' | xargs git update-index -q --refresh
```

This doesn't touch file contents, so it should be safe to run anytime.


The issue is that git-annex v8 uses a filter to expand the small pointers committed to git to full files and vice versa, and if interrupted while doing its work, it can leave files with full annexed contents that do not match the annex pointers git is expecting to see. `update-index` gives git a kickstart to fix it.

### Resetting

`git-annex init` writes to a lot of places: the `git-annex` branch,
`.git/annex` (including several sqlite databases?), `.git`/config, 
and, sometimes, `.git/info/attributes`.

To get rid of it without getting rid of the 
complete repo, you can use

```
git annex uninit
```

To reset just the ID of the current copy, to make it appear like a fresh repo to `git annex whereis`:

```
git config --unset annex.uuid
#  then git annex init again? or what?
```

### `rm: cannot remove`

When trying to get rid of a git-annex dataset, you will run into, for example:

```
$ rm -rf data-single-subject/
[...]
rm: cannot remove 'data-single-subject/.git/annex/objects/mF/GV/SHA256E-s1082687--290a43b80da6f608e3d47107f3b6c05e98eebe56ed4eea633748c08bd1a7837a.nii.gz/SHA256E-s1082687--290a43b80da6f608e3d47107f3b6c05e98eebe56ed4eea633748c08bd1a7837a.nii.gz': Permission denied
rm: cannot remove 'data-single-subject/.git/annex/objects/Vq/vF/SHA256E-s15564390--7d3e45f0d4c67f31883b76eafc6cfdca1c1591590e2243dc8d443b07616b3609.nii.gz/SHA256E-s15564390--7d3e45f0d4c67f31883b76eafc6cfdca1c1591590e2243dc8d443b07616b3609.nii.gz': Permission denied
rm: cannot remove 'data-single-subject/.git/annex/objects/79/G6/SHA256E-s7183853--3262ac5d6c5f573720c5e508da47608bd9fa49d6cd4dd547f75046c1a2f0d5b6.nii.gz/SHA256E-s7183853--3262ac5d6c5f573720c5e508da47608bd9fa49d6cd4dd547f75046c1a2f0d5b6.nii.gz': Permission denied
```

This is because git-annex [tries extra hard](https://git-annex.branchable.com/internals/lockdown/) to make it hard to lose data, by marking its contents read-only. If you really intend to erase the dataset you need to open the permissions first with `chmod -R +w`, for example:
 
```
$ chmod -R +w data-single-subject/.git/annex/
$ rm -rf data-single-subject/
```
