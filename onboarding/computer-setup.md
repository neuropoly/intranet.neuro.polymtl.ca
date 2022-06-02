# Computer Setup

## Modify User Template

Go under:

```bash
 /System/Library/User\ Template/English.lproj
```

## Shell Profile <a href="bash_profile" id="bash_profile"></a>

You can edit your shell profile (usually called `.bash_profile`, but some newer versions of Mac use `.zsh_profile` ) to create custom commands and make the colours in your terminal look nice.


````{tabbed} .bash_profile
To edit, navigate to `$HOME/.bash_profile`

```bash
# Nice .bash_profile
 
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

````{tabbed} .zsh_profile
To edit, navigate to `$HOME/.zsh_profile` 

```bash
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
```
````


## niftiviewer.app <a href="niftiviewerapp" id="niftiviewerapp"></a>

UPDATE: NO NEED TO DO THE THING BELOW ANYMORE WITH NIFTI. Instead, right click > “get info” > Open with > change all… > select fsleyes

In automator, create new application - run apple script. Add the following script:

```
  on run {input, parameters}
  set f to POSIX path of (input as text)
  do shell script "source ~/.bash_profile"
  do shell script "open -n -a fslview.app --args " & f
  end run
```

Select .nii file – open with –> select niftiviewer.app

## Configure virtualenvwrapper under LINUX <a href="configure_virtualenvwrapper_under_linux" id="configure_virtualenvwrapper_under_linux"></a>

Add script under /etc/profile.d/virtual_env_config.sh :

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/
source /usr/local/bin/virtualenvwrapper.sh #centos
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh #ubuntu
```

## Update debian 7 to 8 <a href="update_debian_7_to_8" id="update_debian_7_to_8"></a>

[https://www.prado.lt/how-to-upgrade-debian-7-wheezy-to-10-buster-safely](https://www.prado.lt/how-to-upgrade-debian-7-wheezy-to-10-buster-safely)
