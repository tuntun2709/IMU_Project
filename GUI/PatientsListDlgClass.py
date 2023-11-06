from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from PySide6.QtWidgets import * 
from PySide6.QtCore import Signal
import sys
from PySide6.QtGui import *
import json
from popup_patientsList import Ui_Dialog

class PatientsList_Dlg(Ui_Dialog, QDialog):
    data_Patient = Signal(dict)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget_PatientsList.setSelectionBehavior(QTableWidget.SelectRows)  
        self.tableWidget_PatientsList.setSelectionMode(QTableWidget.SingleSelection)
        self.tableWidget_PatientsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_PatientsList.itemDoubleClicked.connect(self.selectPatient)
        self.tableWidget_PatientsList.sortItems(1)
        self.lineEdit_Search.textChanged.connect(self.searchPatient)
        self.file_data = {}

    def updateTable(self):        
        with open('sample.json','r') as file:
            self.file_data = json.load(file)
            file.close()

        self.tableWidget_PatientsList.setRowCount(len(self.file_data))
        for index_person in range(len(self.file_data)):
            self.tableWidget_PatientsList.setItem(index_person,0, QTableWidgetItem(str(index_person)))
            self.tableWidget_PatientsList.setItem(index_person,1, QTableWidgetItem(self.file_data[str(index_person)]['PatientCode']))
            self.tableWidget_PatientsList.setItem(index_person,2, QTableWidgetItem(self.file_data[str(index_person)]['name']))
            self.tableWidget_PatientsList.setItem(index_person,3, QTableWidgetItem(self.file_data[str(index_person)]['DateOfBirth']))
            self.tableWidget_PatientsList.setItem(index_person,4, QTableWidgetItem(self.file_data[str(index_person)]['ID']))
            self.tableWidget_PatientsList.setItem(index_person,5, QTableWidgetItem(self.file_data[str(index_person)]['Gender']))

    def selectPatient(self):
        patient = self.tableWidget_PatientsList.selectedItems()
        # print(patient[0].text())
        # if(patient[0].text() in self.file_data):
        #     print(self.file_data[patient[0].text()])  
        patientInfo = self.file_data[patient[0].text()]
        self.data_Patient.emit(patientInfo)
        self.accept()

    def searchPatient(self):
        self.tableWidget_PatientsList.setCurrentItem(None)
        if not self.lineEdit_Search.text():
            return
        matching_items = self.tableWidget_PatientsList.findItems(self.lineEdit_Search.text(), Qt.MatchStartsWith)
        if matching_items:
            item = matching_items[0] 
            self.tableWidget_PatientsList.setCurrentItem(item)
            self.tableWidget_PatientsList.scrollToItem(item, QAbstractItemView.PositionAtTop)