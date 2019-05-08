import FreeCAD
import os
import Mesh

class SlcrDoc:
    def __init__(self):
        self.doc=FreeCAD.ActiveDocument
        if not self.doc:
            raise Exception("No document open to slice")

    def hasInvisibleParent(self, o):
        for parent in o.InList:
            if parent.TypeId=="App::Part" or parent.TypeId=="PartDesign::Body":
                if not parent.ViewObject.isVisible():
                    return True

                if self.hasInvisibleParent(parent):
                    return True

        return False

    def getVisibleObjects(self):
        visibleObjs=[]
        for obj in self.doc.Objects:
            if obj.TypeId!="App::Part" and obj.TypeId!="PartDesign::Body":
                if obj.ViewObject.isVisible() and not self.hasInvisibleParent(obj):
                    visibleObjs.append(obj)

        return visibleObjs

    def exportVisible(self):
        if self.doc.FileName=="":
            raise Exception("Please save the document first to give it a filename.")

        visibleObjs=self.getVisibleObjects()
        if not len(visibleObjs):
            raise Exception("No visible objects to export")

#        for obj in visibleObjs:
#            print(obj.Name)

        stlFileName=os.path.splitext(self.doc.FileName)[0]+".stl"
        Mesh.export(visibleObjs,stlFileName)