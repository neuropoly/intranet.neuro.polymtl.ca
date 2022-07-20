# Password management

By working in the laboratory you will be close to very sensitive information such as secure access keys and passwords, for personal or group use, allowing you to gain access to servers or critical physical spaces.

In this context, it is everyone's duty to ensure the security of these sensitive information throughout its use and you should take this responsibility in account in all your actions and decisions.

For example:

 - Taking a picture inside the lab can lead to sensible information leaking on social's network due to some computer screen, note or post-it in the background of the picture
 - Committing files on git without reread can lead to sensible information leaking on the cloud due to config file containing password or keys 

Although we cannot have total security, simple practices and awareness of laboratory members can already avoid a lot of problems.

## Storage of the sensitive information

Polytechnique Montreal does not provide a secure password system within the university, this responsibility is therefore distributed to each member of the laboratory.

**You should:**

 - Use a protected password manager like `KeyPass`, `Apple's keychain`, `Google password` or `Dashlane`.

**You should not:**

 - Keep sensitive information on physical paper (post-it, printed paper)
 - Keep password in clear inside a file in your computer.
 - Keep password in clear on a cloud storage (Google Drive, Evernote, ..).
 - Keep password in Git repositories

In place try to save the sensitive information inside a protected password manager and destroy the physical paper.

## Sharing of the sensitive information

The sharing of the sensitive information is as much important as the storage of them since it could result in a leak of security.

**You should:**

 - Use a shared password vault (ie: `Passbolt`, `dashlane`, `lastpass`, ..).
   - Discuss this solution with your coworker to see if one already exist or to create a new one that match your needs.
 - Use an encryption method to share only the encrypted password.
   - Manual encryption (ex: private/public key).
   - End-to-end encryption method like `signal` application.

**You should not:**
 - Share password on Slack.
 - Share password by email.
 - Share password on papers.
 - Share password on Github.

## Deletion of the sensitive information

Deleting sensitive information is most of the time the forgotten step in the information lifecycle. It is however a crucial step since it is what allows us to ensure that the information will never be more accessible and that we can no longer worry about it.

**You should:**

 - Destroy paper containing sensible information (crusher or fire depending on the level of sensitivity).

**You should not:**

 - Put paper containing sensitive information in the trash without making it unreadable beforehand.
