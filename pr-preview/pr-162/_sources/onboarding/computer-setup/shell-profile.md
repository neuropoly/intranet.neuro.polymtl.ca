# <span>💻</span> Shell Profile

You can edit your shell profile to create custom commands and make the colours in your terminal look nice.


::::{tab-set}
:::{tab-item} ~/.bash_profile

```bash
# Nice .bash_profile

# Set error message in English (if you want to)
LANG=en_CA.UTF-8

# COLOR
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
 
# PROMPT
PS1='\[\e[1;31m\]\h:\[\e[m\]\[\e[0;36m\]\w\[\e[m\] \[\e[0;38m\]\$ \[\e[m\]\[\e[0;38m\]'
 
# ALIAS
alias ll="ls -la"
alias edit="open -a textedit"
alias matlab="/Applications/MATLAB_R2020a.app/bin/matlab &"
alias test_sct="/Users/julien/code/spinalcordtoolbox/testing/test_all.py"
alias abbey="ssh p101317@abbey.neuro.polymtl.ca"
alias django="ssh jcohen@django.neuro.polymtl.ca"
alias davis="ssh jcohen@davis.neuro.polymtl.ca"
alias rosenberg="ssh p101317@rosenberg.neuro.polymtl.ca"
alias bireli="ssh p101317@bireli.neuro.polymtl.ca"
alias joplin="ssh p101317@joplin.neuro.polymtl.ca"
alias guillimin="ssh jcohen@guillimin.hpc.mcgill.ca"
alias cedar="ssh jcohen@cedar.computecanada.ca"
alias graham="ssh jcohen@graham.computecanada.ca"
alias niagara="ssh jcohen@niagara.computecanada.ca"
alias gs="git status -s"
alias gc="git commit -S -a"
alias gp="git push"
alias gl="git log --pretty=oneline"
alias glg="git log --pretty=oneline --decorate --all --graph"
alias gd="git diff"
alias gb="git branch"
 
# FSL Setup
FSLDIR=/usr/local/fsl
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH
. ${FSLDIR}/etc/fslconf/fsl.sh
 
# FSLeyes
PATH=${PATH}:/Applications/FSLeyes.app/Contents/MacOS
 
# DCM2NII
PATH=${PATH}:/Applications/mricron
 
# ANTS
PATH=${PATH}:/usr/local/ants/bin
 
# cmake
export PATH=${PATH}:/Applications/CMake.app/Contents/bin
 
# MINICONDA
export PATH="$HOME/miniconda3/bin:$PATH"  # commented out by conda initialize
source ~/miniconda3/etc/profile.d/conda.sh
```
:::

:::{tab-item} ~/.zshrc
```bash
# Set error message in English (if you want to)
LANG=en_CA.UTF-8

# COLOR
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
 
# PROMPT
PS1='%B%F{red}%m:%F{cyan}%~ %F{white}$ '
 
# ALIAS
alias ll="ls -la"
alias edit="open -a textedit"
alias matlab="/Applications/MATLAB_R2020a.app/bin/matlab &"
alias test_sct="/Users/julien/code/spinalcordtoolbox/testing/test_all.py"
alias abbey="ssh p101317@abbey.neuro.polymtl.ca"
alias django="ssh jcohen@django.neuro.polymtl.ca"
alias davis="ssh jcohen@davis.neuro.polymtl.ca"
alias rosenberg="ssh p101317@rosenberg.neuro.polymtl.ca"
alias bireli="ssh p101317@bireli.neuro.polymtl.ca"
alias joplin="ssh p101317@joplin.neuro.polymtl.ca"
alias guillimin="ssh jcohen@guillimin.hpc.mcgill.ca"
alias cedar="ssh jcohen@cedar.computecanada.ca"
alias graham="ssh jcohen@graham.computecanada.ca"
alias niagara="ssh jcohen@niagara.computecanada.ca"
alias gs="git status -s"
alias gc="git commit -S -a"
alias gp="git push"
alias gl="git log --pretty=oneline"
alias glg="git log --pretty=oneline --decorate --all --graph"
alias gd="git diff"
alias gb="git branch"
alias nn='nano'
alias grep='grep --color=auto'

# FUNCTIONS
# ls in combination with head or tail commands with definable number of output lines
function lh { if [ "$#" -eq 0 ];then num=10;else num=${1};fi; ls -lath | head -${num} }
function lt { if [ "$#" -eq 0 ];then num=10;else num=${1};fi; ls -lath | tail -${num} }
# quick (and nice looking) check of tabulator, comma, and semicolon separated files (.tsv, .csv)
# Note: tput rnam and tput smam disable line wrapping temporarily; see https://unix.stackexchange.com/a/515938
function column_tab { tput rmam; column -t -s $'\t' ${1};tput smam }
function column_comma { tput rmam; column -t -s $',' ${1};tput smam }
function column_semicol { tput rmam; column -t -s $';' ${1};tput smam }
# get nii header using sct_image
function header { sct_image -i ${1} -header }

# VENV workflow
# create venv (and install requirements if requirements.txt file exists)
function ce { python3 -m venv venv; echo "venv was created successfully"; if [ -f requirements.txt ]; then echo "requirements.txt file found, installing dependencies..."; source ./venv/bin/activate; pip install -r requirements.txt;fi } 
# activate venv
alias ae='deactivate &> /dev/null; source ./venv/bin/activate'
# deactivate venv
alias de='deactivate'

# FSL Setup
FSLDIR=/usr/local/fsl
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH
. ${FSLDIR}/etc/fslconf/fsl.sh
 
# FSLeyes
PATH=${PATH}:/Applications/FSLeyes.app/Contents/MacOS
alias ff='fsleyes'

# DCM2NII
PATH=${PATH}:/Applications/mricron
 
# ANTS
PATH=${PATH}:/usr/local/ants/bin
 
# cmake
export PATH=${PATH}:/Applications/CMake.app/Contents/bin
 
# MINICONDA
export PATH="$HOME/miniconda3/bin:$PATH"  # commented out by conda initialize
source ~/miniconda3/etc/profile.d/conda.sh
# Remove "(base)" from the prompt added by miniconda
PROMPT=$(echo $PROMPT | sed 's/(base) //')
```
:::
::::
