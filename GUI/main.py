from numpy import angle
from random import randint
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation,Qt, QCoreApplication, Signal, QDate, QTimer
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QTableWidgetItem, QAbstractItemView, QTableWidget, QFileDialog
from ui_menu import Ui_MainWindow
import pyqtgraph as pg
import math
import json
import datetime
from ExerciseDlgClass import Exercise_Dlg
from PatientInfoDlgClass import PatientInfo_Dlg
from PatientsListDlgClass import PatientsList_Dlg

import paho.mqtt.client as mqtt
import threading
import time
from queue import Queue
import csv
# -------------------------------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.uic = Ui_MainWindow()		
		self.uic.setupUi(self)

		self.thisPage = 'Main'
		self.currentMainPatientCode = '-1'
		self.declare_var()
		self.currentTime = datetime.datetime.now()
		self.uic.stackedWidget.setCurrentWidget(self.uic.page_Main)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		self.uic.fr_sideMenu.setLineWidth(200)

		self.uic.rb_SettingCm.setChecked(True)
		self.uic.rb_SettingKg.setChecked(True)

		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)
		self.uic.fr_topMenu.mouseMoveEvent = self.mover 

		self.pb_menu_function()
		
		self.uic.pb_MainPatientsList.clicked.connect(self.onPatientListClinked)
		self.uic.pb_MainAddPatient.clicked.connect(self.onPatientAddClinked)
		self.uic.pb_ReviewPatientsList.clicked.connect(self.onPatientListClinked)
		self.uic.cb_MainExcercise.currentIndexChanged.connect(self.onExerciseChanged)
		self.uic.tableWidget_PatientInfoPatientTable.itemDoubleClicked.connect(self.getPatientInfoToEdit)
		self.uic.tableWidget_PatientInfoPatientTable.sortItems(0)
		self.uic.le_PatientInfoSearch.textChanged.connect(self.searchPatientInfo)
		self.uic.pb_PatientInfoSavePatient.clicked.connect(self.editPatientInfo)
		self.uic.pb_MainStartExercise.clicked.connect(self.startExercise)
		self.uic.pb_PatientInfoRemovePatient.clicked.connect(self.removePatientInfo)
		self.uic.pb_PatientInfoRemoveAll.clicked.connect(self.removeAllPatientInfo)
		self.uic.pb_MainConnector.clicked.connect(self.connectBroker)
		self.uic.pb_MainEndExercise.clicked.connect(self.disconnectBroker)

		self.lowerlimbMain()
		self.lineChartMain()
		self.lowerlimbReview()
		self.lineChartReview()

		self.dlg_PatientInfo.data_signal.connect(self.handle_newPatientInfo)
		self.dlg_PatientsList.data_Patient.connect(self.handle_Patient)
		# load exercise
		f = open("Exercise.txt",'r', encoding='utf-8')
		for line in f:		
			if not (line == ''):
				self.uic.cb_MainExcercise.addItem(line.replace('\n', ''))
		f.close()
		self.uic.cb_MainExcercise.addItem("Thêm mới")

		# -----------------------Connect-------------------------------------------
		self.q1 = Queue() #process queue for sensor 1
		self.log_list1 = [] #log list for sensor 1
		self.q2 = Queue()
		self.log_list2 = []
		self.q3 = Queue()
		self.log_list3 = []
		self.q4 = Queue()
		self.log_list4 = []

		self.nclients = 4
		self.process_queues = [self.q1, self.q2, self.q3, self.q4]
		self.log_lists = [self.log_list1, self.log_list2, self.log_list3, self.log_list4]
		# self.client_threads = []
		self.clients = []
		for i in range(self.nclients):
			cname="client"+str(i)
			t=int(time.time())
			client_id =cname+str(t) #create unique client_id
			client = mqtt.Client(client_id) #create new instance
			client.proq = self.process_queues[i]
			client.logL = self.log_lists[i]
			client.logfile = f'log_list{i+1}'
			client.on_connect = self.on_connect
			#client.on_publish = self.on_publish
			client.on_message = self.on_message
			client.username_pw_set("user" + str(i+1),"1234")
		# Create connection, the three parameters are broker address, broker port number, and keep-alive time respectively			
			self.clients.append(client)
		
		self.timer = QTimer()
		self.timer.setInterval(500)
		self.timer.timeout.connect(self.update_plot_data)
		self.timer.start()

		# self.q = next((q for q in self.process_queues if not q.empty()), Queue())

