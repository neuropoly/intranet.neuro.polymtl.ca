# `⚙️` Other configuration tips

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