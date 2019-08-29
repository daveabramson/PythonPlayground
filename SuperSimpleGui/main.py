from PySide2 import QtWidgets
import sys
from SuperSimpleMainWindow import SuperSimpleMainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = SuperSimpleMainWindow()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()