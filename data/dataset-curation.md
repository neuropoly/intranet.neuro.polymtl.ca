# Dataset curation

## Converting data to BIDS

All git-annex datasets should be BIDS-compliant. For more information about the BIDS standard, please visit [http://bids.neuroimaging.io](http://bids.neuroimaging.io).

When you receive data from an external collaborator, you can save them under a temporary location: `duke/temp`.

Then, inspect the data and convert them to BIDS. It is recommended to write a script that does the conversion. The 
script should then be saved under the `code` folder of the final dataset. Some previous scripts can be found on 
[GitHub](https://github.com/neuropoly/data-management/tree/master/scripts) or under the `code` folder of already existing datasets.

Once the data are converted to BIDS and [uploaded](git-datasets.md#upload) to git-annex repository, delete the temporary folder to save space.

## Building the `raw` dataset

> [Brackets] are characterizing optional informations

The `raw` dataset corresponds to the core dataset that contains all the different acquisition generated for one or several subjects. **NO** postprocessing steps should be applied to these acquisitions.

### Folders structure and filenames

Subjects folders in the `raw` dataset are structured as follows for MRI, with folders corresponding to subjects, [sessions] and MRI modalities:

#### Raw structure

```
sub-<label>/
    [ses-<label>/]
        anat/
            sub-<label>[_ses-<label>][_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>][_part-<mag|phase|real|imag>]_<suffix>.json
            sub-<label>[_ses-<label>][_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>][_part-<mag|phase|real|imag>]_<suffix>.nii[.gz]
        dwi/
            sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.bval
            sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.bvec
            sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.json
            sub-<label>[_ses-<label>][_acq-<label>][_rec-<label>][_dir-<label>][_run-<index>][_part-<mag|phase|real|imag>]_dwi.nii[.gz]
```

```{note}
Data collected from actual subjects goes under their specific sub-folder
```

#### Subject naming convention

**Basic convention**: sub-XXX

Example:

```
sub-001
sub-002
```

**Multi-institution/Multi-pathology convention**: sub-\<site>\<pathology>XXX

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

Regarding BIDS filenames, they are constructed using 3 types of elements:


#### Raw entities

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

```{note}
If you to combine several above mentioned tags, use camelCase. For example, `sub-001_acq-cspineSagittal_T1w.nii.gz`.
```

#### Raw suffixes

An alphanumeric string located after all the entities following a final underscore `_` (i.e. the `<suffix>`). This suffix corresponds for MRI to the MRI contrast:
- `T1w`
- `MP2RAGE`
- `dwi`
- etc.

Only **ONE** suffix can be used within the filename.


#### Raw extensions

 Files extensions:
- `.nii.gz`
- `.json`
- `.bval`
- etc.

#### Other modalities

Many kinds of data have a place specified for them by BIDS. See [file naming conventions](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#filesystem-structure) and the [MRI](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html) and [Microscopy](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html) extensions for full details.


### Raw template

⚠️ In addition to the subjects folders, every `raw` dataset must include the following files: 

```
├── README.md
├── dataset_description.json
├── participants.tsv
├── participants.json
├── code/
│   └── curate.py
├── sub-XXX
│   └── anat
│       └──sub-XXX_T1w.nii.gz
 ...
```

For details, see [BIDS specification](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code).

#### `README.md`

The [`README.md`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#readme) is a [markdown](https://markdown-guide.readthedocs.io/en/latest/index.html) file describing the dataset in more detail.

Please use the `README.md` template below:

```
# <NAME OF DATASET>

This is an <MRI/Microscopy> dataset acquired in the context of the <XYZ> project. 
<IF DATASET CONTAINS DERIVATIVES>It also contains <manual segmentation/labels> of <MS lesions/tumors/etc> from <one/two/or more> expert raters located under the derivatives folder.

## Contact Person

Dataset shared by: <NAME AND EMAIL>
<IF THERE WAS EMAIL COMM>Email communication: <DATE OF EMAIL AND SUBJECT>
<IF THERE IS A PRIMARY PROJECT/MODEL>Repository: https://github.com/<organization>/<repository_name>

## <IF DATA ARE MISSING FOR SOME SUBJECT(S)>missing data

<LIST HERE MISSING SUBJECTS>
```

#### `dataset_description.json`

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
    
 ```{warning}
The `dataset_description.json` file within the top-level dataset should include `"DatasetType": "raw"`.
 ```


#### `participants.tsv`

The [`participants.tsv`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file) is a TSV file and should include at least the following columns:

| participant_id | source_id | species | age | sex | pathology  | institution |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| sub-001 | 001 | homo sapiens | 30 | F | HC | montreal |
| sub-002 | 005 | homo sapiens | 40 | O | MS | montreal |
| sub-003 | 007 | homo sapiens  | n/a | n/a | MS | toronto |

Authorized values for `pathology` are listed under [`participants.json`](#participantsjson).

Please use the `participants.tsv` template below:
    
```
participant_id	source_id	species	age	sex	pathology	institution
sub-001	001	homo sapiens	30	F	HC	montreal
sub-002	005	homo sapiens	40	O	MS	montreal
sub-003	007	homo sapiens	n/a	n/a	MS	toronto
```

Other columns may be added if the data exists to fill them and it would be useful to keep.

```{warning}
Indicate missing values with `n/a` (for "not available"), not by empty cells!
```

```{warning}
This is a Tab-Separated-Values file. Make sure to use tabs between entries if editing with a text editor. Most spreadsheet software can read and write .tsv correctly.
```


#### `participants.json`

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

#### `code/`

The data cleaning and curation script(s) that create the `sub-XXX/` folders should be kept with them, under the [`code/`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code) folder. Within reason, every dataset should have a script that when run like

```
python code/curate.py path/to/sourcedata ./
```
    
unpacks, converts and renames all the images and related files in `path/to/sourcedata/` into BIDS format in the current dataset `./`.

This program should be committed first, before the curated data it produces. Afterwards, every commit that modifies the code should also re-run it, and the code and re-curated data should be committed in tandem.

```{note}
Analysis scripts should not be kept here. Keep them in separate repositories, usually in public on GitHub, with instructions about. See [PIPELINE-DOC](TODO-PIPELINE-DOC).
```


## Building the `derivative` datasets

First, it is important to understand what are [BIDS derivatives](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html#bids-derivatives) folders:

> Derivatives are outputs of common processing pipelines, capturing data and meta-data sufficient for a researcher to understand and (critically) reuse those outputs in subsequent processing. Standardizing derivatives is motivated by use cases where formalized machine-readable access to processed data enables higher level processing.

Basically, derivative folders are derived datasets generated from a raw dataset. They must include **ONLY** processed data obtained from a specific raw dataset (i.e. segmentations, masks, labels...).

```{warning}
Derivative data obtained using DIFFERENT processes/workflows should be stored using DIFFERENT derivatives folders. Eg:
- `derivatives/labels/`
- `derivatives/sct_5.6/`
- `derivatives/fmriprep_2.3/`
```

```{note}
According to BIDS, derived datasets could be stored inside a parent folder [`derivatives/`](https://bids-specification.readthedocs.io/en/stable/common-principles.html#storage-of-derived-datasets) _"to make a clear distinction between raw data and results of data processing"_. This folder should also follow the same folder logic as the one used for the `raw` data.
```

### Folders structure and filenames

Here, we describe how the `derivative` folder should be organized.

```{note}
In the guideline below, [brackets] refer to optional items.
```

#### Derivatives structure

Derived datasets follow the **same structure and hierarchy** as the `raw` dataset, with folders corresponding to subjects, [sessions] and MRI modalities:

```
sub-<label>/
    [ses-<label>/]
        modality/
            <source_entities>[_space-<space>][_res-<label>][_den-<label>][_desc-<label>]_<suffix>.<extension>
```

Regarding derivatives filenames, we can identify the same 3 type of elements as before (entities, suffixes and extensions) plus 1 extra-consideration related to the raw data:

```{warning}
Entities and suffixes are different from those used with the raw filenames and are specific to [data types](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#imaging-data-types).
```

#### `<source_entities>`

This element corresponds to the entire source filename, with the **omission** of the source suffix and extension. For example, if the source file name is `sub-02_acq-MTon_MTS.nii.gz`, the `<source_entities>` to be used for the derivatives is `sub-02_acq-MTon`.

```{note}
For MRI, it means that the contrast needs to be removed from the filename (see [here](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html#file-naming-conventions)). The desc-<label> entity will be used instead (i.e. `_desc-T1w` and `_desc-T2w`).
```


#### Derivative entities

Characterized by a key word (space, res, den, etc.) and a value (label = an alphanumeric value, index = a nonnegative integer, etc) separated with a dash `-`
- `[space-<space>]`: image space if different from raw space: template space (i.e. MNI305 etc), orig, other etc. (see [BIDS](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html#spatial-references))
- `[res-<label>]`: for changes in resolution
- `[den-<label>]`: for changes related to density
- `[desc-<label>]`: [should](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html#file-naming-conventions) be used to specify the contrast (i.e. `_desc-T1w` and `_desc-T2w`)
- `[label-<label>]`: to avoid confusion if multiple masks are available we can specify the masked [structure](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#common-image-derived-labels) (i.e. `_label-WM` for white matter, `_label-GM` for gray matter, `_label-L` for lesions etc.)
- `[seg-<label>]`: to specify the atlas used when multiple structures are present in the image

Entities are then separated using underscores `_`


#### Derivative suffixes

An alphanumeric string located after all the entities following a final underscore `_` :

| Image type (suffix) | Associated entities | Description |
| :---: | :---: | --- |
|`mask`| `label-<label>` | Suffix used for binary masks (0 and 1 only). The entity is used to specify the structure masked in the image. |
|`dseg`| `seg-<label>` | Suffix used for discrete segmentations representing multiple anatomical structures. The entity is used to specify the atlas used to map the different structures. |
|`probseg`| `seg-<label>` or `label-<label>` | Suffix used for probabilistic segmentations representing anatomical structures with values ranging from 0 to 1. The entity `label` is used if only one structure is present in the image. If more structures are present (image with more dimensions) the `seg` entity must be used and structures have to be added to the JSON file (see [BIDS](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#probabilistic-segmentations)).|
|`blabel` (**NOT BIDS**)| `label-<label>` | Suffix used for binary labels (0 and 1 only). The entity is used to specify the type of structure labeled in the image. |
|`dlabel` (**NOT BIDS**)| `seg-<label>` | Suffix used for discrete labels representing multiple anatomical structures. The entity is used to specify the atlas used to label the different structures |

```{warning}
These associated entities can only be used with these specific suffixes! This association depends on the imaging data [type](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#imaging-data-types).
```

#### Derivatives extensions

 Files extensions:
- `.nii.gz`
- `.json`
- etc.


### Derivative template

In addition to the subjects folders, derived datasets must include their own `dataset_description.json` file to track all the processing steps used to create the data. Example:


#### `dataset_description.json`
    
```json
{
    "BIDSVersion": "1.9.0",
    "Name": "<dataset_name>",
    "DatasetType": "derivative",
    "GeneratedBy": [
        {
            "Name": "sct_deepseg_sc",
            "Version": "SCT v6.1"
        },
        {
            "Name": "Manual",
            "Description": "Manually corrected by Nathan Molinier and Pierre-Louis Benveniste."
        }
    ]
}
```

```{warning}
The `dataset_description.json` file within the derived dataset should include `"DatasetType": "derivative"`.
```


```{note}
If more details about the processing steps used have to be provided (e.g., reorientation, resampling etc.), a [`descriptions.tsv`](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html#descriptionstsv) file may be added at the root of the folder. This file must contain at least two columns:
- `desc_id`: contains all the labels used with the [desc](https://bids-specification.readthedocs.io/en/stable/appendices/entities.html#desc) entity within the filenames accross the entire dataset.
- `description`: human readable descriptions
```

```{note}
Because derived datasets are datasets, files and folders presented in the raw template section could also be included in this dataset (e.g. README.md, code/, etc.)
```

### JSON sidecars

JSON sidecars are companion files linked to data files. They share the same filenames but have a ".json" extension. These files store essential metadata, serving as guidebooks to provide crucial details about the associated data, ensuring organized and comprehensive information.

Therefore, to improve the way we track our data, `.json` sidecars will have to be generated for each data present in derived datasets. Here are few examples of JSON sidecar:

<details>
<summary>JSON sidecar (ORIGINAL SPACE)</summary>
    
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

</details>

<details>
<summary>JSON sidecar (RESAMPLED and CROPPED)</summary>
    
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

</details>

<details>
<summary>JSON sidecar (PAM50 SPACE)</summary>
    
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

</details>

```{note}
If the image space is different from the original image, the entity `space-<label>` has to be used. The entity `space-template` may be used for templates and `space-other` for other transformations.
```

### Regions and atlases

To be consistent regarding the way anatomical regions will be referred to, please follow this table (based on the BIDS [labels](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#common-image-derived-labels)):

| Abbreviation (label) | Description |
| :---: | :---: |
| SC | Spinal Cord |
| GM | Gray Matter |
| WM | White Matter |
| MS | Multiple Sclerosis Lesion |
| SCI | Spinal Cord Injury Lesion |
| CSF | Cerebrospinal Fluid |
| compression | Spinal Cord Compression |
| tumor | Tumor |
| edema | Edema |
| cavity | Cavity |
| axon | Axon |
| myelin | Myelin |

When multiple anatomical regions are present in the image, atlases should be used. When specified, these atlases **SHOULD** be added to a folder `atlases/` at the root of the derivative folder.

### Examples and use cases

Let's consider a dataset with one single subject `sub-001`. This dataset comes from a clinical partner who segmented spinal cord injury (SCI) lesions and created point labels for spinal cord (SC) compressions. Based on this dataset, we decide to generate SC segmentations and disc labels. Here is the structure of the final dataset:

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
    │       └──sub-001_acq-sag_T1w.nii.gz
    │       └──sub-001_acq-sag_T2w.nii.gz
    │
    └── derivatives
        ├── clinical-labels
        │   ├── dataset_description.json
        │   ├── README.md
        │   └── sub-001
        │           └── anat
        │               ├── sub-001_acq-sag_label-SCI_desc-T1w_mask.nii.gz
        │               ├── sub-001_acq-sag_label-SCI_desc-T1w_mask.json
        │               ├── sub-001_acq-sag_label-compression_desc-T1w_blabel.nii.gz
        │               ├── sub-001_acq-sag_label-compression_desc-T1w_blabel.json
        │               ├── sub-001_acq-sag_label-SCI_desc-T2w_mask.nii.gz
        │               ├── sub-001_acq-sag_label-SCI_desc-T2w_mask.json
        │               ├── sub-001_acq-sag_label-compression_desc-T2w_blabel.nii.gz
        │               └── sub-001_acq-sag_label-compression_desc-T2w_blabel.json
        │
        ├── SC-masks
        │   ├── dataset_description.json
        │   ├── README.md
        │   └── sub-001
        │           └── anat
        │               ├── sub-001_acq-sag_label-SC_desc-T1w_mask.nii.gz
        │               ├── sub-001_acq-sag_label-SC_desc-T1w_mask.json
        │               ├── sub-001_acq-sag_label-SC_desc-T2w_mask.nii.gz
        │               └── sub-001_acq-sag_label-SC_desc-T2w_mask.json
        │
        └── disc-labels
            ├── dataset_description.json
            ├── README.md
            └── sub-001
                    └── anat
                        ├── sub-001_acq-sag_seg-discs_desc-T1w_dlabel.nii.gz
                        ├── sub-001_acq-sag_seg-discs_desc-T1w_dlabel.json
                        ├── sub-001_acq-sag_seg-discs_desc-T2w_dlabel.nii.gz
                        └── sub-001_acq-sag_seg-discs_desc-T2w_dlabel.json

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
