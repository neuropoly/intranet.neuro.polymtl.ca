# Anima

## Installation

Docu: [https://github.com/Inria-Visages/Anima-Scripts-Public/wiki/Installation](https://github.com/Inria-Visages/Anima-Scripts-Public/wiki/Installation)

* Download and unzip latest Anima under `/Users/user/Anima-Public/build/bin` release from: [https://github.com/Inria-Visages/Anima-Public/releases](https://github.com/Inria-Visages/Anima-Public/releases)
* Download and unzip Anima-Scripts data under `/Users/user/Anima-Scripts_data/` from: [https://team.inria.fr/visages/files/2018/09/Anima\_Data.zip](https://team.inria.fr/visages/files/2018/09/Anima_Data.zip)
* Download and unzip Anima-Scripts-Public under `/Users/user/Anima-Scripts-Public/` from : [https://github.com/Inria-Visages/Anima-Scripts-Public/archive/master.zip](https://github.com/Inria-Visages/Anima-Scripts-Public/archive/master.zip)

Configure ANIMA in `~/.anima/config.txt`:

```text
 # Variable names and section titles should stay the same
 # Put this file in your HomeFolder/.anima/config.txt
 # Make the anima variable point to your Anima public build
 # Make the extra-data-root point to the data folder of Anima-Scripts
 # The last folder separator for each path is crucial, do not forget them
 # Use full paths, nothing relative or using tildes
 [anima-scripts]
 anima-scripts-public-root = /Users/USER/Anima-Scripts-Public/
 anima-scripts-root = /Users/USER/Anima-Scripts/
 anima = /Users/USER/Anima-Public/build/bin/
 extra-data-root = /Users/USER/Anima-Scripts_data/
```

Configure `.bash_profile`:

```bash
 #ANIMA
 PATH=${PATH}:/Users/USER/Anima-Public/build/bin
```

