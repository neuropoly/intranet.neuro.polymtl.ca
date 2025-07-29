# Admin guide for `data.neuro.polymtl.ca`

```{warning}
This needs updating following the Gitolite -> Gitea migration. See https://github.com/neuropoly/computers/issues/457.
What appears below is mostly leftover documentation that still needs to be rewritten.
```

## New repository

To make a new repo, follow this [recipe](../geek-tips/git-annex.md#new-repo).

Then, to upload it, pick a name under `datasets/`, e.g. "my-new-repo", and do

```
git remote add origin git@data.neuro.polymtl.ca:datasets/my-new-repo
git branch -M master
# initialize remote and upload metadata
git push -u origin master
# initialize remote annex
git annex sync -a --no-content
# upload images to remote annex
git annex copy --to origin
# verify your .nii.gz files were annexed and uploaded
git annex whereis
```

## Releases

To make a release, use an [annotated git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging#_annotated_tags). Use the tag name for the name of the release, and the annotation for the release notes. Our naming convention for datasets is "rYYYYMMDD".

*or*, for example in a reproducible processing script, you can use `clone -b` to download only that specific release:

```
git clone --depth 1 -b r20190908 git@data.neuro.polymtl.ca:datasets/example.git
```

We are using [`Gitolite`](https://gitolite.com/) with [`git-annex`](https://git-annex.branchable.com/) as our dataset server.
It is compatible with [`datalad`](https://www.datalad.org/) but to reduce the fragility we only support the basics.

Datasets are stored as git repositories on the server, with the bulk of their data *also* stored on the server in each repo's "annex" folder. Using `git-annex` enables data on-demand -- in our default configuration, only the data needed for the active branch is actually downloaded by a user, and it is also possible for the user to choose specific folders to focus on. Datasets are `git-annex` [ssh remotes](https://git-annex.branchable.com/walkthrough/#index11h2).

The VM is monitored [here](https://monitor.neuro.polymtl.ca/host/data.neuro.polymtl.ca/#menu_system_submenu_cpu;after=0;before=0;theme=slate;help=true;utc=America/Toronto) (requires VPN to connect to the dashboard monitor).

## Backups

Encrypted backups are sent daily to `s3+https://s3.ca-central-1.amazonaws.com/data.neuro.polymtl.ca.restic` and `sftp://narval.computecanada.ca:projects/def-jcohen/data.neuro.polymtl.ca.restic`. Daily backups are retained for the current week, weekly for the current month, and monthly for the current year. 

We use a backup tool called `restic` and to recover files you should [review its full recovery documentation](https://restic.readthedocs.io/en/stable/050_restore.html) to use it safely, but the quick version is that you need to provide backup credentials, one set for either location. **It is your responsibility as a data server admin** to ensure you have generated and can protect these credentials.

```
# AWS
export RESTIC_REPOSITORY=s3:s3.ca-central-1.amazonaws.com/data.neuro.polymtl.ca.restic
export RESTIC_PASSWORD="...."
export AWS_ACCESS_KEY_ID="...."
export AWS_SECRET_ACCESS_KEY="....."
```

```
# ComputeCanada
export RESTIC_REPOSITORY=sftp:narval.computecanada.ca:projects/def-jcohen/data.neuro.polymtl.ca.restic
export RESTIC_PASSWORD="...."
# you also implicitly need an account that can `ssh narval.computecanada.ca`
```

Once credentialed, the easiest way to recover files is `restic mount`:

```
mkdir data-backups
restic mount backups &
# datasets are now in backups/snapshots/*/repositories/datasets/
ls -l backups/snapshots/latest/repositories/datasets/
```

Then you can use `git clone` or `rsync` to recover specific old files/git objects/commits/etc

<details><summary>For example</summary>

You can examine any old version of any git repo

```
git@data:~$ cd backups/snapshots/2022-06-30T02\:00\:02-04\:00/repositories/datasets/uk-biobank.git/; git log HEAD~3..
commit 96bdd193d0da999895734a57f8bbfa275db91ad1 (HEAD -> master)
Author: Alexandru Foias <alexandrufoias@gmail.com>
Date:   Fri Feb 12 15:24:04 2021 -0500

    Add 650 subjects

commit 3d55fe9a3b6f04f5a6bd1b50274108de1810fcc8
Author: Nick Guenther <nick.guenther@polymtl.ca>
Date:   Thu Feb 11 12:37:26 2021 -0500

    bids-validator: missing }

commit 892c030faef331591048f8b6487dd65f74afbea7
Author: Nick Guenther <nick.guenther@polymtl.ca>
Date:   Thu Feb 11 12:36:32 2021 -0500

    bids-validator: README should be named just 'README'
```

</details>

## Recovery Shortcut

If you are in a pinch, _and the server is still running_, you can use its credentials instead of loading your own.

```
ssh root@data.neuro.polymtl.ca
su -l git -s /bin/bash
set -a && . .config/restic/s3
mkdir -p backups
restic mount backups &
# datasets are now in backups/snapshots/*/repositories/datasets/
```

## Troubleshooting

If you are having a problem, please open an issue [here](https://github.com/neuropoly/data-management/issues). Please don't be shy, if you don't report the issue, we won't know about it and it will never be solved 😉 

If the server is doing something strange, contact someone with sysadmin-access to the server.

These people can investigate by following the gitolote guide in the [sysadmin docs](https://github.com/neuropoly/management/blob/master/docs/gitolite.md).
