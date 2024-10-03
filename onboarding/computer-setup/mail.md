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

## Add PolyMTL email to Email Clients without Exchange

This solution uses OAuth2 instead of Exchange, avoiding the need for your client to have root level permission on your operating system. However, this requires you to log-in in once a month

⚠️ **Only tested on Ubuntu `22.04` w/ Thunderbird version `128.0.1esr`; if you have confirmed this method works on another email client and/or operating system, please update this site or let [Kalum Ost](mailto:kalum.ost@polymtl.ca) know so he may do so** ⚠️

1. Begin to add a new account to your client, as normal, proceeding until you reach the server configurations (this may require you to click a button labelled "Configure Manually" or the like).

2. Change the server type to `IMAP` if it is not already, and the `Authentication Method` to `OAuth2` for both the **Incoming** and **Outgoing** servers. Everything else should be safe to leave alone.

3. Click `Done`; if everything worked correctly, you should see your email synchronize shortly!
