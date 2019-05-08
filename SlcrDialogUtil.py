from PySide import QtCore, QtGui

class DialogUtil:
    def showErrorMessage(err):
        message=str(err)
        dialog=QtGui.QMessageBox(QtGui.QMessageBox.Critical,'Error',message)
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.exec_()