# --------------------------------------------------------------------------\
	def declare_var(self):
		self.dlg_Exercise = None
		self.dlg_PatientInfo = PatientInfo_Dlg()
		self.dlg_PatientsList = PatientsList_Dlg()
		self.numOfPatient = 0
		try:
			with open('sample.json', 'r', encoding='utf-8') as f:
				e = json.load(f)
				self.numOfPatient = len(e)
				# print(self.numOfPatient)
				f.close()
		except:
			f = open('sample.json', 'w', encoding='utf-8')
			f.write('{}')
			f.close()

	def pb_menu_function(self):
		self.uic.pb_Main.clicked.connect(lambda: self.changePage("Main"))
		self.uic.pb_Calibration.clicked.connect(lambda: self.changePage("Calib"))
		self.uic.pb_Introduction.clicked.connect(lambda: self.changePage("Introduction"))
		self.uic.pb_Patient.clicked.connect(lambda: self.changePage("PatientInfo"))
		self.uic.pb_Review.clicked.connect(lambda: self.changePage("Review"))
		self.uic.pb_Setting.clicked.connect(lambda: self.changePage("Setting"))
		self.uic.bt_smallSize.hide()
		self.uic.bt_close.clicked.connect(self.control_bt_close)
		self.uic.bt_expand.clicked.connect(self.control_bt_expand)
		self.uic.bt_mini.clicked.connect(self.control_bt_mini)
		self.uic.bt_smallSize.clicked.connect(self.control_bt_smallSize)
		self.uic.bt_Menu.clicked.connect(self.control_menu)

	def control_bt_mini(self):
		self.showMinimized()
	
	def control_bt_close(self):		
		self.close()

	def control_bt_expand(self):
		self.showMaximized()
		self.uic.bt_smallSize.show()
		self.uic.bt_expand.hide()

	def control_bt_smallSize(self, event):
		self.showNormal()
		if self.y() <=20:
			self.move(200 , 20)        
		self.uic.bt_smallSize.hide()
		self.uic.bt_expand.show()

	def control_menu(self):
		width = self.uic.fr_sideMenu.width()
		normal = 0
		if width == 0:
			expand_width = 200
		else:
			expand_width = normal
		
		self.animation = QPropertyAnimation(self.uic.fr_sideMenu, b'minimumWidth')
		self.animation.setDuration(300)
		self.animation.setStartValue(width)
		self.animation.setEndValue(expand_width)
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
		self.animation.start()

	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	def mousePressEvent(self, event):
		self.clickPosition = event.globalPosition()

	def mover(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == Qt.LeftButton:
				delta = QtCore.QPointF(event.globalPosition() - self.clickPosition)
				self.move(self.x() + delta.x(), self.y() + delta.y())
				# self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPosition()
				event.accept()

		if event.globalPosition().y() <=20:
			self.showMaximized()
			self.uic.bt_smallSize.show()
			self.uic.bt_expand.hide()
		else:
			self.showNormal()
			self.uic.bt_smallSize.hide()
			self.uic.bt_expand.show()
	
	def changePage(self, page):
		if(page == "Main"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Main)
			self.thisPage = "Main"
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Trang Ch\u1ee7", None))
		elif(page == "Calib"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Calib)
			self.thisPage = "Calib"
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Hi\u1ec7u Ch\u1ec9nh", None))
		elif(page == "Review"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Review)
			self.thisPage = "Review"
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Xem L\u1ea1i", None))
		elif(page == "PatientInfo"):
			self.loadPatientsList()
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_PatientInfomation)
			self.thisPage = "PatientInfo"
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin b\u1ec7nh nh\u00e2n", None))
		elif(page == "Setting"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Setting)
			self.thisPage = "Setting"
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0110\u1eb7t", None))
		elif(page == "Introduction"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Introduction)
			self.thisPage = "Introduction"
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"", None))

	def lowerlimbMain(self):
		l_back = 400
		l_thigh = 400
		l_shin = 380
		l_foot = 200
		x0 = 0
		y0 = 0
		x1 = x0 + l_back*math.cos(math.radians(-90))
		y1 = y0 + l_back*math.sin(math.radians(-90))
		x2 = x1 + l_thigh*math.cos(math.radians(-40))
		y2 = y1 + l_thigh*math.sin(math.radians(-40))
		x3 = x2 + l_shin*math.cos(math.radians(-70))
		y3 = y2 + l_shin*math.sin(math.radians(-70))
		x4 = x3 + l_foot*math.cos(math.radians(-10))
		y4 = y3 + l_foot*math.sin(math.radians(-10))
		
		pen1 = pg.mkPen(color=(39, 164, 242), width=30)
		pen2 = pg.mkPen(color=(62, 174, 244), width=25)
		pen3 = pg.mkPen(color=(110, 194, 247), width=20)
		pen4 = pg.mkPen(color=(159, 215, 248), width=15)

		lowerlimbChart = pg.plot()
		lowerlimbChart.showGrid(x = True, y = True)
		lowerlimbChart.plot([x3,x4], [y3,y4], pen= pen4, symbol = 'o')
		lowerlimbChart.plot([x2,x3], [y2,y3], pen= pen3, symbol = 'o')
		lowerlimbChart.plot([x1,x2], [y1,y2], pen= pen2, symbol = 'o')
		lowerlimbChart.plot([x0,x1], [y0,y1], pen= pen1, symbol = 'o')
		lowerlimbChart.setBackground('w')
		lowerlimbChart.setXRange(-100, 1100, padding= 0)
		lowerlimbChart.setYRange(-1100, 100, padding= 0)
		layoutMain_lowerlimb = QHBoxLayout()
		self.uic.widget_MLowerlimb.setLayout(layoutMain_lowerlimb)		
		layoutMain_lowerlimb.addWidget(lowerlimbChart)

	def lineChartMain(self):
		self.time = [0 for _ in range(10)]
		self.hipAngle = [0 for _ in range(10)]
		self.kneeAngle = [0 for _ in range(10)]
		self.ankleAngle = [0 for _ in range(10)]
		linechart = pg.plot()
		linechart.showGrid(x = True, y = True)
		linechart.addLegend()
		# set properties of the label for y axis
		linechart.setLabel('left', 'Vertical Values', units ='y')
		# set properties of the label for x axis
		linechart.setLabel('bottom', 'Horizontal Values', units ='s')
		# setting horizontal range
		linechart.setXRange(0, 10)
		pen1 = pg.mkPen(color=(39, 164, 242), width=5)
		pen2 = pg.mkPen(color=(255, 0, 0), width=5)
		pen3 = pg.mkPen(color=(0, 255, 0), width=5)
		self.line1 = linechart.plot(self.time, self.hipAngle, pen =pen1)
		self.line2 = linechart.plot(self.time, self.kneeAngle, pen =pen2)
		self.line3 = linechart.plot(self.time, self.ankleAngle, pen =pen3)
		self.line1.setSymbol('o')
		self.line2.setSymbol('o')
		self.line3.setSymbol('o')
		linechart.setBackground('w')
		layoutMain_linechart = QHBoxLayout()		
		self.uic.widget_MLinechart.setLayout(layoutMain_linechart)		
		layoutMain_linechart.addWidget(linechart)	

	def update_plot_data(self):
		
		if not (self.q1.empty() or self.q2.empty() or self.q3.empty() or self.q4.empty()):
			self.time = self.time[1:]  # Remove the first y element.
			self.time.append(self.time[-1] + 1)  # Add a new value 1 higher than the last.

			data1 = self.q1.get()
			data2 = self.q2.get()
			data3 = self.q3.get()
			data4 = self.q4.get()
			hip = float(data2.split(',')[2]) - float(data1.split(',')[2])
			knee = float(data3.split(',')[2]) - float(data2.split(',')[2])
			ankle = float(data4.split(',')[2]) - float(data3.split(',')[2])
			self.hipAngle = self.hipAngle[1:]  # Remove the first
			self.kneeAngle = self.kneeAngle[1:]
			self.ankleAngle = self.ankleAngle[1:]
			self.hipAngle.append(hip)  # Add a new random value.
			self.kneeAngle.append(knee)
			self.ankleAngle.append(ankle)

			self.line1.setData(self.time, self.hipAngle)  # Update the data.
			self.line2.setData(self.time, self.kneeAngle)
			self.line3.setData(self.time, self.ankleAngle)

	def onPatientAddClinked(self):
		if self.dlg_PatientInfo == None:
			self.dlg_PatientInfo = PatientInfo_Dlg(self)
		if self.dlg_PatientInfo.isVisible():
			self.dlg_PatientInfo.close()
		else:
			self.dlg_PatientInfo.show()

	def onExerciseClinked(self):
		if self.dlg_Exercise == None:
			self.dlg_Exercise = Exercise_Dlg(self)
		if self.dlg_Exercise.isVisible():
			self.dlg_Exercise.close()
		else:
			self.dlg_Exercise.show()

	def onExerciseChanged(self):
		if (self.uic.cb_MainExcercise.currentText() == "Thêm mới"):        
			self.onExerciseClinked()
	
	def onPatientListClinked(self):
		if self.dlg_PatientsList == None:
			self.dlg_PatientsList = PatientsList_Dlg(self)
		if self.dlg_PatientsList.isVisible():
			self.dlg_PatientsList.close()
		else:
			self.dlg_PatientsList.updateTable()
			self.dlg_PatientsList.show()

	def handle_newPatientInfo(self, data):
		data_list = {}
		# print(data)
		with open('sample.json', 'r', encoding='utf-8') as f:
			data_list = json.load(f)
			data_list[str(self.numOfPatient)] = data	
			self.numOfPatient += 1		
			f.close()
		
		with open('sample.json','w', encoding='utf-8') as f:			
			json.dump(data_list, f, indent= 4)
			f.close()
		
		self.uic.lb_MainPatientName.setText(data['name'])
		self.uic.lb_MainPatientID.setText(data['ID'])
		self.uic.lb_MainDateOfBirth.setText(data['DateOfBirth'])
		self.uic.lb_MainPatientGender.setText(data['Gender'])
		self.uic.lb_MainPatientWeight.setText(data['Weight']+'kg')
		self.uic.lb_MainPatientHeight.setText(data['Height']+ 'cm')
		self.uic.lb_MainPatientCode.setText(data['PatientCode'])
		self.currentTime = datetime.datetime.now()
		self.uic.lb_MainDayExercise.setText(str(self.currentTime))
		
	def loadPatientsList(self):
		file_data = {}
		with open('sample.json','r', encoding='utf-8') as file:
			file_data = json.load(file)
			file.close()
		self.uic.tableWidget_PatientInfoPatientTable.setRowCount(len(file_data))
		for index_person in range(len(file_data)):
			self.uic.tableWidget_PatientInfoPatientTable.setItem(index_person,0, QTableWidgetItem(str(index_person)))
			self.uic.tableWidget_PatientInfoPatientTable.setItem(index_person,1, QTableWidgetItem(file_data[str(index_person)]['PatientCode']))
			self.uic.tableWidget_PatientInfoPatientTable.setItem(index_person,2, QTableWidgetItem(file_data[str(index_person)]['name']))
			self.uic.tableWidget_PatientInfoPatientTable.setItem(index_person,3, QTableWidgetItem(file_data[str(index_person)]['DateOfBirth']))
			self.uic.tableWidget_PatientInfoPatientTable.setItem(index_person,4, QTableWidgetItem(file_data[str(index_person)]['ID']))
			self.uic.tableWidget_PatientInfoPatientTable.setItem(index_person,5, QTableWidgetItem(file_data[str(index_person)]['Gender']))
		
		self.uic.tableWidget_PatientInfoPatientTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.uic.tableWidget_PatientInfoPatientTable.setSelectionBehavior(QTableWidget.SelectRows)  
		self.uic.tableWidget_PatientInfoPatientTable.setSelectionMode(QTableWidget.SingleSelection)

	def lowerlimbReview(self):
		l_back = 400
		l_thigh = 400
		l_shin = 380
		l_foot = 200
		x0 = 0
		y0 = 0
		x1 = x0 + l_back*math.cos(math.radians(-90))
		y1 = y0 + l_back*math.sin(math.radians(-90))
		x2 = x1 + l_thigh*math.cos(math.radians(-40))
		y2 = y1 + l_thigh*math.sin(math.radians(-40))
		x3 = x2 + l_shin*math.cos(math.radians(-70))
		y3 = y2 + l_shin*math.sin(math.radians(-70))
		x4 = x3 + l_foot*math.cos(math.radians(-10))
		y4 = y3 + l_foot*math.sin(math.radians(-10))
		
		pen1 = pg.mkPen(color=(39, 164, 242), width=30)
		pen2 = pg.mkPen(color=(62, 174, 244), width=25)
		pen3 = pg.mkPen(color=(110, 194, 247), width=20)
		pen4 = pg.mkPen(color=(159, 215, 248), width=15)

		lowerlimbChartReview = pg.plot()
		lowerlimbChartReview.showGrid(x = True, y = True)
		lowerlimbChartReview.plot([x3,x4], [y3,y4], pen= pen4, symbol = 'o')
		lowerlimbChartReview.plot([x2,x3], [y2,y3], pen= pen3, symbol = 'o')
		lowerlimbChartReview.plot([x1,x2], [y1,y2], pen= pen2, symbol = 'o')
		lowerlimbChartReview.plot([x0,x1], [y0,y1], pen= pen1, symbol = 'o')
		lowerlimbChartReview.setBackground('w')
		lowerlimbChartReview.setXRange(-100, 1100, padding= 0)
		lowerlimbChartReview.setYRange(-1100, 100, padding= 0)
		layoutReview_lowerlimb = QHBoxLayout()
		self.uic.widget_ReviewLowerlimb.setLayout(layoutReview_lowerlimb)		
		layoutReview_lowerlimb.addWidget(lowerlimbChartReview)

	def lineChartReview(self):
		hour = [1,2,3,4,5,6,7,8,9,10]
		temperature = [30,32,34,32,33,31,29,32,35,45]
		linechartReview = pg.plot()
		linechartReview.showGrid(x = True, y = True)
		linechartReview.addLegend()
		# set properties of the label for y axis
		linechartReview.setLabel('left', 'Vertical Values', units ='y')
		# set properties of the label for x axis
		linechartReview.setLabel('bottom', 'Horizontal Values', units ='s')
		# setting horizontal range
		linechartReview.setXRange(0, 10)
		pen = pg.mkPen(color=(39, 164, 242), width=5)
		line1 = linechartReview.plot(hour, temperature, pen =pen)
		line1.setSymbol('o')
		linechartReview.setBackground('w')
		layoutReview_linechart = QHBoxLayout()		
		self.uic.widget_ReviewLinechart.setLayout(layoutReview_linechart)		
		layoutReview_linechart.addWidget(linechartReview)	

	def handle_Patient(self, data):
		if(self.thisPage == "Main"):
			self.uic.lb_MainPatientName.setText(data['name'])
			self.uic.lb_MainPatientID.setText(data['ID'])
			self.uic.lb_MainDateOfBirth.setText(data['DateOfBirth'])
			self.uic.lb_MainPatientGender.setText(data['Gender'])
			self.uic.lb_MainPatientWeight.setText(data['Weight']+'kg')
			self.uic.lb_MainPatientHeight.setText(data['Height']+ 'cm')
			self.uic.lb_MainPatientCode.setText(data['PatientCode'])
			self.currentTime = datetime.datetime.now()
			self.uic.lb_MainDayExercise.setText(str(self.currentTime))
			self.currentMainPatientCode = data['PatientCode']
		
		if(self.thisPage == "Review"):
			self.uic.lb_ReviewPatientName.setText(data['name'])
			self.uic.lb_ReviewPatientID.setText(data['ID'])
			self.uic.lb_ReviewPatientDateOfBirth.setText(data['DateOfBirth'])
			self.uic.lb_ReviewPatientGender.setText(data['Gender'])
			self.uic.lb_ReviewWeight.setText(data['Weight']+'kg')
			self.uic.lb_ReviewHeight.setText(data['Height']+ 'cm')
			self.uic.lb_ReviewCode.setText(data['PatientCode'])
			self.currentTime = datetime.datetime.now()
			# self.uic.lb_ReviewDayExercise.setText(str(self.currentTime))
			self.uic.cb_ReviewExercise.clear()
			self.uic.cb_ReviewDayExercise.clear()
			for value in data['Exercise']:
				# print(value)
				self.uic.cb_ReviewExercise.addItem(value.split('_')[0])
				self.uic.cb_ReviewDayExercise.addItem(value.split('_')[1])

	def editPatientInfo(self):
		Patient = self.uic.tableWidget_PatientInfoPatientTable.selectedItems()
		ParitentList = {}
		with open('sample.json','r', encoding='utf-8') as file:
			ParitentList = json.load(file)
			file.close()
		# PatientInfo = ParitentList[Patient[0].text()]
		if self.uic.cb_PatientInfoGender.currentText() == 'Nam':
			Gender = 'Male'
		else:
			Gender = 'FeMale'
		data = {'name':self.uic.le_PatientInfoName.text(),
				'ID':self.uic.le_PatientInfoID.text(),
				'Height': self.uic.le_PatientInfoHeight.text(),
				'Weight': self.uic.le_PatientInfoWeight.text(),
				'Gender': Gender,
				'DateOfBirth': self.uic.de_PatientInfoDateOfBirth.text(),
				'PatientCode': ParitentList[Patient[0].text()]['PatientCode'],
				'Exercise': ParitentList[Patient[0].text()]['Exercise']}
		ParitentList[Patient[0].text()] = data
		with open('sample.json','w', encoding='utf-8') as f:			
			json.dump(ParitentList, f, indent= 4)
			f.close()
		self.loadPatientsList()

	def getPatientInfoToEdit(self):
		Patient = self.uic.tableWidget_PatientInfoPatientTable.selectedItems()
		ParitentList = {}
		with open('sample.json','r', encoding='utf-8') as file:
			ParitentList = json.load(file)
			file.close()
		PatientInfo = ParitentList[Patient[0].text()]
		self.uic.le_PatientInfoName.setText(PatientInfo['name'])
		self.uic.le_PatientInfoID.setText(PatientInfo['ID'])
		date = PatientInfo['DateOfBirth'].split('/')
		self.uic.de_PatientInfoDateOfBirth.setDate(QDate(int(date[2]),int(date[1]) , int(date[0])))
		if(PatientInfo['Gender'] == 'Male'):
			self.uic.cb_PatientInfoGender.setCurrentIndex(0)
		else:
			self.uic.cb_PatientInfoGender.setCurrentIndex(1)		
		self.uic.le_PatientInfoWeight.setText(PatientInfo['Weight'])
		self.uic.le_PatientInfoHeight.setText(PatientInfo['Height'])
		self.uic.lb_PatientInfoPatitentCode.setText(PatientInfo['PatientCode'])

	def startExercise(self):
		Exercise = self.uic.cb_MainExcercise.currentText()+'_' + self.uic.lb_MainDayExercise.text()
		
		with open('sample.json','r', encoding='utf-8') as file:
			file_data = json.load(file)
			file.close()
		for index_person in range(len(file_data)):
			if file_data[str(index_person)]['PatientCode'] == self.currentMainPatientCode:				
				file_data[str(index_person)]['Exercise'].append(Exercise)				
		
		with open('sample.json','w', encoding='utf-8') as f:			
			json.dump(file_data, f, indent= 4)
			f.close()
		
		self.client_threads = []
		for client in self.clients:
			self.client_threads.append(threading.Thread(target=self.Sub, args=(client,f'mqtt{self.clients.index(client)+1}')))
		for thread in self.client_threads:
			thread.start()
