# Dropbox

Having dropbox on a Mac network can be a nightmare.

**AppleDouble files**

Example: `._myfile.txt`. These files are created when the file system is different than AFP \(e.g., if your network home folders are mounted with NFS\). I haven't found any workaround to prevent the creation of these files \(which, in some cases, seem to be mandatory to OSX otherwise can cause issues\). So you have to live with them. If too annoying, you can always suppress them with `dot_clean -m`. Although be aware of potential issues…

**Reinstall Dropbox**

If you want to unlink and then relink your computer to a dropbox account, make your you suppress the hidden folder `.dropbox/` in your home folder before you relink \(of course, quit dropbox before removing the folder\).

**Updating freezes**

If it keeps saying “Updating \(453 files\)” without any change, it is probably a permission issue. Go to the problematic folder and type `sudo chmod -R 775 *`. If this does not work, it may be an owner issue. To fix this, change ownership of the problematic folder using: `sudo chown -R USERNAME FOLDER`

