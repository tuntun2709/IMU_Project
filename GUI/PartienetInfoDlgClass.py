from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from PySide6.QtCore import Signal
from PySide6.QtWidgets import * 
import sys
from PySide6.QtGui import *
import json
from popup_partientInformation import Ui_Dialog

class PartientInfo_Dlg(Ui_Dialog, QDialog):
    data_signal = Signal(dict) 

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.radioButton_Female.setChecked(True)
        self.pushButton_SaveInfomation.clicked.connect(self.saveData)

    def saveData(self):
        if self.radioButton_Female.isChecked:
            sex = 'Female'
        else:
            sex = 'Male'
        data = {'name':self.lineEdit_Name.text(),
                'ID':self.lineEdit_ID.text(),
                'Height': self.lineEdit_Height.text(),
                'Weight': self.lineEdit_Weight.text(),
                'Sex': sex,
                'Exercise':self.comboBox_Exercise.currentText(),
                'DateOfBirth': self.dateEdit_DateOfBirth.text()}
        self.data_signal.emit(data)
        self.lineEdit_Name.clear()
        self.lineEdit_ID.clear()
        self.lineEdit_Height.clear()
        self.lineEdit_Weight.clear()
        self.dateEdit_DateOfBirth.clear()
        self.accept()