# Deep Learning Models

Creating a new model involves a number of substeps, summarized below:

1. Creating a **new GitHub repository** for the model.
   - This repository will track issues, as well as store the README and any code or scripts associated with your model.
2. **Training** the model.
3. **Packaging** the trained model into a `.zip`.
4. **Integrating** the model into the Spinal Cord Toolbox (SCT), if appropriate.

More details on each step can be found below:

## 1. Creating and naming the model repository

Each model is saved in its own repository under the [ivadomed](https://github.com/ivadomed) organization. The convention for naming repositories is the following:

Syntax:
~~~
model_task_anatomy_animal_pathology_condition_contrast_architecture
~~~

Keys/Values:
~~~
- task = {seg, label, find}, default=None
- anatomy = {sc, gm, csf, brainstem, axon, myelin, ...}, default=sc
- animal = {human, dog, cat, rat, mouse, ...}, default=human
- pathology = {hc, ms, sci}, default=hc
- condition = {invivo, exvivo}, default=invivo
- contrast = {t1, t2, t2star, dwi, sem, tem, oi, ...}, default=None
- architecture = {unet2d, unet3d, filmCharley, hemisAndreanne}, default=unet2d
~~~

> [!NOTE]  
> Default fields can be ommited to avoid long names.

Examples:
~~~
model_seg_monkey_sc_t1_unet3d
model_seg_sc-gm-lesion_human_ms_exvivo_t2star
model_seg_sc-gm_t1-t2_unet3d  # multi-channel, multi-class
~~~

----

## 2. Training the model

For instructions on how to train a new model using the nnU-Net framework, please refer to the [nnU-Net Quick Start Guide](https://github.com/ivadomed/utilities/blob/main/quick_start_guides/nnU-Net_quick_start_guide.md).

----

## 3. Packaging models

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
    ├── plans.json
    └── trainer_class.py

```

```{important}
The `dataset.json` file should contain the `image_orientation` entry, for example: `"image_orientation": "RPI"`. This
entry is used by SCT to determine the image orientation. But, it is also a good idea to document which orientation was 
used during training (for the sake of reproducibility).
```

```{warning}
The `trainer_class.py` file is only necessary if you have used a custom trainer during training. For more information
on what should be in this file, please refer to the [nnUNet Quick Start Guide](https://github.com/ivadomed/utilities/blob/main/quick_start_guides/nnU-Net_quick_start_guide.md#ii-using-a-custom-trainer).
```

3. Zip the folder and upload it as an asset in the release
4. Publish the release.

----

## 4. Integrating the model into SCT.

For instructions on how to integrate the model into the Spinal Cord Toolbox, please refer to the [Integrating a new model into SCT](https://github.com/spinalcordtoolbox/spinalcordtoolbox/wiki/DL-models%3A-Integrating-a-new-model-into-SCT) page on the SCT Developer Wiki.
