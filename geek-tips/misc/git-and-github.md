# Git & GitHub

## Tutorials & Courses

```{note}
**Everyone working with `git` at NeuroPoly Lab: Please take 2+ hours of your time and learn how to use `git` before using it.**
```

[**Official Git Documentation**](https://git-scm.com/book/en/v2)****

****

| Name                                                                                                                                                                          | Type          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [Learn By Doing](https://githowto.com)                                                                                                                                        | Tutorial      |
| [Coursera: Introduction to Git/GitHub](https://www.coursera.org/learn/introduction-git-github)                                                                                | Course        |
| [Github's Learn By Doing](https://try.github.io)                                                                                                                              | Resource List |
| [sr.ht's Learn By Doing](https://git-send-email.io)                                                                                                                           | Tutorial      |
| [Ramp up on Git and GitHub (GitHub Learning Lab)](https://lab.github.com/githubtraining/ramp-up-on-git-and-github)                                                            | Course        |
| [Managing merge conflicts (GitHub Learning Lab)](https://lab.github.com/githubtraining/managing-merge-conflicts)                                                              | Course        |
| [Atlassian Git Tutorial](http://www.atlassian.com/git)                                                                                                                        | Tutorial      |
| [A guide to managing git mistakes (Julia Evans)](https://wizardzines.com/zines/oh-shit-git/)                                                                                  | Guide         |
| [The curious coder's guide to git (Matthew Brett)](https://matthew-brett.github.io/curious-git/index.html)                                                                    | Guide         |
| [Another great tutorial from Elizabeth DuPre](http://emdupre.github.io/git-course/), and a video [here](https://neurohackademy.org/course/collaborating-with-git-and-github/) | Course        |
| [Pierre Rioux Presentation](https://www.neuro.polymtl.ca/\_media/tips_and_tricks/git.pdf)                                                                                     | Guide         |
| [Sven Hofmann README](https://gist.github.com/hofmannsven/6814451)                                                                                                            | Notes         |
| [git - the simple guide (Roger Dudler)](https://rogerdudler.github.io/git-guide/)                                                                                             | Guide         |
| Snapshot of all commands: [http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf](http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf)                            | Notes         |
| [Methods to dig yourself out of common pitfalls](https://ohshitgit.com)                                                                                                       | Guide         |

## Installation

Full instructions to install `git` [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). We have a quick-start below:


````{tabbed} Linux
```bash
sudo apt-get update
apt-get install git-all
```
````

````{tabbed} MacOSX
Probably the easiest way to install on MacOSX is to install via [XCode Command Line Tools](https://developer.apple.com/downloads/). To check if `git` is installed:

```bash
git --version
```
````

````{tabbed} Windows
Recommended install: Go to [https://git-scm.com/download/win](https://git-scm.com/download/win) and the download will start automatically.
````


## Contribute to a Project

Basic steps are:

1. Fork the repository
2. Create a branch
3. Create new features while updating your branch from the Master
4. Submit a pull request

### 1. Fork the repository

1. Log in to your GitHub account
2. Fork the project repository: click on the ‘Fork’ button near the top of the page. This creates a copy of the code under your account on the GitHub server.
3. In a Terminal window, go to the folder where you want to copy locally the code.
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



#### Keep your branch up-to-date <a href="maintain_your_branch_up-to-date" id="maintain_your_branch_up-to-date"></a>

Once the clone is complete your repo will have a remote named “origin” that points to your fork on GitHub. Don’t let the name confuse you, this does not point to the original repo you forked from. To help you keep track of that repo you need to add another remote named “upstream”:

* open a terminal, go to your repos and type:

```
  git remote add upstream git://github.com/neuropoly/spinalcordtoolbox.git
  git fetch upstream
```

* Then (like “git pull” which is fetch + merge):

git merge upstream/master master

* Or if you want, replace your local work on top of the fetched branch (like a “git pull –rebase”)

```
  git rebase upstream/master
```

The `–rebase` option can be used to ensure a linear history by preventing unnecessary merge commits. Many developers prefer rebasing over merging, since it’s like saying, “I want to put my changes on top of what everybody else has done.”

### 4. Submit a Pull Request

* In a Terminal window, go to your git repository and type:

```bash
  git push origin <BRANCH_NAME>
```

* Log in to your Github account and go to your branch.
* Click on “Pull request”. You will be sent to a page asking you to describe your modifications; you can give any title you want to your modifications (it doesn't need to be the name of your branch).
* Click on “Create a pull request”.

Now you need to wait that the person in charge of the project accepts your modifications; if this person finds problems in your code, you can still push new changes to your code and they will be added to your pull request.Edit

#### How to "merge" specific files from another branch <a href="how_to_merge_specific_files_from_another_branch" id="how_to_merge_specific_files_from_another_branch"></a>

The tool to use is “git checkout”:

```
  git checkout source_branch <paths>...
```

You simply need to give “git checkout” the name of the feature branch and the paths to the specific files that we want to add to your master branch as follows:

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
```

$ git commit -m “explanation of the commit you are doing”

See the page [git tip how to merge specific files from another branch](http://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/) for more details.

It is not possible to do this on SourceTree yet but an issue was opened on July 17th 2013 and is not closed yet. See [the issue here](https://jira.atlassian.com/browse/SRCTREEWIN-827?jql=text%20\~%20%22merge%20specific%20files%22%20AND%20created%20%3E%3D%202013-07-17%20AND%20created%20%3C%3D%202013-07-18).

See also the interesting page [Smart branching with sourcetree and git flow](http://blog.sourcetreeapp.com/2012/08/01/smart-branching-with-sourcetree-and-git-flow/) about using Git flow to set the right strategy to gang up to contribute to your project.

## Branches

### List remote branches

```
  git remote show origin
```

#### Track remote branch <a href="track_remote_branch" id="track_remote_branch"></a>

```
  git remote update
  git fetch
```

#### Checkout existing branch <a href="checkout_existing_branch" id="checkout_existing_branch"></a>

```bash
  git checkout <branch_name>
```

If branch is not tracked (use \`\`\`git remote show origin\`\`\` to check if branch is listed), then use:

```
  git fetch
```

If you still don't see the branch listed, maybe your local git repository does not allow to fetch all branches on master. This happens if you clone with –depth=X. To check if this is the case, run:

```
  git config --get remote.origin.fetch
```

If result is not “+refs/heads/\*:refs/remotes/origin/\*”, then update the remote.origin.fetch variable using:

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

#### Clone specific branch <a href="clone_specific_branch" id="clone_specific_branch"></a>

```
git clone -b <branch> <remote_repo> --depth 1 
```

#### Create a branch <a href="create_a_branch" id="create_a_branch"></a>

```
  git checkout -b <branch_name>
```

#### Push to remote <a href="push_to_remote" id="push_to_remote"></a>

```
git push -u
git push -u origin <branch_name>  # push to specific branch
```

#### Remove a branch <a href="remove_a_branch" id="remove_a_branch"></a>

To remove a local branch

```bash
  git branch -D <branch_name>
```

To remove a remote branch (if you know what you are doing!)

```
  git push origin :<branch_name>
```

### General usage <a href="general_usage" id="general_usage"></a>

#### Upload local repository for the first time <a href="upload_local_repository_for_the_first_time" id="upload_local_repository_for_the_first_time"></a>

First, create repository in github or bitbucket. Then, open a Terminal and run:

```bash
cd </path/to/your/project>
git init  # initialize local git repos
git remote add origin https://USERNAME@URL_TO_REPOSITORY.git  # link to remote repos
git add .  # add every file under folder
git commit -m 'First commit'
git push -u origin master
```

#### Switch local repository to another branch <a href="switch_local_repository_to_another_branch" id="switch_local_repository_to_another_branch"></a>

```bash
git checkout <BRANCH_NAME>
```

#### Check which branch you are currently working on <a href="check_which_branch_you_are_currently_working_on" id="check_which_branch_you_are_currently_working_on"></a>

```bash
git branch
```

#### Create repository inside repository <a href="create_repository_inside_repository" id="create_repository_inside_repository"></a>

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

### Commit Messages

Your commit must be accompanied by a message. For short, simple commits, this can be achieved via:

```bash
git commit -m "A message describing your commit"
```

However, you may want a longer, more descriptive message. To do this, just run:

```
git commit
```

This will open the default text editor, so that you can add a more descriptive message:

```
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

[https://github.com/neuropoly/spinalcordtoolbox/wiki/git_rules](https://github.com/neuropoly/spinalcordtoolbox/wiki/git_rules)

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

### Configure git <a href="configure_git" id="configure_git"></a>

Before starting: configure git to identify you for each commit

Define the author name to be used for all commits by the current user.

```bash
git config --global user.name <YOUR_NAME>
```

Define the author email to be used for all commits by the current user.

```
git config --global alias.<alias-name> <git-command>
```

more info: [http://www.atlassian.com/git/tutorial/git-basics#!config](http://www.atlassian.com/git/tutorial/git-basics#!config)Edit

### Show changed files between two commits <a href="show_changed_files_between_two_commits" id="show_changed_files_between_two_commits"></a>

```
git diff --name-only SHA1 SHA2
```

GIT - repository solution

gitk → cool stuff

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

N.B. Now you can copy/modify files in your working_dir

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

Cancel a “git add”

```
git reset <file_name>
```

Look at the status of the files (tracked? Modified? Added?)

```
git status -s
```

Update changes to your repos

git push path_to_my_repos/my_repos.git master

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

### Download <a href="download" id="download"></a>

Download (server → local station) a repository for the first time

get address of repos, and type

```bash
git clone git@bitbucket.org:neuropoly/spinalcordtoolbox_dev.git
```

### Reset your branch (revert your local commits) <a href="reset_your_branch_revert_your_local_commits" id="reset_your_branch_revert_your_local_commits"></a>

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

### Upload <a href="upload" id="upload"></a>

Upload (local –> server) a repository for the first time

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

### Discard local changes (if pull doesn't work) <a href="discard_local_changes_if_pull_doesn_t_work" id="discard_local_changes_if_pull_doesn_t_work"></a>

For a specific file use:

```
git checkout path/to/file/to/revert
```

For all unstaged files use:

```
git checkout -- .
```

## TODO

### Ignore file mode <a href="ignore_file_mode" id="ignore_file_mode"></a>

If you cannot do a pull due to a change of file mode, you can ignore it:

```
git config core.fileMode false
```

###  <a href="come_back_to_previous_commit_ignore_latest_ones" id="come_back_to_previous_commit_ignore_latest_ones"></a>

## Rebase

### Fix conflicts during rebasing

When doing `git rebase master` to update a working branch, if there are any conflicts,Edit

### Recover lost commits after rebase

If rebasing caused commits to be lost, use `git reflog` to find the commits that were deleted, and then do a `git reset –hard HEAD@{XX}`, XX being the commit that comes right before the merge (the one that says: `checkout: moving from master to YOUR_BRANCH`)

###  <a href="commit_message_convention" id="commit_message_convention"></a>

### GitHub <a href="github" id="github"></a>

#### Add SSH key <a href="add_ssh_key" id="add_ssh_key"></a>

1. Log in to your Github account and click on the button at the top right-hand corner called “Account settings”.
2. Click on “SSH keys in the left panel”.
3. Click on “Add SSH keys”.
4. Copy and paste the content of id_rsa.pub (open a Terminal and type: `more ~/.ssh/id_rsa.pub`)

If you don't have the file id_rsa.pub, do the following:

1. open a terminal
2. go to the folder `~/.ssh/` and type:

```
ssh-keygen -t rsa -C your_email@example.com
```

#### port 22: Connection refused <a href="port_22connection_refused" id="port_22connection_refused"></a>

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

#### Compare commits/branches/tags <a href="compare_commitsbranchestags" id="compare_commitsbranchestags"></a>

```
https://github.com/ORGANIZATION/REPOSITORY/compare/TAG1...TAG2
```

#### Connection closed by remote host <a href="connection_closed_by_remote_host" id="connection_closed_by_remote_host"></a>

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

#### Search file name <a href="search_file_name" id="search_file_name"></a>

Go to search and type:

```
filename:my_file
```

## Tags

### Checkout specific tag or commit <a href="checkout_specific_tag_or_commit" id="checkout_specific_tag_or_commit"></a>

List all tags

```bash
git tag
```

Get the commit number of the tag you want, using:

```bash
git show <tag_xx>
```

Then, checkout on commit

```bash
git checkout <commit_xx>
```

Note: It is not possible to checkout directly using the tag. More info [here](https://git-scm.com/book/en/v2/Git-Basics-Tagging#Checking-out-Tags)

If you got the following error message:

```
fatal: reference is not a tree: #commit
```

It means that the commit is not listed in the tree of your local git repository. To reach older commits from your local tree, do:

```bash
git pull --depth=X  # with X=number of commit back in time
```

### Add Tag

```bash
git tag -a vx.y.z #COMMIT -m "added tag for vx.y.z"
git push --tag origin master
```

### Remove Tag

```bash
git push --delete origin <TAGNAME>
git tag -d <TAGNAME>
```

## Useful aliases

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

## Git Software

### Pycharm <a href="pycharm" id="pycharm"></a>

Interactive squash, rebase: [https://www.jetbrains.com/help/pycharm/edit-project-history.html](https://www.jetbrains.com/help/pycharm/edit-project-history.html)

### SourceTree <a href="sourcetree" id="sourcetree"></a>

**Select default branches for pushing**

Preferences > “Git” > Push branches: select “current”

**Switch to another branch**

On the left side bar you will find a `BRANCHES` header with a list of branches. You are currently on the branch in bold. To change branch, you simply double click on the branch you want to work on.

**Update your branch**

In case you have not used fork and you want to update your branch from master, do this:

```bash
git checkout <YOUR_BRANCH>
git rebase master
```
