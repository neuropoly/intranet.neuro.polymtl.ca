---
description: 3T Siemens Prisma at the Unité de Neuroimagerie Fonctionnelle (UNF), CRIUGM
---

# UNF (3T Prisma)

More details on the UNF website: [https://unfmontreal.github.io/en/mri/](https://unfmontreal.github.io/en/mri/)

## Booking the scanner

1. First, you should take the MRI safety training (Send an email to support.unf@criugm.qc.ca requesting participation in the training).
2. Second, you must have an account to reserve the scanner (Send another email to the same address to get your account ready).
3. The last step includes a disinfection training which will be given to you once you get to UNF for your first scan.

Details about the booking system [here](https://unfmontreal.github.io/en/reservations/).

```{note}
Under the `session name` you will need to enter a study suffix that is listed in this [JSON file](https://github.com/UNFmontreal/bids_configs/blob/master/studies.json). Look for the fields that start with `neuropoly`.
```


## Finding participants

Check our [internal list of participants](https://docs.google.com/spreadsheets/d/1S0v-YWxYrILJmqb3PtaSTgwBECKEbnljoDfnfIROoSk/edit?usp=sharing) (requires NeuroPoly credentials).

## Filling MRI eligibility form

Have your participant fill the MRI eligibility form, which is accessible once the MRI slot is booked (the person who booked the scanner knows how to access this form).

## Access to UNF

The UNF is located at the Institut universitaire de gériatrie de Montréal (IUGM), 4565 chemin Queen-Mary, Montréal ([Google Maps](https://www.google.com/maps/search/?api=1&query=4565+chemin+Queen-Mary+Montreal)). Detailed access maps are on the [UNF website](https://unfmontreal.github.io/en/access/).

![](../.gitbook/assets/path\_to\_unf.png)

## Download the data

See info here: [https://unfmontreal.github.io/en/download-data/](https://unfmontreal.github.io/en/download-data/)

Data for NeuroPoly group are located under: `elm.criugm.qc.ca:/unf/dicoms/by_groups/neuropoly/`

In case you need to [reset your password](https://pwd.unf-montreal.ca/).

## Reconstruct raw data

[GitHub NeuroPoly: Siemens Recon](https://github.com/neuropoly/siemens-recon)
