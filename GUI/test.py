# importing Qt widgets
from PySide6.QtWidgets import * 
import sys

# importing pyqtgraph as pg
import pyqtgraph as pg
from PySide6.QtGui import *
from testui import Ui_MainWindow



class Window(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		


		# calling method
		self.UiComponents()


	# method for components
	def UiComponents(self):

		
		# creating a new label
		label = QLabel("GeeksforGeeks Line Plot")

		# making it multiline
		label.setWordWrap(True)

		# y values to plot by line 1
		y = [2, 8, 6, 8, 6, 11, 14, 13, 18, 19]

		# y values to plot by line 2
		y2 = [3, 1, 5, 8, 9, 11, 16, 17, 14, 16]
		x = range(0, 10)

		# create plot window object
		plt = pg.plot()

		# showing x and y grids
		plt.showGrid(x = True, y = True)

		# adding legend
		plt.addLegend()

		# set properties of the label for y axis
		plt.setLabel('left', 'Vertical Values', units ='y')

		# set properties of the label for x axis
		plt.setLabel('bottom', 'Horizontal Values', units ='s')

		# setting horizontal range
		plt.setXRange(0, 10)

		# setting vertical range
		plt.setYRange(0, 20)

		# plotting line in green color
		# with dot symbol as x, not a mandatory field
		line1 = plt.plot(x, y, pen ='g', symbol ='x', symbolPen ='g', symbolBrush = 0.2, name ='green')

		# plotting line2 with blue color
		# with dot symbol as o
		line2 = plt.plot(x, y2, pen ='b', symbol ='o', symbolPen ='b', symbolBrush = 0.2, name ='blue')

		# setting symbol of the line 1
		line1.setSymbol('o')

		# label minimum width
		label.setMinimumWidth(120)

		# Creating a grid layout
		layout = QHBoxLayout()

		# setting this layout to the widget
		self.ui.widget.setLayout(layout)

		# adding label to the layout
		layout.addWidget(label)

		# plot window goes on right side, spanning 3 rows
		layout.addWidget(plt)
		print(type(plt))
		print(type(layout))

		





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Window()
    main_win.show()
    sys.exit(app.exec())