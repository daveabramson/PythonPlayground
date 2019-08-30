from PySide2 import QtWidgets
import SuperSimpleMainWindowUi
import os
from DifferentWindow import DifferentWindow


class SuperSimpleMainWindow(QtWidgets.QMainWindow, SuperSimpleMainWindowUi.Ui_MainWindow):
    """the class the connects with SuperSimpleMainWindowUi"""

    def __init__(self, parent=None):
        super(SuperSimpleMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.BrowseFolder)
        self.listWidget.itemClicked.connect(self.DisplayItem)
        self.btnOpenDiffForm.clicked.connect(self.OpenDiffForm)

    def BrowseFolder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a folder")
        if directory:
            self.listWidget.addItems(os.listdir(directory))
            count = self.listWidget.count()
            self.lblItemCount.setText("Items: " + str(count))

    def DisplayItem(self):
        msgBox = QtWidgets.QMessageBox(None)
        msgBox.setWindowTitle("You picked this item")
        msgBox.setText(self.listWidget.currentItem().text())
        msgBox.exec_()

    def OpenDiffForm(self):
        diffForm = DifferentWindow(self)
        diffForm.exec_()
