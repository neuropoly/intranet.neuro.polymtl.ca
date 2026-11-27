# XQuartz

```{note}
Note: XQuartz is for MacOS only
```

## SSH

To get the display in an ssh connection:

1. [Download XQuartz](https://www.xquartz.org/)
2. Open XQuartz
3. Connect with X forwarding: `ssh -X <URL>`
4. Test if forwarding worked using one of those software: `xeyes`, `xclock`, `xdisp`

## XQuartz Terminal

To allow pasting inside the XQuartz terminal:

1. Create the file `~/.Xdefaults`
2. Edit it and add the line: `*VT100.translations: #override Meta <KeyPress> V: insert-selection(PRIMARY, CUT_BUFFER0) \n`
3. run: `xrdb -merge ~/.Xdefaults`

