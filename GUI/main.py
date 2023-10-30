import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation
from PyQt6 import uic
from PySide6.QtCore import Qt
from ui_menu import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.uic.fr_sideMenu.setLineWidth(200)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.uic.fr_topMenu.mouseMoveEvent = self.mover 

        self.uic.pb_Main.clicked.connect(lambda: self.uic.stackedWidget.setCurrentWidget(self.uic.page_Main))
        self.uic.pb_Calibration.clicked.connect(lambda: self.uic.stackedWidget.setCurrentWidget(self.uic.page_Calib))
        self.uic.pb_Introduction.clicked.connect(lambda: self.uic.stackedWidget.setCurrentWidget(self.uic.page_Introduction))
        self.uic.pb_Patient.clicked.connect(lambda: self.uic.stackedWidget.setCurrentWidget(self.uic.page_PartientInfomation))
        self.uic.pb_Review.clicked.connect(lambda: self.uic.stackedWidget.setCurrentWidget(self.uic.page_Review))
        self.uic.pb_Setting.clicked.connect(lambda: self.uic.stackedWidget.setCurrentWidget(self.uic.page_Setting))

        self.uic.bt_close.clicked.connect(self.control_bt_close)
        self.uic.bt_expand.clicked.connect(self.control_bt_expand)
        self.uic.bt_mini.clicked.connect(self.control_bt_mini)
        self.uic.bt_smallSize.clicked.connect(self.control_bt_smallSize)

        self.uic.bt_smallSize.hide()

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
       

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())