<<<<<<< Updated upstream
=======
		
		self.threadTimer = RepeatTimer(0.027, self.update_plotDataMain)
		self.threadTimer.start()
>>>>>>> Stashed changes

	def searchPatientInfo(self):
		self.uic.tableWidget_PatientInfoPatientTable.setCurrentItem(None)
		if not self.uic.le_PatientInfoSearch.text():
			return	

		matching_items = self.uic.tableWidget_PatientInfoPatientTable.findItems(self.uic.le_PatientInfoSearch.text(), Qt.MatchStartsWith)
		if matching_items:
			# we have found something
			item = matching_items[0]  # take the first
			self.uic.tableWidget_PatientInfoPatientTable.setCurrentItem(item)
			self.uic.tableWidget_PatientInfoPatientTable.scrollToItem(item, QAbstractItemView.PositionAtTop)

	def removePatientInfo(self):
		Patient = self.uic.tableWidget_PatientInfoPatientTable.selectedItems()
		ParitentList = {}
		with open('sample.json','r', encoding='utf-8') as file:
			ParitentList = json.load(file)
			file.close()
		print(ParitentList[Patient[0].text()])
		del ParitentList[Patient[0].text()]
		with open('sample.json','w', encoding='utf-8') as f:			
			json.dump(ParitentList, f, indent= 4)
			f.close()
		self.loadPatientsList()
	
	def removeAllPatientInfo(self):
		with open('sample.json','w', encoding='utf-8') as f:			
			json.dump({}, f)
			f.close()
		self.loadPatientsList()
	
	def on_connect(self, client, userdata, flags, rc):
		print(f"Connected with result code {rc}")

	def on_log(self, client, userdata, level, buf):
		print("log: " + buf)

	def on_message(self, client, userdata, msg):
		message = str(msg.payload.decode("utf-8"))
		topics = msg.topic.split('/')
		subtopic = topics[1]
		match subtopic:
			case 'data':
				client.proq.put(message)
				client.logL.append([message])
				# print(f'{topics[0]}: {client.proq.qsize()}')
		# Save data to file on each message
