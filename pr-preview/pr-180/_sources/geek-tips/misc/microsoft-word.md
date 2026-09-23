# Microsoft Word

##  Useful shortcuts for OSX <a id="useful_shortcuts_for_osx"></a>

| Action | Keyboard shortcut |
| :--- | :--- |
| Turn track changes on or off | COMMAND + Shift + E |
| Add comment | COMMMAND + ALT + A |

## How to always open a page with "page width" view <a id="how_to_always_open_a_page_with_page_width_view"></a>

Create a new macro in Normal.dot template:

```text
Sub AutoOpen()
ActiveWindow.View.Type = 3
ActiveWindow.View.Zoom.PageFit = wdPageFitBestFit
End Sub
```



