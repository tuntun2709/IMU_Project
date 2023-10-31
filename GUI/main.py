import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation,Qt, QCoreApplication
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from ui_menu import Ui_MainWindow
import pyqtgraph as pg
import math

# -------------------------------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_Main)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.uic.fr_sideMenu.setLineWidth(200)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.uic.fr_topMenu.mouseMoveEvent = self.mover 

        self.uic.pb_Main.clicked.connect(lambda: self.changePage("Main"))
        self.uic.pb_Calibration.clicked.connect(lambda: self.changePage("Calib"))
        self.uic.pb_Introduction.clicked.connect(lambda: self.changePage("Introduction"))
        self.uic.pb_Patient.clicked.connect(lambda: self.changePage("PartientInfo"))
        self.uic.pb_Review.clicked.connect(lambda: self.changePage("Review"))
        self.uic.pb_Setting.clicked.connect(lambda: self.changePage("Setting"))

        self.uic.bt_close.clicked.connect(self.control_bt_close)
        self.uic.bt_expand.clicked.connect(self.control_bt_expand)
        self.uic.bt_mini.clicked.connect(self.control_bt_mini)
        self.uic.bt_smallSize.clicked.connect(self.control_bt_smallSize)

        self.uic.bt_smallSize.hide()

        self.uic.bt_Menu.clicked.connect(self.control_menu)

        self.lowerlimb()
        self.lineChart()

        

# --------------------------------------------------------------------------
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

    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
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
        lowerlimbChart.plot([x2,x3], [y2,y3], pen= pen4, symbol = 'o')
        lowerlimbChart.plot([x1,x2], [y1,y2], pen= pen4, symbol = 'o')
        lowerlimbChart.plot([x0,x1], [y0,y1], pen= pen4, symbol = 'o')
        layout_lowerlimb = QHBoxLayout()
        self.uic.widget_MLowerlimb.setLayout(layout_lowerlimb)
        layout_lowerlimb.addWidget(lowerlimbChart)

    def lineChart(self):
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
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
        line1 = linechart.plot(hour, temperature, pen =pen)
        line1.setSymbol('o')
        layout_linechart = QHBoxLayout()
        self.uic.widget_MLinechart.setLayout(layout_linechart)
        layout_linechart.addWidget(linechart)
# -------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())