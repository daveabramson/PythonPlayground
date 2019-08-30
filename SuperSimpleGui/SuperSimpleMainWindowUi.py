# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperSimpleMainWindow.ui',
# licensing of 'SuperSimpleMainWindow.ui' applies.
#
# Created: Thu Aug 29 19:28:27 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(307, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.lblItemCount = QtWidgets.QLabel(self.centralwidget)
        self.lblItemCount.setObjectName("lblItemCount")
        self.verticalLayout.addWidget(self.lblItemCount)
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.verticalLayout.addWidget(self.btnBrowse)
        self.btnOpenDiffForm = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenDiffForm.setObjectName("btnOpenDiffForm")
        self.verticalLayout.addWidget(self.btnOpenDiffForm)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lblItemCount.setText(QtWidgets.QApplication.translate("MainWindow", "Items: 0", None, -1))
        self.btnBrowse.setText(QtWidgets.QApplication.translate("MainWindow", "Pick a folder", None, -1))
        self.btnOpenDiffForm.setText(QtWidgets.QApplication.translate("MainWindow", "Open a Different Form", None, -1))

