# Dataset curation

## I - Converting data to BIDS

All git-annex datasets should be BIDS-compliant. For more information about the BIDS standard, please visit [http://bids.neuroimaging.io](http://bids.neuroimaging.io).

When you receive data from an external collaborator, you can save them under a temporary location: `duke/temp`.

Then, inspect the data and convert them to BIDS. It is recommended to write a script that does the conversion. The 
script should then be saved under the `code` folder of the final dataset. Some previous scripts can be found on 
[GitHub](https://github.com/neuropoly/data-management/tree/master/scripts) or under the `code` folder of already existing datasets.

Once the data are converted to BIDS and [uploaded](git-datasets.md#upload) to git-annex repository, delete the temporary folder to save space.

## II - Building the `raw` dataset

> [Brackets] are characterizing optional informations

The `raw` dataset corresponds to the core dataset that contains all the different acquisition generated for one or several subjects. **NO** postprocessing steps should be applied to these acquisitions.

### Folders structure and filenames

Subjects folders in the `raw` dataset are structured as follows for MRI, with folders corresponding to subjects, [sessions] and MRI modalities:

<details>
<summary>Raw structure</summary>

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

</details>

```{note}
Data collected from actual subjects goes under their specific sub-folder
```

<details>
<summary>Subject naming convention</summary>

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
</details>

Regarding BIDS filenames, they are constructed using 3 types of elements:

<details>
<summary>Raw entities</summary>

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

</details>

<details>
<summary>Raw suffixes</summary>

An alphanumeric string located after all the entities following a final underscore `_` (i.e. the `<suffix>`). This suffix corresponds for MRI to the MRI contrast:
- `T1w`
- `MP2RAGE`
- `dwi`
- etc.

Only **ONE** suffix can be used within the filename.

</details>

<details>
<summary>Raw extensions</summary>

 Files extensions:
- `.nii.gz`
- `.json`
- `.bval`
- etc.

</details>

```{note}
If you need to differentiate spinal cord images from the brain, use the `acq-cspine` tag. For example, `sub-001_acq-cspine_T1w.nii.gz`.

ℹ️ We opted for `acq-cspine` tag (see [BIDS template](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#anatomy-imaging-data)) because `bp-cspine` is not currently supported by the BIDS convention (see [BEP25](https://docs.google.com/document/d/1chZv7vAPE-ebPDxMktfI9i1OkLNR2FELIfpVYsaZPr4/edit) BIDS extension proposal).
```

```{note}
If you need to differentiate between sequences acquired with different orientations, use the `acq-ax`, `acq-cor`, or `acq-sag` tag. For example, `sub-001_acq-ax_T1w.nii.gz`.
```

```{note}
If you need to differentiate between different magnetization transfer (MT) sequences, use the [`flip-<index>_mt-<on|off>`](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#anatomy-imaging-data) tag. For example, `sub-001_flip-1_mt-on_MTS.nii.gz`, `sub-001_flip-1_mt-off_MTS.nii.gz` or `sub-001_flip-2_mt-off_MTS.nii.gz`.
```

```{note}
If you to combine several above mentioned tags, use camelCase. For example, `sub-001_acq-cspineSagittal_T1w.nii.gz`.
```

```{note}
Many kinds of data have a place specified for them by BIDS. See [file naming conventions](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#filesystem-structure) and the [MRI](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html) and [Microscopy](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html) extensions for full details.
```

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

<details>
<summary>README.md</summary>

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
</details>

<details>
<summary>dataset_description.json</summary>

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
</details>

<details>
<summary>participants.tsv</summary>

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
</details>

<details>
<summary>participants.json</summary>

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
    }
    "notes": {
        "Description": "Additional notes about the participant. For example, if there is more information about a disease, indicate it here.",
        "LongName": "Additional notes"
    }
}
```
</details>

<details>
<summary>code/</summary>

The data cleaning and curation script(s) that create the `sub-XXX/` folders should be kept with them, under the [`code/`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code) folder. Within reason, every dataset should have a script that when run like

```
python code/curate.py path/to/sourcedata ./
```
    
unpacks, converts and renames all the images and related files in `path/to/sourcedata/` into BIDS format in the current dataset `./`.

This program should be committed first, before the curated data it produces. Afterwards, every commit that modifies the code should also re-run it, and the code and re-curated data should be committed in tandem.

```{note}
Analysis scripts should not be kept here. Keep them in separate repositories, usually in public on GitHub, with instructions about. See [PIPELINE-DOC](TODO-PIPELINE-DOC).
```
</details>

## III - Building the `derivative` datasets

> [Brackets] are characterizing optional informations

First, it is important to understand what are [BIDS derivatives](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html#bids-derivatives) folders:

"Derivatives are outputs of common processing pipelines, capturing data and meta-data sufficient for a researcher to understand and (critically) reuse those outputs in subsequent processing. Standardizing derivatives is motivated by use cases where formalized machine-readable access to processed data enables higher level processing."

Basically, derivative folders are derived datasets generated from a raw dataset. They must include **ONLY** processed data obtained from a specific raw dataset (i.e. segmentations, masks, labels...).

```{warning}
DIFFERENT data obtained using DIFFERENT processes/workflows should be stored using DIFFERENT derivatives folders.
```

```{note}
According to BIDS, derived datasets could be stored inside a parent folder [`derivatives/`](https://bids-specification.readthedocs.io/en/stable/common-principles.html#storage-of-derived-datasets) "to make a clear distinction between raw data and results of data processing". This folder should also follow the same folder logic as the one used for the `raw` data.
```

### Folders structure and filenames

Derived datasets follow the **same structure** as the `raw` dataset, with folders corresponding to subjects, [sessions] and MRI modalities. 

<details>
<summary>Derivatives structure</summary>

```
sub-<label>/
    [ses-<label>/]
        modality/
            <source_entities>[_space-<space>][_res-<label>][_den-<label>][_desc-<label>]_<suffix>.<extension>
```
</details>

```{warning}
The derived dataset must adhere to the identical folder hierarchy used for the raw dataset.
```

```{note}
Data generated for a specific subject will go under their specific sub-folder
```

Finally, regarding derivatives filenames, we can identify the same 3 type of elements as before (entities, suffixes and extensions) plus 1 extra-consideration related to the raw data:
> ⚠️ Entities and suffixes are different from those used with the raw filenames and are specific to [data types](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#imaging-data-types).

<details>
<summary>source_entities</summary>

This element corresponds to the entire source filename, with the **omission** of the source suffix and extension. 

```{note}
For MRI, the contrast will need to be removed from the filename (see [here](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html#file-naming-conventions)). The desc-<label> entity will be used instead (i.e. `_desc-T1w` and `_desc-T2w`).
```

</details>

<details>
<summary>Derivative entities</summary>

Characterized by a key word (space, res, den, etc.) and a value (label = an alphanumeric value, index = a nonnegative integer, etc) separated with a dash `-`
- `[space-<space>]`: image space if different from raw space: template space (i.e. MNI305 etc), individual, study etc. (see [BIDS](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html#spatial-references) for allowed spaces)
- `[res-<label>]`: for changes in resolution
- `[den-<label>]`: for changes related to density
- `[desc-<label>]`: [should](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html#file-naming-conventions) be used to specify the contrast (i.e. `_desc-T1w` and `_desc-T2w`)
- `[label-<label>]`: to avoid confusion if multiple masks are available we can specify the masked [structure](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#common-image-derived-labels) (i.e. `_label-WM` for white matter, `_label-GM` for gray matter, `_label-L` for lesions etc.)

Entities are then separated using underscores `_`

</details>

<details>
<summary>Derivative suffixes</summary>

An alphanumeric string located after all the entities following a final underscore `_` :
- `mask` for binary masks (0 and 1 only)
- `dseg` for discrete segmentations representing multiple anatomical structures
- `probseg` for probabilistic segmentations representing a single anatomical structure with values ranging from 0 to 1
- `plabel` (**NOT BIDS**)
- etc.

</details>

<details>
<summary>Derivatives extensions</summary>

 Files extensions:
- `.nii.gz`
- `.json`
- etc.

</details>


### Derivative template

⚠️  In addition to the subjects folders, derived datasets must include their own `dataset_description.json` file to track all the processing steps used to create the data. Example:

<details>
<summary>dataset_description.json</summary>
    
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

</details>

```{note}
If more details about the processing steps used have to be provided (e.g., reorientation, resampling etc.), a [`descriptions.tsv`](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html#descriptionstsv) file may be added at the root of the folder. This file must contain at least two columns:
- `desc_id`: contains all the labels used with the [desc](https://bids-specification.readthedocs.io/en/stable/appendices/entities.html#desc) entity within the filenames accross the entire dataset.
- `description`: human readable descriptions
```

```{note}
Because derived datasets are datasets, files and folders presented in the raw template section could also be included in this dataset (e.g. README.md, code/, etc.)
```

### json sidecars

> This section is part of an initiavite to improve our ability to track our data 

JSON sidecars are companion files linked to data files. They share the same filenames but have a ".json" extension. These files store essential metadata, serving as guidebooks to provide crucial details about the associated data, ensuring organized and comprehensive information.

Therefore, to improve the way we track our data, `.json` sidecars will have to be generated for each data present in derived datasets. This file will contain information about

<details>
<summary>dataset_description.json</summary>
    
```json
{
    "Space": "orig",
    "Type": "mask",
    "Region": "SC",
    "GeneratedBy": [
        {
            "Name": "sct_deepseg_sc",
            "Version": "SCT v6.1"
        },
        {
            "Name": "Manual",
            "Author": "Nathan Molinier",
            "Date": "2023-07-14 13:43:10"
            "Description": ""
        }
    ]
}
```

</details>

### Regions and atlases

To be consistent regarding the way anatomical regions will be reffered to, please follow this table (based on the BIDS [labels](https://bids-specification.readthedocs.io/en/stable/derivatives/imaging.html#common-image-derived-labels)):

| Abbreviation (label) | Description |
| :---: | :---: |
| SC || Spinal Cord |
| GM || Gray Matter |
| WM || White Matter |
| MSL || Multiple Sclerosis Lesion |
| SCIL || Spinal Cord Injury Lesion |
| CSF || Cerebrospinal Fluid |
| TUM || Tumor |
| ED || Edema |
| CAV || Cavity |
| AX || Axon |
| MYEL || Myelin |

When multiple anatomical regions are present in the image, atlases should be used. When specified, these atlases **SHOULD** be added to a folder `atlases/` at the root of the derivative folder.

### Examples and use case

Let's consider a dataset with one single subject `sub-001`. This dataset comes from a clinical partner who segmented spinal cord injuries (SCI) lesions and created point labels for spinal cord (SC) compressions. Based on this dataset, we decide to generate SC segmentations and discs labels.

Example:

```
...
...
├── sub-XXX
│   └── anat
│       └──sub-XXX_T1w.nii.gz
...
...
└── derivatives
    └── labels
        ├── dataset_description.json
        ├── sub-XXX
        │   ├── anat
        │   │   ├──sub-XXX_T1w_label-SC_seg.nii.gz
        │   │   ├──sub-XXX_T1w_label-SC_softseg.nii.gz
        │   │   ├──sub-XXX_T1w_label-SC_mask.nii.gz
        │   │   ├──sub-XXX_T1w_label-GM_seg.nii.gz
        │   │   ├──sub-XXX_T1w_label-WM_seg.nii.gz
        │   │   ├──sub-XXX_T1w_label-centerline.nii.gz
        │   │   ├──sub-XXX_T1w_label-disc.nii.gz
        │   │   ├──sub-XXX_T1w_label-lesion.nii.gz
        │   │   ├──sub-XXX_T1w_label-compression.nii.gz
        │   │   ├──sub-XXX_T1w_label-rootlet.nii.gz
        ...
        ...
```

The convention for suffix is inspired from the [BIDS convention](https://bids-specification.readthedocs.io/en/stable/05-derivatives/03-imaging.html#imaging-data-types) and is the following:

- `label-<region>_seg.nii.gz`: binary segmentation of the region `<region>`
- `label-<region>_softseg.nii.gz`: probabilistic (soft) segmentation (i.e., values can lie between 0 and 1) of the region `<region>`
- `label-<region>_mask.nii.gz`: binary mask of the region `<region>`, for example, cylinder mask with diameter of 35mm centered at the center of the spinal cord
- `label-<region>_softmask.nii.gz`: probabilistic mask of the region `<region>`
- `label-centerline.nii.gz`: binary spinal cord centerline
- `label-disc.nii.gz`: voxels located at the posterior tip of each intervertebral disc, with values corresponding to [SCT convention](https://spinalcordtoolbox.com/user_section/tutorials/registration-to-template/vertebral-labeling/labeling-conventions.html?highlight=labeling)
- `label-pmj.nii.gz`: a single voxel with value of `50` corresponding to the pontomedullary junction (PMJ), see [SCT convention](https://spinalcordtoolbox.com/user_section/tutorials/registration-to-template/vertebral-labeling/labeling-conventions.html?highlight=labeling) for details
- `label-compression.nii.gz`: voxel(s) with value of `1` located at the posterior tip of each intervertebral disc corresponding to the spinal cord compression(s), see [here](https://github.com/spinalcordtoolbox/spinalcordtoolbox/issues/3984#issuecomment-1373008539) for details
- `label-rootlet.nii.gz`: spinal root segmentation
- `label-<region>_lesion.nii.gz`: lesion (for example in multiple sclerosis), see [here](https://github.com/ivadomed/model_seg_sci#data) for details

```
Fields:
- region = {SC, GM, WM, CSF, brain, brainstem, tumor, edema, cavity, axon, myelin}
```

⚠️ Each label file (such as segmentations or disc label) should be accompanied by a JSON sidecar file. Convention (see this [issue](https://github.com/spinalcordtoolbox/manual-correction/issues/34)) for JSON sidecar files is the following:

```json
{
    "GeneratedBy": [
        {
            "Author": "Firstname Lastname",
            "Date": "YYYY-MM-DD HH:MM:SS"
        }
    ]
}
```

```{note}
`"Date"` is optional. We include it when running the manual correction via the [manual correction](https://github.com/spinalcordtoolbox/manual-correction) python script.
```

If you are running multiple processing based on the same `raw` data, you must create a folder for each of them and then follow the same logic as above. For example:

```
...
...
└── derivatives
    ├── manual_labels
    |   └── dataset_description_1.json
    └── manual_labels_softseg
        └── dataset_description_2.json
```

## IV - Changelog policy

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
