# MacOSX

## Booting Options

| Key | Action |
| :--- | :--- |
| cmd+R | Recovery |
| alt | Boot from External Device |

## Nice Software

**Recommended**

* [Quicksilver](https://qsapp.com/). Do stuff using keyboard instead of mouse \(e.g., open applications, Google search, send email, etc.\).
* Textpander. Use abbreviation to call useful text e.g. email address, phone, etc. that you write 10 times a day.
  * Cheaper alternative: atext
* Time Machine. User-friendly backup solution. To track backups you can use TimeTracker
* [Slack](https://slack.com/intl/en-ca/downloads/instructions/mac)
* [Evernote](https://evernote.com/) Note management
* [MonitorControl: Monitor brightness in 2nd monitor \(without touching the buttons\)](https://github.com/MonitorControl/MonitorControl)

**Image**

* Pixelmator. Image editor that fully took advantage of the Mac OS \(Open GL, Automator, ColorSync etc.\).
* Seashore. Image editor - Simpler than Pixelmator. Good for quick fix.
* [ImageMagick](http://www.imagemagick.org/index.php). Command line processing tools for images. E.g., can create GIF. [Tips for installation and usage](https://www.neuro.polymtl.ca/tips_and_tricks/mac/imagemagick_installation)

**Audio/Video**

* [https://obsproject.com/](https://obsproject.com/): Free and open source software for video recording and live streaming.
* EasyWMA. Convert WMA format into MP3, M4A, WAV or AIFF
* MacTheRipper. Extract your DVD into TS\_VIDEO/TS\_AUDIO folder \(then use HandBrake to compress\).
* HandBrake. Convert DVD into DivX. Also convert various video formats \(MOV, MP4, AVI, etc.\)
* [VLC](https://www.videolan.org/vlc/index.fr.html). Nice video player \(can be used for DVD as well\).
* Camtasia. Record videos

**3D objects**

* [MeshLab](http://meshlab.sourceforge.net/). Read STL, OBJ, 3DS, etc., convert, resample.

**Figures**

* InkScape …………. Free equivalent of Illustrator: do vectorial figures. One disadvantage: the application has been developed under X11 so the GUI is sometimes “hesitating”…
* ShapeOnYou ……. Generate 3D shapes for Keynote
* Organigram ……… OmniGraffle.app
* [graphviz](http://www.graphviz.org/). Generate nice diagrams.

**MRI**

* [Horos](https://www.horosproject.org/): Free DICOM/NIFTI viewer \(replaces OsiriX\)
* MITK workbench
* ITKSNAP

**Programming**

* Pycharm. Great IDE For Python.
* [SourceTree](http://www.sourcetreeapp.com/). Manages git repository.

**Internet stuff**

* Transmission. Torrent manager \(by default the one from OSX is Opera - which is not that cool\)
* [Cyberduck](http://cyberduck.io/?l=en). FTP/SFTP protocol handler with nice GUI.
* adblock. block adds

**Misc**

* Pdfshrink: Very convenient, because the default 'save pdf' option of Word, etc. does not compress pictures
* Mailplane: Gmail-dedicated application that makes life easier: drag/drop stuff, get notifications, etc.
* [MenuMeters](https://www.ragingmenace.com/software/menumeters/index.html): System monitoring \(free\).
* Caffeine: Allows to avoid entering into sleep mode, e.g., while you're showing a funny clip on youtube
* xGestures: Allows you to perform common functions using quick mouse movements \(e.g. close window, previous page on Safari, etc.\)
* MultiClutch: Allows you to perform common functions using touchpad movements \(e.g. previous page on Firefox, etc.\).
* Expandrive: Create a virtual FTP disk
* Capture Me: For screen recording
* [ScreenFlow](http://www.telestream.net/screenflow/overview.htm): Create demo videos for software

**QuickLook modules**

* NIFTI: [dtitk](http://www.nitrc.org/projects/dtitk)
* DICOM & NIFTI: [Brainsight-quicklook](https://www.rogue-research.com/downloads/)
  * NOTE: The Brainsight plugin is not working \(at least on my station\) with Mojave.
* DICOM: [Osirix](http://macappstore.org/osirix-quicklook/)

Full list of QuickLook modules [here](https://www.quicklookplugins.com/page/2/)\)

**Science**

* [G\*Power](http://www.macupdate.com/app/mac/24037/g-power): power calculation for statistics

**Programming**

* [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac) IDE
* [Atom](https://atom.io/) Enhanced editor

## General

### Global default config <a id="global_default_config"></a>

[https://gist.github.com/brandonb927/3195465](https://gist.github.com/brandonb927/3195465)

### Maintenance

Clean cache:

```bash
~/Library/Caches
/Library/Caches
```

### Files and Folders

#### Change Folder Icon <a id="change_folder_icon"></a>

1.  Find an icon you like. A good place is interface lift. 
2. Once you have found your icon, right click and “Get Info” on both your icon file and the folder you wish to change. Click on the small icon in the top left hand corner. There will be a blue outline around the icon. Now press Command + C, this will copy the icon to your clip board.
3. On your folder icon that you want to change, click it again and press `CMD + V`. This will paste the icon. 

#### Copy/Make a disk image from CD/DVD \(ISO format\) <a id="copymake_a_disk_image_from_cddvd_iso_format"></a>

Open Disk Utility, click on “create new image”, then save as DVD/CD .cdr format. Then you can convert your CDR into ISO using the following Terminal command:

```text
hdiutil makehybrid -iso -joliet -o Master.iso Master.cdr
```

### Recovery

#### Create recovery partition <a id="create_recovery_partition"></a>

[http://www.macworld.co.uk/how-to/mac-software/downgrade-mavericks-mountain-lion-3494785/](http://www.macworld.co.uk/how-to/mac-software/downgrade-mavericks-mountain-lion-3494785/)

For Mavericks: [http://support.apple.com/kb/HT5856](http://support.apple.com/kb/HT5856)

Is it possible to downgrade to Mountain Lion on a Mac with native Mavericks installation? ANSWER: [no.](https://discussions.apple.com/thread/5595780)

### Displays

#### Lock screen <a id="lock_screen"></a>

In order to run a script overnight:

* Keyboard Shortcut: `Ctrl+Shift+Eject`
* Icon in your menu bar: Keychain Access &gt; Preferences &gt; General tab &gt; select the Show Status in Menu Bar option.

#### Lock screen upon sleep <a id="lock_screen_upon_sleep"></a>

Looking through this site, I found part of the solution in this hint. The trick was getting this script to activate on Sleep \(or wake up\). After some searching, I found Bernhard Baehr's excellent Sleepwatcher. Sleepwatcher is a daemon that calls a pair of scripts, ~/.sleep and ~/.wakeup, upon sleep and wakeup. Combining these two, I installed Sleepwatcher, and used the code below as my .sleep file \(the /System… line is shown on two lines; enter it as one line without any added spaces\):

\#!/bin/sh /System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend

Restart, and your Mac will fast-user switch itself to the log in screen when you close the lid! Hope this helps other paranoid PowerBook owners! Note: You can also put this script in your .wakeup file, but there's a few \(three to five\) seconds' delay between wake and the script call, leaving the system wide open for a few seconds, and looking a bit tacky to boot.

To download sleepwatcher: [http://www.bernhard-baehr.de/](http://www.bernhard-baehr.de/)

Source of this tips: [http://hints.macworld.com/article.php?story=20040724203315798&query=CGSession](http://hints.macworld.com/article.php?story=20040724203315798&query=CGSession)

### Notifications

#### Disable Notification Center <a id="disable_notification_center"></a>

If you don't need the Notification Center feature introduced in OS X Mountain Lion, you can easily disable it with a Terminal command.

Open Terminal by searching for it in Spotlight or opening it from the Applications &gt; Utilities folder. Enter the following command

```text
launchctl unload -w /System/Library/LaunchAgents/com.apple.notificationcenterui.plist
```

Next you have to close Notification Center. Enter the following command:

```text
killall NotificationCenter
```

If you see an error reading that there was no process, don't worry.

And right away, you will see that the Notification Center icon is gone from the menu bar! If you need to get it back:

Enter the following command in Terminal

```text
launchctl load -w /System/Library/LaunchAgents/com.apple.notificationcenterui.plist
```

Hit Command+Shift+G in Finder and go to /System/Library/CoreServices/ then find “Notification Center” and double-click it to launch it.

### Keyboard

#### Dialog box: select option with Tab <a id="dialog_boxselect_option_with_tab"></a>

After Snow Leopard, this useful feature was removed by default. To put it back: System Preferences &gt; Keyboard &gt; Shortcuts &gt; select “All Controls”

### **Misc**

#### Dock in 2d <a id="dock_in_2d"></a>

```bash
defaults write com.apple.dock no-glass -boolean YES
killall Dock
```

#### Make Hidden Applications Icons Transparent <a id="make_hidden_applications_icons_transparent"></a>

```bash
defaults write com.apple.Dock showhidden -bool YES
killall Dock
```

#### Set The Expanded Print Dialogue As Default <a id="set_the_expanded_print_dialogue_as_default"></a>

```text
defaults write -g PMPrintingExpandedStateForPrint -bool TRUE
```

#### Reboot station with Terminal <a id="reboot_station_with_terminal"></a>

```bash
sudo shutdown -r now
```

#### Set The Expanded Save Dialogue As Default <a id="set_the_expanded_save_dialogue_as_default"></a>

```bash
defaults write -g NSNavPanelExpandedStateForSaveMode -bool TRUE
```

#### Screenshot in desired format <a id="screenshot_in_desired_format"></a>

```bash
defaults write com.apple.screencapture type jpg
```

needs re-logging

## Servers

[How to manage a server](https://www.neuro.polymtl.ca/tips_and_tricks/mac/server)

## Software-specific

### MATLAB

help crash. use this command in matlab : `com.mathworks.mlwidgets.html.HtmlComponentFactory.setDefaultType('HTMLRENDERER');`

### Automator

Launch app automator –&gt; New app OR service –&gt; add “Run shell script” module –&gt; select module Option: Pass input “as argument” –&gt; write you script

### FSL and FSLeyes

#### **Launch fslview via double click**

```bash
FSLDIR=/usr/local/fsl . ${FSLDIR}/etc/fslconf/fsl.sh PATH=${PATH}:/usr/local/fsl/bin fslview “$@” &
```

#### **generate dwi\_mean in same folder**

```bash
FSLDIR=/usr/local/fsl . ${FSLDIR}/etc/fslconf/fsl.sh PATH=${PATH}:/usr/local/fsl/bin fold=$(dirname “$1”) NAME=`echo “$(basename “$1”)” | cut -d'.' -f1` fslmaths “$1” -Tmean $fold“/“$NAME”_mean”
```

### **Use a service**

* select a file or text \(depending on your service input\)
* application menu \(e.g. finder\) → Services → your service. \(Or specify a keyboard shortcut in “Services preferences”\)

### Chrome

**Won't launch**

* Terminal –&gt; go to folder:
  * ~/Library/Application\ Support/Google/Chrome/
  * ~/Library/Application\ Support/Skype/
  * Remove user folder or even everything

### Dropbox

**Sync is stuck**

**Solution 1**

Remove the ACL manually. Go to the problematic folder\(s\) and type:

```text
chmod -N foldername
chmod -RN foldername  --> do do it for all files/folders recursively
```

**Solution 2**

* Terminal –&gt; cd ~ –&gt; rm -rf .dropbox/

### Finder

**Enable The Path View**

```text
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
```

**Show Hidden Files**

```text
defaults write com.apple.finder AppleShowAllFiles TRUE
```

N.B. Must restart: [http://ianlunn.co.uk/articles/quickly-showhide-hidden-files-mac-os-x-mavericks/](http://ianlunn.co.uk/articles/quickly-showhide-hidden-files-mac-os-x-mavericks/)

**Display full path**

```text
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES
```

**Sort Folders first**

[http://fahmiesalleh.blogspot.com/2008/04/mac-os-x-finder-sort-folder-before-file.html](http://fahmiesalleh.blogspot.com/2008/04/mac-os-x-finder-sort-folder-before-file.html)

### Image Capture

**iPhone or scanner is no more recognized**

Close Image capture. Delete \(or rename\) the plist files:

```text
cd ~/Library/Preferences
mv com.apple.Image_Capture.plist com.apple.Image_Capture.plist__old
mv com.apple.ImageCaptureExtension2.plist com.apple.ImageCaptureExtension2.plist__old
```

Open Image Capture and plug your device.

### Keynote

In the new version of Keynote \(6.2\), files are now saved as packages instead of files. This creates huge problems with Dropbox, git, etc. I did not find any workaround so far, so had to install the older version \(not possible to downgrade from Apple Store– you need to manually install the previous version inside the Applications/ folder\).

### Microsoft Word

**Word freezes after copy/paste**

Solutions:

1. work with .docx, not .doc
2. [http://word.mvps.org/Mac/fontweeding.html](http://word.mvps.org/Mac/fontweeding.html)

**Error: A COM Exception has occurred**

Related to EndNote. Solution:

1. Go to ~/Library/
2. Rename **Saved Application State** as **Saved Application State\_old**

**Error: "Microsoft Word has encountered a problem and needs to close"**

Try rebooting.

**Hyperlinks are lost when saving as pdf**

This is a [known bug](http://msgroups.net/microsoft.public.mac.office.word/links-lost-on-conversion-to/63190). Solution: convert your word document using [freepdfconvert](https://www.freepdfconvert.com/)

### Papers

#### **Port Papers to another mac**

This only applies to Papers 1. Not possible to do with Papers 2+ for security reasons \(at least I haven't figured out how to do it\).

Copy these files to another mac:

```text
/Applications/Papers
~/Library/Application Support/Papers
```

Open Papers and register.

Your library is managed by the file **Library.papers**. To port your existing library, do the following:

1. Go to menu Papers &gt; Preferences &gt; Library
2. Edit the folder **PDF Library Location**
3. When it says “Papers library found already”, click **switch**
4. Restart Papers.

### Preview

**Add a signature**

To avoid having to click multiple times to add a signature, here is an awesome AppleScript + QuickSilver combo:

Create this AppleScript:

```text
tell application "Preview" to activate
  tell application "System Events" to tell process "Preview"
    click menu item 1 of menu 1 of menu item "Signature" of menu 1 of menu item "Annotate" of menu 1 of menu bar item "Tools" of menu bar 1
end tell
```

Then drag/drop this script as a “Trigger” in [quicksilver](https://qsapp.com/), add a specific keyboard shortcut \(e.g. alt+cmd+s\) and make the scope specific to “Preview”.

To create other AppleScript, you can use this UI inspector: [UI Browser](https://pfiddlesoft.com/uibrowser/index-downloads.html).

If you want to run the above script without QuickSilver:

1. Open Automator.
2. Make a new Quick Action.
3. Make sure it receives 'no input' at all programs.
4. Select Run Apple Script \(the script from above\) and type in your code.
5. Save!
6. Now go to System Preferences &gt; Keyboard &gt; Shortcuts. Select Services from the sidebar and find your service. Add a shortcut by double clicking \(none\).
7. Finally go to System Preferences &gt; Security &gt; Privacy &gt; Accessibility and add Automator and the preferred app to run the shortcut.

### QuickLook

Reload cache

```text
qlmanage -r
```

List all plugins

```text
qlmanage -m
```

Debug

```text
qlmanage -p "path_to_plugin"
Example: qlmanage -p /Library/QuickLook/DTITK_QuickLookPlugin.qlgenerator
```

Nice plugins

* [http://www.nitrc.org/projects/dtitk](http://www.nitrc.org/projects/dtitk)

### Terminal

#### **Let Terminal Talk**

```text
say hola
```

for more UNIX commands, see [http://www.neuro.polymtl.ca/doku.php?id=tips\_and\_tricks:unix](http://www.neuro.polymtl.ca/doku.php?id=tips_and_tricks:unix)

#### **display log**

```text
syslog
```

### TextMate

If TextMate does not open, delete folder `~/Library/Application Support/TextMate` .

## Troubleshooting

### Right-click sharing for Google Drive

The Share menu might not show one or more sharing options—such as Email This Page, AirDrop, or Facebook—or the Markup feature might be missing.

Follow these steps if the issue occurred immediately after upgrading to Yosemite or El Capitan. Open the Terminal app, and run:

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -seed
```

source: [https://support.apple.com/en-us/HT203129](https://support.apple.com/en-us/HT203129)

### fslview opening out of screen

* try to restart the application.
* try to restart the computer.
* Try this:

```bash
rm ~/Library/Preferences/org.macosforge.xquartz.X11.plist
rm ~/Library/Preferences/uk.fmrib.ox.ac.fslview.plist
```

* open AppleScript Editor and run:

```bash
tell application "fslview"
  set bounds of windows to {100, 100, 800, 800}
end tell
```

### Archive Utility: Permanent loading

* Restart Computer
* Use other program: [http://wakaba.c3.cx/s/apps/unarchiver](http://wakaba.c3.cx/s/apps/unarchiver)

### Trash: Stuck when being emptied

* Terminal –&gt; killall Finder –&gt; `rm -rf ~/.Trash/*`

### Error: "disk quota exceeded"

ONLY APPLIES TO PEOPLE AT NEUROPOLY: If you see this message, try to unmount **django**: from the Finder, click on the eject button. If you still have problems, ask an administrator system.

### Cannot repair permission

Probably some ACL issues. Download and run this: [http://nomulous.com/goodies/ACLr8/](http://nomulous.com/goodies/ACLr8/)

### Password prompts: "Finder wants to make changes"

#### **Solution 1**

Remove the ACL manually. Go to the problematic folder\(s\) and type:

```bash
chmod -N <FOLDER>
chmod -RN <FOLDER>  # --> do do it for all files/folders recursively
```

#### **Solution 2**

1. Open Applications &gt; Utilities &gt; Disk Utility.
2. Select your hard drive in the left column. Most likely it will be named “Macintosh HD.”
3. Click on “Repair Disk Permissions.”
4. Close Disk Utility. Check if the problem is still there.

#### **Solution 3**

If it is still not resolved:

1. Restart and hold down the Command and R keys. You will boot into the Repair Utilities screen. On top, in the Menu Bar click the Utilities item then select Terminal.
2. In the Terminal window, type `resetpassword` and hit Return. The Password reset utility launches, but you’re not going to reset the password.
3. Instead, click on the icon for your Mac’s hard drive at the top. From the drop-down below it, select the user account where you are having issues. At the bottom of the window, you’ll see a button labeled ‘Reset Home Directory Permissions and ACLs’. Click the Reset button there.

