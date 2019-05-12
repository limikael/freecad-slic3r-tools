# freecad-slic3r-tools
Tools for running Slic3r from FreeCAD

This module lets you quickly export all visible parts in the current document, and open the resulting .stl file in Slic3r.
You can also set up a default print profile, and directly get information about the resources that would be used to print it,
as well as quickly generate the .gcode file.

## Settings

Before you can use the module there are a few settings you need to set. To access these settings, go to Edit >> Preferences and then select "Slic3r Tools". The settings are:

### Path to slic3r executable

Set up the path to your where your slic3r executable is on your hard drive. If you run windows, this is the .exe file. If you run Linux, you can point to the .AppImage file here.

### Path to slic3r profile .ini file

This should point to a slic3r .ini file. The .ini file contains information about which printer you are using as well as layer
height, etc. While Slic3r has a GUI to let you work with several profiles at once and quickly change between them, the SLic3r
Toolbar can only work with one profile. To export the current profile from slic3r and use it from Slic3r Toolbar, go to File >>
Export Config... from inside Slic3r.

## Tools
