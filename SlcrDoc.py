import FreeCAD, os, sys, math, Mesh, MeshPart, subprocess

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


        # TODO: These should be configurable parameters
        degrees = 3
        millimeters = 0.1

        angl = degrees * math.pi/180

        visibleObjs=self.getVisibleObjects()
        if not len(visibleObjs):
            raise Exception("No visible objects to export")

#        for obj in visibleObjs:
#            print(obj.Name)

        mesh = Mesh.Mesh()
        for obj in visibleObjs:
            # Don't spam console with missing attribute errors for "Shape"
            if not hasattr(obj, "Shape"):
                continue

            try:
                shape = obj.Shape.copy(False)
                shape.Placement= obj.getGlobalPlacement()
                # See Mesh Design workbench => Tesselate shape => Standard
                # LinearDeflection is "Surface deviation"
                # AngularDeflection is "Angular deviation" but in radians (i.e. 3.14159 is 180°)
                mesh2 = MeshPart.meshFromShape(Shape=shape, LinearDeflection=millimeters, AngularDeflection=angl, Relative=False)
                mesh = mesh.unite(mesh2)
            except:
                print(obj.Name, sys.exc_info()[1])

        mesh.write(Filename=self.getStlFileName())

    def getStlFileName(self):
        if self.doc.FileName=="":
            raise Exception("Please save the document first to give it a filename.")

        return os.path.splitext(self.doc.FileName)[0]+".stl"

    def getGcodeFileName(self):
        if self.doc.FileName=="":
            raise Exception("Please save the document first to give it a filename.")

        return os.path.splitext(self.doc.FileName)[0]+".gcode"

    def generateGcode(self):
        preferences=FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/slcr")
        slic3rPath=preferences.GetString('slic3rPath')
        if not slic3rPath.strip():
            raise Exception("Please set the path to the slic3r executable in preferences")

        slic3rIniPath=preferences.GetString('slic3rIniPath')
        if not slic3rIniPath.strip():
            raise Exception("Please set the path to the slic3r profile .ini in preferences")

        slic3rOpts=[
            slic3rPath,
            "--no-gui",
            "--load",
            slic3rIniPath,
            self.getStlFileName(),
            "--output",
            self.getGcodeFileName()
        ]

        subprocess.check_output(slic3rOpts)
