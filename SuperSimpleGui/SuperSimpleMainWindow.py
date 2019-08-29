from PySide2 import QtWidgets
import SuperSimpleMainWindowUi
import os


class SuperSimpleMainWindow(QtWidgets.QMainWindow, SuperSimpleMainWindowUi.Ui_MainWindow):
    """the class the connects with SuperSimpleMainWindowUi"""

    def __init__(self, parent=None):
        super(SuperSimpleMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.BrowseFolder)
        self.listWidget.itemClicked.connect(self.DisplayItem)

    def BrowseFolder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Pick a folder")
        if directory:
            self.listWidget.addItems(os.listdir(directory))

    def DisplayItem(self):
        msgBox = QtWidgets.QMessageBox(None)
        msgBox.setWindowTitle("You picked this item")
        msgBox.setText(self.listWidget.currentItem().text())
        msgBox.exec_()

