# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1489, 759)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_topMenu = QFrame(self.centralwidget)
        self.fr_topMenu.setObjectName(u"fr_topMenu")
        self.fr_topMenu.setMaximumSize(QSize(16777215, 40))
        self.fr_topMenu.setStyleSheet(u"background-color: #dfe3e6;")
        self.fr_topMenu.setFrameShape(QFrame.StyledPanel)
        self.fr_topMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_topMenu)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_Menu = QPushButton(self.fr_topMenu)
        self.bt_Menu.setObjectName(u"bt_Menu")
        self.bt_Menu.setMinimumSize(QSize(200, 35))
        self.bt_Menu.setMaximumSize(QSize(200, 35))
        self.bt_Menu.setStyleSheet(u"QPushButton{\n"
"background-color:#dfe3e6;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #b3b3b3;\n"
"font: 87 12pt \"Arial Black\";\n"
"}")
        icon = QIcon()
        icon.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/barra-de-menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Menu.setIcon(icon)
        self.bt_Menu.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bt_Menu)

        self.label_Page = QLabel(self.fr_topMenu)
        self.label_Page.setObjectName(u"label_Page")

        self.horizontalLayout_2.addWidget(self.label_Page)

        self.horizontalSpacer = QSpacerItem(481, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_mini = QPushButton(self.fr_topMenu)
        self.bt_mini.setObjectName(u"bt_mini")
        self.bt_mini.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #0008ff;\n"
"background-color:white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_mini.setIcon(icon1)
        self.bt_mini.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_mini)

        self.bt_smallSize = QPushButton(self.fr_topMenu)
        self.bt_smallSize.setObjectName(u"bt_smallSize")
        self.bt_smallSize.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #0008ff;\n"
"background-color:white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_smallSize.setIcon(icon2)
        self.bt_smallSize.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_smallSize)

        self.bt_expand = QPushButton(self.fr_topMenu)
        self.bt_expand.setObjectName(u"bt_expand")
        self.bt_expand.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #0008ff;\n"
"background-color:white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_expand.setIcon(icon3)
        self.bt_expand.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_expand)

        self.bt_close = QPushButton(self.fr_topMenu)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #0008ff;\n"
