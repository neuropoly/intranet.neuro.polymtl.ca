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
1. Create a release of the repository. The tag and title of the release should be `rYYYYMMDD`, example: `r20240915`.
2. Prepare a folder with the model in the following format. Keep the nnUNet folder structure intact. To save space,
include only `checkpoint_final.pth`. Example:

```bash
$ tree model-spinal-rootlets-mp2rage-r20240915.zip
└── nnUNetTrainer_2000epochs__nnUNetPlans__3d_fullres
    ├── dataset.json
    ├── dataset_fingerprint.json
    ├── fold_0
    │         ├── checkpoint_final.pth
    │         ├── debug.json
    │         ├── progress.png
    │         ├── training_log_2024_9_3_14_06_03.png
    │         └── training_log_2024_9_3_14_06_03.txt
    └── plans.json
```

```{important}
The `dataset.json` file should contain the `image_orientation` entry, for example: `"image_orientation": "RPI"`. This
entry is used by SCT to determine the image orientation. But, it is also a good idea to document which orientation was 
used during training (for the sake of reproducibility).
```

3. Zip the folder and upload it as an asset in the release
4. Publish the release.
