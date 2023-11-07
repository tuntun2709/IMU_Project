# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1475, 845)
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
        icon.addFile(u"icon/barra-de-menus.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"icon/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon2.addFile(u"icon/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"icon/max.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u"icon/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon5.addFile(u"icon/inteligencia-artificial.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon8.addFile(u"icon/patient_info.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.pb_Setting.setFlat(False)

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
        self.widget.setGeometry(QRect(0, 0, 251, 141))
        self.widget.setStyleSheet(u"font:75 12pt \"Droid Sans\";\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pb_MainConnector = QPushButton(self.widget)
        self.pb_MainConnector.setObjectName(u"pb_MainConnector")
        self.pb_MainConnector.setMinimumSize(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.pb_MainConnector)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_MainImu1 = QLabel(self.widget)
        self.label_MainImu1.setObjectName(u"label_MainImu1")

        self.horizontalLayout_5.addWidget(self.label_MainImu1)

        self.pb_MainCheckImu1 = QPushButton(self.widget)
        self.pb_MainCheckImu1.setObjectName(u"pb_MainCheckImu1")
        self.pb_MainCheckImu1.setEnabled(True)
        self.pb_MainCheckImu1.setMaximumSize(QSize(20, 16777215))
        icon11 = QIcon()
        icon11.addFile(u"icon/accept.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_MainCheckImu1.setIcon(icon11)
        self.pb_MainCheckImu1.setIconSize(QSize(12, 12))
        self.pb_MainCheckImu1.setCheckable(False)
        self.pb_MainCheckImu1.setAutoDefault(False)
        self.pb_MainCheckImu1.setFlat(True)

        self.horizontalLayout_5.addWidget(self.pb_MainCheckImu1)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_MainImu2 = QLabel(self.widget)
        self.label_MainImu2.setObjectName(u"label_MainImu2")

        self.horizontalLayout_6.addWidget(self.label_MainImu2)

        self.pb_MainCheckImu2 = QPushButton(self.widget)
        self.pb_MainCheckImu2.setObjectName(u"pb_MainCheckImu2")
        self.pb_MainCheckImu2.setMaximumSize(QSize(20, 16777215))
        self.pb_MainCheckImu2.setIcon(icon11)
        self.pb_MainCheckImu2.setIconSize(QSize(12, 12))
        self.pb_MainCheckImu2.setFlat(True)

        self.horizontalLayout_6.addWidget(self.pb_MainCheckImu2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_MainImu3 = QLabel(self.widget)
        self.label_MainImu3.setObjectName(u"label_MainImu3")

        self.horizontalLayout_7.addWidget(self.label_MainImu3)

        self.pb_MainCheckImu3 = QPushButton(self.widget)
        self.pb_MainCheckImu3.setObjectName(u"pb_MainCheckImu3")
        self.pb_MainCheckImu3.setMaximumSize(QSize(20, 16777215))
        self.pb_MainCheckImu3.setIcon(icon11)
        self.pb_MainCheckImu3.setIconSize(QSize(12, 12))
        self.pb_MainCheckImu3.setFlat(True)

        self.horizontalLayout_7.addWidget(self.pb_MainCheckImu3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_MainImu4 = QLabel(self.widget)
        self.label_MainImu4.setObjectName(u"label_MainImu4")

        self.horizontalLayout_8.addWidget(self.label_MainImu4)

        self.pb_MainCheckImu4 = QPushButton(self.widget)
        self.pb_MainCheckImu4.setObjectName(u"pb_MainCheckImu4")
        self.pb_MainCheckImu4.setMaximumSize(QSize(20, 16777215))
        self.pb_MainCheckImu4.setIcon(icon11)
        self.pb_MainCheckImu4.setIconSize(QSize(12, 12))
        self.pb_MainCheckImu4.setFlat(True)

        self.horizontalLayout_8.addWidget(self.pb_MainCheckImu4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        self.frame = QFrame(self.page_Main)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 150, 461, 651))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.tableWidget_MDataTable = QTableWidget(self.frame)
        if (self.tableWidget_MDataTable.columnCount() < 3):
            self.tableWidget_MDataTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_MDataTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_MDataTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_MDataTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_MDataTable.setObjectName(u"tableWidget_MDataTable")
        self.tableWidget_MDataTable.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.tableWidget_MDataTable)

        self.widget_2 = QWidget(self.page_Main)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(250, 0, 211, 141))
        self.widget_2.setStyleSheet(u"font:75 12pt \"Droid Sans\";")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pb_MainPatientsList = QPushButton(self.widget_2)
        self.pb_MainPatientsList.setObjectName(u"pb_MainPatientsList")

        self.verticalLayout_7.addWidget(self.pb_MainPatientsList)

        self.pb_MainAddPatient = QPushButton(self.widget_2)
        self.pb_MainAddPatient.setObjectName(u"pb_MainAddPatient")

        self.verticalLayout_7.addWidget(self.pb_MainAddPatient)

        self.widget_3 = QWidget(self.page_Main)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(460, 0, 311, 801))
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
        self.layoutWidget.setGeometry(QRect(10, 90, 291, 22))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.lb_MainPatientGender = QLabel(self.layoutWidget)
        self.lb_MainPatientGender.setObjectName(u"lb_MainPatientGender")

        self.horizontalLayout_12.addWidget(self.lb_MainPatientGender)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lb_MainDateOfBirth = QLabel(self.layoutWidget)
        self.lb_MainDateOfBirth.setObjectName(u"lb_MainDateOfBirth")

        self.horizontalLayout_12.addWidget(self.lb_MainDateOfBirth)

        self.layoutWidget_2 = QWidget(self.widget_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 120, 291, 22))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_13.addWidget(self.label_14)

        self.lb_MainPatientWeight = QLabel(self.layoutWidget_2)
        self.lb_MainPatientWeight.setObjectName(u"lb_MainPatientWeight")

        self.horizontalLayout_13.addWidget(self.lb_MainPatientWeight)

        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.lb_MainPatientHeight = QLabel(self.layoutWidget_2)
        self.lb_MainPatientHeight.setObjectName(u"lb_MainPatientHeight")

        self.horizontalLayout_13.addWidget(self.lb_MainPatientHeight)

        self.layoutWidget_6 = QWidget(self.widget_3)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 150, 291, 22))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.layoutWidget_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_23.addWidget(self.label_34)

        self.lb_MainPatientCode = QLabel(self.layoutWidget_6)
        self.lb_MainPatientCode.setObjectName(u"lb_MainPatientCode")

        self.horizontalLayout_23.addWidget(self.lb_MainPatientCode)

        self.layoutWidget_7 = QWidget(self.widget_3)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 180, 291, 25))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.layoutWidget_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.label_36)

        self.cb_MainExcercise = QComboBox(self.layoutWidget_7)
        self.cb_MainExcercise.setObjectName(u"cb_MainExcercise")

        self.horizontalLayout_24.addWidget(self.cb_MainExcercise)

        self.layoutWidget_8 = QWidget(self.widget_3)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 210, 291, 22))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.layoutWidget_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_25.addWidget(self.label_37)

        self.lb_MainDayExercise = QLabel(self.layoutWidget_8)
        self.lb_MainDayExercise.setObjectName(u"lb_MainDayExercise")

        self.horizontalLayout_25.addWidget(self.lb_MainDayExercise)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 650, 121, 31))
        self.label.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.layoutWidget_15 = QWidget(self.widget_3)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(10, 240, 291, 22))
        self.horizontalLayout_32 = QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_2)

        self.lb_MainTimer = QLabel(self.layoutWidget_15)
        self.lb_MainTimer.setObjectName(u"lb_MainTimer")
        self.lb_MainTimer.setStyleSheet(u"font:75 12pt \"Droid Sans\";")

        self.horizontalLayout_32.addWidget(self.lb_MainTimer)

        self.pb_MainStartExercise = QPushButton(self.widget_3)
        self.pb_MainStartExercise.setObjectName(u"pb_MainStartExercise")
        self.pb_MainStartExercise.setGeometry(QRect(20, 290, 281, 41))
        self.pb_MainEndExercise = QPushButton(self.widget_3)
        self.pb_MainEndExercise.setObjectName(u"pb_MainEndExercise")
        self.pb_MainEndExercise.setGeometry(QRect(20, 340, 281, 41))
        self.pb_MainSaveData = QPushButton(self.widget_3)
        self.pb_MainSaveData.setObjectName(u"pb_MainSaveData")
        self.pb_MainSaveData.setGeometry(QRect(20, 390, 281, 41))
        self.frame_3 = QFrame(self.widget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 460, 311, 171))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
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
        self.lb_MainMaxHipAngle = QLabel(self.frame_3)
        self.lb_MainMaxHipAngle.setObjectName(u"lb_MainMaxHipAngle")

        self.horizontalLayout_34.addWidget(self.lb_MainMaxHipAngle)

        self.lb_MainMaxLastHipAngle = QLabel(self.frame_3)
        self.lb_MainMaxLastHipAngle.setObjectName(u"lb_MainMaxLastHipAngle")

        self.horizontalLayout_34.addWidget(self.lb_MainMaxLastHipAngle)


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
        self.lb_MainMaxKneeAngle = QLabel(self.frame_3)
        self.lb_MainMaxKneeAngle.setObjectName(u"lb_MainMaxKneeAngle")

        self.horizontalLayout_36.addWidget(self.lb_MainMaxKneeAngle)

        self.lb_MainMaxLastKneeAngle = QLabel(self.frame_3)
        self.lb_MainMaxLastKneeAngle.setObjectName(u"lb_MainMaxLastKneeAngle")

        self.horizontalLayout_36.addWidget(self.lb_MainMaxLastKneeAngle)


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
        self.lb_MainMaxAnkleAngle = QLabel(self.frame_3)
        self.lb_MainMaxAnkleAngle.setObjectName(u"lb_MainMaxAnkleAngle")

        self.horizontalLayout_38.addWidget(self.lb_MainMaxAnkleAngle)

        self.lb_MainMaxLastAnkleAngle = QLabel(self.frame_3)
        self.lb_MainMaxLastAnkleAngle.setObjectName(u"lb_MainMaxLastAnkleAngle")

        self.horizontalLayout_38.addWidget(self.lb_MainMaxLastAnkleAngle)


        self.verticalLayout_8.addLayout(self.horizontalLayout_38)

        self.layoutWidget_3 = QWidget(self.widget_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 30, 291, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_17.addWidget(self.label_20)

        self.lb_MainPatientName = QLabel(self.layoutWidget_3)
        self.lb_MainPatientName.setObjectName(u"lb_MainPatientName")

        self.horizontalLayout_17.addWidget(self.lb_MainPatientName)

        self.layoutWidget1 = QWidget(self.widget_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 60, 291, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_16.addWidget(self.label_18)

        self.lb_MainPatientID = QLabel(self.layoutWidget1)
        self.lb_MainPatientID.setObjectName(u"lb_MainPatientID")

        self.horizontalLayout_16.addWidget(self.lb_MainPatientID)

        self.widget_MLinechart = QWidget(self.page_Main)
        self.widget_MLinechart.setObjectName(u"widget_MLinechart")
        self.widget_MLinechart.setGeometry(QRect(770, 0, 500, 300))
        self.widget_MLowerlimb = QWidget(self.page_Main)
        self.widget_MLowerlimb.setObjectName(u"widget_MLowerlimb")
        self.widget_MLowerlimb.setGeometry(QRect(770, 300, 500, 500))
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

        self.rb_SettingCm = QRadioButton(self.layoutWidget_22)
        self.rb_SettingCm.setObjectName(u"rb_SettingCm")
        self.rb_SettingCm.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.rb_SettingCm)

        self.rb_SettingInch = QRadioButton(self.layoutWidget_22)
        self.rb_SettingInch.setObjectName(u"rb_SettingInch")

        self.horizontalLayout_40.addWidget(self.rb_SettingInch)

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

        self.rb_SettingKg = QRadioButton(self.layoutWidget_23)
        self.rb_SettingKg.setObjectName(u"rb_SettingKg")
        self.rb_SettingKg.setMinimumSize(QSize(20, 20))

        self.horizontalLayout_41.addWidget(self.rb_SettingKg)

        self.rb_SettingLb = QRadioButton(self.layoutWidget_23)
        self.rb_SettingLb.setObjectName(u"rb_SettingLb")

        self.horizontalLayout_41.addWidget(self.rb_SettingLb)

        self.pb_SettingResetSystem = QPushButton(self.frame_4)
        self.pb_SettingResetSystem.setObjectName(u"pb_SettingResetSystem")
        self.pb_SettingResetSystem.setGeometry(QRect(20, 210, 401, 121))
        self.layoutWidget2 = QWidget(self.frame_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(70, 50, 311, 41))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.cb_SettingLanguage = QComboBox(self.layoutWidget2)
        self.cb_SettingLanguage.addItem("")
        self.cb_SettingLanguage.addItem("")
        self.cb_SettingLanguage.setObjectName(u"cb_SettingLanguage")

        self.horizontalLayout_11.addWidget(self.cb_SettingLanguage)

        self.stackedWidget.addWidget(self.page_Setting)
        self.page_PatientInfomation = QWidget()
        self.page_PatientInfomation.setObjectName(u"page_PatientInfomation")
        self.label_4 = QLabel(self.page_PatientInfomation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 0, 131, 41))
        self.label_4.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.frame_9 = QFrame(self.page_PatientInfomation)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(40, 60, 401, 461))
        self.frame_9.setStyleSheet(u"font:75 12pt \"Droid Sans\";")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(5, -1, 5, -1)
        self.label_138 = QLabel(self.frame_9)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(110, 0))
        self.label_138.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_63.addWidget(self.label_138)

        self.le_PatientInfoName = QLineEdit(self.frame_9)
        self.le_PatientInfoName.setObjectName(u"le_PatientInfoName")

        self.horizontalLayout_63.addWidget(self.le_PatientInfoName)


        self.verticalLayout_12.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(5, -1, 5, -1)
        self.label_139 = QLabel(self.frame_9)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(110, 0))
        self.label_139.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_64.addWidget(self.label_139)

        self.le_PatientInfoID = QLineEdit(self.frame_9)
        self.le_PatientInfoID.setObjectName(u"le_PatientInfoID")

        self.horizontalLayout_64.addWidget(self.le_PatientInfoID)


        self.verticalLayout_12.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(5, -1, 5, -1)
        self.label_151 = QLabel(self.frame_9)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setMinimumSize(QSize(110, 0))
        self.label_151.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_72.addWidget(self.label_151)

        self.de_PatientInfoDateOfBirth = QDateEdit(self.frame_9)
        self.de_PatientInfoDateOfBirth.setObjectName(u"de_PatientInfoDateOfBirth")

        self.horizontalLayout_72.addWidget(self.de_PatientInfoDateOfBirth)


        self.verticalLayout_12.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(5, -1, 5, -1)
        self.label_140 = QLabel(self.frame_9)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(0, 0))
        self.label_140.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_65.addWidget(self.label_140)

        self.cb_PatientInfoGender = QComboBox(self.frame_9)
        self.cb_PatientInfoGender.addItem("")
        self.cb_PatientInfoGender.addItem("")
        self.cb_PatientInfoGender.setObjectName(u"cb_PatientInfoGender")

        self.horizontalLayout_65.addWidget(self.cb_PatientInfoGender)


        self.verticalLayout_12.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(5, -1, 5, -1)
        self.label_143 = QLabel(self.frame_9)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_67.addWidget(self.label_143)

        self.le_PatientInfoHeight = QLineEdit(self.frame_9)
        self.le_PatientInfoHeight.setObjectName(u"le_PatientInfoHeight")

        self.horizontalLayout_67.addWidget(self.le_PatientInfoHeight)

        self.label_144 = QLabel(self.frame_9)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_67.addWidget(self.label_144)


        self.verticalLayout_12.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(5, -1, 5, -1)
        self.label_141 = QLabel(self.frame_9)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_66.addWidget(self.label_141)

        self.le_PatientInfoWeight = QLineEdit(self.frame_9)
        self.le_PatientInfoWeight.setObjectName(u"le_PatientInfoWeight")

        self.horizontalLayout_66.addWidget(self.le_PatientInfoWeight)

        self.label_142 = QLabel(self.frame_9)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_66.addWidget(self.label_142)


        self.verticalLayout_12.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_153 = QLabel(self.frame_9)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_74.addWidget(self.label_153)

        self.lb_PatientInfoPatitentCode = QLabel(self.frame_9)
        self.lb_PatientInfoPatitentCode.setObjectName(u"lb_PatientInfoPatitentCode")

        self.horizontalLayout_74.addWidget(self.lb_PatientInfoPatitentCode)


        self.verticalLayout_12.addLayout(self.horizontalLayout_74)

        self.frame_10 = QFrame(self.page_PatientInfomation)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(50, 590, 341, 121))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.pb_PatientInfoSavePatient = QPushButton(self.frame_10)
        self.pb_PatientInfoSavePatient.setObjectName(u"pb_PatientInfoSavePatient")

        self.horizontalLayout_76.addWidget(self.pb_PatientInfoSavePatient)

        self.pb_PatientInfoRemovePatient = QPushButton(self.frame_10)
        self.pb_PatientInfoRemovePatient.setObjectName(u"pb_PatientInfoRemovePatient")

        self.horizontalLayout_76.addWidget(self.pb_PatientInfoRemovePatient)

        self.pb_PatientInfoRemoveAll = QPushButton(self.page_PatientInfomation)
        self.pb_PatientInfoRemoveAll.setObjectName(u"pb_PatientInfoRemoveAll")
        self.pb_PatientInfoRemoveAll.setGeometry(QRect(120, 720, 191, 51))
        self.frame_11 = QFrame(self.page_PatientInfomation)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(480, 10, 781, 791))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.le_PatientInfoSearch = QLineEdit(self.frame_11)
        self.le_PatientInfoSearch.setObjectName(u"le_PatientInfoSearch")
        self.le_PatientInfoSearch.setMinimumSize(QSize(0, 35))

        self.horizontalLayout_14.addWidget(self.le_PatientInfoSearch)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.tableWidget_PatientInfoPatientTable = QTableWidget(self.frame_11)
        if (self.tableWidget_PatientInfoPatientTable.columnCount() < 6):
            self.tableWidget_PatientInfoPatientTable.setColumnCount(6)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setForeground(brush);
        self.tableWidget_PatientInfoPatientTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_PatientInfoPatientTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_PatientInfoPatientTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_PatientInfoPatientTable.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_PatientInfoPatientTable.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_PatientInfoPatientTable.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        self.tableWidget_PatientInfoPatientTable.setObjectName(u"tableWidget_PatientInfoPatientTable")

        self.verticalLayout_13.addWidget(self.tableWidget_PatientInfoPatientTable)

        self.stackedWidget.addWidget(self.page_PatientInfomation)
        self.page_Review = QWidget()
        self.page_Review.setObjectName(u"page_Review")
        self.frame_5 = QFrame(self.page_Review)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-1, 150, 461, 651))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_42.setSpacing(1)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(1, 1, 1, 1)
        self.tableWidget_ReviewDataAngle = QTableWidget(self.frame_5)
        if (self.tableWidget_ReviewDataAngle.columnCount() < 3):
            self.tableWidget_ReviewDataAngle.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_ReviewDataAngle.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_ReviewDataAngle.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_ReviewDataAngle.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        self.tableWidget_ReviewDataAngle.setObjectName(u"tableWidget_ReviewDataAngle")
        self.tableWidget_ReviewDataAngle.setEnabled(True)

        self.horizontalLayout_42.addWidget(self.tableWidget_ReviewDataAngle)

        self.widget_9 = QWidget(self.page_Review)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(460, 0, 311, 801))
        self.widget_9.setStyleSheet(u"QLabel{\n"
"font:75 10pt \"Droid Sans\";\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font:75 12pt \"Droid Sans\";\n"
"}\n"
"")
        self.pb_ReviewRunAndPauseExercise = QPushButton(self.widget_9)
        self.pb_ReviewRunAndPauseExercise.setObjectName(u"pb_ReviewRunAndPauseExercise")
        self.pb_ReviewRunAndPauseExercise.setGeometry(QRect(70, 380, 161, 41))
        self.frame_6 = QFrame(self.widget_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(5, 537, 181, 171))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_86 = QLabel(self.frame_6)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_49.addWidget(self.label_86)


        self.verticalLayout_9.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.lb_ReivewMaxHipAngle = QLabel(self.frame_6)
        self.lb_ReivewMaxHipAngle.setObjectName(u"lb_ReivewMaxHipAngle")

        self.horizontalLayout_50.addWidget(self.lb_ReivewMaxHipAngle)


        self.verticalLayout_9.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_90 = QLabel(self.frame_6)
        self.label_90.setObjectName(u"label_90")

        self.horizontalLayout_51.addWidget(self.label_90)


        self.verticalLayout_9.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.lb_ReivewMaxKneeAngle = QLabel(self.frame_6)
        self.lb_ReivewMaxKneeAngle.setObjectName(u"lb_ReivewMaxKneeAngle")

        self.horizontalLayout_52.addWidget(self.lb_ReivewMaxKneeAngle)


        self.verticalLayout_9.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_94 = QLabel(self.frame_6)
        self.label_94.setObjectName(u"label_94")

        self.horizontalLayout_53.addWidget(self.label_94)


        self.verticalLayout_9.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.lb_ReivewMaxAnkleAngle = QLabel(self.frame_6)
        self.lb_ReivewMaxAnkleAngle.setObjectName(u"lb_ReivewMaxAnkleAngle")

        self.horizontalLayout_54.addWidget(self.lb_ReivewMaxAnkleAngle)


        self.verticalLayout_9.addLayout(self.horizontalLayout_54)

        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 730, 111, 21))
        self.label_5.setStyleSheet(u"font: 12pt \"Segoe UI Historic\";")
        self.layoutWidget_31 = QWidget(self.widget_9)
        self.layoutWidget_31.setObjectName(u"layoutWidget_31")
        self.layoutWidget_31.setGeometry(QRect(10, 100, 296, 30))
        self.horizontalLayout_56 = QHBoxLayout(self.layoutWidget_31)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.layoutWidget_31)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_56.addWidget(self.label_100)

        self.pb_ReviewPatientsList = QPushButton(self.layoutWidget_31)
        self.pb_ReviewPatientsList.setObjectName(u"pb_ReviewPatientsList")

        self.horizontalLayout_56.addWidget(self.pb_ReviewPatientsList)

        self.layoutWidget3 = QWidget(self.widget_9)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 445, 301, 81))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_84 = QLabel(self.layoutWidget3)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_57.addWidget(self.label_84)

        self.horizontalSlider_ReviewSpeed = QSlider(self.layoutWidget3)
        self.horizontalSlider_ReviewSpeed.setObjectName(u"horizontalSlider_ReviewSpeed")
        self.horizontalSlider_ReviewSpeed.setValue(50)
        self.horizontalSlider_ReviewSpeed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_57.addWidget(self.horizontalSlider_ReviewSpeed)


        self.verticalLayout_5.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_101 = QLabel(self.layoutWidget3)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_58.addWidget(self.label_101)

        self.horizontalSlider_ReviewTimer = QSlider(self.layoutWidget3)
        self.horizontalSlider_ReviewTimer.setObjectName(u"horizontalSlider_ReviewTimer")
        self.horizontalSlider_ReviewTimer.setOrientation(Qt.Horizontal)

        self.horizontalLayout_58.addWidget(self.horizontalSlider_ReviewTimer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_58)

        self.layoutWidget4 = QWidget(self.widget_9)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 150, 301, 200))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_98 = QLabel(self.layoutWidget4)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_55.addWidget(self.label_98)

        self.lb_ReviewPatientName = QLabel(self.layoutWidget4)
        self.lb_ReviewPatientName.setObjectName(u"lb_ReviewPatientName")

        self.horizontalLayout_55.addWidget(self.lb_ReviewPatientName)


        self.verticalLayout_6.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_9 = QLabel(self.layoutWidget4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_15.addWidget(self.label_9)

        self.lb_ReviewPatientID = QLabel(self.layoutWidget4)
        self.lb_ReviewPatientID.setObjectName(u"lb_ReviewPatientID")

        self.horizontalLayout_15.addWidget(self.lb_ReviewPatientID)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_71 = QLabel(self.layoutWidget4)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_43.addWidget(self.label_71)

        self.lb_ReviewPatientGender = QLabel(self.layoutWidget4)
        self.lb_ReviewPatientGender.setObjectName(u"lb_ReviewPatientGender")

        self.horizontalLayout_43.addWidget(self.lb_ReviewPatientGender)

        self.label_73 = QLabel(self.layoutWidget4)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_43.addWidget(self.label_73)

        self.lb_ReviewPatientDateOfBirth = QLabel(self.layoutWidget4)
        self.lb_ReviewPatientDateOfBirth.setObjectName(u"lb_ReviewPatientDateOfBirth")

        self.horizontalLayout_43.addWidget(self.lb_ReviewPatientDateOfBirth)


        self.verticalLayout_6.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_75 = QLabel(self.layoutWidget4)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_44.addWidget(self.label_75)

        self.lb_ReviewWeight = QLabel(self.layoutWidget4)
        self.lb_ReviewWeight.setObjectName(u"lb_ReviewWeight")

        self.horizontalLayout_44.addWidget(self.lb_ReviewWeight)

        self.label_77 = QLabel(self.layoutWidget4)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_44.addWidget(self.label_77)

        self.lb_ReviewHeight = QLabel(self.layoutWidget4)
        self.lb_ReviewHeight.setObjectName(u"lb_ReviewHeight")

        self.horizontalLayout_44.addWidget(self.lb_ReviewHeight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_79 = QLabel(self.layoutWidget4)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_45.addWidget(self.label_79)

        self.lb_ReviewCode = QLabel(self.layoutWidget4)
        self.lb_ReviewCode.setObjectName(u"lb_ReviewCode")

        self.horizontalLayout_45.addWidget(self.lb_ReviewCode)


        self.verticalLayout_6.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_81 = QLabel(self.layoutWidget4)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_46.addWidget(self.label_81)

        self.cb_ReviewExercise = QComboBox(self.layoutWidget4)
        self.cb_ReviewExercise.setObjectName(u"cb_ReviewExercise")

        self.horizontalLayout_46.addWidget(self.cb_ReviewExercise)


        self.verticalLayout_6.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_82 = QLabel(self.layoutWidget4)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_47.addWidget(self.label_82)

        self.cb_ReviewDayExercise = QComboBox(self.layoutWidget4)
        self.cb_ReviewDayExercise.setObjectName(u"cb_ReviewDayExercise")

        self.horizontalLayout_47.addWidget(self.cb_ReviewDayExercise)


        self.verticalLayout_6.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_3)

        self.lb_ReviewTimer = QLabel(self.layoutWidget4)
        self.lb_ReviewTimer.setObjectName(u"lb_ReviewTimer")
        self.lb_ReviewTimer.setStyleSheet(u"font:75 12pt \"Droid Sans\";")

        self.horizontalLayout_48.addWidget(self.lb_ReviewTimer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_48)

        self.widget_ReviewLowerlimb = QWidget(self.page_Review)
        self.widget_ReviewLowerlimb.setObjectName(u"widget_ReviewLowerlimb")
        self.widget_ReviewLowerlimb.setGeometry(QRect(770, 300, 500, 500))
        self.widget_ReviewLinechart = QWidget(self.page_Review)
        self.widget_ReviewLinechart.setObjectName(u"widget_ReviewLinechart")
        self.widget_ReviewLinechart.setGeometry(QRect(770, 0, 500, 300))
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

        self.lb_CalibGyroIMU1 = QLabel(self.frame_7)
        self.lb_CalibGyroIMU1.setObjectName(u"lb_CalibGyroIMU1")
        self.lb_CalibGyroIMU1.setMinimumSize(QSize(10, 30))

        self.horizontalLayout_59.addWidget(self.lb_CalibGyroIMU1)

        self.pb_CalibGyroIMU1 = QPushButton(self.frame_7)
        self.pb_CalibGyroIMU1.setObjectName(u"pb_CalibGyroIMU1")
        self.pb_CalibGyroIMU1.setEnabled(True)
        self.pb_CalibGyroIMU1.setMaximumSize(QSize(20, 16777215))
        icon12 = QIcon()
        icon12.addFile(u"../1.tutorial/icon/accept.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_CalibGyroIMU1.setIcon(icon12)
        self.pb_CalibGyroIMU1.setIconSize(QSize(12, 12))
        self.pb_CalibGyroIMU1.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pb_CalibGyroIMU1)

        self.label_93 = QLabel(self.frame_7)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_59.addWidget(self.label_93)

        self.lb_CalibAccIMU1 = QLabel(self.frame_7)
        self.lb_CalibAccIMU1.setObjectName(u"lb_CalibAccIMU1")

        self.horizontalLayout_59.addWidget(self.lb_CalibAccIMU1)

        self.pb_CalibAccIMU1 = QPushButton(self.frame_7)
        self.pb_CalibAccIMU1.setObjectName(u"pb_CalibAccIMU1")
        self.pb_CalibAccIMU1.setEnabled(True)
        self.pb_CalibAccIMU1.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibAccIMU1.setIcon(icon12)
        self.pb_CalibAccIMU1.setIconSize(QSize(12, 12))
        self.pb_CalibAccIMU1.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pb_CalibAccIMU1)

        self.label_102 = QLabel(self.frame_7)
        self.label_102.setObjectName(u"label_102")

        self.horizontalLayout_59.addWidget(self.label_102)

        self.lb_CalibMagIMU1 = QLabel(self.frame_7)
        self.lb_CalibMagIMU1.setObjectName(u"lb_CalibMagIMU1")

        self.horizontalLayout_59.addWidget(self.lb_CalibMagIMU1)

        self.pb_CalibMagIMU1 = QPushButton(self.frame_7)
        self.pb_CalibMagIMU1.setObjectName(u"pb_CalibMagIMU1")
        self.pb_CalibMagIMU1.setEnabled(True)
        self.pb_CalibMagIMU1.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibMagIMU1.setIcon(icon12)
        self.pb_CalibMagIMU1.setIconSize(QSize(12, 12))
        self.pb_CalibMagIMU1.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pb_CalibMagIMU1)

        self.label_97 = QLabel(self.frame_7)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_59.addWidget(self.label_97)

        self.lb_CalibSysIMU1 = QLabel(self.frame_7)
        self.lb_CalibSysIMU1.setObjectName(u"lb_CalibSysIMU1")

        self.horizontalLayout_59.addWidget(self.lb_CalibSysIMU1)

        self.pb_CalibSysIMU1 = QPushButton(self.frame_7)
        self.pb_CalibSysIMU1.setObjectName(u"pb_CalibSysIMU1")
        self.pb_CalibSysIMU1.setEnabled(True)
        self.pb_CalibSysIMU1.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibSysIMU1.setIcon(icon12)
        self.pb_CalibSysIMU1.setIconSize(QSize(12, 12))
        self.pb_CalibSysIMU1.setFlat(True)

        self.horizontalLayout_59.addWidget(self.pb_CalibSysIMU1)


        self.verticalLayout_10.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_105 = QLabel(self.frame_7)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_60.addWidget(self.label_105)

        self.label_106 = QLabel(self.frame_7)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_60.addWidget(self.label_106)

        self.lb_CalibGyroIMU2 = QLabel(self.frame_7)
        self.lb_CalibGyroIMU2.setObjectName(u"lb_CalibGyroIMU2")

        self.horizontalLayout_60.addWidget(self.lb_CalibGyroIMU2)

        self.pb_CalibGyroIMU2 = QPushButton(self.frame_7)
        self.pb_CalibGyroIMU2.setObjectName(u"pb_CalibGyroIMU2")
        self.pb_CalibGyroIMU2.setEnabled(True)
        self.pb_CalibGyroIMU2.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibGyroIMU2.setIcon(icon12)
        self.pb_CalibGyroIMU2.setIconSize(QSize(12, 12))
        self.pb_CalibGyroIMU2.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pb_CalibGyroIMU2)

        self.label_108 = QLabel(self.frame_7)
        self.label_108.setObjectName(u"label_108")

        self.horizontalLayout_60.addWidget(self.label_108)

        self.lb_CalibAccIMU2 = QLabel(self.frame_7)
        self.lb_CalibAccIMU2.setObjectName(u"lb_CalibAccIMU2")

        self.horizontalLayout_60.addWidget(self.lb_CalibAccIMU2)

        self.pb_CalibAccIMU2 = QPushButton(self.frame_7)
        self.pb_CalibAccIMU2.setObjectName(u"pb_CalibAccIMU2")
        self.pb_CalibAccIMU2.setEnabled(True)
        self.pb_CalibAccIMU2.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibAccIMU2.setIcon(icon12)
        self.pb_CalibAccIMU2.setIconSize(QSize(12, 12))
        self.pb_CalibAccIMU2.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pb_CalibAccIMU2)

        self.label_110 = QLabel(self.frame_7)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_60.addWidget(self.label_110)

        self.lb_CalibMagIMU2 = QLabel(self.frame_7)
        self.lb_CalibMagIMU2.setObjectName(u"lb_CalibMagIMU2")

        self.horizontalLayout_60.addWidget(self.lb_CalibMagIMU2)

        self.pb_CalibMagIMU2 = QPushButton(self.frame_7)
        self.pb_CalibMagIMU2.setObjectName(u"pb_CalibMagIMU2")
        self.pb_CalibMagIMU2.setEnabled(True)
        self.pb_CalibMagIMU2.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibMagIMU2.setIcon(icon12)
        self.pb_CalibMagIMU2.setIconSize(QSize(12, 12))
        self.pb_CalibMagIMU2.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pb_CalibMagIMU2)

        self.label_112 = QLabel(self.frame_7)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_60.addWidget(self.label_112)

        self.lb_CalibSysIMU2 = QLabel(self.frame_7)
        self.lb_CalibSysIMU2.setObjectName(u"lb_CalibSysIMU2")

        self.horizontalLayout_60.addWidget(self.lb_CalibSysIMU2)

        self.pb_CalibSysIMU2 = QPushButton(self.frame_7)
        self.pb_CalibSysIMU2.setObjectName(u"pb_CalibSysIMU2")
        self.pb_CalibSysIMU2.setEnabled(True)
        self.pb_CalibSysIMU2.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibSysIMU2.setIcon(icon12)
        self.pb_CalibSysIMU2.setIconSize(QSize(12, 12))
        self.pb_CalibSysIMU2.setFlat(True)

        self.horizontalLayout_60.addWidget(self.pb_CalibSysIMU2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_114 = QLabel(self.frame_7)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_61.addWidget(self.label_114)

        self.label_115 = QLabel(self.frame_7)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_61.addWidget(self.label_115)

        self.lb_CalibGyroIMU3 = QLabel(self.frame_7)
        self.lb_CalibGyroIMU3.setObjectName(u"lb_CalibGyroIMU3")

        self.horizontalLayout_61.addWidget(self.lb_CalibGyroIMU3)

        self.pb_CalibGyroIMU3 = QPushButton(self.frame_7)
        self.pb_CalibGyroIMU3.setObjectName(u"pb_CalibGyroIMU3")
        self.pb_CalibGyroIMU3.setEnabled(True)
        self.pb_CalibGyroIMU3.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibGyroIMU3.setIcon(icon12)
        self.pb_CalibGyroIMU3.setIconSize(QSize(12, 12))
        self.pb_CalibGyroIMU3.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pb_CalibGyroIMU3)

        self.label_117 = QLabel(self.frame_7)
        self.label_117.setObjectName(u"label_117")

        self.horizontalLayout_61.addWidget(self.label_117)

        self.lb_CalibAccIMU3 = QLabel(self.frame_7)
        self.lb_CalibAccIMU3.setObjectName(u"lb_CalibAccIMU3")

        self.horizontalLayout_61.addWidget(self.lb_CalibAccIMU3)

        self.pb_CalibAccIMU3 = QPushButton(self.frame_7)
        self.pb_CalibAccIMU3.setObjectName(u"pb_CalibAccIMU3")
        self.pb_CalibAccIMU3.setEnabled(True)
        self.pb_CalibAccIMU3.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibAccIMU3.setIcon(icon12)
        self.pb_CalibAccIMU3.setIconSize(QSize(12, 12))
        self.pb_CalibAccIMU3.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pb_CalibAccIMU3)

        self.label_119 = QLabel(self.frame_7)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_61.addWidget(self.label_119)

        self.lb_CalibMagIMU3 = QLabel(self.frame_7)
        self.lb_CalibMagIMU3.setObjectName(u"lb_CalibMagIMU3")

        self.horizontalLayout_61.addWidget(self.lb_CalibMagIMU3)

        self.pb_CalibMagIMU3 = QPushButton(self.frame_7)
        self.pb_CalibMagIMU3.setObjectName(u"pb_CalibMagIMU3")
        self.pb_CalibMagIMU3.setEnabled(True)
        self.pb_CalibMagIMU3.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibMagIMU3.setIcon(icon12)
        self.pb_CalibMagIMU3.setIconSize(QSize(12, 12))
        self.pb_CalibMagIMU3.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pb_CalibMagIMU3)

        self.label_121 = QLabel(self.frame_7)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_61.addWidget(self.label_121)

        self.lb_CalibSysIMU3 = QLabel(self.frame_7)
        self.lb_CalibSysIMU3.setObjectName(u"lb_CalibSysIMU3")

        self.horizontalLayout_61.addWidget(self.lb_CalibSysIMU3)

        self.pb_CalibSysIMU3 = QPushButton(self.frame_7)
        self.pb_CalibSysIMU3.setObjectName(u"pb_CalibSysIMU3")
        self.pb_CalibSysIMU3.setEnabled(True)
        self.pb_CalibSysIMU3.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibSysIMU3.setIcon(icon12)
        self.pb_CalibSysIMU3.setIconSize(QSize(12, 12))
        self.pb_CalibSysIMU3.setFlat(True)

        self.horizontalLayout_61.addWidget(self.pb_CalibSysIMU3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_123 = QLabel(self.frame_7)
        self.label_123.setObjectName(u"label_123")

        self.horizontalLayout_62.addWidget(self.label_123)

        self.label_124 = QLabel(self.frame_7)
        self.label_124.setObjectName(u"label_124")

        self.horizontalLayout_62.addWidget(self.label_124)

        self.lb_CalibGyroIMU4 = QLabel(self.frame_7)
        self.lb_CalibGyroIMU4.setObjectName(u"lb_CalibGyroIMU4")

        self.horizontalLayout_62.addWidget(self.lb_CalibGyroIMU4)

        self.pb_CalibGyroIMU4 = QPushButton(self.frame_7)
        self.pb_CalibGyroIMU4.setObjectName(u"pb_CalibGyroIMU4")
        self.pb_CalibGyroIMU4.setEnabled(True)
        self.pb_CalibGyroIMU4.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibGyroIMU4.setIcon(icon12)
        self.pb_CalibGyroIMU4.setIconSize(QSize(12, 12))
        self.pb_CalibGyroIMU4.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pb_CalibGyroIMU4)

        self.label_126 = QLabel(self.frame_7)
        self.label_126.setObjectName(u"label_126")

        self.horizontalLayout_62.addWidget(self.label_126)

        self.lb_CalibAccIMU4 = QLabel(self.frame_7)
        self.lb_CalibAccIMU4.setObjectName(u"lb_CalibAccIMU4")

        self.horizontalLayout_62.addWidget(self.lb_CalibAccIMU4)

        self.pb_CalibAccIMU4 = QPushButton(self.frame_7)
        self.pb_CalibAccIMU4.setObjectName(u"pb_CalibAccIMU4")
        self.pb_CalibAccIMU4.setEnabled(True)
        self.pb_CalibAccIMU4.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibAccIMU4.setIcon(icon12)
        self.pb_CalibAccIMU4.setIconSize(QSize(12, 12))
        self.pb_CalibAccIMU4.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pb_CalibAccIMU4)

        self.label_128 = QLabel(self.frame_7)
        self.label_128.setObjectName(u"label_128")

        self.horizontalLayout_62.addWidget(self.label_128)

        self.lb_CalibMagIMU4 = QLabel(self.frame_7)
        self.lb_CalibMagIMU4.setObjectName(u"lb_CalibMagIMU4")

        self.horizontalLayout_62.addWidget(self.lb_CalibMagIMU4)

        self.pb_CalibMagIMU4 = QPushButton(self.frame_7)
        self.pb_CalibMagIMU4.setObjectName(u"pb_CalibMagIMU4")
        self.pb_CalibMagIMU4.setEnabled(True)
        self.pb_CalibMagIMU4.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibMagIMU4.setIcon(icon12)
        self.pb_CalibMagIMU4.setIconSize(QSize(12, 12))
        self.pb_CalibMagIMU4.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pb_CalibMagIMU4)

        self.label_130 = QLabel(self.frame_7)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_62.addWidget(self.label_130)

        self.lb_CalibSysIMU4 = QLabel(self.frame_7)
        self.lb_CalibSysIMU4.setObjectName(u"lb_CalibSysIMU4")

        self.horizontalLayout_62.addWidget(self.lb_CalibSysIMU4)

        self.pb_CalibSysIMU4 = QPushButton(self.frame_7)
        self.pb_CalibSysIMU4.setObjectName(u"pb_CalibSysIMU4")
        self.pb_CalibSysIMU4.setEnabled(True)
        self.pb_CalibSysIMU4.setMaximumSize(QSize(20, 16777215))
        self.pb_CalibSysIMU4.setIcon(icon12)
        self.pb_CalibSysIMU4.setIconSize(QSize(12, 12))
        self.pb_CalibSysIMU4.setFlat(True)

        self.horizontalLayout_62.addWidget(self.pb_CalibSysIMU4)


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

        self.stackedWidget.setCurrentIndex(3)
        self.pb_MainCheckImu1.setDefault(False)


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
        self.pb_MainConnector.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft N\u1ed1i", None))
        self.label_MainImu1.setText(QCoreApplication.translate("MainWindow", u"IMU1: ", None))
        self.pb_MainCheckImu1.setText("")
        self.label_MainImu2.setText(QCoreApplication.translate("MainWindow", u"IMU2: ", None))
        self.pb_MainCheckImu2.setText("")
        self.label_MainImu3.setText(QCoreApplication.translate("MainWindow", u"IMU3: ", None))
        self.pb_MainCheckImu3.setText("")
        self.label_MainImu4.setText(QCoreApplication.translate("MainWindow", u"IMU4: ", None))
        self.pb_MainCheckImu4.setText("")
        ___qtablewidgetitem = self.tableWidget_MDataTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Hip", None));
        ___qtablewidgetitem1 = self.tableWidget_MDataTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Knee", None));
        ___qtablewidgetitem2 = self.tableWidget_MDataTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ankle", None));
        self.pb_MainPatientsList.setText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch b\u1ec7nh nh\u00e2n", None))
        self.pb_MainAddPatient.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam b\u1ec7nh nh\u00e2n m\u1edbi", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.lb_MainPatientGender.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y Sinh:", None))
        self.lb_MainDateOfBirth.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng:", None))
        self.lb_MainPatientWeight.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao:", None))
        self.lb_MainPatientHeight.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n:", None))
        self.lb_MainPatientCode.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"B\u00e0i ki\u1ec3m tra:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111o:", None))
        self.lb_MainDayExercise.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"MAIN WIDGET", None))
        self.lb_MainTimer.setText(QCoreApplication.translate("MainWindow", u"00:00.0000ms", None))
        self.pb_MainStartExercise.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u \u0111o", None))
        self.pb_MainEndExercise.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft th\u00fac \u0111o", None))
        self.pb_MainSaveData.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u k\u1ebft qu\u1ea3", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Max Hip angle", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Max last Hip angle", None))
        self.lb_MainMaxHipAngle.setText(QCoreApplication.translate("MainWindow", u"100.77", None))
        self.lb_MainMaxLastHipAngle.setText(QCoreApplication.translate("MainWindow", u"100.66", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Max Knee angle", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Max last Knee angle", None))
        self.lb_MainMaxKneeAngle.setText(QCoreApplication.translate("MainWindow", u"359.99", None))
        self.lb_MainMaxLastKneeAngle.setText(QCoreApplication.translate("MainWindow", u"111.11", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Max Ankle angle", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Max last Ankle angle", None))
        self.lb_MainMaxAnkleAngle.setText(QCoreApplication.translate("MainWindow", u"423.123", None))
        self.lb_MainMaxLastAnkleAngle.setText(QCoreApplication.translate("MainWindow", u"123.123", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean: ", None))
        self.lb_MainPatientName.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CCCD: ", None))
        self.lb_MainPatientID.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Intro WIDGET", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 t\u00e0i tr\u1ee3 s\u1eaft: Only C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Setting WIDGET", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb \u0111\u1ed9 d\u00e0i:", None))
        self.rb_SettingCm.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.rb_SettingInch.setText(QCoreApplication.translate("MainWindow", u"inch", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n v\u1ecb kh\u1ed1i l\u01b0\u1ee3ng:", None))
        self.rb_SettingKg.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.rb_SettingLb.setText(QCoreApplication.translate("MainWindow", u"lb", None))
        self.pb_SettingResetSystem.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1eb7t l\u1ea1i h\u1ec7 th\u1ed1ng( ch\u1ee9c n\u0103ng m\u1edf r\u1ed9ng sau n\u00e0y)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ng\u00f4n ng\u1eef", None))
        self.cb_SettingLanguage.setItemText(0, QCoreApplication.translate("MainWindow", u"Ti\u1ebfng Vi\u1ec7t", None))
        self.cb_SettingLanguage.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Patient WIDGET", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.le_PatientInfoName.setText("")
        self.le_PatientInfoName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ean", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"CCCD:", None))
        self.le_PatientInfoID.setText("")
        self.le_PatientInfoID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CCCD", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh:", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.cb_PatientInfoGender.setItemText(0, QCoreApplication.translate("MainWindow", u"Nam", None))
        self.cb_PatientInfoGender.setItemText(1, QCoreApplication.translate("MainWindow", u"N\u1eef", None))

        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao:", None))
        self.le_PatientInfoHeight.setText("")
        self.le_PatientInfoHeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng:", None))
        self.le_PatientInfoWeight.setText("")
        self.le_PatientInfoWeight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n:", None))
        self.lb_PatientInfoPatitentCode.setText("")
        self.pb_PatientInfoSavePatient.setText(QCoreApplication.translate("MainWindow", u"L\u01b0u", None))
        self.pb_PatientInfoRemovePatient.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.pb_PatientInfoRemoveAll.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a to\u00e0n b\u1ed9 danh s\u00e1ch", None))
        self.le_PatientInfoSearch.setText("")
        self.le_PatientInfoSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"T\u00ecm Ki\u1ebfm...", None))
        ___qtablewidgetitem3 = self.tableWidget_PatientInfoPatientTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"STT", None));
        ___qtablewidgetitem4 = self.tableWidget_PatientInfoPatientTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n", None));
        ___qtablewidgetitem5 = self.tableWidget_PatientInfoPatientTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem6 = self.tableWidget_PatientInfoPatientTable.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None));
        ___qtablewidgetitem7 = self.tableWidget_PatientInfoPatientTable.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"CCCD", None));
        ___qtablewidgetitem8 = self.tableWidget_PatientInfoPatientTable.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh", None));
        ___qtablewidgetitem9 = self.tableWidget_ReviewDataAngle.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Hip", None));
        ___qtablewidgetitem10 = self.tableWidget_ReviewDataAngle.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Knee", None));
        ___qtablewidgetitem11 = self.tableWidget_ReviewDataAngle.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ankle", None));
        self.pb_ReviewRunAndPauseExercise.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ea1y/T\u1ea1m D\u1eebng", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Max Hip angle", None))
        self.lb_ReivewMaxHipAngle.setText(QCoreApplication.translate("MainWindow", u"100.77", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Max Knee angle", None))
        self.lb_ReivewMaxKneeAngle.setText(QCoreApplication.translate("MainWindow", u"359.99", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Max Ankle angle", None))
        self.lb_ReivewMaxAnkleAngle.setText(QCoreApplication.translate("MainWindow", u"423.123", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Review WIDGET", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Th\u00f4ng tin b\u1ec7nh nh\u00e2n:", None))
        self.pb_ReviewPatientsList.setText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch b\u1ec7nh nh\u00e2n", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"T\u1ed1c \u0111\u1ed9:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Th\u1eddi gian:", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.lb_ReviewPatientName.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"CCCD:", None))
        self.lb_ReviewPatientID.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh:", None))
        self.lb_ReviewPatientGender.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y Sinh:", None))
        self.lb_ReviewPatientDateOfBirth.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"C\u00e2n n\u1eb7ng:", None))
        self.lb_ReviewWeight.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Chi\u1ec1u cao:", None))
        self.lb_ReviewHeight.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 b\u1ec7nh nh\u00e2n:", None))
        self.lb_ReviewCode.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"B\u00e0i ki\u1ec3m tra:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y \u0111o:", None))
        self.lb_ReviewTimer.setText(QCoreApplication.translate("MainWindow", u"00:00.0000ms", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Calib WIDGET", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"IMU1:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.lb_CalibGyroIMU1.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibGyroIMU1.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.lb_CalibAccIMU1.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibAccIMU1.setText("")
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.lb_CalibMagIMU1.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibMagIMU1.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.lb_CalibSysIMU1.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibSysIMU1.setText("")
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"IMU2:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.lb_CalibGyroIMU2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibGyroIMU2.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.lb_CalibAccIMU2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibAccIMU2.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.lb_CalibMagIMU2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibMagIMU2.setText("")
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.lb_CalibSysIMU2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibSysIMU2.setText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"IMU3:", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.lb_CalibGyroIMU3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibGyroIMU3.setText("")
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.lb_CalibAccIMU3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibAccIMU3.setText("")
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.lb_CalibMagIMU3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibMagIMU3.setText("")
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.lb_CalibSysIMU3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibSysIMU3.setText("")
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"IMU4:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"Gyro", None))
        self.lb_CalibGyroIMU4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibGyroIMU4.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Acc", None))
        self.lb_CalibAccIMU4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibAccIMU4.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Mag", None))
        self.lb_CalibMagIMU4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibMagIMU4.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Sys", None))
        self.lb_CalibSysIMU4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pb_CalibSysIMU4.setText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh t\u1eeb k\u1ebf(mag): Gi\u1eef c\u1ea3m bi\u1ebfn song song v\u1edbi m\u1eb7t \u0111\u1ea5t v\u00e0 di chuy\u1ec3n theo h\u00ecnh s\u1ed1 8", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh gia t\u1ed1c k\u1ebf(gyro): \u0110\u1eb7t c\u1ea3m bi\u1ebfn \u1edf 6 v\u1ecb tr\u00ed \u1ed5n \u0111\u1ecbnh v\u00e0i gi\u00e2y m\u1ed7i v\u1ecb tr\u00ed", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh con quay h\u1ed3i chuy\u1ec3n(acc): \u0110\u1eb7t c\u1ea3m bi\u1ebfn \u1edf b\u1ea5t k\u00ec v\u1ecb tr\u00ed \u1ed5n \u0111\u1ecbnh n\u00e0o trong v\u00e0i gi\u00e2y", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"- Hi\u1ec7u ch\u1ec9nh h\u1ec7 th\u1ed1ng(sys): S\u1ebd t\u1ef1 \u0111\u1ed9ng \u0111i\u1ec1u ch\u1ec9nh theo 3 th\u00f4ng s\u1ed1 tr\u00ean. Trong tr\u01b0\u1eddng h\u1ee3p c\u00f3 v\u1ea5n \u0111\u1ec1 kh\u00f4ng t\u1ef1 hi\u1ec7u ch\u1ec9nh th\u00ec kh\u1edfi \u0111\u1ed9ng l\u1ea1i thi\u1ebft b\u1ecb", None))
        self.label_136.setText("")
        self.label_137.setText("")
    # retranslateUi

