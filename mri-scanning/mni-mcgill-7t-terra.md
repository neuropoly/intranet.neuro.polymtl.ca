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

## Fill out the screening form
* Download the screening form [here](https://drive.google.com/file/d/1ezjUSRP9EYNM5zzqMNMIAwwkhevagay6/view?usp=sharing)
* Ask your participant to fill it out
* Send it to [Bic-Finance](mailto:bic-finance.mni@mcgill.ca) at least 24h before your scan

## Download the data

Extensive list of BIC how-to information: [https://forum.bic.mni.mcgill.ca/t/how-to-retrieve-download-mri-dicom-data/1657](https://forum.bic.mni.mcgill.ca/t/how-to-retrieve-download-mri-dicom-data/1657)

Short version:
1. Login to BIC server (you need to ask for an account in the first place): [http://www.bic.mni.mcgill.ca/Services/HowToLogin](http://www.bic.mni.mcgill.ca/Services/HowToLogin)
2. Type "find_mri sessionname", where MRIID is the name of your scan session (for example acdc_spine_7t_049p)
3. Note down the full path of the sessionname under _/data/transfer/dicom/sessionname_X_X_ (for example, `/data/dicom/acdc_spine_7t_049p_20220923_111852672`)
4. Claim the data as yours: "find_mri -claim sessionname"
5. Exit the ssh session
6. Use scp or rsync or Filezilla to download that data. 

   Using scp:
   ```
   scp -r username@login.bic.mni.mcgill.ca:/data/transfer/dicom/sessionname_X_X ~/local/direction/path
   ```
   For our example, that would be:
   ```
   scp -r unsername@login.bic.mni.mcgill.ca:/data/transfer/dicom/acdc_spine_7t_049p_20220923_111852672 /Users/username/local/path/to/data
   ```
7. Zip the data and put them on duke under `mri/projectname` if not already there.
