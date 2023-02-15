# Dataset curation

## Subject naming convention

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
    
Data collected from actual subjects goes under their specific sub-folder, for example:
    
```
sub-001
├── anat
│   ├── sub-001_T1w.json
│   ├── sub-001_T1w.nii.gz
│   ├── sub-001_T2star.json
│   ├── sub-001_T2star.nii.gz
│   ├── sub-001_T2w.json
│   └── sub-001_T2w.nii.gz
└── dwi
    ├── sub-001_dwi.bval
    ├── sub-001_dwi.bvec
    ├── sub-001_dwi.json
    └── sub-001_dwi.nii.gz
```

Many kinds of data have a place specified for them by BIDS. See [file naming conventions](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#filesystem-structure) and the [MRI](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html) and [Microscopy](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/10-microscopy.html) extensions for full details.

```{note}
If you need to differentiate spinal cord images from the brain, use the `acq-cspine` tag. For example, `sub-001_acq-cspine_T1w.nii.gz`.

ℹ️ We opted for `acq-cspine` tag (see [BIDS template](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#anatomy-imaging-data)) because `bp-cspine` is not currently supported by the BIDS convention (see [BEP25](https://docs.google.com/document/d/1chZv7vAPE-ebPDxMktfI9i1OkLNR2FELIfpVYsaZPr4/edit) BIDS extension proposal).
```

```{note}
If you need to differentiate between sequences acquired with different orientations, use the `acq-axial` or `acq-sagittal` tag. For example, `sub-001_acq-axial_T1w.nii.gz`.
```

```{note}
If you need to differentiate between different magnetization transfer (MT) sequences, use the [`flip-<index>_mt-<on|off>`](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#anatomy-imaging-data) tag. For example, `sub-001_flip-1_mt-on_MTS.nii.gz`, `sub-001_flip-1_mt-off_MTS.nii.gz` or `sub-001_flip-2_mt-off_MTS.nii.gz`.
```

```{note}
 If you to combine several above mentioned tags, use camelCase. For example, `sub-001_acq-cspineSagittal_T1w.nii.gz`.
```

## BIDS template

⚠️ Every dataset must have the following files: 

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
 ...
└── derivatives
    ├── dataset_description.json
    └── labels
        └── sub-XXX
        ...
        ...
```

For details, see [BIDS specification](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code).

### `README.md`

The [`README.md`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#readme) is a [markdown](https://markdown-guide.readthedocs.io/en/latest/index.html) file describing the dataset in more detail.

Below is a template - modify it!!!

<details><summary>README.md template:</summary>

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

### `dataset_description.json`

The [`dataset_description.json`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson) is a JSON file describing the dataset.
 
<details><summary>dataset_description.json template:</summary>

Refer to the [BIDS spec](https://bids-specification.readthedocs.io/) to know what version to fill in here.
    
```json
{
    "BIDSVersion": "BIDS X.Y.Z",
    "Name": "<dataset_name>",
    "DatasetType": "raw"
}
```

</details>

 ```{warning}
The `dataset_description.json` file within the top-level dataset should include `"DatasetType": "raw"`.
 ```
 
### `participants.tsv`

The [`participants.tsv`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file) is a TSV file and should include at least the following columns:

| participant_id | source_id | species | age | sex | pathology  | institution |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| sub-001 | 001 | homo sapiens | 30 | F | HC | montreal |
| sub-002 | 005 | homo sapiens | 40 | O | MS | montreal |
| sub-003 | 007 | homo sapiens  | n/a | n/a | MS | toronto |

Authorized values for `pathology` are listed under [`participants.json`](#participants-json).

Below is an example `participants.tsv` file:
    
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

### `participants.json`

The [`participants.json`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file) is a JSON file providing a legend for the columns in `participants.tsv`, with longer descriptions, units, and in the case of categorical variables, allowed levels. Please use the template below:

```json
{
    "participant_id": {
        "Description": "Unique Participant ID",
        "LongName": "Participant ID"
    },
    "source_id": {
        "Description": "Subject ID in the unprocessed data",
        "LongName": "Subject ID in the unprocessed data"
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

### `code/`

The data cleaning and curation script(s) that create the `sub-XXX/` folders should be kept with them, under the [`code/`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#code) folder. Within reason, every dataset should have a script that when run like

```
python code/curate.py path/to/sourcedata ./
```
    
unpacks, converts and renames all the images and related files in `path/to/sourcedata/` into BIDS format in the current dataset `./`.

This program should be committed first, before the curated data it produces. Afterwards, every commit that modifies the code should also re-run it, and the code and re-curated data should be committed in tandem.

```{note}
Analysis scripts should not be kept here. Keep them in separate repositories, usually in public on GitHub, with instructions about. See [PIPELINE-DOC](TODO-PIPELINE-DOC).
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

## Derivatives Structure

This is a folder at the root of the dataset, which includes derivatives files generated from the top-level dataset such as segmentations or labeling.
According to BIDS, these data should go under [`derivatives/`](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html) folder, and follow the same folder logic as the `sub-*` data. 

```{warning}
If derivatives files were generated from preprocessed data (e.g., after reorientation and resampling), describe the 
preprocessing steps in README.md file. Also, include the link (pointing to fixed GitHub version) to the pipeline to the 
README.md file.
```

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
    ├── dataset_description.json
    └── manual_labels
        ├── sub-XXX
        │   ├── anat
        │   │   ├──sub-XXX_T1w_label-SC_seg.nii.gz
        │   │   ├──sub-XXX_T1w_label-SC_probseg.nii.gz
        │   │   ├──sub-XXX_T1w_label-SC_mask.nii.gz
        │   │   ├──sub-XXX_T1w_label-GM_seg.nii.gz
        │   │   ├──sub-XXX_T1w_label-WM_seg.nii.gz
        │   │   ├──sub-XXX_T1w_label-centerline.nii.gz
        │   │   ├──sub-XXX_T1w_label-disc.nii.gz
        │   │   ├──sub-XXX_T1w_label-lesion.nii.gz
        │   │   ├──sub-XXX_T1w_label-compression.nii.gz
        ...
        ...
```

The convention for suffix is inspired from the [BIDS convention](https://bids-specification.readthedocs.io/en/stable/05-derivatives/03-imaging.html#imaging-data-types) and is the following::

- `label-<region>_seg.nii.gz`: binary segmentation of the region `<region>`
- `label-<region>_probseg.nii.gz`: probabilistic (soft) segmentation (i.e., values can lie between 0 and 1) of the region `<region>`
- `label-<region>_mask.nii.gz`: binary mask of the region `<region>`, for example, cylinder mask with diameter of 35mm centered at the center of the spinal cord
- `label-<region>_probmask.nii.gz`: probabilistic mask of the region `<region>`
- `label-centerline.nii.gz`: binary spinal cord centerline
- `label-disc.nii.gz`: voxels located at the posterior tip of each intervertebral disc, with values corresponding to [SCT convention](https://spinalcordtoolbox.com/user_section/tutorials/registration-to-template/vertebral-labeling/labeling-conventions.html?highlight=labeling)
- `label-pmj.nii.gz`: a single voxel with value of `50` corresponding to the pontomedullary junction (PMJ), see [SCT convention](https://spinalcordtoolbox.com/user_section/tutorials/registration-to-template/vertebral-labeling/labeling-conventions.html?highlight=labeling) for details
- `label-compression.nii.gz`: voxel(s) with value of `1` located at the posterior tip of each intervertebral disc corresponding to the spinal cord compression(s), see [here](https://github.com/spinalcordtoolbox/spinalcordtoolbox/issues/3984#issuecomment-1373008539) for details
- `label-<region>_lesion.nii.gz`: lesion (for example in multiple sclerosis), see [here](https://github.com/ivadomed/model_seg_sci#data) for details

```
Fields:
- region = {SC, GM, WM, CSF, brain, brainstem, tumor, edema, cavity, axon, myelin}
```

If you have multiple derivatives, you can create a folder for each of them, and then follow the same logic as above. For example:

```
...
...
└── derivatives
    ├── dataset_description.json
    ├── manual_labels
    └── manual_labels_softseg
```

Convention for derivatives JSON metadata:

```json
{
  "Author": "Firstname Lastname",
  "Date": "YYYY-MM-DD HH:MM:SS"
}
```

```{note}
`"Date"` is optional. We usually include it when running the manual correction via [python scripts](https://github.com/spinalcordtoolbox/manual-correction).
```

```{warning}
The `derivatives` must include its own `dataset_description.json` file (with `"DatasetType": "derivative"`).
```
