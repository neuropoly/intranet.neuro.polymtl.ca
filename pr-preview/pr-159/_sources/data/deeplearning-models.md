# Deep Learning Models

## nnUNET

If you want to use nnU-Net to train your model, please use [NeuroPoly's nnU-Net's fork](https://github.com/spinalcordtoolbox/nnUNet-neuropoly) (also available on [PyPI](https://pypi.org/project/nnunetv2-neuropoly/)), which contains custom trainers, inference, and [other improvements](https://github.com/MIC-DKFZ/nnUNet/compare/master...spinalcordtoolbox:nnUNet-neuropoly:neuropoly-fork-patches), and most importantly, which ensures compatibility with SCT (consistent pytorch version between SCT and nnU-Net, more details [here](https://github.com/spinalcordtoolbox/spinalcordtoolbox/blob/0d1a50b3afddb01ba9deeec610d65d44819e71d3/requirements.txt#L37-L43)). Also check our [nnU-Net quickstart guide](https://github.com/ivadomed/utilities/blob/main/quick_start_guides/nnU-Net_quick_start_guide.md).

## Naming models

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
