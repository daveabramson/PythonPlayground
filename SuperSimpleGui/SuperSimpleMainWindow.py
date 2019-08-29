from PySide2 import QtWidgets
import SuperSimpleMainWindowUi



class SuperSimpleMainWindow(QtWidgets.QMainWindow, SuperSimpleMainWindowUi.Ui_MainWindow):
    """the class the connects with SuperSimpleMainWindowUi"""

    def __init__(self, parent=None):
        super(SuperSimpleMainWindow, self).__init__(parent)
        self.setupUi(self)


