# `data.neuro.polymtl.ca`

Link to the web interface (only accessible on-campus or through the VPN):
<https://data.neuro.polymtl.ca/>

This server includes private MRI and microscopy datasets, which have been curated and organized according to the [BIDS](https://bids.neuroimaging.io/) convention.

`git+ssh://data.neuro.polymtl.ca` has a max size of ~1TB.

It hosts [BIDS](https://bids-specification.readthedocs.io) datasets, version-controlled using [`git-annex`](https://git-annex.branchable.com/).
It is locked behind a [VPN](../computing-resources/neuropoly/README.md#vpn) because much of our data is under medical ethics protections, and needs to be kept off the general internet.

## Connecting to the web interface

You can use the web interface to:
* view our list of datasets,
* browse/preview the content of each dataset,
* create and review pull requests,
* update your user settings, including your registered SSH keys,
* (if you are an admin) manage users and repositories.

How to connect:
1. If you're off-campus: first connect to the [VPN](../computing-resources/neuropoly/README.md#vpn).
2. In your web browser, go to <https://data.neuro.polymtl.ca/>.

   If this takes a long time and/or times out, it's probably because you're not on-campus and not on the VPN. Go back to Step 1.

   If it's the first time you visit this URL, you will probably get a security warning about the [self-signed HTTPS certificate we're using](https://github.com/neuropoly/computers/issues/337#issuecomment-1976098453). You may have to add a security exception in your browser.

   Note that there's a language selector (English / français) at the bottom right of every page.
4. Click "Sign In" at the top right of the page.
5. The username and password should be the same as the ones you normally use to connect to lab computers (that is, your [GRAMES / GE account](../computing-resources/neuropoly/README.md#ge)).
6. If it's your first time using the web interface, you may want to start by [changing some of your settings](#initial-setup).

## Initial setup

While you're [logged in to the web interface](#connecting-to-the-web-interface):

1. (Optional) You may want to change the default language between French and English.
   1. Click your user icon at the top right of any page.
   2. Select "Configuration" or "[Settings](https://data.neuro.polymtl.ca/user/settings)" in the menu that unrolls.
   3. Select "Apparence" or "[Appearance](https://data.neuro.polymtl.ca/user/settings/appearance)" in the left menu bar.
   4. Update the "Langue" or "Language" selection.
   5. Click "Modifier la langue" or "Update Language".
2. (Optional) You may want to change your user icon, instead of using the auto-generated abstract art.
   1. Click your user icon at the top right of any page.
   2. Select "[Settings](https://data.neuro.polymtl.ca/user/settings)" in the menu that unrolls.
   3. Select "[Profile](https://data.neuro.polymtl.ca/user/settings)" in the left menu bar.
   4. Next to "Choose new avatar", click the "Browse..." button.
   5. Select the user image file you want to upload.
   6. Click "Update Avatar".
3. (Recommended) Set up command-line access with an SSH key.
   (This needs to be done once for each computer you use.)
   1. Get your SSH key from the terminal:
      1. Check whether you already have an SSH key:
      ```sh
      ls ~/.ssh/id_ed25519.pub
      ```
      2. If the above file doesn't exist, create it with this command:
         ```sh
         ssh-keygen -t ed25519
         ```
      3. Display the public part of your SSH key:
         ```sh
         cat ~/.ssh/id_ed25519.pub
         ```
         It should be a single line of text that looks something like this:
         ```
         ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEWpqMuw5ifj87tdl12x5+LJ3uqHdfFQmoVQKsDLjKYG your.user.name@some.computer.name
         ```
   2. Put the SSH key in the web interface:
      1. Click your user icon at the top right of any page.
      2. Select "[Settings](https://data.neuro.polymtl.ca/user/settings)" in the menu that unrolls.
      3. Select "[SSH / GPG Keys](https://data.neuro.polymtl.ca/user/settings/keys)" in the left menu bar.
      4. To the right of the heading "Manage SSH Keys", click "Add Key".
      5. Paste the contents of the file `~/.ssh/id_ed25519.pub` into the "Content" box.
      6. Click "Add Key" below.
   3. Test your SSH key from the terminal with the command:
      ```sh
      ssh git@data.neuro.polymtl.ca
      ```
      It might ask for the **passphrase** for your key `~/.ssh/id_ed25519.pub`. It should output something like this:
      ```
      PTY allocation request failed
      Hi there, "$USER"! You've successfully authenticated with the key named "$EMAIL", but Gitea does not provide shell access.
      If this is unexpected, please log in with password and setup Gitea under another user.
      Shared connection to data.neuro.polymtl.ca closed.
      ```
      If it asks for a **password** for `git@data.neuro.polymtl.ca`, or the output ends with this, then it didn't work and you should [ask for help](#getting-help):
      ```
      ...
      git@data.neuro.polymtl.ca: Permission denied (publickey,password).
      ```
4. (Recommended) Make sure you have `git` and `git-annex` installed on your computer. See [`git-annex` installation](../geek-tips/git-annex.md#installation).

## Listing the available datasets

To view the existing repositories, [connect to the web interface](#connecting-to-the-web-interface) and use the "[Explore](https://data.neuro.polymtl.ca/explore/repos)" tab, which is linked from the top of every page. Keep in mind that there are multiple pages, so either use the search box or click "Next" if you're looking for a specific repository or username.

If you're a lab member and you don't see any datasets, it's possible that you weren't added to [the "Lab-members" team](https://data.neuro.polymtl.ca/org/datasets/teams/lab-members) during your onboarding. If that's the case, [ask an admin](#getting-help) to add you.

## Downloading a datasete

If you want to run `git` commands from the command-line (`clone`, `pull`, `push`, etc.):

1. If you're off-campus: first connect to the [VPN](../computing-resources/neuropoly/README.md#vpn).
2. To make a local clone, replace `"$REPO"` with the actual repository name in the following commands:
   ```sh
   git clone git@data.neuro.polymtl.ca:datasets/"$REPO"
   cd "$REPO"
   git annex init
   git annex dead here
   git annex get
   ```

   If the `clone` command fails, it's possible that you need to tell the server about your computer's SSH public key. See the section on doing the [initial setup](#initial-setup).
3. All other `git` commands should work normally.

## Getting changes from the server

If you have already cloned a repository and would like to get the latest version:

1. Make sure you're on the right branch, and all your changes are saved, and you have a clean worktree. The command `git status` should say:
   ```
   On branch "$BRANCH"
   ...
   nothing to commit, working tree clean
   ```
2. Run the command:
   ```sh
   git annex pull
   ```
   If your version of `git-annex` is older, you may need to use this command instead:
   ```sh
   git annex sync --content --no-push
   ```

## Getting write access to a repository

By default, all lab members have _read_ access to all repositories, so you can [clone repositories](#connecting-from-the-command-line-cloning-a-repo) and [pull changes from the server](#getting-changes-from-the-server). If you want to [push changes to the server](#making-a-pull-request), you will need _write_ access to the repository in question.

To get write access to a repository, ask [one of the current admins](#getting-help). They will need to use the web interface, go to the repository's "Settings" tab, and add your username to the list of "Collaborators".

## Opening an issue

If you're working with a dataset, and you notice that something is wrong, or something could be better, consider opening an issue!

Since we sometimes want to discuss issues with people outside the lab, we use [Github issues in `neuropoly/data-management`](https://github.com/neuropoly/data-management/issues), which is publicly visible to the whole internet. Open an issue there, and avoid putting private information there (but you can include links to <https://data.neuro.polymtl.ca/>).

## Making a pull request

If you want to modify a dataset, you should make a pull request, which can then be reviewed and merged into the master branch.

1. First make sure you have a [local clone](#connecting-from-the-command-line-cloning-a-repo) of the repo, and that it's [up to date](#getting-changes-from-the-server).
2. Create a new branch for your work, starting from the current `master` branch. If your initials are `xyz` and you want to work on `some-topic`, your branch should be called `xyz/some-topic`. From inside your local clone of the repo, use the command:
   ```sh
   git checkout -b xyz/some-topic master
   ```
   > If you are pushing data for the first time, and you did not run any `git annex` command, please run a command like `git annex dead here` before doing the next steps.
3. Make the changes you want to the files in the repo, then save the changes in a commit (or several commits). You can use the commands:
   ```sh
   git add .
   git commit
   ```
4. For the previous steps, only read access was needed. For the following steps, you will need [write access](#getting-write-access-to-a-repository).
5. To push the changes to the server (both the changes in your branch `xyz/some-topic` and in the special branch `git-annex`), you can use the command:
   ```sh
   git annex push --all
   ```
   If your version of `git-annex` is older, you may need to use this command instead:
   ```sh
   git annex sync --all --content
   ```
6. On the web interface <https://data.neuro.polymtl.ca/>, open a pull request:
   1. Go the the repository's page.
   2. Click on the "Pull Requests" tab.
   3. Click the "New Pull Request" button.
   4. Leave the dropdown menu that says "merge into: datasets:master" as it is.
   5. Select your branch `datasets:xyz/some-topic` in the "pull from:" dropdown menu. A preview of your changes should appear below.
   6. Click the "New Pull Request" button that appeared below.
   7. Enter a title and a description of your changes, along with any relevant context, in the text boxes that appeared.
   8. Click "Create Pull Request".

## Getting help

If you need help with anything related to <https://data.neuro.polymtl.ca/>, your best bet is to post a question on the [#database_mri](https://app.slack.com/client/T034UD4QN/CB232HT46) Slack channel.

The usual server admins are:

* mathieu.guay-paquet@polymtl.ca
* emma.lichtenstein@polymtl.ca

In case of emergency, these people also have admin access:

* eva.alonso-ortiz@polymtl.ca
* jcohen@polymtl.ca
* joshua.newton@polymtl.ca
* mathieu.boudreau@polymtl.ca
* nathan.gorvett@polymtl.ca
