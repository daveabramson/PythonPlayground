from PySide2 import QtWidgets
from SuperSimpleGui import SuperSimpleMainWindowUi
import os
from SuperSimpleGui.DifferentWindow import DifferentWindow
import math


class SuperSimpleMainWindow(QtWidgets.QMainWindow, SuperSimpleMainWindowUi.Ui_MainWindow):
    """the class the connects with SuperSimpleMainWindowUi"""

    __MAX_ANGLE_RAD = math.pi / 2
    __MIN_ANGLE_RAD = -__MAX_ANGLE_RAD
    __MAX_ANGLE_DEG = 90
    __MIN_ANGLE_DEG = -__MAX_ANGLE_DEG


    def __init__(self, parent=None):
        super(SuperSimpleMainWindow, self).__init__(parent)
        self.setupUi(self)

        # connect events
        self.btnBrowse.clicked.connect(self.BrowseFolder)
        self.listWidget.itemClicked.connect(self.DisplayItem)
        self.btnOpenDiffForm.clicked.connect(self.OpenDiffForm)
        self.radRadians.toggled.connect(self.AngleUnitsChanged)
        self.radSteps.toggled.connect(self.RangeDefinitionMethodChanged)
        self.btnCalculate.clicked.connect(self.CalculateCosines)
        self.spinRangeMax.valueChanged.connect(self.MaxRangeValueChanged)
        self.spinRangeMin.valueChanged.connect(self.MinRangeValueChanged)

        # setup permissible ranges for angles
        if(self.radRadians.isChecked()):
            self.spinRangeMin.setMinimum(self.__MIN_ANGLE_RAD)
            self.spinRangeMax.setMaximum(self.__MAX_ANGLE_RAD)
        else:
            self.spinRangeMin.setMinimum(self.__MIN_ANGLE_DEG)
            self.spinRangeMax.setMaximum(self.__MAX_ANGLE_DEG)
        self.spinRangeMin.setMaximum(0)
        self.spinRangeMax.setMinimum(0)
       

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

    def AngleUnitsChanged(self):

        spinMax = 0 
        spinMin = 0

        # get the current values
        maxVal = self.spinRangeMax.value()
        minVal = self.spinRangeMin.value()


        # make the appropriate conversion and pick the min and max
        if(self.radRadians.isChecked()):
            maxVal = math.radians(maxVal)
            minVal = math.radians(minVal)
            spinMax = self.__MAX_ANGLE_RAD
            spinMin = self.__MIN_ANGLE_RAD
        elif(self.radDegrees.isChecked()):
            maxVal = math.degrees(maxVal)
            minVal = math.degrees(minVal)
            spinMax = self.__MAX_ANGLE_DEG
            spinMin = self.__MIN_ANGLE_DEG


        # set converted values back (and modified range of spin boxes)
        self.spinRangeMax.setMaximum(spinMax)
        self.spinRangeMin.setMinimum(spinMin)
        self.spinRangeMax.setMinimum(minVal)
        self.spinRangeMin.setMaximum(maxVal)
        self.spinRangeMax.setValue(maxVal)
        self.spinRangeMin.setValue(minVal)

    def MinRangeValueChanged(self):
        # don't allow the max to go below the min
        self.spinRangeMax.setMinimum(self.spinRangeMin.value())

    def MaxRangeValueChanged(self):
        # don't allow the min to go above the max
        self.spinRangeMin.setMaximum(self.spinRangeMax.value())


    def RangeDefinitionMethodChanged(self):
        pass
        # which method is checked?
        # set the decimal places and (initially display the new value somewhere)

    def CalculateCosines(self):
        pass
        # clear the list
        # collect values in form and create range source
        # call to calculate cosines
        # format the output into the list view