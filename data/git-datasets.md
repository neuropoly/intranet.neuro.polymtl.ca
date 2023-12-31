# `data`

This server includes private MRI and microscopy datasets, which have been curated and organized according to the [BIDS](https://bids.neuroimaging.io/) convention.

`git+ssh://data.neuro.polymtl.ca` has a max size of ~1TB.

It hosts [BIDS](https://bids-specification.readthedocs.io) datasets, version-controlled using [`git-annex`](https://git-annex.branchable.com/).
It is locked behind a [VPN](../computing-resources/neuropoly/README.md#vpn) because much of our data is under medical ethics protections, and needs to be kept off the general internet.


Initial setup
-------------

### Prerequisites

0. You must have a \*nix OS with `git-annex>=8` installed. See [`git-annex` installation](../geek-tips/git-annex.md#installation).
2. Make sure you have an ssh key.
    * If not, run `ssh-keygen -t ed25519 -C your.name@polymtl.ca`. Your keys will be in the hidden folder `~/.ssh/`.

### Getting an account

```{note}
If you already have an account on a server and/or laptop, and you want to have access from a new machine, see the section on [adding extra devices](#add-extra-devices) instead.
```

If not already done, reopen your [onboarding ticket](https://github.com/neuropoly/onboarding/issues/) to request to be added to the git-annex by providing the contents of your **public key** (examples: `~/.ssh/id_rsa.pub`, `~/.ssh/id_ed25519.pub`).

A **public key** should look like

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDE+b5vj+WvS5l6j56NF/leMpC2xT7JUCMUWDAqvWoVmNZ7UR3dGXQeTPTlmPmxPGD2Hk9/zFzxO2kYOt9o4lHQ0QQSKLUmTyuieyJE26wL1ZiLilmTgvgMxxkxvInF/Vr78V5Ll72zAmXzUxVSvuDGY2GRjnLreYheiqg1F3xTuD68uWInX8ZwA7NDtKpoZ7Aat063vD79WBrtiCfvAMbM8QhC3294zxqAjjy9fxs+TMTqAxtKdaWCA/eCs7sx9uvtFcj2Q9jxCMB3br5HyPLotgJMoIMt+fywj+vQG907LODRcqm9J0+ih+38/3Y6aqECMkHA9WWIfFywwjeA7EGr your.name@polymtl.ca
```

or

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJwsjlem+acuTOZGyNQKjyI7kJe9ULkhZo7N04QfC/tA your.name@polymtl.ca
```

Current **server admins** are:

* mathieu.guay-paquet@polymtl.ca
* mathieu.boudreau@polymtl.ca
* nathan.gorvett@polymtl.ca
* nick.guenther@polymtl.ca
* joshua.newton@polymtl.ca
* jcohen@polymtl.ca
* eva.alonso-ortiz@polymtl.ca

The admins should follow [Admin Guide > Add Users](#add-users) to create your account.

### Connecting to `data.neuro.polymtl.ca`

Because this server contains private medical data, you need to be on campus, connected to the VPN, or working from a server on campus, like `joplin` or `rosenberg` to access it.

*If connecting from off-campus*, connect to [polyvpn](http://www.polymtl.ca/si/reseaux/acces-securise-rvp-ou-vpn).

> 🏚️ Verify connectivity by running `ping data.neuro.polymtl.ca`. If **you cannot ping** then you need to double-check your VPN connection; make sure it is connected, make sure you can reach `joplin`, and if it still isn't working *ask the [Poly network admins](mailto:dge.informatique@polymtl.ca)* to unblock your account from this server.

Verify you can use the server by running `ssh git@data.neuro.polymtl.ca help`. If it hangs, triple-check again your VPN. If it asks for `git@data.neuro.polymtl.ca's password`, double-check that `ls -la ~/.ssh` shows permissions of `drwx------` for the `.` folder, and that the files `id_ed25519` and `id_ed25519.pub` (or `id_rsa` and `id_rsa.pub`) exist with exactly those names. A successful connection looks like:

```
$ ssh git@data.neuro.polymtl.ca help
Enter passphrase for key '/home/kousu/.ssh/id_ed25519.neuropoly': 
hello yourusername, this is git@data running gitolite3 3.6.11-2 (Debian) on git 2.27.0

list of remote commands available:

	D
	create
	desc
	git-annex-shell
	help
	info
	keys
	perms
	readme
	writable
```

Usage
-----

During daily usage, you will need to be [*on the polyvpn network*](../computing-resources/neuropoly/README.md#vpn) to access the server.

You should also make sure to [configure git annex](../geek-tips/git-annex.md#global-git-config) for the best performance.

### List

To see what datasets you have available, use `info`, for example:

```
ssh git@data.neuro.polymtl.ca info
```

And the output would look like this:
```
hello yourusername, this is git@data running gitolite3 3.6.11-2 (Debian) on git 2.27.0
 R      datasets/..*
 R      datasets/basel-mp2rage
 R W    datasets/bavaria-quebec-spine-ms
...
```

You are identified to the server by your ssh keys, but notice that this tells you the username you are known as.

### Download

To download an existing repository use `git clone`:

```
git clone git@data.neuro.polymtl.ca:datasets/<dataset_name> 	# download folders and metadata
cd <dataset_name>
```

After running `git clone git@data.neuro.polymtl.ca:datasets/<dataset_name>`, only metadata and small-size files such as `.json` sidecars are cloned (downloaded). In other words, you can access the content of the `.json` sidecars but can not open image `.nii` files.

To download all image `.nii` files, run:

```
git annex get . 						# download images
```

If you just want to explore, you can opt for a portion of the image `.nii` files by specifying paths instead of the last step, for example:

```
git annex get sub-karo*                                        	# download images under any of sub-karo*/*
```

> **Note**: If you want to download images together with corresponding derivatives files for a specific subject(s), use: 

```
git annex get {./,derivatives/**/}sub-karo*                       # download images and derivatives for sub-karo* subjects
```

### Update

If you have already cloned a repository and you would like to get its latest version, do:

```
git pull && git annex sync --no-content && git annex get .
```

### Upload

Despite not being hosted on Github, we are still using a [pull-request workflow](https://guides.github.com/introduction/flow/).
So, to make changes to a dataset, first ask an admin to [grant you upload rights](#permissions), then make a working branch for your changes. If your initials are `xy` and you are working on `some-topic`:

```{note}
If you are uploading data to a dataset for the first time, run `git annex dead here` to configure your local clone of the repository.
```

```
git checkout -b xy/some-topic master
# Edit your files, add new ones, etc. 
# Add all modified files to be commited
git add .
# To add specific files, do: git add path/to/new/file
# Commit and write a useful commit message
git commit
```

The *first* time before uploading, verify you have access with `info`. You need "W" (for "Write") permission, like this:

```
ssh git@data.neuro.polymtl.ca info datasets/uk-biobank
```

The output would look like:
```
hello yourusername, this is git@data running gitolite3 3.6.11-2 (Debian) on git 2.27.0

 R W    datasets/uk-biobank
```

Once you have access you should:

```
git annex copy --all --to=origin
git annex sync --no-content --only-annex
git push
```

Finally, ask one of that dataset's reviewers to [look at your pull request](#reviewing-pull-requests) by **opening an issue** (not creating a new pull request) on [neuropoly/data-management](https://github.com/neuropoly/data-management). The details of your pull request (i.e. the changes made to the dataset) must be explained in the issue along with name of your branch on which the changes can be found. 

```{note}
You do not have to open an issue if your change is small, such as updating a single image. Instead, describe your change in the commit message and ask one of that dataset's reviewers by Slack.
```

If you are uploading changes gradually, you can reuse the same branch:

```
# First, update your local master branch:
git checkout master
git pull && git annex sync --no-content

# Then, bring your branch up to include the recent changes:
git checkout branch_you_are_reusing
git merge --ff-only master
git pull && git annex sync --no-content

# Then, modify a file and make a new commit:
git add .
git commit
git push origin branch_you_are_reusing
```

### Reviewing Pull Requests

If someone asks you to review their changes on branch `xy/some-topic`:

```
git fetch
git checkout xy/some-topic
git annex get .
```

Then look at the branch to see if it looks right to you.

To investigate what changed:

```
# list changed files
git diff --name-only master..HEAD
# list changed files (each commit)
git log --stat master..HEAD
# to see content, overall
git diff master..HEAD
# to see content, commit-by-commit
git log -p master..HEAD
```

Also, it's a good idea to run:

```
git annex whereis
```

To check that all the annexed files have been uploaded.


> 🏚️ `git-annex` is not well-suited to a pull-request flow. It is mostly designed for a single person to share data among many computers, not for multiple people to share data between a few computers. We can make it work but it needs some patience. Have a cat to make it better: 🐈🌺


#### Commit Rights


Each repo has its own [`OWNERS` group](#permissions) attached. These are the people allowed to commit to `master`, and usually they should be the [reviewers](#reviewing-pull-requests) as well.

In order to join this group, someone already in it needs to grant you access:

```
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo + OWNERS yourusername
```

You can check if you have commit rights to a dataset "my-new-repo" by seeing if you appear in the group:

```
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo -l | grep OWNERS
```

#### Committing

Once a branch is finalized:

```
git checkout master
git merge --ff-only xy/some-topic
# or use git pull --squash xy/some-topic
git push
# no need for git-annex sync here, no annex files have been moved
```

(Optional) Clean up the branch:

```
git branch -d xy/some-topic
# redundancy
git branch -d synced/xy/some-topic
git push origin :xy/some-topic
git push origin :synced/xy/some-topic
```


### New repository

```{note}
Only NeuroPoly admnistrators have the needed privileges to create a new repository. Please contact the admins on the [#database_mri](https://app.slack.com/client/T034UD4QN/CB232HT46) Slack channel for assistance; they'll create a new empty repository for you and grant you write privileges so that you can add your dataset in a git branch and open a [pull-request](#upload).
```

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

### Releases

To make a release, use an [annotated git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging#_annotated_tags). Use the tag name for the name of the release, and the annotation for the release notes. Our naming convention for datasets is "rYYYYMMDD".

For example, if today is September 8th, 2019, then to create a release do:

```
git tag -a r20190908
```

To view available releases, first [download](#download) a dataset, then run

```
git tag -l
```

To see the release notes for a specific release, use

```
git show r20190908
```

To use a specific release, either [download](#download) the dataset and then

```
git checkout r20190908
```

*or*, for example in a reproducible processing script, you can use `clone -b` to download only that specific release:

```
git clone --depth 1 -b r20190908 git@data.neuro.polymtl.ca:datasets/example.git
```

### Permissions

You can grant others permissions to your repositories with `perms`.

```
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo + WRITERS someone # grant someone upload rights
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo - WRITERS someone # revoke someone's upload rights
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo + OWNERS researcher2 # grant someone rights to add (and remove) others and to merge to master
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo -l # view users
ssh git@data.neuro.polymtl.ca perms datasets/my-new-repo -lr # view access rules
```

Use

```
ssh git@data.neuro.polymtl.ca perms -h
```

and see https://gitolite.com/gitolite/user#setget-additional-permissions-for-repos-you-created for full details.


### Renaming

There is no way for a user to rename a repo directly ([bug report](https://github.com/neuropoly/data-management/issues/83)).
You can [ask an admin to do it](#renaming-1).

### Deletion

If you created or own a repo and decide it is no longer necessary:

```
ssh git@data.neuro.polymtl.ca D trash repo
```

The "trash" is cleaned out after a week. *Except it's not, yet: https://github.com/neuropoly/data-management/issues/54*

#### Deleting a branch

If you no longer are working on a specific, make sure that it is deleted (in order to save space and avoid maintaining unnecessary commit history). The relevant commands can be found under _Clean up a branch_ [here](#committing).


### Add extra devices

Like with Github, you can authorize any number of secondary devices. Assuming you already have authorization on `romane` and want to authorize yourself on `joplin`, here is the procedure: 

* Log on to `joplin` and create a new ssh key with `ssh-keygen`. Once this is done, the public part of the new ssh key can be found in the file `~/.ssh/id_*.pub`. 
* In a new terminal, log on to `romane` and run `ssh git@data.neuro.polymtl.ca keys add <yourusername>@joplin`. This asks for the public part of the new ssh key created on `joplin`. Copy-paste the contents of the file and press Enter!

Note: you can check your `<yourusername>` by running `ssh git@data.neuro.polymtl.ca info`.

Once added, you should be able to see the newly added key by running:

```
ssh git@data.neuro.polymtl.ca keys list
```

Admin Guide
-----------

We are using [`Gitolite`](https://gitolite.com/) with [`git-annex`](https://git-annex.branchable.com/) as our dataset server.
It is compatible with [`datalad`](https://www.datalad.org/) but to reduce the fragility we only support the basics.

Datasets are stored as git repositories on the server, with the bulk of their data *also* stored on the server in each repo's "annex" folder. Using `git-annex` enables data on-demand -- in our default configuration, only the data needed for the active branch is actually downloaded by a user, and it is also possible for the user to choose specific folders to focus on. Datasets are `git-annex` [ssh remotes](https://git-annex.branchable.com/walkthrough/#index11h2).

`gitolite` manages users and their permissions. The repositories containing datasets are under `data.neuro.polymtl.ca:datasets/*`, and the server also contains a few admin-only repositories outside of `datasets/*`.

The VM is monitored [here](https://monitor.neuro.polymtl.ca/host/data.neuro.polymtl.ca/#menu_system_submenu_cpu;after=0;before=0;theme=slate;help=true;utc=America/Toronto) (requires VPN to connect to the dashboard monitor).


### List users

```
ssh git@data.neuro.polymtl.ca keys list
```

### Add users

To grant access to a lab member, [as above](#add-extra-devices), ask the lab member to generate an ssh key using `ssh-keygen` and have them send you the *public key*. Save it to a file `firstnamelastname.pub` and add them with

```
cat firstnamelastname.pub | ssh git@data.neuro.polymtl.ca keys add firstnamelastname
```

You can also paste the key in, followed by `ctrl-d`; this looks like:

```
ssh git@data.neuro.polymtl.ca keys add firstnamelastname
```

The output looks like:
```
Enter passphrase for key '/home/kousu/.ssh/id_rsa.github': 
please supply the new key on STDIN (e.g. cat you.pub | ssh gitolite@git.example.com keys add @laptop).
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAID11N3hQpJP4Okivd5xO3N0CuO24ioMwXYv+l/1PM/+z firstname.lastname@polymtl.ca
Added SHA256:hwil2tmaw/prgIBX5odO8vOAj2i38gPrUGjGZnnkVvo : firstnamelastname.pub
```

You should use the person's full name as their username, in the form `firstnamelastname`, with no spaces or periods or anything. It's essentially an arbitrary string that the user doesn't really need to know, since everyone is authenticated using just their public/private keys without supplying a username. The only time users see them is when they run `info` or use `perms`. We would **like** to use the format firstname.lastname@polymtl.ca, but [there is a bug](https://github.com/kousu/gitolite-mods/issues/3), so just use `firstnamelastname`. Once someone is registered they can add and remove their own keys without having to know their username.


### Permissions

As admin, you can add or revoke any permissions to any repo [using `perms`](#permissions).

There is unfortunately no way to view permissions *as another user* so you will need to rely on people sending you screenshots if they are having problems
but you can at least inspect the active sets of permissions on a repo with

```
ssh git@data.neuro.polymtl.ca perms <repo> -l
```

If you need to add new namespaces or finer grained permissions, first, reconsider if the extra complexity and the _risk of locking yourself out_ is worth it. Everything you should need to manage the lab should be doable via `ssh git@data.neuro.polymtl.ca help`. If you are sure, then review [gitolite's permissions model](https://gitolite.com/gitolite/conf.html) and [official docs for this use case](https://gitolite.com/gitolite/fool_proof_setup.html#administration-tasks), then:

```
git clone git@data.neuro.polymtl.ca:gitolite-admin
cd gitolite-admin
vi conf/gitolite.conf  # optional: investigate/change the repo definitions
ls -R keydir/          # optional: investigate/change who has access; this *should* be unnecessary, use `keys` as above instead.
git add -u . && git push
```

### Renaming

As an admin, you can rename a repo by connecting to the server directly:

```
ssh root@data.neuro.polymtl.ca
sudo -u git -i
cd repositories/datasets/
mv $dataset.git $new_name.git
```

### Deletion

You can also delete any repo [using `D`](#deletion).

You can also get rid of a dataset immediately by:

```
ssh git@data.neuro.polymtl.ca D unlock datasets/<dataset>
ssh git@data.neuro.polymtl.ca D rm datasets/<dataset>
```

### Backups

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

#### Recovery Shortcut

If you are in a pinch, _and the server is still running_, you can use its credentials instead of loading your own.

```
ssh root@data.neuro.polymtl.ca
su -l git -s /bin/bash
set -a && . .config/restic/s3
mkdir -p backups
restic mount backups &
# datasets are now in backups/snapshots/*/repositories/datasets/
```


	
### Troubleshooting

If you are having a problem, please open an issue [here](https://github.com/neuropoly/data-management/issues). Please don't be shy, if you don't report the issue, we won't know about it and it will never be solved 😉 

If the server is doing something strange, contact someone with sysadmin-access to the server.

These people can investigate by following the gitolote guide in the [sysadmin docs](https://github.com/neuropoly/management/blob/master/docs/gitolite.md).

### References

* Patel, Hiren - [Wildrepos in Gitolite](https://caesr.uwaterloo.ca/wildrepos-in-gitolite/) -- detailing how a research lab manages their code and publications collaboratively through `gitolite`
