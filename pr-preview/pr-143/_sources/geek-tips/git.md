
(git)=
# Git & Github


```{note}
Eliot is good at GitHub actions. This is a test.
```

## Tutorials & Courses

```{note}
**Everyone working with `git` at NeuroPoly Lab: Please take 2+ hours of your time and learn how to use `git` before using it.**
```

[**Official Git Documentation**](https://git-scm.com/book/en/v2)

### Tutorials: 
  * [Learn By Doing](https://githowto.com)
  * [sr.ht's Learn By Doing](https://git-send-email.io)
  * [http://www.atlassian.com/git](http://www.atlassian.com/git)
  * [Learn with dynamic git tree](https://learngitbranching.js.org/?locale=fr_EN)


### Courses:
  * [Coursera: Introduction to git/github](https://www.coursera.org/learn/introduction-git-github)


### Other resources:
  * [Github's Learn By Doing](https://try.github.io)
  * [A guide to managing git mistakes from Julia Evans](https://wizardzines.com/zines/oh-shit-git/)
  * [Excellent notes from Matthew Brett](https://matthew-brett.github.io/curious-git/index.html)
  * [Another great tutorial from Elizabeth DuPre](http://emdupre.github.io/git-course/), and a [video](https://neurohackademy.org/course/collaborating-with-git-and-github/)
  * [Sven Hofmann README](https://gist.github.com/hofmannsven/6814451)
  * [git - the simple guide (Roger Dudler)](https://rogerdudler.github.io/git-guide/)
  * Snapshot of all commands: [cheat sheet](http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf)
  * [Methods to dig yourself out of common pitfalls](https://ohshitgit.com)

## Install git

Full instructions to install `git` [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). We have a quick-start below:

::::{tab-set}
:::{tab-item} Linux/Docker
```bash
sudo apt-get update
apt-get install git-all
```
:::

:::{tab-item} macOS
Probably the easiest way to install on macOS is to install via [XCode Command Line Tools](https://developer.apple.com/downloads/). To check if `git` is installed:

```bash
git --version
```
:::

:::{tab-item} Windows
Recommended install: Go to [https://git-scm.com/download/win](https://git-scm.com/download/win) and the download will start automatically.
:::
::::

## Contribute to a project

Basic steps are:

1. Fork the repository
2. Create a branch
3. Create new features while updating your branch from the Master 
4. Submit a pull request

### Fork the repository

1. Log in to your GitHub account
2.  Fork the project repository: click on the `Fork` button near the top of the page. This creates a copy of the code under your account on the GitHub server.
3.  In a Terminal window, go to the folder where you want to copy locally the code.
4. Clone the copy of the code to your local disk:

```bash
  git clone git@github.com:your_login/project_name.git
```

If you get the following error message, [create an SSH key](http://www.neuro.polymtl.ca/doku.php?id=tips_and_tricks:git#github):

```{warning}
> Warning: Permanently added the RSA host key for IP address 'XX.XX.XX.XX' to the list of known hosts.\
> Permission denied (publickey).\
> fatal: Could not read from remote repository.\
> Please make sure you have the correct access rights and the repository exists.
```

### Keep your branch up-to-date

Once the clone is complete your repo will have a remote named `origin` that points to your fork on GitHub. Don't let the name confuse you, this does not point to the original repo you forked from. To help you keep track of that repo you need to add another remote named `upstream`:

* open a terminal, go to your repos and type:

```bash
  git remote add upstream git://github.com/neuropoly/spinalcordtoolbox.git
  git fetch upstream
```

* Then (like `git pull` which is fetch + merge):

```bash
  git merge upstream/master master
```

*   Or if you want, replace your local work on top of the fetched branch

    (like a `git pull --rebase`)

```bash
  git rebase upstream/master
```

The `--rebase` option can be used to ensure a linear history by preventing unnecessary merge commits. Many developers prefer rebasing over merging, since it's like saying, "I want to put my changes on top of what everybody else has done."

### Submit a pull request

* In a Terminal window, go to your git repository and type:

```bash
  git push origin <BRANCH_NAME>
```

* Log in to your GitHub account and go to your branch.
* Click on `Pull request`. You will be sent to a page asking you to describe your modifications; you can give any title you want to your modifications (it doesn't need to be the name of your branch).
* Click on `Create a pull request`.

Now you need to wait that the person in charge of the project accepts your modifications; if this person finds problems in your code, you can still push new changes to your code and they will be added to your pull request.

### How to `merge` specific files from another branch

The tool to use is `git checkout`:

```bash
  git checkout source_branch <paths>...
```

You simply need to give `git checkout` the name of the feature branch and the paths to the specific files that we want to add to your `master` branch as follows:

```bash
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

```bash
  git remote show origin
```

### Track remote branch

```bash
  git remote update
  git fetch
```

### Checkout existing branch

```bash
  git checkout <branch_name>
```

If branch is not tracked (use `git remote show origin` to check if branch is listed), then use:

```bash
  git fetch
```

If you still don't see the branch listed, maybe your local git repository does not allow to fetch all branches on `master`. This happens if you `clone` with `--depth=X`. To check if this is the case, run:

```bash
  git config --get remote.origin.fetch
```

If result is not `+refs/heads/\*:refs/remotes/origin/\*`, then update the `remote.origin.fetch` variable using:

```bash
  git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
```

Then, fetch:

```bash
  git fetch
```

Now, all tracked branches should appear when running:

```bash
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

```bash
git clone -b <branch> <remote_repo> --depth 1
```

### Create a branch

* Prefix the branch name with a personal identifier (such as your initials) and a forward slash. 
* If the branch you are working on is in response to an issue, provide the issue number. 
* Add some text that make the branch name meaningful.

```bash
  git checkout -b <jv/123-branch_name>
```

### Push to remote

```bash
git push -u
git push -u origin <branch_name>  # push to specific branch
```

### Remove a branch

To remove a local branch

```bash
  git branch -d <branch_name>
```

To remove a remote branch (if you know what you are doing!)

```bash
  git push origin :<branch_name>
```

## General usage

### Upload local repository for the first time

First, create a repository on the GitHub website. Then, open a Terminal and run:

```bash
    cd </path/to/your/project>
    git init  # initialize local git repos
    git remote add origin https://USERNAME@URL_TO_REPOSITORY.git  # link to remote repos
    git add .  # add every file under folder
    git commit -m 'First commit'
    git push -u origin master
```

### Switch local repository to another branch

on Sourcetree:

```bash
Checkout > Checkout New Branch
```

on Terminal:

```bash
git checkout <BRANCH_NAME>
```

### Check which branch you are currently working on

```bash
git branch
```

### Create repository inside repository

Use submodules:

1. [http://git-scm.com/book/en/Git-Tools-Submodules](http://git-scm.com/book/en/Git-Tools-Submodules)
2. [http://www.arlocarreon.com/blog/git/git-repo-inside-a-git-repo/](http://www.arlocarreon.com/blog/git/git-repo-inside-a-git-repo/)

## Commits

| Term               | Description                                                                                                                                                                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **tracked file**   | A tracked file is one that is part of the git version control. New files are untracked.                                                                                                                                                                                                      |
| **untracked file** | An untracked file is one that is not part of the git version control. This includes new files, and any files that are specified to be untracked. For example, you may want to ignore files in the `env/` folder. To mark a file as untracked, you can add the file to the `.gitignore` file. |
| **head**           | The HEAD is the most recent snapshot, or commit.                                                                                                                                                                                                                                             |
| **commit ID**      | The commit ID is the 40-character alphanumeric identifier for a given commit. It is a hash, generated using SHA1 (cryptographic algorithm).                                                                                                                                                  |

### Commit message convention

Writing good commit messages is an art. They should be concise but accurate. They should help someone several years from now with little knowledge of your project understand at a high-level what each change was for, and they should help you remember the direction you are working in while working on a branch in the present.

For short, simple commits, this can be achieved via:

```bash
git commit -m "A message describing your commit"
```

However, you may want a longer, more descriptive message. To do this, just run:

```bash
git commit
```

This will open the default text editor, so that you can add a more descriptive message:

```text
Commit message style guide for Git

The first line of a commit message serves as a summary.  When displayed
on the web, it's often styled as a heading, and in emails, it's
typically used as the subject.  As such, you should capitalize it and
omit any trailing punctuation.  Aim for about 50 characters, give or
take, otherwise it may be painfully truncated in some contexts.  Write
it, along with the rest of your message, in the imperative tense: "Fix
bug" and not "Fixed bug" or "Fixes bug".  Consistent wording makes it
easier to mentally process a list of commits.

Oftentimes a subject by itself is sufficient.  When it's not, add a
blank line (this is important) followed by one or more paragraphs hard
wrapped to 72 characters.  Git is strongly opinionated that the author
is responsible for line breaks; if you omit them, command line tooling
will show it as one extremely long unwrapped line.  Fortunately, most
text editors are capable of automating this.

:q
```

For more information on commit messages:

[https://commit.style/](https://commit.style)

[https://thoughtbot.com/blog/5-useful-tips-for-a-better-commit-message](https://thoughtbot.com/blog/5-useful-tips-for-a-better-commit-message)


### Amending Commits

If you made a mistake in your last commit, want to add something, or change the commit message, you can do so with the --amend flag:

```bash
git commit --amend
```

or

```bash
git commit --amend -m "New commit message"
```

This will add the changes you have added to the most recent commit. Make sure to only use this on local commits (i.e. commits that have not been pushed).

### Rollbacks

What if you made a commit that you need to revert? The revert command allows for you to fix this. It undoes your last commit by performing the inverse of everything in the last commit. That way, you still have all the correct history, and you will be able to still see the commit you reverted.

```bash
git revert HEAD
```

Alternatively, you can revert any commit using the commit ID:

```bash
git revert <COMMIT_ID>
```

### Reset Commit

If you want to go back to a previous commit and ignore the latest ones:

```bash
git reset --hard <COMMIT_NUMBER>
git push -f
```

```{warning}
**WARNING:** This will erase the latest commits!
```

## HOW TO

### Configure git

Before starting: configure git to identify you for each commit

Define the author name to be used for all commits by the current user.

```bash
git config --global user.name <name>
```

Define the author email to be used for all commits by the current user.

```bash
git config --global alias.<alias-name> <git-command>
```

more info: [http://www.atlassian.com/git/tutorial/git-basics#!config](http://www.atlassian.com/git/tutorial/git-basics#!config)

### Show changed files between two commits

```bash
git diff --name-only SHA1 SHA2
```

GIT - repository solution

gitk -> cool stuf

Doc: [http://gitref.org/basic/](http://gitref.org/basic/)

Download: [http://git-scm.com/download](http://git-scm.com/download)

Create a repository

Create folder:

```bash
mkdir my_repos.git
```

Go there:

```bash
cd my_repos.git
```

Copy repository to your station

```bash
git clone path_to_my_repos/my_repos.git
```

Rename directory

```bash
mv my_repos.git working_dir
```

Note: Now you can copy/modify files in your working_dir

Commit changes locally

Add the files you want to your commit list, e.g.:

```bash
git add *.m
```

To add all modified (or deleted) files automatically, use:

```bash
git add -u
```

Commit the files

```bash
git commit -m 'enter description here'
```

Note: You have to configure the commit params (do only once):

```bash
git config --global user.name 'Your Name'
git config --global user.email you@somedomain.com
```

Cancel a `git add`

```bash
git reset <file_name>
```

Look at the status of the files (tracked? Modified? Added?)

```bash
git status -s
```

Update changes to your repos

```bash
git push path_to_my_repos/my_repos.git master
```

example:

```bash
git push jcohen@door.nmr.mgh.harvard.edu:/autofs/cluster/connectome/git/process_data.git master
```

or:

```bash
git push -u origin master
```

Download changes from your repos

```bash
git pull
```

Removed tracked files

```bash
git rm "file name"
```

### Download

Download (server -> local station) a repository for the first time

get address of repos, and type

```bash
git clone git@bitbucket.org:neuropoly/spinalcordtoolbox_dev.git
```

### Reset your branch (revert your local commits)

Using the Terminal:

```bash
git fetch
git reset --hard origin/master
```

Moving the current branch backward by N commits:

```bash
git reset --hard HEAD~N
```

Warning: This comment effectively removes the N snapshots created from the project history. Remember that this kind of reset should only be used on unpublished commits. Never perform the above operation if you've already pushed your commits to a shared repository.

Using Sourcetree:

assume you are on the branch `example-fix`. Find the commit with `origin/example-fix`, and right click on it. Select in the menu `Reset example-fix to this commit` and a dialog will appear. If don't want to keep the changes, you can select `Hard`, else select `Soft`

### Upload

Upload (local --> server) a repository for the first time

* Create repository in GitHub
* Clone repository to local station:

```bash
git clone https://github.com/xxx/xxx.git
```

* Copy files to upload to repository
* Update repository:

```bash
git add *
git commit -m "First commit"
git push -u origin master
```

### Discard local changes (if `pull` doesn't work)

For a specific file use:

```bash
git checkout <path/to/file/to/revert>
```

For all unstaged files use:

```bash
git checkout -- .
```

### Commit: change message

If you haven't pushed and wish to replace your commit message, use that:

```bash
git commit --amend -m "New commit message"
```

### Ignore file mode

If you cannot do a pull due to a change of file mode, you can ignore it:

```bash
git config core.fileMode false
```

### Come back to previous commit (ignore the latest ones)

WARNING: This will erase the latest commits!

```bash
git reset --hard #COMMIT
git push -f
```

### Fix conflicts during rebasing

When doing `git rebase master` to update a working branch, if there are any conflicts,

### Recover lost commits after rebase

If rebasing caused commits to be lost, use `git reflog` to find the commits that were deleted, and then do a `git reset --hard HEAD@{XX}`, XX being the commit that comes right before the merge (the one that says: `checkout: moving from master to YOUR_BRANCH`)

## GitHub

### Add SSH key

1. Log in to your Github account and click on the button at the top right-hand corner called “Account settings”.
2. Click on “SSH keys in the left panel”.
3. Click on “Add SSH keys”.
4. Copy and paste the content of id_rsa.pub (open a Terminal and type: `more ~/.ssh/id_rsa.pub`)

If you don't have the file id_rsa.pub, do the following:

1. Open a Terminal
2. Go to the folder `~/.ssh/` and type:

```bash
ssh-keygen -t rsa -C your_email@example.com
```

### port 22: Connection refused

If you get this message, try this:

```bash
vim ~/.ssh/config
```

Add:

```bash
Host github.com
  Hostname ssh.github.com
  Port 443
```

### Compare commits/branches/tags

```bash
https://github.com/ORGANIZATION/REPOSITORY/compare/TAG1...TAG2
```

### Connection closed by remote host

If you get this:

```bash
ssh_exchange_identification: Connection closed by remote host
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists.
```

this might be due to Wi-Fi connection that does not allow ssh. So you can temporarily switch to https:

```bash
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

```bash
filename:my_file
```

## Tags

### Checkout specific tag or commit

List all tags

```bash
git tag
```

Get the commit number of the tag you want, using:

```bash
git show tag_xx
```

Then, checkout on commit

```bash
git checkout commit_xx
```

Note: It is not possible to checkout directly using the tag. More info [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging#Checking-out-Tags)

If you got the following error message:

```bash
fatal: reference is not a tree: #commit
```

It means that the commit is not listed in the tree of your local git repository. To reach older commits from your local tree, do:

```bash
git pull --depth=X  # with X=number of commit back in time
```

### Add tag

```bash
git tag -a vx.y.z #COMMIT -m "added tag for vx.y.z"
git push --tag origin master
```

### Remove Tag

```bash
git push --delete origin tagname
git tag -d tagname
```

### Useful aliases

Here are useful aliases that you could add to your `~/.bash_profile`

```bash
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

### gpg

If you are getting:

```
error: gpg failed to sign the data
fatal: failed to write commit object
```

Follow [this procedure](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key).

Then, if you experience this:
```
error: unsupported value for gpg.format: ssh
fatal: bad config variable 'gpg.format' in file '/Users/julien/.gitconfig' at line 3
```

Maybe git is not up-to-date (see: [this comment](https://1password.community/discussion/comment/656138/#Comment_656138)). Update it.

```{note}
After reinstalling git, you need to open a new Terminal. 
```


## Git software

### Pycharm

Interactive squash, rebase: [https://www.jetbrains.com/help/pycharm/edit-project-history.html](https://www.jetbrains.com/help/pycharm/edit-project-history.html)

### SourceTree

#### **Select default branches for pushing**

Preferences > "Git" > Push branches: select "current"

#### **Switch to another branch**

On the left side bar you will find a `BRANCHES` header with a list of branches. You are currently on the branch in bold. To change branch, you simply double click on the branch you want to work on.

#### **Update your branch**

In case you have not used fork, and you want to update your branch from master, do this:

```bash
git checkout <YOUR_BRANCH>
git rebase master
```
