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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 571)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_topMenu = QFrame(self.centralwidget)
        self.fr_topMenu.setObjectName(u"fr_topMenu")
        self.fr_topMenu.setMaximumSize(QSize(16777215, 40))
        self.fr_topMenu.setStyleSheet(u"background-color: rgb(0, 153, 229);")
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
"background-color: #009dec;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"}")
        icon = QIcon()
        icon.addFile(u"../codecat/gui-pyside2-qtdesigner/Menu lateral desplegable/barra-de-menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Menu.setIcon(icon)
        self.bt_Menu.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bt_Menu)

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
        self.fr_sideMenu.setMaximumSize(QSize(200, 16777215))
        self.fr_sideMenu.setStyleSheet(u"background-color: rgb(0, 157, 236);")
        self.fr_sideMenu.setFrameShape(QFrame.StyledPanel)
        self.fr_sideMenu.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.fr_sideMenu)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(60, 20, 75, 24))
        self.pushButton_11 = QPushButton(self.fr_sideMenu)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(50, 480, 75, 24))

        self.horizontalLayout.addWidget(self.fr_sideMenu)

        self.fr_mainContent = QFrame(self.fr_bottom)
        self.fr_mainContent.setObjectName(u"fr_mainContent")
        self.fr_mainContent.setFrameShape(QFrame.StyledPanel)
        self.fr_mainContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_mainContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.fr_mainContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.fr_mainContent)


        self.verticalLayout.addWidget(self.fr_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_Menu.setText(QCoreApplication.translate("MainWindow", u"    Menu", None))
        self.bt_mini.setText("")
        self.bt_smallSize.setText("")
        self.bt_expand.setText("")
        self.bt_close.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

