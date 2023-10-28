import sys
from PySide6 import QtWidgets
from PyQt6 import uic
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QPushButton
import pyqtgraph as pg
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsTextItem, QGraphicsPixmapItem


rowCount = 0



class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.screen = QGraphicsScene()
        self.uic.test_rotate.setScene(self.screen)
        self.text_item = QGraphicsTextItem("-----------------")
        self.text_item.setRotation(45)  # Set the rotation angle (in degrees)

        self.angle = 0
        self.uic.submit_button.clicked.connect(self.changeAngle)
        # Add the QGraphicsTextItem to the scene
        self.screen.addItem(self.text_item)
        # self.uic.test_rotate.setScreen(self.screen)

    def changeAngle(self):
        self.angle += 10
        # self.text_item.setPos(12,1)
        self.text_item.setRotation(self.angle)


        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())