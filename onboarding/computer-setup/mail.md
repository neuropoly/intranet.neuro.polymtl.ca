# <span>📧</span> Email

You can access your PolyMTL email account (@polymtl.ca) at https://zimbra.polymtl.ca.

More info and manuals how to add your PolyMTL email to your phone or mail client are available [here](https://www.polymtl.ca/si/courrier-electronique) under _Utilisation du service_.

## Add PolyMTL email to the macOS Mail app

Click on Apple logo () / System Preferences / Internet Accounts / Add Other Account / Mail account

Fill in your `Name`, `Email Address`, and `Password`:

```
Name: NAME SURNAME
Email Address: name.surname@polymtl.ca
Password: your_password
```

Click `Sign In`

Then fill in as follows:

```
Email Address: name.surname@polymtl.ca
User Name: name.surname
Password: your_password

Account Type: IMAP
Incoming Mail Server: zimbra.polymtl.ca
Outgoing Mail Server: smtp.polymtl.ca
```

## Add PolyMTL email to Thunderbird

***Note 1:*** A similar process should work for other non-Exchange email provides as well, though this has not been formally tested. 

***Note 2:*** This requires the use of OAuth2, and as such will require you to re-log-in in once a month. Unfortunately, its this or paying 10$ per month for a plugin.

1. Open the settings for your accounts (right click on an email you already have -> `settings`)

2. Near the bottom right, click the `Account Actions` drop-down and select `Add Mail Account`

3. Fill in your credentials as requested, and click `Continue`

4. Once the auto-config has run (which may prompt you to login again via a pop-up), select `IMAP` then click the `Configure Manually` button at the bottom

5. Change the `Authentication Method` to `OAuth2` for both the **Incoming** and **Outgoing** servers. Everything else should be safe to leave alone.

6. Click `Done`; if everything worked, you should see your email synchronize shortly!
