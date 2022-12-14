# `💻` Shell Profile

You can edit your shell profile to create custom commands and make the colours in your terminal look nice.


````{tabbed} ~/.bash_profile

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
````

````{tabbed} ~/.zshrc

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
# Remove "(base)" from the prompt added by miniconda
PROMPT=$(echo $PROMPT | sed 's/(base) //')
```
````
