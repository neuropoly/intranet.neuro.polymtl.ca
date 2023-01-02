# Dataset curation

## Subject naming convention

**Basic convention**: sub-XXX

example:
- sub-001
- sub-002

**Multi-institution/Multi-pathology convention**: sub-\<site>\<pathology>XXX

example:
- sub-montrealDCM001
- sub-torontoHC001

    
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

```{warning}
TODO: describe neuropoly-specific BIDS entities, like bp-cspine or acq-MTon
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
    
<details><summary>participants.tsv template:</summary>
    
```
participant_id	source_id	species	age	sex	pathology	institution
sub-001	001	homo sapiens	30	F	HC	montreal
sub-002	005	homo sapiens	40	O	MS	montreal
sub-003	007	homo sapiens	n/a	n/a	MS	toronto
```
</details>

Other columns may be added if the data exists to fill them and it would be useful to keep.

```{warning}
Indicate missing values with `n/a` (for "not available"), not by empty cells!
```

```{warning}
This is a Tab-Separated-Values file. Make sure to use tabs between entries if editing with a text editor. Most spreadsheet software can read and write .tsv correctly.
```

### `participants.json`

The [`participants.json`](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#participants-file) is a JSON file providing a legend for the columns in `participants.tsv`, with longer descriptions, units, and in the case of categorical variables, allowed levels.

<details><summary>participants.json template:</summary>

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
}
```

</details>

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

The [`derivatives`](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html) are files generated from the top-level dataset such as segmentations or labels.

Convention for derivatives JSON metadata:

```json
{
  "Author": "Firstname Lastname",
  "Date": "YYYY-MM-DD HH:MM:SS"
}
```

NOTE: "Date" is optional. We usually include it when running the manual correction via python scripts.

```{warning}
The `derivatives` must include its own `dataset_description.json` file (with `"DatasetType": "derivative"`).
```
