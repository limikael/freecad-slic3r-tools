# -*- coding: utf-8 -*-
# Slcr gui init module
# (c) 2001 Juergen Riegel
# License LGPL

import SlcrResources3

class SlcrWorkbench ( Workbench ):
    "Slcr workbench object"

    import SlcrRoot,os
    Icon = os.path.dirname(SlcrRoot.__file__)+"/Resources/icons/Slic3r.svg"
    MenuText = "Slic3r Tools"
    ToolTip = "Slic3r Tools workbench"
    
    def Initialize(self):
        # load the module
        import SlcrGui,SlcrRoot,os
        commands=[
            'Slcr_ExportVisible',
            'Slcr_Slice',
            'Slcr_SliceInfo',
            'Slcr_ExportGcode'
        ]

        self.appendToolbar('Slic3r Tools',commands)
        self.appendMenu('Slic&3r Tools',commands)

        FreeCADGui.addPreferencePage(
            os.path.dirname(SlcrRoot.__file__)+
            '/Resources/ui/slcr-prefs.ui','Slic3r Tools'
        )
    
    def GetClassName(self):
        return "Gui::PythonWorkbench"

Gui.addWorkbench(SlcrWorkbench())
