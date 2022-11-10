# Computer Setup

## Shell Profile <a href="bash_profile" id="bash_profile"></a>

You can edit your shell profile to create custom commands and make the colours in your terminal look nice.


````{tabbed} ~/.bash_profile

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

````{tabbed} ~/.zshrc

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
# Remove "(base)" from the prompt added by miniconda
PROMPT=$(echo $PROMPT | sed 's/(base) //')
```
````


## niftiviewer.app (MacOS) <a href="niftiviewerapp" id="niftiviewerapp"></a>

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

## Add LINUX machine to GRAMES <a href="add_linux_machine_to_grames" id="add_linux_machine_to_grames"></a>

See info under Gdrive/Neuropoly/network/SOP_add_linux_station_grames.docx

## Configure virtualenvwrapper under LINUX <a href="configure_virtualenvwrapper_under_linux" id="configure_virtualenvwrapper_under_linux"></a>

Add script under /etc/profile.d/virtual_env_config.sh :

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/
source /usr/local/bin/virtualenvwrapper.sh #centos
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh #ubuntu
```

## Email

You can access your PolyMTL email account (@polymtl.ca) at https://zimbra.polymtl.ca, or you can add it to the macOS Mail app.

## Add PolyMTL email to the macOS Mail app

Click on Apple logo () / System Preferences / Internet Accounts / Add Other Account / Mail account

Fill in your `Name`, `Email Address`, and `Password`:

```
Name: NAME SURNAME
Email Address: name.surname@polymtl.ca
Password: your_password
```

Click `Sign In`

Then fill in as follows:

```
Email Address: name.surname@polymtl.ca
User Name: name.surname
Password: your_password

Account Type: IMAP
Incoming Mail Server: zimbra.polymtl.ca
Outgoing Mail Server: smtp.polymtl.ca
```

Click `Sign In`