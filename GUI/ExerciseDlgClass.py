from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from popup_exercise import Ui_Dialog
from PySide6.QtWidgets import * 
import sys
from PySide6.QtGui import *


class Exercise_Dlg(Ui_Dialog, QDialog):
    def __init__(self, parent:  None , ):
        super().__init__(parent)
        self.setupUi(self)        
        self.tableWidget_Exercise.setColumnWidth(0,300)
        self.pb_AddExercise.clicked.connect(self.AddExercise)
        self.pb_EditExercise.clicked.connect(self.EditExercise)
        self.tableWidget_Exercise.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.rowCount = 0
        self.editMode = False
        f = open("Exercise.txt",'r', encoding='utf-8')
        for line in f:		
            if not (line == ''):
                self.tableWidget_Exercise.setRowCount(self.rowCount)
                self.tableWidget_Exercise.insertRow(self.rowCount)
                self.tableWidget_Exercise.setItem(self.rowCount, 0, QTableWidgetItem(line.replace("\n", "")))
                self.rowCount += 1
        f.close()

    def AddExercise(self):
        if not (self.lineEdit_Exercise.text() == ""):
            self.tableWidget_Exercise.setRowCount(self.rowCount)
            self.tableWidget_Exercise.insertRow(self.rowCount)
            self.tableWidget_Exercise.setItem(self.rowCount, 0, QTableWidgetItem(self.lineEdit_Exercise.text()))
            f = open("Exercise.txt", 'a', encoding='utf-8')
            f.write(self.lineEdit_Exercise.text()+ "\n")
            f.close()
            self.lineEdit_Exercise.clear()
            self.rowCount += 1
    
    def EditExercise(self):
        if not self.editMode:
            self.tableWidget_Exercise.setEditTriggers(QAbstractItemView.AllEditTriggers)
            self.pb_EditExercise.setText("Lưu")
            self.editMode = True
        else:
            self.tableWidget_Exercise.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.editMode = False
            self.pb_EditExercise.setText("Sửa")