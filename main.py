import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QPushButton
import pyqtgraph as pg
import math
loader = QUiLoader()
rowCount = 0
app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
#-------------------------------------------------------------------------------
# function
def do_something():
    global rowCount    
    window.table_data.setRowCount(rowCount)
    window.table_data.insertRow(0)
    window.table_data.setItem(0, 0, QtWidgets.QTableWidgetItem(window.roll_lineEdit.text()))
    window.table_data.setItem(0, 1, QtWidgets.QTableWidgetItem(window.pitch_lineEdit.text()))
    window.table_data.setItem(0, 2, QtWidgets.QTableWidgetItem(window.yaw_lineEdit.text()))
    rowCount += 1   
    

def pushButton():
    window.setWindowTitle("Nothing")
# -------------------------------------------------------------------
# -----------------------------------------------------------
# setup ui in started
window.setWindowTitle("IMU-FMA")
window.table_data.setColumnWidth(0,150)
window.table_data.setColumnWidth(1,150)
window.table_data.setColumnWidth(2,150)
window.submit_button.clicked.connect(do_something)


window.graphWidget = pg.PlotWidget(window.lineChartWidget)
hour = [1,2,3,4,5,6,7,8,9,10]
temperature = [30,32,34,32,33,31,29,32,35,45]
window.graphWidget.setGeometry(QtCore.QRect(0, 0, 500, 300))
window.graphWidget.setBackground('w')
pen = pg.mkPen(color=(39, 164, 242), width=5)
window.graphWidget.plot(hour, temperature, pen= pen)
window.graphWidget.resize(500,255)

hour1 = [1,2,3,4]
temperature1 = [30,32,34,32]
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
window.graphWidget2 = pg.PlotWidget(window.lineChartWidget)
window.graphWidget2.setGeometry(QtCore.QRect(0, 260, 500, 300))
window.graphWidget2.setBackground('w')

pen1 = pg.mkPen(color=(39, 164, 242), width=30)
pen2 = pg.mkPen(color=(62, 174, 244), width=25)
pen3 = pg.mkPen(color=(110, 194, 247), width=20)
pen4 = pg.mkPen(color=(159, 215, 248), width=15)
window.graphWidget2.setXRange(-100, 1500, padding=0)
window.graphWidget2.setYRange(-1500, 100, padding=0)

window.graphWidget2.plot([x3,x4], [y3,y4], pen= pen4, symbol = 'o')
window.graphWidget2.plot([x2,x3], [y2,y3], pen= pen3, symbol = 'o')
window.graphWidget2.plot([x1,x2], [y1,y2], pen= pen2, symbol = 'o')
window.graphWidget2.plot([x0,x1], [y0,y1], pen= pen1, symbol = 'o')
window.graphWidget2.resize(500,500)

#---------------------------------------------------------------


window.show()

app.exec()
