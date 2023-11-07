from random import randint
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation,Qt, QCoreApplication, Signal, QTimer
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QTableWidgetItem, QAbstractItemView
from ui_menu import Ui_MainWindow
import pyqtgraph as pg
import math
import json
from ExerciseDlgClass import Exercise_Dlg
from PartienetInfoDlgClass import PartientInfo_Dlg
from PartientListDlgClass import PartientList_Dlg

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

		self.declare_var()
		self.uic.stackedWidget.setCurrentWidget(self.uic.page_Main)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		self.uic.fr_sideMenu.setLineWidth(200)

		self.uic.rb_Stcm.setChecked(True)
		self.uic.rb_StKg.setChecked(True)

		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		self.uic.fr_topMenu.mouseMoveEvent = self.mover 

		self.pb_menu_function()
		
		self.uic.pb_MainPartientList.clicked.connect(self.onPartientListClinked)
		self.uic.pb_MainAddPartient.clicked.connect(self.onPartientAddClinked)
		self.uic.pb_ReviewPartientList.clicked.connect(self.onPartientListClinked)
		self.uic.cb_MainExcercise.currentIndexChanged.connect(self.onExerciseChanged)
		
		self.lowerlimb()
		self.lineChart()

		self.dlg_PartientInfo.data_signal.connect(self.handle_data)

		# load exercise
		f = open("Exercise.txt",'r', encoding='utf-8')
		for line in f:		
			if not (line == ''):
				self.uic.cb_MainExcercise.addItem(line.replace('\n', ''))
				self.uic.cb_ReviewExercise.addItem(line.replace('\n', ''))
		f.close()
		self.uic.cb_MainExcercise.addItem("Thêm mới")



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
		self.client_threads = []
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
			client.connect("192.168.50.10", 1883, 3600)
			self.client_threads.append(threading.Thread(target=self.Sub, args=(client,f'mqtt{i+1}')))

		for thread in self.client_threads:
			thread.start()
	### Start the threads aka start receiving data	
		

		# self.timer1 = QTimer()
		# self.timer1.setInterval(20)
		# self.timer1.timeout.connect(self.update_data)
		# self.timer1.start()

		self.timer2 = QTimer()
		self.timer2.setInterval(500)
		self.timer2.timeout.connect(self.update_plot_data)
		self.timer2.start()

		# self.q = next((q for q in self.process_queues if not q.empty()), Queue())
	
	# def update_data(self):
	# 	for queue in self.process_queues:
	# 		queue.put(randint(0, 180))

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
				mess = message.split(',')
				client.logL.append([mess[0], mess[1], mess[2]])
		# Save data to file on each message
				with open(f'{client.logfile}.csv', 'w', newline='') as f:
					csvwriter = csv.writer(f)
					csvwriter.writerows(client.logL)
					f.close()
				print(message)
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


