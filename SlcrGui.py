# -*- coding: utf-8 -*-
# FreeCAD tools of the Slcr workbench
# (c) 2001 Juergen Riegel
# License LGPL

import FreeCAD, FreeCADGui, os, Slcr

class CmdExportVisible:
    def Activated(self):
        Slcr.devReload()
        Slcr.exportVisible()
    def IsActive(self):
        return True
    def GetResources(self):
        return {
            'Pixmap': os.path.dirname(__file__)+"/Resources/icons/Stl.svg",
            'MenuText': 'Export visible as .stl', 
            'ToolTip':
                "Export visible as .stl\n\n"+
                "Before you can run this command you need\n"+
                "to save the document to give it a name."
        }

class CmdSlice:
    def Activated(self):
        Slcr.devReload()
        Slcr.slice()
    def IsActive(self):
        return True
    def GetResources(self):
        return {
            'Pixmap': os.path.dirname(__file__)+"/Resources/icons/Slic3r.svg",
            'MenuText': 'Run Slic3r',
            'ToolTip':
                "Run Slic3r"
        }

class CmdSliceInfo:
    def Activated(self):
        Slcr.devReload()
        Slcr.sliceInfo()
    def IsActive(self):
        return True
    def GetResources(self):
        return {
            'Pixmap': os.path.dirname(__file__)+"/Resources/icons/Slic3rInfo.svg",
            'MenuText': 'Get slicing info',
            'ToolTip':
                "Get Slic3r info"
        }

class CmdExportGcode:
    def Activated(self):
        Slcr.devReload()
        Slcr.exportGcode()
    def IsActive(self):
        return True
    def GetResources(self):
        return {
            'Pixmap': os.path.dirname(__file__)+"/Resources/icons/Slic3rGcode.svg",
            'MenuText': 'Export visible as .gcode',
            'ToolTip':
                "Export visible as .gcode"
        }

FreeCADGui.addCommand('Slcr_ExportVisible', CmdExportVisible())
FreeCADGui.addCommand('Slcr_Slice', CmdSlice())
FreeCADGui.addCommand('Slcr_SliceInfo', CmdSliceInfo())
FreeCADGui.addCommand('Slcr_ExportGcode', CmdExportGcode())
