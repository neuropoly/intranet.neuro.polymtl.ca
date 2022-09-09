# <span>📶</span> Eduroam

## Overview

As a student or employee of Polytechnique Montreal, you are granted access to the ['eduroam'](https://eduroam.org/what-is-eduroam/) network. 

> What is eduroam?
> 
> eduroam (education roaming) is the secure, world-wide roaming access service developed for the international research and education community.
> 
> eduroam allows students, researchers and staff from participating institutions to obtain Internet connectivity across campus and when visiting other participating institutions by simply opening their laptop.

When on campus, you may see a WiFi network called 'eduroam'. However, to use this network, some extra setup is required. (You can't just log in with your PolyMTL email address and password.)

## Setup

PolyMTL recommends using the ["Eduroam CAT tool"](https://cat.eduroam.org/) to set up the network connection on each of your devices. This tool is available for Windows, macOS, and Linux, as well as Android and iOS.

Before downloading and installing the tool, make sure that you delete any previously saved profiles for the 'eduroam' network. You can do this by going into your device's WiFi settings and looking for the "Saved networks" or "Known WiFi networks" menu option, or similar.

If you are using a tool for computers, you will need to select your institution before downloading. If you are using a smartphone app, you will need to enter your institution in the  it will prompt you for your institution (in this case, École Polytechnique de Montréal).

Once you download and run the tool, it will prompt for a username and password.

* **User ID**: This will depend on whether you are an employee, student, or guest.
  * pMatricule@polymtl.ca -> Employés
  * abcde@polymtl.ca -> Étudiants
  * uNuméro@polymtl.ca -> Invités
* **Password**: This will be your CAS account password (i.e. the same password used for your `@polymtl.ca` email, VPN access, etc.)

Once entered, the tool will create a wireless connection profile for 'eduroam' on your behalf, so you should be able to connect to the network without needing to do anything else. 

## Why do I need to use this tool? Why can't I just sign into the network directly?

The tool is meant to help set up some additional login information beyond your username and password:

* **Authentication**: Protected EAP (PEAP)
* **Inner/Phase 2 authentication**: MSCHAPv2
* **CA Certificate**: Instructions vary depending on device. (Some say "Use system certificates", others will create a custom certificate just for 'eduroam'.)
* **Anonymous identity**: anonymous#####@polymtl.ca

It's possible to set some or all of these yourself if you know what you're doing, but using the tool helps to automate this procedure.
