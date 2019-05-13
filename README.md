# freecad-slic3r-tools
Tools for running Slic3r from FreeCAD

* [Installation](https://github.com/limikael/freecad-slic3r-tools/#installation)
* [Settings](https://github.com/limikael/freecad-slic3r-tools/#settings)
* [Tools](https://github.com/limikael/freecad-slic3r-tools/#tools)

This module lets you quickly export all visible parts in the current document, and open the resulting .stl file in Slic3r.
You can also set up a default print profile, and directly get information about the resources that would be used to print it,
as well as quickly generate the .gcode file.

## Installation

This module is not in the add-on manager (yet). In order to install it, simply download it from:

https://github.com/limikael/freecad-slic3r-tools/archive/master.zip

And extract it into your FreeCAD Mod directory. For more info on how to find this directory, see [this link](https://www.freecadweb.org/wiki/index.php?title=Installing_more_workbenches).

## Settings

Before you can use the module there are a few settings you need to set. To access these settings, go to "Edit >> Preferences" and then select "Slic3r Tools". The settings are:

### Path to slic3r executable

Set up the path to your where your slic3r executable is on your hard drive. If you run windows, this is the .exe file. If you run Linux, you can point to the .AppImage file here.

### Path to slic3r profile .ini file

This should point to a slic3r .ini file. The .ini file contains information about which printer you are using as well as layer
height, etc. While Slic3r has a GUI to let you work with several profiles at once and quickly change between them, the SLic3r
Toolbar can only work with one profile. To export the current profile from slic3r and use it from Slic3r Toolbar, go to
"File >> Export Config..." from inside Slic3r.

## Tools
<img align="right" width="50" src="https://raw.githubusercontent.com/limikael/freecad-slic3r-tools/master/Resources/icons/Stl.svg?sanitize=true">

### Export visible as .stl
This command exports the current document as a .stl file. It works in a similar way as choosing "File... >> Export..." in
the menu. However, while the default export option requires you to first select which objects you want to export, this
option exports all visible object. There is no prompt to ask for a file name, the name of the exported .stl file will be derived from your document file name.

<img align="right" width="50" src="https://raw.githubusercontent.com/limikael/freecad-slic3r-tools/master/Resources/icons/Slic3r.svg?sanitize=true">

### Run Slic3r
Export the current document as .stl. Run slic3r and open the .stl file in Slic3r.

<img align="right" width="50" src="https://raw.githubusercontent.com/limikael/freecad-slic3r-tools/master/Resources/icons/Slic3rInfo.svg?sanitize=true">

### Show Slic3r Info
Show quick information for your print. The information includes estimated print time, used filament and filament cost. In order to use this command, you need to set a profile .ini file for slic3r to use, see above.

<img align="right" width="50" src="https://raw.githubusercontent.com/limikael/freecad-slic3r-tools/master/Resources/icons/Slic3rGcode.svg?sanitize=true">

### Run Slic3r
Export .gcode for the current document, with the current slic3r settings. In order to use this command, you need to set a profile .ini file for slic3r to use, see above. There is no prompt to ask for a file name, the name of the exported .gcode file will be derived from your document file name.