<<<<<<< Updated upstream
				with open(f'{client.logfile}.csv', 'w', newline='') as f:
					csvwriter = csv.writer(f)
					csvwriter.writerows(client.logL)
					f.close()
				print(message)
=======
				# with open(f'{client.logfile}.csv', 'w', newline='') as f:
				# 	csvwriter = csv.writer(f)
				# 	csvwriter.writerows(client.logL)
				# 	f.close()
				# angles = message.split(',')
				# # print(message)
				# self.uic.lb_MainMaxHipAngle.setText(angles[0])
				# self.uic.lb_MainMaxKneeAngle.setText(angles[1])
				# self.uic.lb_MainMaxAnkleAngle.setText(angles[2])
				# self.countData +=1
				# self.uic.tableWidget_MDataTable.setRowCount(self.countData)
				# self.uic.tableWidget_MDataTable.insertRow(0)
				# self.uic.tableWidget_MDataTable.setItem(0,0,QTableWidgetItem(angles[0]))
				# self.uic.tableWidget_MDataTable.setItem(0,1,QTableWidgetItem(angles[1]))
				# self.uic.tableWidget_MDataTable.setItem(0,2,QTableWidgetItem(angles[2]))
				
>>>>>>> Stashed changes
			case 'calib':
				print(f'{topics[0]}: {message}')
			case 'calib_status':
				if message == 'a':
					print('imu is not calibrated')
				else:
					print('imu is calibrated')

	def Sub(self, client, topic):
		client.subscribe(f'{topic}/#')
		client.loop_start()

	def connectBroker(self):
		for client in self.clients:
			client.connect("192.168.50.10", 1883, 3600)

	def disconnectBroker(self):
		while not self.q1.empty():
			self.update_plot_data()
		for client in self.clients:
			client.proq = Queue()
			client.loop_stop()
		for thread in self.client_threads:
			thread.join()
