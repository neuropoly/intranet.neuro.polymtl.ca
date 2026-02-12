# Password management

By working in the laboratory you will be close to very sensitive information such as secure access keys and passwords, for personal or group use, allowing you to gain access to servers or critical physical spaces.

In this context, it is everyone's duty to ensure the security of these sensitive information throughout its use and you should take this responsibility in account in all your actions and decisions.

For example:

 - Taking a picture inside the lab can lead to sensible information leaking on social's network due to some computer screen, note or post-it in the background of the picture
 - Committing files on git without reread can lead to sensible information leaking on the cloud due to config file containing password or keys 

Although we cannot have total security, simple practices and awareness of laboratory members can already avoid a lot of problems.

```{note}
In the following documentation, the word "password" is used for any "secret" phrase, like "secret key", 
"secret tokens", "password" or "passphrase" that help to gain access to private access. Sensitive information 
of research (patients data, NDA covered data, etc..) are not covered by this documentation.
```

## Storage of the passwords

Polytechnique Montreal does not provide a secure password system within the university, but NeuroPoly expects members of the laboratory will use password managers for all accounts granted as part their work with us.

**You should:**

 - Use a unique password for each account. 
   - A good password manager will help you do this, and you shouldn't even have to memorize each password.
 - Use an encrypted password manager like [KeyPass](https://keepass.info/), [Passbolt](https://www.passbolt.io/), [Google password](https://passwords.google.com/) or [Dashlane](https://www.dashlane.com/).

**You should not:**

 - Keep passwords on physical paper (post-it, printed paper)
 - Keep passwords in clear inside a file in your computer.
 - Keep passwords in clear on a cloud storage (Google Drive, Evernote, ..).
 - Keep passwords in Git repositories

In place try to save the passwords inside an encrypted password manager and destroy the physical paper.

## Sharing of the passwords

The sharing of the passwords is as much important as the storage of them since it could result in a leak of security.

**You should:**

 - Always try to use per-user account if it's available and share access by adding other members into the team/group
   - Ex: Youtube, Github, DigitalOcean
 - Use a shared password vault (ie: `Passbolt`, `dashlane`, `lastpass`, ..).
   - Discuss this solution with your coworker to see if one already exist or to create a new one that match your needs.
 - Use an encryption method to share only the encrypted password.
   - Manual encryption (ex: private/public key).
   - End-to-end encryption method like `signal` application.
 - Use a third-party encryption service like [privnote](https://privnote.com/) or [dpaste](https://dpaste.org/)
   - Note that these sites could be a risk if their owners decided to exploit us, they are "accepted" solution

**You should not:**
 - Share password on Slack.
 - Share password by email.
 - Share password on papers.
 - Share password or secret keys/tokens on Github.

## Deletion of the passwords

Deleting passwords is most of the time the forgotten step in the information lifecycle. It is however a 
crucial step since it is what allows us to ensure that the information will never be more accessible and 
that we can no longer worry about it.

```{warning}
This section does not cover data of research like ML data or patient sensitive information. We are speaking 
about passwords like the one you get from polytechnique on your first days or that people shared with you on paper.
```

**You should:**

 - Destroy papers containing passwords (crusher or fire depending on the level of sensitivity).

**You should not:**

 - Put papers containing passwords in the trash without making it unreadable beforehand.
