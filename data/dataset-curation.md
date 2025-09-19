# Dataset curation

## Converting data to BIDS

All git-annex datasets should be BIDS-compliant. For more information about the BIDS standard, please visit [http://bids.neuroimaging.io](http://bids.neuroimaging.io). For some examples of BIDS datasets, visit [this page](https://github.com/bids-standard/bids-examples). If you have questions, go to the [Neurostars BIDS forum](https://neurostars.org/tag/bids). A quick way to verify compliance with the convention is this [online BIDS validator](https://bids-standard.github.io/bids-validator/).

When you receive raw data from an external collaborator, save them under a temporary location on one of NeuroPoly's server, e.g.: `duke/temp`.

Then, inspect the data and convert them to BIDS. It is recommended to write a script that does the conversion. The 
script should then be saved under the `code` folder of the final dataset. Some previous scripts can be found on 
[GitHub](https://github.com/neuropoly/data-management/tree/master/scripts) or under the `code` folder of already existing datasets.

```{important}
Once the data are converted to BIDS and [uploaded](git-datasets.md#upload) to git-annex repository, please delete the temporary folder.
```

## Naming the dataset

Accurately naming our datasets is essential for effective data management and eliminating any ambiguity about their content. This practice significantly reduces the time required to select data for any project.

**Syntax:**
~~~
animal-pathology-condition-anatomy-study-field-modality
~~~

**Keys/Values:**
~~~
- animal = {human, dog, cat, rat, mouse, ...}. Default=human
- pathology = {hc, ms, sci}. Default=hc
- condition = {invivo, exvivo}. Default=invivo
- anatomy = {sc, gm, csf, brainstem, axon, myelin, ...}. Default=sc
- study = Study/site associated with the dataset. Example: canproco, zurich, mni. Default=None
- field = {3t, 7t}. Do not specify if multiple strengths are present Default = 3t.
- modality = {t1, t2, t2star, dwi, psir, stir, sem, tem, oi, ct, ...}. Do not specify if multiple contrasts/modalities are present. Default=None
~~~

> [!NOTE]  
> Default fields can be ommited to avoid long names.

**Examples:**
~~~
ms-basel-mp2rage
hc-spinegeneric
ms-exvivo-nih
~~~


## Building the `raw` dataset

The `raw` dataset corresponds to the core dataset that contains all the different acquisitions generated for one or several subjects. **NO** postprocessing steps should be applied to these acquisitions.

Subjects folders in the `raw` dataset are structured as follows for MRI, with folders corresponding to subjects, [sessions] and MRI modalities:

### Raw structure

Useful BIDS specifications are:
- [File naming conventions](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#filesystem-structure), 
- [Modality-agnostic conventions](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code),
- [MRI-specific conventions](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html),
- [Microscopy-specific conventions](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html)

The example below applies for MRI data:

```
├── README.md
├── dataset_description.json
├── participants.tsv
├── participants.json
├── code/
│   └── curate.py
├── sub-<label>/
│   └── [ses-<label>/]
│        ├── anat/
│        │   ├── sub-<label>[_ses-<label>][_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>][_part-<mag|phase|real|imag>]_<suffix>.json
│        │   └── sub-<label>[_ses-<label>][_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>][_part-<mag|phase|real|imag>]_<suffix>.nii[.gz]
│        ├── fmap/
│        ├── func/
│        └── dwi/
│            ├── sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.bval
│            ├── sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.bvec
│            ├── sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.json
│            └── sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.nii[.gz]
```

```{note}
[Brackets] are characterizing optional informations
```

### Subject naming convention

**Basic convention**: `sub-XXX`

Example:

```
sub-001
sub-002
```

**Multi-institution/Multi-pathology convention**: `sub-\<site>\<pathology>XXX`

Example of Multi-institution dataset:

```
sub-mon001      # mon stands for Montreal
sub-tor001      # tor stands for Toronto
```

Example of Multi-institution/Multi-pathology dataset:

In the case of multi-pathology dataset (two or more distinct diseases + healthy controls), it is convenient to include also pathology to the subjectID, for example:

```
sub-torDCM001      # tor stands for Toronto and DCM stands for Degenerative Cervical Myelopathy
sub-torHC001       # tor stands for Toronto and HC stands for Healthy Controls
sub-zurSCI001      # zur stands for Zurich and SCI stands for Spinal Cord Injury
```


### Raw entities

Characterized by a key word (sub, ses, acq, etc.) and a value (label = an alphanumeric value, index = a nonnegative integer, etc) separated with a dash `-`
- `sub-<label>`
- `[ses-<label>]`
- `[acq-<label>]`
- `[ce-<label>]`
- `[rec-<label>]`
- `[run-<index>]`
- `[part-<mag|phase|real|imag>]`
- `[dir-<label>]`

Multiple entities can be used, but they must be separated using underscores `_`

Examples of special cases below:

- If you need to **differentiate spinal cord images from the brain** within the same dataset, use the `acq-cspine` tag. For example, `sub-001_acq-cspine_T1w.nii.gz`. We opted for `acq-cspine` tag (see [BIDS template](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#anatomy-imaging-data)) because `bp-cspine` is not currently supported by the BIDS convention (see [BEP25](https://docs.google.com/document/d/1chZv7vAPE-ebPDxMktfI9i1OkLNR2FELIfpVYsaZPr4/edit) BIDS extension proposal).
- If you need to differentiate between sequences acquired with **different orientations**, use the `acq-ax`, `acq-cor`, or `acq-sag` tag. For example, `sub-001_acq-ax_T1w.nii.gz`.
- If you need to differentiate between different **magnetization transfer (MT)** sequences, use the [`flip-<index>_mt-<on|off>`](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#anatomy-imaging-data) tag. For example, `sub-001_flip-1_mt-on_MTS.nii.gz`, `sub-001_flip-1_mt-off_MTS.nii.gz` or `sub-001_flip-2_mt-off_MTS.nii.gz`.

> [!NOTE]
> "old" vs "new" MT naming ([source](https://github.com/spine-generic/data-multi-subject/pull/135#issue-1535423905)):
> ```console
> acq-MTon_MTS → flip-1_mt-on_MTS
> acq-MToff_MTS → flip-1_mt-off_MTS
> acq-T1w_MTS → flip-2_mt-off_MTS
> ```

```{note}
If you to combine several above mentioned tags, use camelCase. For example, `sub-001_acq-cspineSag_T1w.nii.gz`.
```

### Raw suffixes

An alphanumeric string located after all the entities following a final underscore `_` (i.e. the `<suffix>`). This suffix corresponds for MRI to the MRI contrast:
- `T1w`
- `MP2RAGE`
- `dwi`
- etc.

Only **ONE** suffix can be used within the filename.

```{note}
For localizer/scout images, you can use `<entities>_acq-localizer_T1w.nii.gz`. (Relevant discussion [here](https://github.com/neuropoly/data-management/issues/325#issuecomment-2186894284) and [here](https://neurostars.org/t/how-to-name-localizer-scans-in-bids/29720/2).)
```

### Raw extensions

 Files extensions:
- `.nii.gz`
- `.json`
- `.bval`
- etc.


### `README.md`

The [`README.md`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#readme) is a [markdown](https://markdown-guide.readthedocs.io/en/latest/index.html) file describing the dataset in more detail.

Please use the `README.md` template below:

```
# <NAME OF DATASET>

This is an <MRI/Microscopy> dataset acquired in the context of the <XYZ> project. 
<IF DATASET CONTAINS DERIVATIVES>It also contains <manual segmentation/labels> of <MS lesions/tumors/etc> from <one/two/or more> expert raters located under the derivatives folder.

## Contact Person

Dataset shared by:
- <NAME>, <EMAIL>
<IF THERE WAS EMAIL COMM>Email communication: <DATE OF EMAIL AND SUBJECT>
<IF THERE IS A PRIMARY PROJECT/MODEL>Repository: https://github.com/<organization>/<repository_name>

## Publishing with the dataset

If you publish with this dataset, please add the following co-authors:
- <NAME>, <EMAIL>
- <NAME>, <EMAIL>
- <NAME>, <EMAIL>
...

Please also include the following grant/funding acknowledgment in your publication:
"Supported by ..."

## <IF DATA ARE MISSING FOR SOME SUBJECT(S)>missing data

<LIST HERE MISSING SUBJECTS>
```

### `dataset_description.json`

The [`dataset_description.json`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson) is a JSON file describing the dataset.

Please use the `dataset_description.json` template below:
    
```json
{
    "BIDSVersion": "1.9.0",
    "Name": "<dataset_name>",
    "DatasetType": "raw"
}
```

```{note}
Refer to the [BIDS spec](https://bids-specification.readthedocs.io/) to know what version to fill in here.
```


### `participants.tsv`

The [`participants.tsv`](https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/data-summary-files.html#participants-file) is a Tab-separated value file that lists all subjects in the dataset with useful metadata. Please start off from the example below:

```tsv
participant_id	source_id	species	age	sex	pathology	institution
sub-001	001	homo sapiens	30	F	HC	montreal
sub-002	005	homo sapiens	40	M	MS	montreal
sub-003	032	homo sapiens	n/a	O	MS	montreal
sub-004	007	homo sapiens	n/a	n/a	MS	toronto
```

Additional notes:
- Authorized values for `pathology` are listed under [`participants.json`](#participantsjson).
- Indicate missing values with `n/a` (for "not available"), not by empty cells!
- In the example above, the apparent mismatch between 'pathology' and the values is caused by the tabs
- Other columns can be added if the metadata are relevant


### `participants.json`

The [`participants.json`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file) is a JSON file providing a legend for the columns in `participants.tsv`, with longer descriptions, units, and in the case of categorical variables, allowed levels. Please use the template below:

```json
{
    "participant_id": {
        "Description": "Unique Participant ID",
        "LongName": "Participant ID"
    },
    "source_id": {
        "Description": "Subject ID in the source unprocessed data",
        "LongName": "Subject ID in the source unprocessed data"
    },
    "species": {
        "Description": "Binomial species name of participant",
        "LongName": "Species"
    },
    "age": {
        "Description": "Participant age",
        "LongName": "Participant age",
        "Units": "years"
    },
    "sex": {
        "Description": "sex of the participant as reported by the participant",
        "Levels": {
            "M": "male",
            "F": "female",
            "O": "other"
        }
    },
    "pathology": {
        "Description": "The diagnosis of pathology of the participant",
        "LongName": "Pathology name",
        "Levels": {
            "HC": "Healthy Control",
            "DCM": "Degenerative Cervical Myelopathy (synonymous with CSM - Cervical Spondylotic Myelopathy)",
            "MildCompression": "Asymptomatic cord compression, without myelopathy",
            "MS": "Multiple Sclerosis",
            "PD": "Parkinson's Disease",
            "SCI": "Traumatic Spinal Cord Injury"
        }
    },
    "institution": {
        "Description": "Human-friendly institution name",
        "LongName": "BIDS Institution ID"
    },
    "notes": {
        "Description": "Additional notes about the participant. For example, if there is more information about a disease, indicate it here.",
        "LongName": "Additional notes"
    }
}
```

### `code/`

The data cleaning and curation script(s) that create the `sub-XXX/` folders should be kept with them, under the [`code/`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code) folder. Within reason, every dataset should have a script that when run like

```
python code/curate.py path/to/sourcedata ./
```
    
unpacks, converts and renames all the images and related files in `path/to/sourcedata/` into BIDS format in the current dataset `./`.

This program should be committed first, before the curated data it produces. Afterwards, every commit that modifies the code should also re-run it, and the code and re-curated data should be committed in tandem.

```{note}
Analysis scripts should not be kept here. Keep them in separate repositories, usually in public on GitHub, with instructions about.
```


## Building the `derivatives` datasets

First, it is important to understand what are [BIDS derivatives](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html#bids-derivatives) folders:

> Derivatives are outputs of common processing pipelines, capturing data and meta-data sufficient for a researcher to understand and (critically) reuse those outputs in subsequent processing. Standardizing derivatives is motivated by use cases where formalized machine-readable access to processed data enables higher level processing.

Derivative folders are derived datasets generated from a raw dataset. They must include **ONLY** processed data obtained from a specific raw dataset (e.g., segmentations, masks, labels).

```{warning}
In this section we decided not to fully follow the BIDS derivatives convention. For more information please see our related [issue](https://github.com/neuropoly/data-management/issues/282). 
```


### Derivatives structure

According to BIDS, derived datasets could be stored inside a parent folder [`derivatives/`](https://bids-specification.readthedocs.io/en/stable/common-principles.html#storage-of-derived-datasets) _"to make a clear distinction between raw data and results of data processing"_. This folder should also follow the same folder logic as the one used for the `raw` data.

Derivative data obtained using different processes/workflows should ideally be stored using different derivatives folders. Eg:
- `derivatives/labels/`
- `derivatives/sct_5.6/`
- `derivatives/fmriprep_2.3/`

```{note}
Despite what is written above, to streamline data identification and reduce the need for extensive folder crawling, we [opted](https://github.com/neuropoly/data-management/issues/282) for common folder names, such as `labels/`, that typically contains binary segmentation and point-wise labels.
```

Derived datasets follow the **same structure and hierarchy** as the `raw` dataset, with folders corresponding to subjects, [sessions] and MRI modalities:

```
├── README.md
├── dataset_description.json
├── participants.tsv
├── participants.json
├── code/
├── sub-<label>/
└── derivatives/
    └── <label>  <-- name of the derivative folder
        └── sub-<label>/]
            └── [ses-<label>/]
                └── data type/  <-- could be 'anat', 'fmap', 'func', etc.
                    └── <source_filename>[_space-<space>][_res-<label>][_den-<label>][_desc-<label>]_<suffix>.<extension>
```

```{warning}
Entities and suffixes are different from those used with the raw filenames and are specific to [data types](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#imaging-data-types).
```

```{note}
Because derived datasets are datasets, files and folders presented in the raw template section could also be included in this dataset (e.g. README.md, code/, etc.)
```


### `<source_filename>`

This element corresponds to the entire source filename, with the **omission** of the extension. For example, if the source file name is `sub-02_acq-MTon_MTS.nii.gz`, the `<source_filename>` to be used for the derivatives is `sub-02_acq-MTon_MTS`.


### Derivative entities

Characterized by a key word (space, res, den, etc.) and a value (label = an alphanumeric value, index = a nonnegative integer, etc) separated with a dash `-`
- `[space-<space>]`: image space if different from raw space: template space (e.g. MNI305 etc), orig, other etc. (see [BIDS](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html#spatial-references))
- `[res-<label>]`: for changes in resolution
- `[den-<label>]`: for changes related to density
- `[desc-<label>]`: should be used to distinguish two files that do not otherwise have a distinguishing entity. (e.g. `sub-001_UNIT1_desc-denoised.nii.gz`)
- `[label-<label>]`: to avoid confusion if multiple masks are available we have to specify the masked [structure](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#common-image-derived-labels) (i.e. `_label-WM` for white matter, `_label-GM` for gray matter, `_label-lesion` for lesions etc.)

Entities are then separated using underscores `_`


### Derivative suffixes

An alphanumeric string located after all the entities following a final underscore `_` :

| Image type (suffix) | Associated entities | Description |
| :---: | :---: | --- |
|`seg`| `label-<label>` | Suffix used for binary masks (0 and 1 only). The entity is used to specify the segmented structure in the image. |
|`dseg`| `label-<label>` | Suffix used for discrete segmentations representing multiple anatomical structures. The entity is used to specify the atlas used to map the different structures. |
|`softseg`| `label-<label>` | Suffix used for soft segmentations representing anatomical structures with values ranging from 0 to 1. The entity is used to specify the segmented structure in the image.|
|`label`| `label-<label>` | Suffix used for binary labels (0 and 1 only). The entity is used to specify the type of structure labeled in the image. |
|`dlabel`| `label-<label>` | Suffix used for discrete labels representing multiple anatomical structures. The entity is used to specify the atlas used to label the different structures |

```{warning}
Here, the corresponding entity `label-<label>` is mandatory to specify the labeled region.
```


### Derivatives extensions

 Files extensions:
- `.nii.gz`
- `.json`
- etc.

In addition to the subjects folders, derived datasets must include their own `dataset_description.json` file to track all the processing steps used to create the data. Example:


### `derivatives/labels/dataset_description.json`
    
```json
{
    "BIDSVersion": "1.9.0",
    "Name": "<dataset_name>",
    "DatasetType": "derivative"
}
```


### `derivatives/labels/descriptions.tsv`

To provide more details about the processing steps (e.g., reorientation, resampling), a [`descriptions.tsv`](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html#descriptionstsv) file may be added at the root of the folder. This file must contain at least two columns:
- `desc_id`: contains all the labels used with the [desc](https://bids-specification.readthedocs.io/en/stable/appendices/entities.html#desc) entity within the filenames accross the entire dataset.
- `description`: human readable descriptions


### JSON sidecars

JSON sidecars are companion files linked to data files. They share the same filenames but have a ".json" extension. These files store essential metadata, serving as guidebooks to provide crucial details about the associated data, ensuring organized and comprehensive information.

Therefore, to improve the way we track our data, `.json` sidecars have to be generated for each data present in derived datasets. Here are few examples of JSON sidecar:

Below is a JSON sidecar describing a fully-manual labels created in the ORIGINAL SPACE:
    
```json
{
    "SpatialReference": "orig",
    "GeneratedBy": [
        {
            "Name": "Manual",
            "Author": "Nathan Molinier",
            "Date": "2023-07-14 13:43:10"
        }
    ]
}
```

If the label was previously produced by an automatic algorithm, append to the `GeneratedBy` section:
    
```json
{
    "SpatialReference": "orig",
    "GeneratedBy": [
        {
            "Name": "sct_deepseg_sc",
            "Version": "SCT v6.1"
        },
        {
            "Name": "Manual",
            "Author": "Nathan Molinier",
            "Date": "2023-07-14 13:43:10"
        }
    ]
}
```

If the label is created _after_ the data was resampled and cropped, indicate it under `SpatialReference`:
    
```json
{
    "SpatialReference": {
        "ResamplingFactor": "2",
        "Interpolation": "spline",
        "Xmin": 5,
        "Xmax": 95,
        "Ymin": 2,
        "Ymax": 18,
        "Zmin": 4,
        "Zmax": 100
    },
    "GeneratedBy": [
        {
            "Name": "sct_resample",
            "Version": "SCT v6.1"
        },
        {
            "Name": "sct_crop_image",
            "Version": "SCT v6.1"
        }
    ]
}
```

Another example of a label created in another space than the image (here: the PAM50 template space):

```json
{
    "SpatialReference": "PAM50",
    "GeneratedBy": [
        {
            "Name": "sct_register_to_template",
            "Version": "SCT v6.1"
        }
    ]
}
```

```{warning}
For better clarity, if the image space is different between the raw data and the label (as is the case above), the entity `space-other` **MUST** also be used in the filename. For templates, the entity `space-template` or `space-<template_name>` (e.g. `space-PAM50`) may be used instead.
```



### Label names

To be consistent regarding the way anatomical regions will be referred to, please follow this table (based on the BIDS [labels](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#common-image-derived-labels)):

| label | Description |
| --- | --- |
| SC | Spinal Cord |
| GM | Gray Matter |
| WM | White Matter |
| discs | Intervertebral discs, with values following [this convention](https://spinalcordtoolbox.com/user_section/tutorials/vertebral-labeling/labeling-conventions.html) |
| vertebrae | Vertebrae, with values following [this convention](https://spinalcordtoolbox.com/user_section/tutorials/vertebral-labeling/labeling-conventions.html) |
| rootlets | Spinal rootlets |
| PMJ | Pontomedullary Junction, indicated as a single voxel with a value '50' |
| CSF | Cerebrospinal Fluid |
| canal | Spinal canal |
| compression | Spinal Cord Compression, indicated as a single voxel with a value '1' at the point of compression. There can be more than one compression. |
| lesion | Lesion (e.g., multiple sclerosis plaques, spinal cord injury lesions). The pathology associated with the lesion is indicated in the file `participants.tsv` |
| tumor | Tumor |
| edema | Edema |
| cavity | Cavity |
| axon | Axon (used in microscopy datasets) |
| myelin | Myelin (used in microscopy datasets) |

When multiple anatomical regions are present in the image, atlases should be used. When specified, these atlases **SHOULD** be added to a folder `atlases/` at the root of the derivative folder or a URL should be included inside the json sidecars.


### Examples and use cases

Here is an example of a dataset structure with a single subject `sub-001`:

```
sci-bordeaux
├── README.md
├── dataset_description.json
├── participants.tsv
├── participants.json
├── code/
│   └── curate.py
│
├── sub-001
│   └── anat
│       ├──sub-001_acq-sag_T2w.nii.gz
│       └──sub-001_acq-sag_T2w.json
│
└── derivatives
    └── labels
        ├── dataset_description.json
        ├── README.md
        └── sub-001
            └── anat
                ├── sub-001_acq-sag_T2w_label-SC_seg.nii.gz  # spinal cord (SC) binary segmentation 
                ├── sub-001_acq-sag_T2w_label-SC_softseg.nii.gz  # spinal cord (SC) soft segmentation
                ├── sub-001_acq-sag_T2w_label-discs_dlabel.nii.gz  # discrete discs labeling
                ├── sub-001_acq-sag_T2w_label-vertebrae_dseg  # vertebrae discrete segmentation (segmented stuctures have different values based on the vertebral levels)
                ├── sub-001_acq-sag_T2w_label-rootlets_dseg  # nerve rootlets discrete segmentation
                ├── sub-001_acq-sag_T2w_label-compression_label.nii.gz  # binary compression labeling
                ├── sub-001_acq-sag_T2w_label-PMJ_dlabel  # Pontomedullary junction, indicated as a single voxel with a value '50'
                └── sub-001_acq-sag_T2w_label-lesion_seg  # lesion binary segmentation
```


## Changelog policy

We use `git log` to track our changes. That means care should be taken to [write good messages](../geek-tips/git.md#commit-message-convention): they are there to help both you and future researchers understand how the dataset evolved.

Good commit message examples:

```
git commit -m 'Segment spines of subjects 010 through 023
    
Produced manually, using fsleyes.'
```

or

```
git commit -m 'Add new subjects provided by <email_adress>'
```
    
If you choose to also fill in BIDS's optional [CHANGES](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#changes) file make sure it reflects the `git log`.