"background-color:white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close.setIcon(icon4)
        self.bt_close.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_close)


        self.verticalLayout.addWidget(self.fr_topMenu)

        self.fr_bottom = QFrame(self.centralwidget)
        self.fr_bottom.setObjectName(u"fr_bottom")
        self.fr_bottom.setFrameShape(QFrame.StyledPanel)
        self.fr_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_bottom)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_sideMenu = QFrame(self.fr_bottom)
        self.fr_sideMenu.setObjectName(u"fr_sideMenu")
        self.fr_sideMenu.setMinimumSize(QSize(200, 0))
        self.fr_sideMenu.setMaximumSize(QSize(0, 16777215))
        self.fr_sideMenu.setStyleSheet(u"QFrame{\n"
"	background-color:#93d0ed;\n"
"}\n"
"QPushButton{\n"
"background-color: #93d0ed;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font:75 12pt \"Droid Sans\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font:75 12pt \"Droid Sans\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #bcbec2;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font:75 12pt \"Droid Sans\";\n"
"}")
        self.fr_sideMenu.setFrameShape(QFrame.StyledPanel)
        self.fr_sideMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_sideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_Main = QPushButton(self.fr_sideMenu)
        self.pb_Main.setObjectName(u"pb_Main")
        self.pb_Main.setMinimumSize(QSize(0, 40))
        self.pb_Main.setMaximumSize(QSize(16777215, 40))
        icon5 = QIcon()
        icon5.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/inteligencia-artificial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Main.setIcon(icon5)
        self.pb_Main.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pb_Main)

        self.pb_Calibration = QPushButton(self.fr_sideMenu)
        self.pb_Calibration.setObjectName(u"pb_Calibration")
        self.pb_Calibration.setMinimumSize(QSize(0, 40))
        self.pb_Calibration.setMaximumSize(QSize(16777215, 40))
        icon6 = QIcon()
        icon6.addFile(u"icon/calib.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Calibration.setIcon(icon6)
        self.pb_Calibration.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pb_Calibration)

        self.pb_Review = QPushButton(self.fr_sideMenu)
        self.pb_Review.setObjectName(u"pb_Review")
        self.pb_Review.setMinimumSize(QSize(0, 40))
        self.pb_Review.setMaximumSize(QSize(16777215, 40))
        icon7 = QIcon()
        icon7.addFile(u"icon/review.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Review.setIcon(icon7)
        self.pb_Review.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pb_Review)

        self.pb_Patient = QPushButton(self.fr_sideMenu)
        self.pb_Patient.setObjectName(u"pb_Patient")
        self.pb_Patient.setMinimumSize(QSize(0, 40))
        self.pb_Patient.setMaximumSize(QSize(16777215, 40))
        icon8 = QIcon()
        icon8.addFile(u"icon/partient_info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Patient.setIcon(icon8)
        self.pb_Patient.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pb_Patient)

        self.pb_Setting = QPushButton(self.fr_sideMenu)
        self.pb_Setting.setObjectName(u"pb_Setting")
        self.pb_Setting.setMinimumSize(QSize(0, 40))
        self.pb_Setting.setMaximumSize(QSize(16777215, 40))
        icon9 = QIcon()
        icon9.addFile(u"icon/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Setting.setIcon(icon9)
        self.pb_Setting.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pb_Setting)

        self.verticalSpacer = QSpacerItem(20, 285, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_Introduction = QPushButton(self.fr_sideMenu)
        self.pb_Introduction.setObjectName(u"pb_Introduction")
        self.pb_Introduction.setMinimumSize(QSize(0, 40))
        self.pb_Introduction.setMaximumSize(QSize(40, 40))
        self.pb_Introduction.setStyleSheet(u"border-radius: 20px;")
        icon10 = QIcon()
        icon10.addFile(u"icon/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Introduction.setIcon(icon10)
        self.pb_Introduction.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pb_Introduction)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addWidget(self.fr_sideMenu)

        self.fr_Main = QFrame(self.fr_bottom)
        self.fr_Main.setObjectName(u"fr_Main")
        self.fr_Main.setStyleSheet(u"background-color: white;")
        self.fr_Main.setFrameShape(QFrame.StyledPanel)
        self.fr_Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_Main)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.fr_Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_Main = QWidget()
        self.page_Main.setObjectName(u"page_Main")
        self.widget = QWidget(self.page_Main)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 251, 151))
        self.widget.setStyleSheet(u"font:75 12pt \"Droid Sans\";")
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pb_Connector = QPushButton(self.widget)
        self.pb_Connector.setObjectName(u"pb_Connector")
        self.pb_Connector.setMinimumSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.pb_Connector)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_imu1 = QLabel(self.widget)
        self.label_imu1.setObjectName(u"label_imu1")

        self.horizontalLayout_5.addWidget(self.label_imu1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMaximumSize(QSize(20, 16777215))
        icon11 = QIcon()
        icon11.addFile(u"../1.tutorial/icon/accept.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon11)
        self.pushButton.setIconSize(QSize(12, 12))
        self.pushButton.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_imu1_2 = QLabel(self.widget)
        self.label_imu1_2.setObjectName(u"label_imu1_2")

        self.horizontalLayout_6.addWidget(self.label_imu1_2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(20, 16777215))
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QSize(12, 12))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_imu1_3 = QLabel(self.widget)
        self.label_imu1_3.setObjectName(u"label_imu1_3")

        self.horizontalLayout_7.addWidget(self.label_imu1_3)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(20, 16777215))
        self.pushButton_3.setIcon(icon11)
        self.pushButton_3.setIconSize(QSize(12, 12))
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pushButton_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_imu1_4 = QLabel(self.widget)
        self.label_imu1_4.setObjectName(u"label_imu1_4")

        self.horizontalLayout_8.addWidget(self.label_imu1_4)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(20, 16777215))
        self.pushButton_4.setIcon(icon11)
        self.pushButton_4.setIconSize(QSize(12, 12))
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_8.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.frame = QFrame(self.page_Main)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 150, 470, 570))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.tableWidget)

        self.widget_2 = QWidget(self.page_Main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(250, 0, 211, 151))
        self.widget_2.setStyleSheet(u"font:75 12pt \"Droid Sans\";")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_7.addWidget(self.pushButton_6)

        self.widget_3 = QWidget(self.page_Main)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(460, 0, 311, 721))
        self.widget_3.setStyleSheet(u"QLabel{\n"
"font:75 10pt \"Droid Sans\";\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font:75 12pt \"Droid Sans\";\n"
"}\n"
"")
        self.layoutWidget = QWidget(self.widget_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 291, 22))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.layoutWidget_2 = QWidget(self.widget_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 90, 291, 22))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_13.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.layoutWidget_6 = QWidget(self.widget_3)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 120, 291, 22))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.layoutWidget_6)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_23.addWidget(self.label_34)

        self.label_35 = QLabel(self.layoutWidget_6)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_23.addWidget(self.label_35)

        self.layoutWidget_7 = QWidget(self.widget_3)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 150, 291, 25))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.layoutWidget_7)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_24.addWidget(self.label_36)

        self.comboBox = QComboBox(self.layoutWidget_7)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_24.addWidget(self.comboBox)

        self.layoutWidget_8 = QWidget(self.widget_3)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 180, 291, 22))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.layoutWidget_8)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_25.addWidget(self.label_37)

        self.label_38 = QLabel(self.layoutWidget_8)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_25.addWidget(self.label_38)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 650, 121, 31))
        self.label.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.layoutWidget_15 = QWidget(self.widget_3)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(10, 210, 291, 22))
        self.horizontalLayout_32 = QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_2)

        self.label_56 = QLabel(self.layoutWidget_15)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font:75 12pt \"Droid Sans\";")

        self.horizontalLayout_32.addWidget(self.label_56)

        self.pushButton_13 = QPushButton(self.widget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(10, 290, 301, 41))
        self.pushButton_14 = QPushButton(self.widget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(10, 340, 301, 41))
        self.pushButton_15 = QPushButton(self.widget_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(10, 390, 301, 41))
        self.frame_3 = QFrame(self.widget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 460, 311, 171))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_55 = QLabel(self.frame_3)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_33.addWidget(self.label_55)

        self.label_57 = QLabel(self.frame_3)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_33.addWidget(self.label_57)


        self.verticalLayout_8.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_58 = QLabel(self.frame_3)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_34.addWidget(self.label_58)

        self.label_59 = QLabel(self.frame_3)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_34.addWidget(self.label_59)


        self.verticalLayout_8.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_60 = QLabel(self.frame_3)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_35.addWidget(self.label_60)

        self.label_61 = QLabel(self.frame_3)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_35.addWidget(self.label_61)


        self.verticalLayout_8.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_62 = QLabel(self.frame_3)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_36.addWidget(self.label_62)

        self.label_63 = QLabel(self.frame_3)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_36.addWidget(self.label_63)


        self.verticalLayout_8.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_64 = QLabel(self.frame_3)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_37.addWidget(self.label_64)

        self.label_65 = QLabel(self.frame_3)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_37.addWidget(self.label_65)


        self.verticalLayout_8.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_66 = QLabel(self.frame_3)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_38.addWidget(self.label_66)

        self.label_67 = QLabel(self.frame_3)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_38.addWidget(self.label_67)


        self.verticalLayout_8.addLayout(self.horizontalLayout_38)

        self.widget1 = QWidget(self.widget_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 30, 291, 21))
        self.horizontalLayout_11 = QHBoxLayout(self.widget1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.label_9 = QLabel(self.widget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.widget_7 = QWidget(self.page_Main)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(770, 0, 500, 300))
        self.widget_8 = QWidget(self.page_Main)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(770, 300, 500, 420))
        self.stackedWidget.addWidget(self.page_Main)
        self.page_Introduction = QWidget()
        self.page_Introduction.setObjectName(u"page_Introduction")
        self.label_3 = QLabel(self.page_Introduction)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 130, 221, 111))
        self.label_3.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.label_157 = QLabel(self.page_Introduction)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(500, 200, 431, 191))
        self.label_157.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.stackedWidget.addWidget(self.page_Introduction)
        self.page_Setting = QWidget()
        self.page_Setting.setObjectName(u"page_Setting")
        self.label_6 = QLabel(self.page_Setting)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 330, 221, 111))
        self.label_6.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.frame_4 = QFrame(self.page_Setting)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(390, 130, 441, 331))
        self.frame_4.setStyleSheet(u"font:75 12pt \"Droid Sans\";")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget_22 = QWidget(self.frame_4)
        self.layoutWidget_22.setObjectName(u"layoutWidget_22")
        self.layoutWidget_22.setGeometry(QRect(70, 100, 311, 41))
        self.horizontalLayout_40 = QHBoxLayout(self.layoutWidget_22)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.layoutWidget_22)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(150, 39))
        self.label_69.setMaximumSize(QSize(150, 39))

        self.horizontalLayout_40.addWidget(self.label_69)

        self.radioButton = QRadioButton(self.layoutWidget_22)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget_22)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_40.addWidget(self.radioButton_2)

        self.layoutWidget_23 = QWidget(self.frame_4)
        self.layoutWidget_23.setObjectName(u"layoutWidget_23")
        self.layoutWidget_23.setGeometry(QRect(70, 150, 311, 41))
        self.horizontalLayout_41 = QHBoxLayout(self.layoutWidget_23)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.layoutWidget_23)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(150, 39))
        self.label_70.setMaximumSize(QSize(150, 39))

        self.horizontalLayout_41.addWidget(self.label_70)

        self.radioButton_3 = QRadioButton(self.layoutWidget_23)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.layoutWidget_23)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_41.addWidget(self.radioButton_4)

        self.pushButton_16 = QPushButton(self.frame_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(190, 210, 181, 71))
        self.widget2 = QWidget(self.frame_4)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(70, 50, 311, 41))
        self.horizontalLayout_39 = QHBoxLayout(self.widget2)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.widget2)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(150, 0))
        self.label_68.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_39.addWidget(self.label_68)

        self.comboBox_3 = QComboBox(self.widget2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_39.addWidget(self.comboBox_3)

        self.stackedWidget.addWidget(self.page_Setting)
        self.page_PartientInfomation = QWidget()
        self.page_PartientInfomation.setObjectName(u"page_PartientInfomation")
        self.label_4 = QLabel(self.page_PartientInfomation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 0, 131, 41))
        self.label_4.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.frame_9 = QFrame(self.page_PartientInfomation)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(50, 70, 351, 331))
        self.frame_9.setStyleSheet(u"font:75 12pt \"Droid Sans\";")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_138 = QLabel(self.frame_9)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_63.addWidget(self.label_138)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_63.addWidget(self.lineEdit)


        self.verticalLayout_12.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_151 = QLabel(self.frame_9)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_72.addWidget(self.label_151)

        self.dateEdit = QDateEdit(self.frame_9)
        self.dateEdit.setObjectName(u"dateEdit")

        self.horizontalLayout_72.addWidget(self.dateEdit)


        self.verticalLayout_12.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_140 = QLabel(self.frame_9)
        self.label_140.setObjectName(u"label_140")

        self.horizontalLayout_65.addWidget(self.label_140)

        self.comboBox_5 = QComboBox(self.frame_9)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.horizontalLayout_65.addWidget(self.comboBox_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_143 = QLabel(self.frame_9)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_67.addWidget(self.label_143)

        self.lineEdit_3 = QLineEdit(self.frame_9)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_67.addWidget(self.lineEdit_3)

        self.label_144 = QLabel(self.frame_9)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_67.addWidget(self.label_144)


        self.verticalLayout_12.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_141 = QLabel(self.frame_9)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_66.addWidget(self.label_141)

        self.lineEdit_2 = QLineEdit(self.frame_9)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_66.addWidget(self.lineEdit_2)

        self.label_142 = QLabel(self.frame_9)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_66.addWidget(self.label_142)


        self.verticalLayout_12.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_153 = QLabel(self.frame_9)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_74.addWidget(self.label_153)

        self.label_154 = QLabel(self.frame_9)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_74.addWidget(self.label_154)


        self.verticalLayout_12.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_152 = QLabel(self.frame_9)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_73.addWidget(self.label_152)

        self.comboBox_7 = QComboBox(self.frame_9)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_73.addWidget(self.comboBox_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_155 = QLabel(self.frame_9)
        self.label_155.setObjectName(u"label_155")

        self.horizontalLayout_75.addWidget(self.label_155)

        self.label_156 = QLabel(self.frame_9)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_75.addWidget(self.label_156)


        self.verticalLayout_12.addLayout(self.horizontalLayout_75)

        self.frame_10 = QFrame(self.page_PartientInfomation)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(50, 420, 341, 121))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.pushButton_35 = QPushButton(self.frame_10)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.horizontalLayout_76.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.frame_10)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.horizontalLayout_76.addWidget(self.pushButton_36)

        self.pushButton_37 = QPushButton(self.page_PartientInfomation)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(120, 610, 191, 51))
        self.frame_11 = QFrame(self.page_PartientInfomation)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(480, 10, 771, 701))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.tableWidget_3 = QTableWidget(self.frame_11)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 60, 751, 631))
        self.widget3 = QWidget(self.frame_11)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 10, 751, 42))
        self.horizontalLayout_77 = QHBoxLayout(self.widget3)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.widget3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_77.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.widget3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_77.addWidget(self.lineEdit_8)

        self.pushButton_38 = QPushButton(self.widget3)
        self.pushButton_38.setObjectName(u"pushButton_38")
        icon12 = QIcon()
        icon12.addFile(u"../1.tutorial/icon/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_38.setIcon(icon12)
        self.pushButton_38.setIconSize(QSize(32, 32))

        self.horizontalLayout_77.addWidget(self.pushButton_38)

        self.stackedWidget.addWidget(self.page_PartientInfomation)
        self.page_Review = QWidget()
        self.page_Review.setObjectName(u"page_Review")
        self.frame_5 = QFrame(self.page_Review)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 150, 470, 570))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = QTableWidget(self.frame_5)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEnabled(True)

        self.horizontalLayout_42.addWidget(self.tableWidget_2)

        self.widget_9 = QWidget(self.page_Review)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(470, 0, 311, 721))
        self.widget_9.setStyleSheet(u"QLabel{\n"
"font:75 10pt \"Droid Sans\";\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font:75 12pt \"Droid Sans\";\n"
"}\n"
"")
        self.layoutWidget_24 = QWidget(self.widget_9)
        self.layoutWidget_24.setObjectName(u"layoutWidget_24")
        self.layoutWidget_24.setGeometry(QRect(10, 100, 291, 22))
        self.horizontalLayout_43 = QHBoxLayout(self.layoutWidget_24)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.layoutWidget_24)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_43.addWidget(self.label_71)

        self.label_72 = QLabel(self.layoutWidget_24)
        self.label_72.setObjectName(u"label_72")

        self.horizontalLayout_43.addWidget(self.label_72)

        self.label_73 = QLabel(self.layoutWidget_24)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_43.addWidget(self.label_73)

        self.label_74 = QLabel(self.layoutWidget_24)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_43.addWidget(self.label_74)

        self.layoutWidget_25 = QWidget(self.widget_9)
        self.layoutWidget_25.setObjectName(u"layoutWidget_25")
        self.layoutWidget_25.setGeometry(QRect(10, 130, 291, 22))
        self.horizontalLayout_44 = QHBoxLayout(self.layoutWidget_25)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.layoutWidget_25)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_44.addWidget(self.label_75)

        self.label_76 = QLabel(self.layoutWidget_25)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_44.addWidget(self.label_76)

        self.label_77 = QLabel(self.layoutWidget_25)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_44.addWidget(self.label_77)

        self.label_78 = QLabel(self.layoutWidget_25)
        self.label_78.setObjectName(u"label_78")

        self.horizontalLayout_44.addWidget(self.label_78)

        self.layoutWidget_26 = QWidget(self.widget_9)
        self.layoutWidget_26.setObjectName(u"layoutWidget_26")
        self.layoutWidget_26.setGeometry(QRect(10, 160, 291, 22))
        self.horizontalLayout_45 = QHBoxLayout(self.layoutWidget_26)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_79 = QLabel(self.layoutWidget_26)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_45.addWidget(self.label_79)

        self.label_80 = QLabel(self.layoutWidget_26)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_45.addWidget(self.label_80)

        self.layoutWidget_27 = QWidget(self.widget_9)
        self.layoutWidget_27.setObjectName(u"layoutWidget_27")
        self.layoutWidget_27.setGeometry(QRect(10, 190, 291, 25))
        self.horizontalLayout_46 = QHBoxLayout(self.layoutWidget_27)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_81 = QLabel(self.layoutWidget_27)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_46.addWidget(self.label_81)

        self.comboBox_4 = QComboBox(self.layoutWidget_27)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_46.addWidget(self.comboBox_4)

        self.layoutWidget_28 = QWidget(self.widget_9)
        self.layoutWidget_28.setObjectName(u"layoutWidget_28")
        self.layoutWidget_28.setGeometry(QRect(10, 220, 291, 22))
        self.horizontalLayout_47 = QHBoxLayout(self.layoutWidget_28)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.layoutWidget_28)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_47.addWidget(self.label_82)

        self.label_83 = QLabel(self.layoutWidget_28)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_47.addWidget(self.label_83)

        self.layoutWidget_29 = QWidget(self.widget_9)
        self.layoutWidget_29.setObjectName(u"layoutWidget_29")
        self.layoutWidget_29.setGeometry(QRect(10, 250, 291, 22))
        self.horizontalLayout_48 = QHBoxLayout(self.layoutWidget_29)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_3)

        self.label_85 = QLabel(self.layoutWidget_29)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"font:75 12pt \"Droid Sans\";")

        self.horizontalLayout_48.addWidget(self.label_85)

        self.pushButton_19 = QPushButton(self.widget_9)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(10, 300, 301, 41))
        self.frame_6 = QFrame(self.widget_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 460, 311, 171))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_86 = QLabel(self.frame_6)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_49.addWidget(self.label_86)


        self.verticalLayout_9.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_88 = QLabel(self.frame_6)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_50.addWidget(self.label_88)


        self.verticalLayout_9.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_90 = QLabel(self.frame_6)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_51.addWidget(self.label_90)


        self.verticalLayout_9.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_92 = QLabel(self.frame_6)
        self.label_92.setObjectName(u"label_92")

        self.horizontalLayout_52.addWidget(self.label_92)


        self.verticalLayout_9.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_94 = QLabel(self.frame_6)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_53.addWidget(self.label_94)


        self.verticalLayout_9.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_96 = QLabel(self.frame_6)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_54.addWidget(self.label_96)


        self.verticalLayout_9.addLayout(self.horizontalLayout_54)

        self.layoutWidget_30 = QWidget(self.widget_9)
        self.layoutWidget_30.setObjectName(u"layoutWidget_30")
        self.layoutWidget_30.setGeometry(QRect(10, 70, 291, 21))
        self.horizontalLayout_55 = QHBoxLayout(self.layoutWidget_30)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.layoutWidget_30)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_55.addWidget(self.label_98)

        self.label_99 = QLabel(self.layoutWidget_30)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_55.addWidget(self.label_99)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 650, 131, 41))
        self.label_5.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.layoutWidget_31 = QWidget(self.widget_9)
        self.layoutWidget_31.setObjectName(u"layoutWidget_31")
        self.layoutWidget_31.setGeometry(QRect(10, 40, 292, 29))
        self.horizontalLayout_56 = QHBoxLayout(self.layoutWidget_31)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.layoutWidget_31)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_56.addWidget(self.label_100)

        self.pushButton_20 = QPushButton(self.layoutWidget_31)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_56.addWidget(self.pushButton_20)

        self.layoutWidget_32 = QWidget(self.widget_9)
        self.layoutWidget_32.setObjectName(u"layoutWidget_32")
        self.layoutWidget_32.setGeometry(QRect(10, 370, 291, 24))
        self.horizontalLayout_57 = QHBoxLayout(self.layoutWidget_32)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.layoutWidget_32)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_57.addWidget(self.label_84)

        self.horizontalSlider = QSlider(self.layoutWidget_32)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_57.addWidget(self.horizontalSlider)

        self.layoutWidget_33 = QWidget(self.widget_9)
        self.layoutWidget_33.setObjectName(u"layoutWidget_33")
        self.layoutWidget_33.setGeometry(QRect(10, 400, 291, 24))
        self.horizontalLayout_58 = QHBoxLayout(self.layoutWidget_33)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_101 = QLabel(self.layoutWidget_33)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_58.addWidget(self.label_101)

        self.horizontalSlider_2 = QSlider(self.layoutWidget_33)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_58.addWidget(self.horizontalSlider_2)

        self.widget_10 = QWidget(self.page_Review)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(780, 300, 500, 420))
        self.widget_11 = QWidget(self.page_Review)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(780, 0, 500, 300))
        self.stackedWidget.addWidget(self.page_Review)
        self.page_Calib = QWidget()
        self.page_Calib.setObjectName(u"page_Calib")
        self.label_2 = QLabel(self.page_Calib)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 50, 111, 51))
        self.label_2.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.frame_7 = QFrame(self.page_Calib)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(330, 20, 591, 171))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_87 = QLabel(self.frame_7)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_59.addWidget(self.label_87)

        self.label_89 = QLabel(self.frame_7)
        self.label_89.setObjectName(u"label_89")

        self.horizontalLayout_59.addWidget(self.label_89)

        self.label_91 = QLabel(self.frame_7)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(10, 30))

        self.horizontalLayout_59.addWidget(self.label_91)

        self.pushButton_17 = QPushButton(self.frame_7)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setMaximumSize(QSize(20, 16777215))
        self.pushButton_17.setIcon(icon11)
        self.pushButton_17.setIconSize(QSize(12, 12))
        self.pushButton_17.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pushButton_17)

        self.label_93 = QLabel(self.frame_7)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_59.addWidget(self.label_93)

        self.label_95 = QLabel(self.frame_7)
        self.label_95.setObjectName(u"label_95")

        self.horizontalLayout_59.addWidget(self.label_95)

        self.pushButton_18 = QPushButton(self.frame_7)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setEnabled(True)
        self.pushButton_18.setMaximumSize(QSize(20, 16777215))
        self.pushButton_18.setIcon(icon11)
        self.pushButton_18.setIconSize(QSize(12, 12))
        self.pushButton_18.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pushButton_18)

        self.label_102 = QLabel(self.frame_7)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_59.addWidget(self.label_102)

        self.label_103 = QLabel(self.frame_7)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_59.addWidget(self.label_103)

        self.pushButton_22 = QPushButton(self.frame_7)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setEnabled(True)
        self.pushButton_22.setMaximumSize(QSize(20, 16777215))
        self.pushButton_22.setIcon(icon11)
        self.pushButton_22.setIconSize(QSize(12, 12))
        self.pushButton_22.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pushButton_22)

        self.label_97 = QLabel(self.frame_7)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_59.addWidget(self.label_97)

        self.label_104 = QLabel(self.frame_7)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_59.addWidget(self.label_104)

        self.pushButton_21 = QPushButton(self.frame_7)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setEnabled(True)
        self.pushButton_21.setMaximumSize(QSize(20, 16777215))
        self.pushButton_21.setIcon(icon11)
        self.pushButton_21.setIconSize(QSize(12, 12))
        self.pushButton_21.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pushButton_21)


        self.verticalLayout_10.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_105 = QLabel(self.frame_7)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_60.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_7)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_60.addWidget(self.label_106)

        self.label_107 = QLabel(self.frame_7)
        self.label_107.setObjectName(u"label_107")

        self.horizontalLayout_60.addWidget(self.label_107)

        self.pushButton_23 = QPushButton(self.frame_7)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setEnabled(True)
        self.pushButton_23.setMaximumSize(QSize(20, 16777215))
        self.pushButton_23.setIcon(icon11)
        self.pushButton_23.setIconSize(QSize(12, 12))
        self.pushButton_23.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pushButton_23)

        self.label_108 = QLabel(self.frame_7)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_60.addWidget(self.label_108)

        self.label_109 = QLabel(self.frame_7)
        self.label_109.setObjectName(u"label_109")

        self.horizontalLayout_60.addWidget(self.label_109)

        self.pushButton_24 = QPushButton(self.frame_7)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setEnabled(True)
        self.pushButton_24.setMaximumSize(QSize(20, 16777215))
        self.pushButton_24.setIcon(icon11)
        self.pushButton_24.setIconSize(QSize(12, 12))
        self.pushButton_24.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pushButton_24)

        self.label_110 = QLabel(self.frame_7)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_60.addWidget(self.label_110)

        self.label_111 = QLabel(self.frame_7)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_60.addWidget(self.label_111)

        self.pushButton_25 = QPushButton(self.frame_7)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setEnabled(True)
        self.pushButton_25.setMaximumSize(QSize(20, 16777215))
        self.pushButton_25.setIcon(icon11)
        self.pushButton_25.setIconSize(QSize(12, 12))
        self.pushButton_25.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pushButton_25)

        self.label_112 = QLabel(self.frame_7)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_60.addWidget(self.label_112)

        self.label_113 = QLabel(self.frame_7)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_60.addWidget(self.label_113)

        self.pushButton_26 = QPushButton(self.frame_7)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setEnabled(True)
        self.pushButton_26.setMaximumSize(QSize(20, 16777215))
        self.pushButton_26.setIcon(icon11)
        self.pushButton_26.setIconSize(QSize(12, 12))
        self.pushButton_26.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pushButton_26)


        self.verticalLayout_10.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_114 = QLabel(self.frame_7)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_61.addWidget(self.label_114)

        self.label_115 = QLabel(self.frame_7)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_61.addWidget(self.label_115)

        self.label_116 = QLabel(self.frame_7)
        self.label_116.setObjectName(u"label_116")

        self.horizontalLayout_61.addWidget(self.label_116)

        self.pushButton_27 = QPushButton(self.frame_7)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setEnabled(True)
        self.pushButton_27.setMaximumSize(QSize(20, 16777215))
        self.pushButton_27.setIcon(icon11)
        self.pushButton_27.setIconSize(QSize(12, 12))
        self.pushButton_27.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pushButton_27)

        self.label_117 = QLabel(self.frame_7)
        self.label_117.setObjectName(u"label_117")

        self.horizontalLayout_61.addWidget(self.label_117)

        self.label_118 = QLabel(self.frame_7)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_61.addWidget(self.label_118)

        self.pushButton_28 = QPushButton(self.frame_7)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setEnabled(True)
        self.pushButton_28.setMaximumSize(QSize(20, 16777215))
        self.pushButton_28.setIcon(icon11)
        self.pushButton_28.setIconSize(QSize(12, 12))
        self.pushButton_28.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pushButton_28)

        self.label_119 = QLabel(self.frame_7)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_61.addWidget(self.label_119)

        self.label_120 = QLabel(self.frame_7)
        self.label_120.setObjectName(u"label_120")

        self.horizontalLayout_61.addWidget(self.label_120)

        self.pushButton_29 = QPushButton(self.frame_7)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setEnabled(True)
        self.pushButton_29.setMaximumSize(QSize(20, 16777215))
        self.pushButton_29.setIcon(icon11)
        self.pushButton_29.setIconSize(QSize(12, 12))
        self.pushButton_29.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pushButton_29)

        self.label_121 = QLabel(self.frame_7)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_61.addWidget(self.label_121)

        self.label_122 = QLabel(self.frame_7)
        self.label_122.setObjectName(u"label_122")

        self.horizontalLayout_61.addWidget(self.label_122)

        self.pushButton_30 = QPushButton(self.frame_7)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setEnabled(True)
        self.pushButton_30.setMaximumSize(QSize(20, 16777215))
        self.pushButton_30.setIcon(icon11)
        self.pushButton_30.setIconSize(QSize(12, 12))
        self.pushButton_30.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pushButton_30)


        self.verticalLayout_10.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_123 = QLabel(self.frame_7)
        self.label_123.setObjectName(u"label_123")

        self.horizontalLayout_62.addWidget(self.label_123)

        self.label_124 = QLabel(self.frame_7)
        self.label_124.setObjectName(u"label_124")

        self.horizontalLayout_62.addWidget(self.label_124)

        self.label_125 = QLabel(self.frame_7)
        self.label_125.setObjectName(u"label_125")

        self.horizontalLayout_62.addWidget(self.label_125)

        self.pushButton_31 = QPushButton(self.frame_7)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setEnabled(True)
        self.pushButton_31.setMaximumSize(QSize(20, 16777215))
        self.pushButton_31.setIcon(icon11)
        self.pushButton_31.setIconSize(QSize(12, 12))
        self.pushButton_31.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pushButton_31)

        self.label_126 = QLabel(self.frame_7)
        self.label_126.setObjectName(u"label_126")

        self.horizontalLayout_62.addWidget(self.label_126)

        self.label_127 = QLabel(self.frame_7)
        self.label_127.setObjectName(u"label_127")

        self.horizontalLayout_62.addWidget(self.label_127)

        self.pushButton_32 = QPushButton(self.frame_7)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setEnabled(True)
        self.pushButton_32.setMaximumSize(QSize(20, 16777215))
        self.pushButton_32.setIcon(icon11)
        self.pushButton_32.setIconSize(QSize(12, 12))
        self.pushButton_32.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pushButton_32)

        self.label_128 = QLabel(self.frame_7)
        self.label_128.setObjectName(u"label_128")

        self.horizontalLayout_62.addWidget(self.label_128)

        self.label_129 = QLabel(self.frame_7)
        self.label_129.setObjectName(u"label_129")

        self.horizontalLayout_62.addWidget(self.label_129)

        self.pushButton_33 = QPushButton(self.frame_7)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setEnabled(True)
        self.pushButton_33.setMaximumSize(QSize(20, 16777215))
        self.pushButton_33.setIcon(icon11)
        self.pushButton_33.setIconSize(QSize(12, 12))
        self.pushButton_33.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pushButton_33)

        self.label_130 = QLabel(self.frame_7)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_62.addWidget(self.label_130)

        self.label_131 = QLabel(self.frame_7)
        self.label_131.setObjectName(u"label_131")

        self.horizontalLayout_62.addWidget(self.label_131)

        self.pushButton_34 = QPushButton(self.frame_7)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setEnabled(True)
        self.pushButton_34.setMaximumSize(QSize(20, 16777215))
        self.pushButton_34.setIcon(icon11)
        self.pushButton_34.setIconSize(QSize(12, 12))
        self.pushButton_34.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pushButton_34)


        self.verticalLayout_10.addLayout(self.horizontalLayout_62)

        self.frame_8 = QFrame(self.page_Calib)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(90, 200, 831, 121))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_132 = QLabel(self.frame_8)
        self.label_132.setObjectName(u"label_132")

        self.verticalLayout_11.addWidget(self.label_132)

        self.label_133 = QLabel(self.frame_8)
        self.label_133.setObjectName(u"label_133")

        self.verticalLayout_11.addWidget(self.label_133)

        self.label_134 = QLabel(self.frame_8)
        self.label_134.setObjectName(u"label_134")

        self.verticalLayout_11.addWidget(self.label_134)

        self.label_135 = QLabel(self.frame_8)
        self.label_135.setObjectName(u"label_135")

        self.verticalLayout_11.addWidget(self.label_135)

        self.label_136 = QLabel(self.page_Calib)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(50, 360, 551, 301))
        self.label_136.setPixmap(QPixmap(u"../1.tutorial/icon/calib acc.svg"))
        self.label_137 = QLabel(self.page_Calib)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(710, 380, 481, 231))
        self.label_137.setPixmap(QPixmap(u"../1.tutorial/icon/calib mag.png"))
        self.label_137.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_Calib)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.fr_Main)


        self.verticalLayout.addWidget(self.fr_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_Menu.setText(QCoreApplication.translate("MainWindow", u"    Menu", None))
        self.label_Page.setText(QCoreApplication.translate("MainWindow", u"Trang Ch\u1ee7", None))
        self.bt_mini.setText("")
        self.bt_smallSize.setText("")
        self.bt_expand.setText("")
        self.bt_close.setText("")
        self.pb_Main.setText(QCoreApplication.translate("MainWindow", u"    Trang Ch\u1ee7", None))
        self.pb_Calibration.setText(QCoreApplication.translate("MainWindow", u"   Hi\u1ec7u Ch\u1ec9nh", None))
        self.pb_Review.setText(QCoreApplication.translate("MainWindow", u"     Xem L\u1ea1i", None))
        self.pb_Patient.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin b\u1ec7nh nh\u00e2n", None))
        self.pb_Setting.setText(QCoreApplication.translate("MainWindow", u"       C\u00e0i \u0110\u1eb7t", None))
        self.pb_Introduction.setText("")
        self.pb_Connector.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft N\u1ed1i", None))
        self.label_imu1.setText(QCoreApplication.translate("MainWindow", u"IMU1: ", None))
        self.pushButton.setText("")
        self.label_imu1_2.setText(QCoreApplication.translate("MainWindow", u"IMU2: ", None))
        self.pushButton_2.setText("")
        self.label_imu1_3.setText(QCoreApplication.translate("MainWindow", u"IMU3: ", None))
        self.pushButton_3.setText("")
        self.label_imu1_4.setText(QCoreApplication.translate("MainWindow", u"IMU4: ", None))
        self.pushButton_4.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Hip", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Knee", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ankle", None));
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch b\u1ec7nh nh\u00e2n", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam b\u1ec7nh nh\u00e2n m\u1edbi", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nam", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y Sinh:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"01/01/1111", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"100kg", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"120cm", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"quang.khuat", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"B\u00e0i ki\u1ec3m tra:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0110i \u0103n", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0110i ng\u1ee7", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Th\u00eam m\u1edbi", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111o:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"12:12-31/02/2031", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MAIN WIDGET", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"00:00.0000ms", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u \u0111o", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft th\u00fac \u0111o", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u k\u1ebft qu\u1ea3", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Max Hip angle", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Max last Hip angle", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"100.77", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"100.66", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Max Knee angle", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Max last Knee angle", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"359.99", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"111.11", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Max Ankle angle", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Max last Ankle angle", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"423.123", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"123.123", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Intro WIDGET", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 t\u00e0i tr\u1ee3 s\u1eaft: Only C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Setting WIDGET", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb \u0111\u1ed9 d\u00e0i:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"inch", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb kh\u1ed1i l\u01b0\u1ee3ng:", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"lb", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1eb7t l\u1ea1i h\u1ec7 th\u1ed1ng", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Ng\u00f4n ng\u1eef", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Ti\u1ebfng Vi\u1ec7t", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Partient WIDGET", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Quang Khu\u1ea5t", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh:", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Nam", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"N\u1eef", None))

        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"120", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng:", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"120", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n:", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Quang.khuat", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"B\u00e0i ki\u1ec3m tra:", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0110i \u0103n", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0110i ng\u1ee7", None))

        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111o:", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"12:12-31/02/2031", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a to\u00e0n b\u1ed9 danh s\u00e1ch", None))
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh", None));
        self.pushButton_38.setText("")
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Hip", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Knee", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Ankle", None));
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Nam", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y Sinh:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"01/01/1111", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"100kg", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"120cm", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"quang.khuat", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"B\u00e0i ki\u1ec3m tra:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0110i \u0103n", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0110i ng\u1ee7", None))

        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111o:", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"12:12-31/02/2031", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"00:00.0000ms", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ea1y/T\u1ea1m D\u1eebng", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Max Hip angle", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"100.77", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Max Knee angle", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"359.99", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Max Ankle angle", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"423.123", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Review WIDGET", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin b\u1ec7nh nh\u00e2n:", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch b\u1ec7nh nh\u00e2n", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"T\u1ed1c \u0111\u1ed9:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Calib WIDGET", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"IMU1:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_17.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_18.setText("")
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_22.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_21.setText("")
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"IMU2:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_23.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_24.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_25.setText("")
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_26.setText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"IMU3:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_27.setText("")
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_28.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_29.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_30.setText("")
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"IMU4:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_31.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_32.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_33.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_34.setText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh t\u1eeb k\u1ebf(mag): Gi\u1eef c\u1ea3m bi\u1ebfn song song v\u1edbi m\u1eb7t \u0111\u1ea5t v\u00e0 di chuy\u1ec3n theo h\u00ecnh s\u1ed1 8", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh gia t\u1ed1c k\u1ebf(gyro): \u0110\u1eb7t c\u1ea3m bi\u1ebfn \u1edf 6 v\u1ecb tr\u00ed \u1ed5n \u0111\u1ecbnh v\u00e0i gi\u00e2y m\u1ed7i v\u1ecb tr\u00ed", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh con quay h\u1ed3i chuy\u1ec3n(acc): \u0110\u1eb7t c\u1ea3m bi\u1ebfn \u1edf b\u1ea5t k\u00ec v\u1ecb tr\u00ed \u1ed5n \u0111\u1ecbnh n\u00e0o trong v\u00e0i gi\u00e2y", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh h\u1ec7 th\u1ed1ng(sys): S\u1ebd t\u1ef1 \u0111\u1ed9ng \u0111i\u1ec1u ch\u1ec9nh theo 3 th\u00f4ng s\u1ed1 tr\u00ean. Trong tr\u01b0\u1eddng h\u1ee3p c\u00f3 v\u1ea5n \u0111\u1ec1 kh\u00f4ng t\u1ef1 hi\u1ec7u ch\u1ec9nh th\u00ec kh\u1edfi \u0111\u1ed9ng l\u1ea1i thi\u1ebft b\u1ecb", None))
        self.label_136.setText("")
        self.label_137.setText("")
    # retranslateUi

