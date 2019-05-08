import os, importlib, sys, FreeCAD, subprocess

from SlcrDoc import SlcrDoc
from SlcrDialogUtil import DialogUtil

def exportVisible():
    try:
        doc=SlcrDoc()
        doc.exportVisible()

    except Exception as e:
        DialogUtil.showErrorMessage(e)

def slice():
    try:
        doc=SlcrDoc()
        doc.exportVisible()
        preferences=FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/slcr")
        slic3rPath=preferences.GetString('slic3rPath')
        if not slic3rPath.strip():
            raise Exception("Please set the path to the slic3r executable in preferences")

        subprocess.Popen([slic3rPath,doc.getStlFileName()])

    except Exception as e:
        DialogUtil.showErrorMessage(e)

def sliceInfo():
    pass

def exportGcode():
    pass

def devReload():
    if not os.path.isfile(os.path.dirname(__file__)+"/__dev__.py"):
        return

    print("Reloading module")
    importlib.reload(sys.modules["SlcrDialogUtil"])
    importlib.reload(sys.modules["SlcrDoc"])
    importlib.reload(sys.modules["Slcr"])
