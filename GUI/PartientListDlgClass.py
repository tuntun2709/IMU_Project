from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from PySide6.QtWidgets import * 
import sys
from PySide6.QtGui import *
import json
from popup_partientList import Ui_Dialog

class PartientList_Dlg(Ui_Dialog, QDialog):
    def __init__(self, parent: None):
        super().__init__(parent)
        self.setupUi(self)
        self.tableWidget_PartientList.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def updateTable(self):
        file_data = {}
        with open('sample.json','r') as file:
            file_data = json.load(file)
            file.close()

        self.tableWidget_PartientList.setRowCount(len(file_data))
        for index_person in range(len(file_data)):
            self.tableWidget_PartientList.setItem(index_person,0, QTableWidgetItem(str(index_person)))
            self.tableWidget_PartientList.setItem(index_person,1, QTableWidgetItem('Quang Suy'))
            self.tableWidget_PartientList.setItem(index_person,2, QTableWidgetItem(file_data[str(index_person)]['name']))
            self.tableWidget_PartientList.setItem(index_person,3, QTableWidgetItem(file_data[str(index_person)]['DateOfBirth']))
            self.tableWidget_PartientList.setItem(index_person,4, QTableWidgetItem(file_data[str(index_person)]['ID']))
            self.tableWidget_PartientList.setItem(index_person,5, QTableWidgetItem(file_data[str(index_person)]['Sex']))