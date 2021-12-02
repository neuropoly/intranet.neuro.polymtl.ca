# BitBucket

**The pull or clone command hangs after your enter the password**

This may be related to the https protocol. Use ssh instead. Here's how to do this:

* Open terminal, type `more ~/.ssh/id_rsa.pub`. Copy the public key.
* Open web browser, go to your bitbucket, under Manage account–&gt;SSH Key, paste the key.
* Go to your repository–&gt;overview, then click on HTTPS and select SSH. Copy the repository address.
* In the terminal, go to your git folder and type `git config -e`. This will open vim, then change the https repository for the ssh one.

If you don't have a public key yet, go to the folder `~/.ssh/` and type:

```bash
ssh-keygen -t rsa -C your_email@example.com
```

