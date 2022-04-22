---
description: >-
  Siemens Terra system located at the Brain Imaging Center (BIC), Montreal
  Neurological Institute (MNI), McGill University.
---

# MNI/McGill (7T Terra)

## Book the scanner

* Email Ilana Leppert [ilana.leppert@mcgill.ca](mailto:ilana.leppert@mcgill.ca) to validate if her or one of the techs ("BIC MRtechs" [mrtechs.neuro@mcgill.ca](mailto:mrtechs.neuro@mcgill.ca)) can attend the scan&#x20;
* Email BIC finance ("Bic-Finance Mni" [bic-finance.mni@mcgill.ca](mailto:bic-finance.mni@mcgill.ca)) in order to open the time slot in the calendar&#x20;
* Login into [https://coreservices.medicine.mcgill.ca/ords/f?p=282:LOGIN\_DESKTOP:215990860603743](https://coreservices.medicine.mcgill.ca/ords/f?p=282:LOGIN\_DESKTOP:215990860603743)::::: with  Julien’s username or another authorised person (Alexandru, Eva ?)
  * For phantom scanning, indicate that it is a "development scan / phantom scan" in the “Other pertinent information or instructions to this study” field when booking your scan request. This is **very important** because the rate is reduced by a factor two. 
* Add the session to the MRI log book (see [MRI scanning](./)).

## Download the data

Extensive list of BIC how-to information: [https://forum.bic.mni.mcgill.ca/c/general/howto](https://forum.bic.mni.mcgill.ca/c/general/howto)

1. Login to BIC server (you need to ask for an account in the first place): [http://www.bic.mni.mcgill.ca/Services/HowToLogin](http://www.bic.mni.mcgill.ca/Services/HowToLogin)
2.  Locate the name of the scanning session that you would like to transfer on _/data/transfer/dicom/. _You can type the following command in your local terminal to get the list of the existing sessions (you will be prompted for your BIC password):&#x20;

    `ssh username@login.bic.mni.mcgill.ca ls /data/transfer/dicom `
3.  Use_ rsync_ or Filezilla to transfer the archive to your computer. Alternatively, you can type(you will be prompted for your BIC password):

    `scp -r username@login.bic.mni.mcgill.ca:/data/transfer/dicom/sessionname ~/local/direction/path`
4. Zip the data and put them on duke under `mri/projectname` if not already there.
