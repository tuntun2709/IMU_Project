
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(892, 569)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_NameSearch = QLineEdit(Dialog)
        self.lineEdit_NameSearch.setObjectName(u"lineEdit_NameSearch")

        self.horizontalLayout.addWidget(self.lineEdit_NameSearch)

        self.lineEdit_CodeSearch = QLineEdit(Dialog)
        self.lineEdit_CodeSearch.setObjectName(u"lineEdit_CodeSearch")

        self.horizontalLayout.addWidget(self.lineEdit_CodeSearch)

        self.pb_PartientListSearch = QPushButton(Dialog)
        self.pb_PartientListSearch.setObjectName(u"pb_PartientListSearch")
        icon = QIcon()
        icon.addFile(u"icon/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_PartientListSearch.setIcon(icon)
        self.pb_PartientListSearch.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pb_PartientListSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget_PartientList = QTableWidget(Dialog)
        if (self.tableWidget_PartientList.columnCount() < 6):
            self.tableWidget_PartientList.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_PartientList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_PartientList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_PartientList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_PartientList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_PartientList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_PartientList.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_PartientList.setObjectName(u"tableWidget_PartientList")

        self.verticalLayout.addWidget(self.tableWidget_PartientList)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pb_PartientListSearch.setText("")
        ___qtablewidgetitem = self.tableWidget_PartientList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"STT", None));
        ___qtablewidgetitem1 = self.tableWidget_PartientList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"M\u00e3 B\u1ec7nh Nh\u00e2n", None));
        ___qtablewidgetitem2 = self.tableWidget_PartientList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"H\u1ecd v\u00e0 T\u00ean", None));
        ___qtablewidgetitem3 = self.tableWidget_PartientList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y Sinh", None));
        ___qtablewidgetitem4 = self.tableWidget_PartientList.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"CCCD", None));
        ___qtablewidgetitem5 = self.tableWidget_PartientList.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Gi\u1edbi t\u00ednh", None));
    # retranslateUi

