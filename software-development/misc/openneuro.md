# OpenNeuro

## Overview

[OpenNeuro](https://openneuro.org/) is a free and open platform for sharing MRI, MEG, EEG, iEEG, ECoG, ASL, and PET data. Below, we describe how to integrate OpenNeuro data with [DataLad](https://www.datalad.org/) and [AWS](https://aws.amazon.com/free/?trk=ps_a134p000003yhMrAAI&trkCampaign=acq_paid_search_brand&sc_channel=ps&sc_campaign=acquisition_CA&sc_publisher=google&sc_category=core-main&sc_country=CA&sc_geo=NAMER&sc_outcome=Acquisition&sc_detail=aws&sc_content=Brand_Core_aws_e&sc_matchtype=e&sc_segment=453053794209&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Core-Main|Core|CA|EN|Text&s_kwcid=AL!4422!3!453053794209!e!!g!!aws&ef_id=Cj0KCQjwk4yGBhDQARIsACGfAesxE-q-wc05cyshZskHgQCJf2Kl3oKHVVmkSNkzHI7F_s2TFOOEre0aAl5KEALw_wcB:G:s&s_kwcid=AL!4422!3!453053794209!e!!g!!aws&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all).

## DataLad

### Installation

{% tabs %}
{% tab title="Debian/Ubuntu" %}
Install `datalad` using `conda` :

```bash
source miniconda3/etc/profile.d/conda.sh
 # TO DO ONLY ONCE:  
conda create -y -n venv3.7 python=3.7 
# TO ACTIVATE: 
conda activate venv3.7 
pip install datalad 
su  apt-get install git-annex
```
{% endtab %}

{% tab title="MacOS" %}
Install `datalad` using `conda` :

```bash
source miniconda3/etc/profile.d/conda.sh
 # TO DO ONLY ONCE:  
conda create -y -n venv3.7 python=3.7 
# TO ACTIVATE: 
conda activate venv3.7 
pip install datalad 
# first, install brew: https://brew.sh/
brew install git-annex
```
{% endtab %}
{% endtabs %}

### Usage

Install dataset from OpenNeuro:

```bash
datalad install https://github.com/OpenNeuroDatasets/ds001919.git
```

Get one subject:

```bash
datalad get sub-unf01
```

Get all subjects:

```bash
datalad get . 
```

Update dataset:

```bash
datalad update -r —merge
```

## AWS

### Installation

{% tabs %}
{% tab title="Linux" %}
Follow the [AWS Installation Instructions for Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html).
{% endtab %}

{% tab title="MacOS" %}
Follow the [AWS Installation Instructions for MacOS](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html).
{% endtab %}

{% tab title="Windows" %}
Follow the [AWS Installation Instructions for Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html).
{% endtab %}
{% endtabs %}

### Download OpenNeuro Dataset

Download dataset from openneuro by running this command:

```bash
/usr/local/bin/aws  s3 sync --no-sign-request s3://openneuro.org/ds001919 ds001919-dwld/
```

