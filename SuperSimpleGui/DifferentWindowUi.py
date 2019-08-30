# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DifferentWindow.ui',
# licensing of 'DifferentWindow.ui' applies.
#
# Created: Thu Aug 29 19:54:47 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_frmDifferentWindow(object):
    def setupUi(self, frmDifferentWindow):
        frmDifferentWindow.setObjectName("frmDifferentWindow")
        frmDifferentWindow.setWindowModality(QtCore.Qt.WindowModal)
        frmDifferentWindow.resize(298, 103)
        self.horizontalLayout = QtWidgets.QHBoxLayout(frmDifferentWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(frmDifferentWindow)
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.dialUpTo11 = QtWidgets.QDial(frmDifferentWindow)
        self.dialUpTo11.setWrapping(False)
        self.dialUpTo11.setObjectName("dialUpTo11")
        self.horizontalLayout.addWidget(self.dialUpTo11)

        self.retranslateUi(frmDifferentWindow)
        QtCore.QMetaObject.connectSlotsByName(frmDifferentWindow)

    def retranslateUi(self, frmDifferentWindow):
        frmDifferentWindow.setWindowTitle(QtWidgets.QApplication.translate("frmDifferentWindow", "Different Window", None, -1))

