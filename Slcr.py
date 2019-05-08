import os, importlib, sys
from SlcrDoc import SlcrDoc
from SlcrDialogUtil import DialogUtil

def exportVisible():
    try:
        doc=SlcrDoc()
        doc.exportVisible()

    except Exception as e:
        DialogUtil.showErrorMessage(e)

def slice():
    pass

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