# --------------------------------------------------------------------------\
	def declare_var(self):
		self.dlg_Exercise = None
		self.dlg_PartientInfo = PartientInfo_Dlg()
		self.dlg_PartientList = None
		self.numOfPartient = 0
		try:
			with open('sample.json', 'r') as f:
				e = json.load(f)
				self.numOfPartient = len(e)
				# print(self.numOfPartient)
				f.close()
		except:
			f = open('sample.json', 'w')
			f.write('{}')
			f.close()

	def pb_menu_function(self):
		self.uic.pb_Main.clicked.connect(lambda: self.changePage("Main"))
		self.uic.pb_Calibration.clicked.connect(lambda: self.changePage("Calib"))
		self.uic.pb_Introduction.clicked.connect(lambda: self.changePage("Introduction"))
		self.uic.pb_Patient.clicked.connect(lambda: self.changePage("PartientInfo"))
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
		for client in self.clients:
			client.loop_stop()
		for thread in self.client_threads:
			thread.join()
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
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Trang Ch\u1ee7", None))
		elif(page == "Calib"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Calib)
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Hi\u1ec7u Ch\u1ec9nh", None))
		elif(page == "Review"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Review)
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Xem L\u1ea1i", None))
		elif(page == "PartientInfo"):
			self.loadPartientList()
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_PartientInfomation)
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin b\u1ec7nh nh\u00e2n", None))
		elif(page == "Setting"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Setting)
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"C\u00e0i \u0110\u1eb7t", None))
		elif(page == "Introduction"):
			self.uic.stackedWidget.setCurrentWidget(self.uic.page_Introduction)
			self.uic.label_Page.setText(QCoreApplication.translate("MainWindow", u"", None))

	def lowerlimb(self):
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

	def lineChart(self):
		self.x = [0 for i in range(10)]
		self.y = [0 for i in range(10)]
		linechart = pg.plot()
		linechart.showGrid(x = True, y = True)
		linechart.addLegend()
		# set properties of the label for y axis
		linechart.setLabel('left', 'Vertical Values', units ='y')
		# set properties of the label for x axis
		linechart.setLabel('bottom', 'Horizontal Values', units ='s')
		# setting horizontal range
		linechart.setXRange(0, 10)
		pen = pg.mkPen(color=(39, 164, 242), width=5)
		self.line1 = linechart.plot(self.x, self.y, pen =pen)
		self.line1.setSymbol('o')
		linechart.setBackground('w')
		layoutMain_linechart = QHBoxLayout()		
		self.uic.widget_MLinechart.setLayout(layoutMain_linechart)		
		layoutMain_linechart.addWidget(linechart)	

	def update_plot_data(self):
		
		if not (self.q1.empty() or self.q2.empty()):
			self.x = self.x[1:]  # Remove the first y element.
			self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

			data1 = self.q1.get()
			data2 = self.q2.get()
			data = float(data1.split(',')[2]) - float(data2.split(',')[2])
			self.y = self.y[1:]  # Remove the first
			self.y.append(data)  # Add a new random value.

			self.line1.setData(self.x, self.y)  # Update the data.

	def onPartientAddClinked(self):
		if self.dlg_PartientInfo == None:
			self.dlg_PartientInfo = PartientInfo_Dlg(self)
		if self.dlg_PartientInfo.isVisible():
			self.dlg_PartientInfo.close()
		else:
			self.dlg_PartientInfo.show()

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
	
	def onPartientListClinked(self):
		if self.dlg_PartientList == None:
			self.dlg_PartientList = PartientList_Dlg(self)
		if self.dlg_PartientList.isVisible():
			self.dlg_PartientList.close()
		else:
			self.dlg_PartientList.updateTable()
			self.dlg_PartientList.show()

	def handle_data(self, data):
		data_list = {}
		with open('sample.json', 'r') as f:
			data_list = json.load(f)
			data_list[self.numOfPartient] = data	
			self.numOfPartient += 1		
			f.close()
		
		with open('sample.json','w') as f:			
			json.dump(data_list, f, indent= 4)
			f.close()

	def loadPartientList(self):
		file_data = {}
		with open('sample.json','r') as file:
			file_data = json.load(file)
			file.close()
		self.uic.tableWidget_PartientInfoPartientTable.setRowCount(len(file_data))
		for index_person in range(len(file_data)):
			self.uic.tableWidget_PartientInfoPartientTable.setItem(index_person,0, QTableWidgetItem(str(index_person)))
			self.uic.tableWidget_PartientInfoPartientTable.setItem(index_person,1, QTableWidgetItem('Quang Suy'))
			self.uic.tableWidget_PartientInfoPartientTable.setItem(index_person,2, QTableWidgetItem(file_data[str(index_person)]['name']))
			self.uic.tableWidget_PartientInfoPartientTable.setItem(index_person,3, QTableWidgetItem(file_data[str(index_person)]['DateOfBirth']))
			self.uic.tableWidget_PartientInfoPartientTable.setItem(index_person,4, QTableWidgetItem(file_data[str(index_person)]['ID']))
			self.uic.tableWidget_PartientInfoPartientTable.setItem(index_person,5, QTableWidgetItem(file_data[str(index_person)]['Sex']))
		
		self.uic.tableWidget_PartientInfoPartientTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
# -------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec())