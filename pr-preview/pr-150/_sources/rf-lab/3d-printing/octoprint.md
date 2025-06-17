# OctoPrint

1. You can download the latest OctoPi image via the following [link](https://octopi.octoprint.org/latest).
2. Unzip the image and install the contained `.img` file to an SD card using [Etcher](https://etcher.io/). **Do not at any point format the SD from your Operating System, even if prompted to do so** - that will break it and you’ll have to start over. Just use Etcher to flash the `.img` file, that is enough!
3. Use the ethernet connection and ssh into raspberry pi. Default username and password are here:  [NeuroPoly Internal Document: OctoPi Default Credentials](https://docs.google.com/document/d/13iNhiBKYZWT9ytsvYeeYV4FJn6Wn00q9Ctka7toMV08/edit#heading=h.m20wwwmvvmjb).
4. Get certificate:

```bash
sudo -i
mkdir /etc/cert/
cd /etc/cert/
wget --user-agent="Mozilla" http://si-reseau.polymtl.ca/entrust_g2_ca.cer
mv /etc/cert/entrust_g2_ca.cer /etc/cert/entrust_g2_ca.pem
 
```

\* Configure your WiFi connection by editing **octopi-wpa-supplicant.txt** on the root of the flashed card when using it like a thumb drive. Important: Do not use WordPad \(Windows\) or TextEdit \(MacOS X\) for this, those editors are known to mangle the file, making configuration fail. Use something like Notepad++, Atom or VSCode instead or at the very least heed the warnings in the file:

```bash
 country=CA
 ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
 update_config=1
 network={
 ssid="eduroam"
 priority=1
 proto=RSN
 key_mgmt=WPA-EAP
 auth_alg=OPEN
 pairwise=CCMP TKIP
 group=CCMP TKIP
 identity=<YOUR_CODE_HERE>
 password=hash:<YOUR_HASH_HERE>
 anonymous_identity="anonymous@polymtl.ca"
 phase1="peaplabel=0"
 phase2="auth=MSCHAPV2"
 eap=PEAP
 ca_cert="/etc/cert/entrust_g2_ca.pem"
 proactive_key_caching=1
 }
 
 
 # Deactivate IPv6 by adding the line **net.ipv6.conf.all.disable_ipv6 = 1** in:
```

```bash
 sudo nano /etc/sysctl.conf
 
 # Disable bluetooth: https://scribles.net/disabling-bluetooth-on-raspberry-pi/
```

## **OctoPrint Plugins**

1. [https://plugins.octoprint.org/plugins/navbartemp/](https://plugins.octoprint.org/plugins/navbartemp/)
2. [https://plugins.octoprint.org/plugins/simpleemergencystop/](https://plugins.octoprint.org/plugins/simpleemergencystop/)
3. [https://plugins.octoprint.org/plugins/heatertimeout/](https://plugins.octoprint.org/plugins/heatertimeout/)
4. [https://plugins.octoprint.org/plugins/filemanager/](https://plugins.octoprint.org/plugins/filemanager/)
5. [https://plugins.octoprint.org/plugins/octolapse/](https://plugins.octoprint.org/plugins/octolapse/)
6. [https://plugins.octoprint.org/plugins/stats/](https://plugins.octoprint.org/plugins/stats/)
7. [https://plugins.octoprint.org/plugins/Octoslack/](https://plugins.octoprint.org/plugins/Octoslack/)

