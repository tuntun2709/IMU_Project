from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QPixmap, QPainter, QTransform
import PySide6
import sys

class RotatedImageLabel(QLabel):
    def __init__(self, image_path):
        super().__init__()
        self.pixmap = QPixmap(image_path)
        
        self.transform = QTransform()
        self.transform.rotate(80)
        self.pixmap = self.pixmap.transformed(self.transform)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

def changeAngle():
    rotated_label.transform.rotate(0)

app = QApplication(sys.argv)

main_window = QMainWindow()
main_window.setMinimumSize(500,500)
central_widget = QWidget()
layout = QVBoxLayout(central_widget)

submit_button = QPushButton()
submit_button.setObjectName(u"submit_button")

# Create a QLabel with a rotated image
rotated_label = RotatedImageLabel("2.png")
layout.addWidget(rotated_label)
layout.addWidget(submit_button)
submit_button.setObjectName(u"submit_button")
submit_button.clicked.connect(changeAngle)
main_window.setCentralWidget(central_widget)
main_window.show()

sys.exit(app.exec())
