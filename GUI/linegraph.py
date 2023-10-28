# from PySide6.QtWidgets import QApplication, QMainWindow
# import pyqtgraph as pg
# import sys


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()

#         self.graphWidget = pg.PlotWidget()
#         self.setCentralWidget(self.graphWidget)

#         hour = [1,2,3,4,5,6,7,8,9,10,11]
#         temperature_1 = [30,32,34,32,33,31,29,32,35,45,22]
#         temperature_2 = [50,35,44,22,38,32,27,38,32,44,45]

#         #Add Background colour to white
#         self.graphWidget.setBackground('w')
#         # Add Title
#         self.graphWidget.setTitle("Your Title Here", color="b", size="20pt")
#         # Add Axis Labels
#         styles = {"color": "#f00", "font-size": "20px"}
#         self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
#         self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
#         #Add legend
#         self.graphWidget.addLegend()
#         #Add grid
#         self.graphWidget.showGrid(x=True, y=True)
#         #Set Range
#         self.graphWidget.setXRange(2, 10, padding=0)
#         self.graphWidget.setYRange(20, 55, padding=0)

#         self.plot(hour, temperature_1, "Sensor1", 'r')
#         self.plot(hour, temperature_2, "Sensor2", 'b')

#     def plot(self, x, y, plotname, color):
#         pen = pg.mkPen(color=color)
#         self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=20, symbolBrush=(color))


# app = QApplication(sys.argv)
# main = MainWindow()
# main.show()
# app.exec()


# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the linechart example from Qt v5.x"""

import sys
from PySide6.QtCore import QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QLineSeries


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.series = QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(QPointF(11, 1))
        self.series.append(QPointF(13, 3))
        self.series.append(QPointF(17, 6))
        self.series.append(QPointF(18, 3))
        self.series.append(QPointF(20, 2))
        self.series.append(QPointF(21, 6))
        self.series.append(QPointF(22, 3))
        self.series.append(QPointF(23, 2))
        

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(440, 300)
    sys.exit(app.exec())