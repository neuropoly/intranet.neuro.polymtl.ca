# git & Github

## Tutorials / courses

**EVERYONE WORKING WITH GIT AT NEUROPOLY LAB: PLEASE TAKE 2+ HOURS OF YOUR TIME AND LEARN HOW TO USE GIT BEFORE ACTUALLY USING IT.**

* [git official documentation](https://git-scm.com/book/en/v2)
* TUTORIAL: 
  * [Learn By Doing](https://githowto.com)
  *   \[Coursera: Introduction to

      git/github]\([https://www.coursera.org/learn/introduction-git-github](https://www.coursera.org/learn/introduction-git-github))
  * [Github's Learn By Doing](https://try.github.io)
  * [sr.ht's Learn By Doing](https://git-send-email.io)
  *   \[Ramp up on Git and GitHub (Github

      Lab)]\([https://lab.github.com/githubtraining/ramp-up-on-git-and-github](https://lab.github.com/githubtraining/ramp-up-on-git-and-github))
  *   \[Managing merge conflicts (Github

      Lab)]\([https://lab.github.com/githubtraining/managing-merge-conflicts](https://lab.github.com/githubtraining/managing-merge-conflicts))
  * [http://www.atlassian.com/git](http://www.atlassian.com/git)
*   \[A guide to managing git mistakes by

    @jvns]\([https://wizardzines.com/zines/oh-shit-git/](https://wizardzines.com/zines/oh-shit-git/))
*   \[Excellent notes from Matthew

    Brett]\([https://matthew-brett.github.io/curious-git/index.html](https://matthew-brett.github.io/curious-git/index.html))
*   \[Another great tutorial from Elizabeth

    DuPre]\([http://emdupre.github.io/git-course/](http://emdupre.github.io/git-course/)), and a video

    [here](https://neurohackademy.org/course/collaborating-with-git-and-github/)
*
* Excellent infos here: [https://gist.github.com/hofmannsven/6814451](https://gist.github.com/hofmannsven/6814451)
*   \[git - the simple guide (Roger

    Dudler)]\([https://rogerdudler.github.io/git-guide/](https://rogerdudler.github.io/git-guide/))
*   Snapshot of all commands:

    [http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf](http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf)

## Install git

If you're running from Docker:

```
sudo apt-get update
apt-get install git-all
```

## Contribute to a project

Basic steps are:

1. Fork the repository
2. Create a branch
3. Create new features while updating your branch from the Master 
4. Submit a pull request

### Fork the repository

1. Log in to your Github account
2.  Fork the project repository: click on the

    `Fork` button near the top of the page.

    This creates a copy of the code under your account on the GitHub

    server.
3.  In a Terminal window, go to the folder where you want to copy

    locally the code.
4. Clone the copy of the code to your local disk:

```
  git clone git@github.com:your_login/project_name.git
```

N.B. If you get the following error message, [create a SSH key](http://www.neuro.polymtl.ca/doku.php?id=tips_and_tricks:git#github):

```
  Warning: Permanently added the RSA host key for IP address 'XX.XX.XX.XX' to the list of known hosts.
  Permission denied (publickey).
  fatal: Could not read from remote repository.
  Please make sure you have the correct access rights
  and the repository exists."
```

### Maintain your branch up-to-date

Once the clone is complete your repo will have a remote named `origin` that points to your fork on GitHub. Don't let the name confuse you, this does not point to the original repo you forked from. To help you keep track of that repo you need to add another remote named `upstream`:

* open a terminal, go to your repos and type:

```
  git remote add upstream git://github.com/neuropoly/spinalcordtoolbox.git
  git fetch upstream
```

* Then (like `git pull` which is fetch + merge):

```
  git merge upstream/master master
```

*   Or if you want, replace your local work on top of the fetched branch

    (like a `git pull --rebase`)

```
  git rebase upstream/master
```

The `--rebase` option can be used to ensure a linear history by preventing unnecessary merge commits. Many developers prefer rebasing over merging, since it's like saying, "I want to put my changes on top of what everybody else has done."

### Send a pull request

* In a Terminal window, go to your git repository and type:

```
  git push origin <name of the feature you want to add to the project>
```

* Log in to your Github account and go to your branch.
*   Click on "Pull request". You will be sent to a page asking you to

    describe your modifications; you can give any title you want to your

    modfications (it doesn't need to be the name of your branch).
* Click on "Create a pull request".

Now you need to wait that the person in charge of the project accepts your modifications; if this person finds problems in your code, you can still push new changes to your code and they will be added to your pull request.

### How to `merge` specific files from another branch

The tool to use is `git checkout`:

```
  git checkout source_branch <paths>...
```

You simply need to give `git checkout` the name of the feature branch and the paths to the specific files that we want to add to your `master` branch as follows:

```
  $ git branch
  * master
    your_branch

  $ git checkout your_branch <path_to_file_1> <path_to_file_2>...

  $ git status
  # On branch master
  # Changes to be committed:
  #   (use "git reset HEAD <file>..." to unstage)
  #
  #   new file:   <path_to_file_1>
  #   new file:   <path_to_file_2>
  #   ...
  
  $ git commit -m "explanation of the commit you are doing"
```

See the page [git tip how to merge specific files from another branch](http://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/) for more details.

It is not possible to do this on SourceTree yet but an issue was opened on July 17th 2013 and is not closed yet. See [the issue here](https://jira.atlassian.com/browse/SRCTREEWIN-827?jql=text%20\~%20%22merge%20specific%20files%22%20AND%20created%20%3E%3D%202013-07-17%20AND%20created%20%3C%3D%202013-07-18).

See also the interesting page [Smart branching with sourcetree and git flow](http://blog.sourcetreeapp.com/2012/08/01/smart-branching-with-sourcetree-and-git-flow/) about using Git flow to set the right strategy to gang up to contribute to your project.

## Branches

### List remote branches

```
  git remote show origin
```

### Track remote branch

```
  git remote update
  git fetch
```

### Checkout existing branch

```
  git checkout <branch_name>
```

If branch is not tracked (use `git remote show origin` to check if branch is listed), then use:

```
  git fetch
```

If you still don't see the branch listed, maybe your local git repository does not allow to fetch all branches on `master`. This happens if you `clone` with `--depth=X`. To check if this is the case, run:

```
  git config --get remote.origin.fetch
```

If result is not `+refs/heads/\*:refs/remotes/origin/\*`, then update the `remote.origin.fetch` variable using:

```
  git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
```

Then, fetch:

```
  git fetch
```

Now, all tracked branches should appear when running:

```
  git remote show origin
```

### Checkout branch from fork

When reviewing a PR, instead of creating a branch locally we recommend using the following approach:

```bash
git remote add username git@github.com:username/repository_name.git
git fetch username
# If you want to temporarily check out the fork's branch in a detached HEAD state:
git checkout username/branch-name
# If you want to create a new local branch that tracks the fork's branch:
git checkout -b branch-name username/branch-name
```

### Clone specific branch

```
git clone -b <branch> <remote_repo> --depth 1
```

### Create a branch

```
  git checkout -b <branch_name>
```

### Push to remote

```
git push -u
git push -u origin <branch_name>  # push to specific branch
```

### Remove a branch

To remove a local branch

```
  git branch -d <branch_name>
```

To remove a remote branch (if you know what you are doing!)

```
  git push origin :<branch_name>
```

## General usage

### Upload local repository for the first time

First, create repository in github or bitbucket. Then, open a Terminal and run:

```
cd /path/to/your/project
git init  # initialize local git repos
git remote add origin https://USERNAME@URL_TO_REPOSITORY.git  # link to remote repos
git add .  # add every file under folder
git commit -m 'First commit'
git push -u origin master
```

### Switch local repository to another branch

on Sourcetree:

```
Checkout > Checkout New Branch
```

on Terminal:

```
git checkout NAME_BRANCH
```

### Check which branch you are currently working on

```
git branch
```

### Create repository inside repository

Use submodules:

1. [http://git-scm.com/book/en/Git-Tools-Submodules](http://git-scm.com/book/en/Git-Tools-Submodules)
2. [http://www.arlocarreon.com/blog/git/git-repo-inside-a-git-repo/](http://www.arlocarreon.com/blog/git/git-repo-inside-a-git-repo/)

## HOW TO

### Configure git

Before starting: configure git to identify you for each commit

Define the author name to be used for all commits by the current user.

```
git config --global user.name <name>
```

Define the author email to be used for all commits by the current user.

```
git config --global alias.<alias-name> <git-command>
```

more info: [http://www.atlassian.com/git/tutorial/git-basics#!config](http://www.atlassian.com/git/tutorial/git-basics#!config)

### Show changed files between two commits

```
git diff --name-only SHA1 SHA2
```

GIT - repository solution

gitk -> cool stuf

Doc: [http://gitref.org/basic/](http://gitref.org/basic/)

Download: [http://git-scm.com/download](http://git-scm.com/download)

Create a repository

Create folder:

```
mkdir my_repos.git
```

Go there:

```
cd my_repos.git
```

Copy repository to your station

```
git clone path_to_my_repos/my_repos.git
```

Rename directory

```
mv my_repos.git working_dir
```

N.B. Now you can copy/modif files in your working_dir

Commit changes locally

Add the files you want to your commit list, e.g.:

```
git add *.m
```

To add all modified (or deleted) files automatically, use:

```
git add -u
```

Commit the files

```
git commit -m 'enter description here'
```

N.B. You have to configure the commit params (do only once):

```
git config --global user.name 'Your Name'
git config --global user.email you@somedomain.com
```

Cancel a `git add`

```
git reset <file_name>
```

Look at the status of the files (tracked? Modified? Added?)

```
git status -s
```

Update changes to your repos

```
git push path_to_my_repos/my_repos.git master
```

example:

```
git push jcohen@door.nmr.mgh.harvard.edu:/autofs/cluster/connectome/git/process_data.git master
```

or:

```
git push -u origin master
```

Download changes from your repos

```
git pull
```

Removed tracked files

```
git rm "file name"
```

### Download

Download (server -> local station) a repository for the first time

get address of repos, and type

```
git clone git@bitbucket.org:neuropoly/spinalcordtoolbox_dev.git
```

### Reset your branch (revert your local commits)

Using the Terminal:

```
git fetch
git reset --hard origin/master
```

Moving the current branch backward by N commits:

```
git reset --hard HEAD~N
```

Warning: This comment effectively removes the N snapshots created from the project history. Remember that this kind of reset should only be used on unpublished commits. Never perform the above operation if you've already pushed your commits to a shared repository.

Using Sourcetree:

assume you are on the branch `example-fix`. Find the commit with `origin/example-fix`, and right click on it. Select in the menu `Reset example-fix to this commit` and a dialog will appear. If don't want to keep the changes, you can select `Hard`, else select `Soft`

### Upload

Upload (local --> server) a repository for the first time

* Create repository in github
* Clone repository to local station:

```
git clone https://github.com/xxx/xxx.git
```

* Copy files to upload to repository
* Update repository:

```
git add *
git commit -m "First commit"
git push -u origin master
```

### Discard local changes (if `pull` doesn't work)

For a specific file use:

```
git checkout path/to/file/to/revert
```

For all unstaged files use:

```
git checkout -- .
```

### Commit: change message

If you haven't pushed and wish to replace your commit message, use that:

```
git commit --amend -m "New commit message"
```

### Ignore file mode

If you cannot do a pull due to a change of file mode, you can ignore it:

```
git config core.fileMode false
```

### Come back to previous commit (ignore latest ones)

WARNING: This will erase the latest commits!

```
git reset --hard #COMMIT
git push -f
```

### Fix conflicts during rebasing

When doing `git rebase master` to update a working branch, if there are any conflicts,

### Recover lost commits after rebase

If rebasing caused commits to be lost, use `git reflog` to find the commits that were deleted, and then do a `git reset --hard HEAD@{XX}`, XX being the commit that comes right before the merge (the one that says: `checkout: moving from master to YOUR_BRANCH`)

## Commit message convention

See: [https://github.com/neuropoly/spinalcordtoolbox/wiki/git_rules](https://github.com/neuropoly/spinalcordtoolbox/wiki/git_rules)

## GitHub

### Add SSH key

1.  Log in to your Github account and click on the button at the top

    right-hand corner called "Account settings".
2. Click on "SSH keys in the left panel".
3. Click on "Add SSH keys".
4.  Copy and paste the content of id_rsa.pub (open a Terminal and type:

    `more ~/.ssh/id_rsa.pub`)

If you don't have the file id_rsa.pub, do the following:

1. open a terminal
2. go to the folder `~/.ssh/` and type:

```
ssh-keygen -t rsa -C your_email@example.com
```

### port 22: Connection refused

If you get this message, try this:

```
vim ~/.ssh/config
```

Add:

```
Host github.com
  Hostname ssh.github.com
  Port 443
```

### Compare commits/branches/tags

```
https://github.com/ORGANIZATION/REPOSITORY/compare/TAG1...TAG2
```

### Connection closed by remote host

If you get this:

```
ssh_exchange_identification: Connection closed by remote host
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists.
```

this might be due to wifi connection that does not allow ssh. So you can temporarily switch to https:

```
# check which username/remote you are set on
git remote -v
# it should give:
# origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
# origin  git@github.com:USERNAME/REPOSITORY.git (push)
# then set to https:
git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
```

### Search file name

Go to search and type:

```
filename:my_file
```

## Tags

### Checkout specific tag or commit

List all tags

```
git tag
```

Get the commit number of the tag you want, using:

```
git show tag_xx
```

Then, checkout on commit

```
git checkout commit_xx
```

N.B. It is not possible to checkout directly using the tag. More info [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging#Checking-out-Tags)

If you got the following error message:

```
fatal: reference is not a tree: #commit
```

It means that the commit is not listed in the tree of your local git repository. To reach older commits from your local tree, do:

```
git pull --depth=X  # with X=number of commit back in time
```

### Add tag

```
git tag -a vx.y.z #COMMIT -m "added tag for vx.y.z"
git push --tag origin master
```

### Remove Tag

```
git push --delete origin tagname
git tag -d tagname
```

### Useful aliases

Here are useful aliases that you could add to your `~/.bash_profile`

```
alias gs="git status -s"
alias gc="git commit -a"
alias gp="git push"
alias gl="git log --pretty=oneline"
alias glg="git log --pretty=oneline --decorate --all --graph"
alias gd="git diff"
alias gb="git branch"
```

## Troubleshooting

[Methods to dig yourself out of common pitfalls](https://ohshitgit.com)

## git software

### Pycharm

Interactive squash, rebase: [https://www.jetbrains.com/help/pycharm/edit-project-history.html](https://www.jetbrains.com/help/pycharm/edit-project-history.html)

### SourceTree

#### **Select default branches for pushing**

Preferences > "Git" > Push branches: select "current"

#### **Switch to another branch**

On the left side bar you will find a `BRANCHES` header with a list of branches. You are currently on the branch in bold. To change branch, you simply double click on the branch you want to work on.

#### **Update your branch**

In case you have not used fork and you want to update your branch from master, do this:

```
git checkout YOUR_BRANCH
git rebase master
```
