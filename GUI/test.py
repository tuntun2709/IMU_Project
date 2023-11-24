from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt

class SliderExample(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a vertical layout for the main window
        layout = QVBoxLayout()

        # Create a horizontal slider
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)  # Set the initial value

        # Connect the valueChanged signal to a custom slot
        slider.valueChanged.connect(self.on_slider_value_changed)

        # Create a label to display the slider value
        self.label = QLabel('Slider Value: {}'.format(slider.value()))

        # Add the slider and label to the layout
        layout.addWidget(slider)
        layout.addWidget(self.label)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set the properties of the main window
        self.setWindowTitle('PySide6 Slider Example')
        self.setGeometry(300, 300, 300, 150)

    def on_slider_value_changed(self, value):
        # Update the label text when the slider value changes
        self.label.setText('Slider Value: {}'.format(value))


if __name__ == '__main__':
    app = QApplication([])
    window = SliderExample()
    window.show()
    app.exec_()