<<<<<<< Updated upstream
		print('All threads ended')
=======
		print('threads stop')
		# self.q1 = Queue()
		# self.q2 = Queue()
		# self.q3 = Queue()
		# self.q4 = Queue()
		print(self.q1.qsize(),self.q2.qsize(),self.q3.qsize(),self.q4.qsize())
		self.threadTimer.cancel()
		

	def save_result(self):
		self.options = QFileDialog.Options()
		self.options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","csv Files (*.csv)", options=self.options)
		if fileName:
			if not fileName[-4:] == '.csv':
				fileName += '.csv'
			text = ['ngay moi','asdbajsd']
			data = [ ['Nikhil', 'COE', '2', '9.0'],  
			['Sanchit', 'COE', '2', '9.1'],  
			['Aditya', 'IT', '2', '9.3'],  
			['Sagar', 'SE', '1', '9.5'],  
			['Prateek', 'MCE', '3', '7.8'],  
			['Sahil', 'EP', '2', '9.1']]
			# print(fileName)
			try:
				f = open(fileName, "w", encoding='utf-8', newline='')
				writer = csv.writer(f)
				writer.writerow(text)
				writer.writerows(data)
				# f.write(text)
				f.close()
				# self.rebuildHTML()
			except IOError:
				QMessageBox.information(
					self,
					"Unable to open file: %s" % fileName
				)

	def update_plotDataMain(self):
		if not (self.q1.empty() or self.q2.empty() or self.q3.empty() or self.q4.empty()):
			t1 = time.perf_counter()
			self.time = self.time[1:]  # Remove the first y element.
			self.time.append(self.time[-1] + 1)  # Add a new value 1 higher than the last.

			data1 = self.q1.get()
			data2 = self.q2.get()
			data3 = self.q3.get()
			data4 = self.q4.get()
			# print(data1, data2, data3, data4)
			# print(self.q1.qsize(),self.q2.qsize(),self.q3.qsize(),self.q4.qsize())
			hip = float(data2.split(',')[2]) - float(data1.split(',')[2])
			knee = float(data3.split(',')[2]) - float(data2.split(',')[2])
			ankle = float(data4.split(',')[2]) - float(data3.split(',')[2])
			print('knee:', knee)
			
			self.hipAngle = self.hipAngle[1:]  # Remove the first
			self.kneeAngle = self.kneeAngle[1:]
			self.ankleAngle = self.ankleAngle[1:]
			self.hipAngle.append(hip)  # Add a new random value.
			self.kneeAngle.append(knee)
			self.ankleAngle.append(ankle)
			print('something')
			self.line1.setData(self.time, self.hipAngle)  # Update the data.
			self.line2.setData(self.time, self.kneeAngle)
			self.line3.setData(self.time, self.ankleAngle)
			print(time.perf_counter())
			t2 = time.perf_counter()
			# print(f'time elapsed: {t2 - t1}')
	def update_plotDataReview(self):
		self.time_review = self.time_review[0:]
		self.time_review.append(self.time_review[-1] + 1) 
		self.angle_review = self.angle_review[0:]
		self.angle_review.append(random.randrange(10,30))
		self.line_review.setData(self.time_review, self.angle_review)
		self.linechartReview.setXRange(len(self.time_review)-10, len(self.time_review))
		l_back = 400
		l_thigh = 400
		l_shin = 380
		l_foot = 200
		x0 = 0
		y0 = 0
		x1 = x0 + l_back*math.cos(math.radians(-90 + random.randrange(-5,5)))
		y1 = y0 + l_back*math.sin(math.radians(-90+ random.randrange(-5,5)))
		x2 = x1 + l_thigh*math.cos(math.radians(-40+ random.randrange(-5,5)))
		y2 = y1 + l_thigh*math.sin(math.radians(-40+ random.randrange(-5,5)))
		x3 = x2 + l_shin*math.cos(math.radians(-70+ random.randrange(-5,5)))
		y3 = y2 + l_shin*math.sin(math.radians(-70+ random.randrange(-5,5)))
		x4 = x3 + l_foot*math.cos(math.radians(-10+ random.randrange(-5,5)))
		y4 = y3 + l_foot*math.sin(math.radians(-10+ random.randrange(-5,5)))
		self.lowerlimbReview1.setData([x3,x4], [y3,y4], symbol = 'o')
		self.lowerlimbReview2.setData([x2,x3], [y2,y3], symbol = 'o')
		self.lowerlimbReview3.setData([x1,x2], [y1,y2], symbol = 'o')
		self.lowerlimbReview4.setData([x0,x1], [y0,y1], symbol = 'o')
	
	def changeSpeed(self, value):
		self.timer = QTimer()
		self.timer.setInterval(value+50)
		self.timer.timeout.connect(self.update_plotDataReview)
		self.timer.start()
>>>>>>> Stashed changes

	def update_data(self):
		if not (self.q1.empty() or self.q2.empty() or self.q3.empty() or self.q4.empty()):
			

# -------------------------------------------------------------------------------

class RepeatTimer(threading.Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
            # print('thread is running')

# ---------------------------------------------------------------------------------
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec())