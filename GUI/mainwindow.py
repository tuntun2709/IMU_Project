# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QGraphicsView,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 672)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"")
        MainWindow.setIconSize(QSize(16, 16))
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.roll_label = QLabel(self.centralwidget)
        self.roll_label.setObjectName(u"roll_label")

        self.horizontalLayout.addWidget(self.roll_label)

        self.roll_lineEdit = QLineEdit(self.centralwidget)
        self.roll_lineEdit.setObjectName(u"roll_lineEdit")
        self.roll_lineEdit.setMinimumSize(QSize(133, 0))

        self.horizontalLayout.addWidget(self.roll_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pitch_label = QLabel(self.centralwidget)
        self.pitch_label.setObjectName(u"pitch_label")

        self.horizontalLayout_2.addWidget(self.pitch_label)

        self.pitch_lineEdit = QLineEdit(self.centralwidget)
        self.pitch_lineEdit.setObjectName(u"pitch_lineEdit")

        self.horizontalLayout_2.addWidget(self.pitch_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.yaw_label = QLabel(self.centralwidget)
        self.yaw_label.setObjectName(u"yaw_label")

        self.horizontalLayout_4.addWidget(self.yaw_label)

        self.yaw_lineEdit = QLineEdit(self.centralwidget)
        self.yaw_lineEdit.setObjectName(u"yaw_lineEdit")

        self.horizontalLayout_4.addWidget(self.yaw_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setCheckable(False)

        self.verticalLayout.addWidget(self.submit_button)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.table_data = QTableWidget(self.centralwidget)
        if (self.table_data.columnCount() < 3):
            self.table_data.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setMinimumSize(QSize(500, 500))
        self.table_data.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_data.setAutoScroll(True)
        self.table_data.setAutoScrollMargin(17)
        self.table_data.setDragDropOverwriteMode(False)
        self.table_data.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_data.setRowCount(0)
        self.table_data.horizontalHeader().setProperty("showSortIndicator", True)

        self.horizontalLayout_3.addWidget(self.table_data)

        self.lineChartWidget = QWidget(self.centralwidget)
        self.lineChartWidget.setObjectName(u"lineChartWidget")
        self.lineChartWidget.setMinimumSize(QSize(500, 500))
        self.leg_test = QLabel(self.lineChartWidget)
        self.leg_test.setObjectName(u"leg_test")
        self.leg_test.setGeometry(QRect(160, 130, 91, 31))
        self.leg_test.setPixmap(QPixmap(u"leg.png"))
        self.test_rotate = QGraphicsView(self.lineChartWidget)
        self.test_rotate.setObjectName(u"test_rotate")
        self.test_rotate.setGeometry(QRect(90, 190, 256, 192))

        self.horizontalLayout_3.addWidget(self.lineChartWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.roll_label.setText(QCoreApplication.translate("MainWindow", u"Roll: ", None))
        self.pitch_label.setText(QCoreApplication.translate("MainWindow", u"Pitch: ", None))
        self.yaw_label.setText(QCoreApplication.translate("MainWindow", u"Yaw: ", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        ___qtablewidgetitem = self.table_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Roll", None));
        ___qtablewidgetitem1 = self.table_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pitch", None));
        ___qtablewidgetitem2 = self.table_data.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Yaw", None));
        self.leg_test.setText("")
    # retranslateUi