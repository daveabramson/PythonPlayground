from PySide2 import QtWidgets
from SuperSimpleGui import DifferentWindowUi


class DifferentWindow(QtWidgets.QDialog, DifferentWindowUi.Ui_frmDifferentWindow):
    """the class the connects with SuperSimpleMainWindowUi"""

    def __init__(self, parent=None):
        super(DifferentWindow, self).__init__(parent)
        self.setupUi(self)
        self.dialUpTo11.valueChanged.connect(self.DialValueChanged)


    def DialValueChanged(self):
        self.lcdNumber.display(self.dialUpTo11.value())