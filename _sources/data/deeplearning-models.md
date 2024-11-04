# Deep Learning Models

## Naming models

Each model is saved in its own repository under the [ivadomed](https://github.com/ivadomed) organization. The convention for naming repositories is the following:

~~~
model_task_animal_pathology_region_contrast_architecture

Should be small letters only.

Fields:
- task = {seg, label, find}, default=seg
- animal = {human, dog, cat, rat, mouse, ...}, default=human
- pathology = {ms, sci}
- region = {sc, gm, csf, brainstem, axon, myelin, ...}, default=sc
- contrast = {t1, t2, t2star, dwi, sem, tem, oi, ...}, default=None
- architecture = {unet2d, unet3d, filmCharley, hemisAndreanne}, default=unet2d

Examples: 

model_seg_monkey_sc_t1_unet3d

# multi-channel, multi-class
model_seg_sc-gm_t1-t2_unet3d
~~~

## Packaging models

Models to be used by 3rd party software (e.g. [SCT](https://spinalcordtoolbox.com/)) should be uploaded as 'assets' to a release of the repository. The steps are:
- Create a release of the repository. The tag and title of the release should be `rYYYYMMDD`, example: `r20211223`.
- Put the model and JSON file inside a folder that has the name of the model.
- Zip the folder and upload it as an asset in the release
- Publish the release.
