# <span>📶</span> Eduroam 

## Overview

As a student or employee of Polytechnique Montreal, you are granted access to the ['eduroam'](https://eduroam.org/what-is-eduroam/) network. 

> ### What is eduroam?
> 
> eduroam (education roaming) is the secure, world-wide roaming access service developed for the international research and education community.
> 
> eduroam allows students, researchers and staff from participating institutions to obtain Internet connectivity across campus and when visiting other participating institutions by simply opening their laptop.

When on campus, you may see a WiFi network called 'eduroam'. However, to use this network, some extra setup is required. (You can't just log in with your PolyMTL email address and password.)

## Setup

PolyMTL [provides instructions](https://www.polymtl.ca/si/reseaux/wifi-onboarding) for using a closed-source tool to set up the network connection on each of your devices. The tool will require admin access to work. It is available for Windows, macOS, and Linux, as well as Android and iOS.

Before downloading and installing the tool, make sure that you delete any previously saved profiles for the 'eduroam' network. You can do this by going into your device's WiFi settings and looking for the "Saved networks" or "Known WiFi networks" menu option, or similar.

Once you download and run the tool, it will prompt for a username and password.

* **User ID**: This will depend on whether you are an [employee, student, or guest](https://www.polymtl.ca/si/reseaux/reseau-sans-fil#WIFI_Personnel_Etudiant).
  * pMatricule@polymtl.ca -> Employés
  * abcde@polymtl.ca -> Étudiants
  * uNumero@polymtl.ca -> Invités
* **Password**: This will be your CAS account password (i.e. the same password used for your `@polymtl.ca` email, VPN access, etc.)

Once entered, the tool will create a client certificate and a wireless connection profile for 'eduroam' on your behalf, so you should be able to connect to the network without needing to do anything else. 

## What if I don't want to use the closed-source tool?

You can use this [PolyRoam](https://www.pointedset.ca/polyroam) python script to generate the client certificate needed to authenticate to eduroam.

## I heard that the WiFi is changing? Could this affect my access? 

Yes. Polytechnique is in the process of switching its eduroam authentication protocol from EAP-PEAP to EAP-TLS. Support for EAP-PEAP ends after March 2024. In order to continue to connect to eduroam, you will need to use the new tool or the python script to generate a client certificate. Depending on your device you may need to delete previous network profiles for eduroam. More information is available [here](https://www.polymtl.ca/si/reseaux/wifi).
