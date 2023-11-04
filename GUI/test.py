import sys
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLineEdit, QLabel, QWidget

class MyDialog(QDialog):
    data_signal = Signal(str)  # Custom signal to pass data
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog")
        layout = QVBoxLayout()

        self.label = QLabel("Enter data:")
        self.input_field = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)

        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def submit(self):
        data = self.input_field.text()
        self.data_signal.emit(data)
        self.accept()  # Close the dialog

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.button = QPushButton("Open Dialog")
        self.button.clicked.connect(self.open_dialog)
        self.label = QLabel("Data from Dialog: ")

        self.dialog = MyDialog()
        self.dialog.data_signal.connect(self.handle_data)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_dialog(self):
        self.dialog.exec()

    def handle_data(self, data):
        self.label.setText(f"Data from Dialog: {data}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())
