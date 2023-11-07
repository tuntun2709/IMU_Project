from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLineEdit, QSizePolicy, QTableWidget,
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
        self.lineEdit_Search = QLineEdit(Dialog)
        self.lineEdit_Search.setObjectName(u"lineEdit_Search")

        self.horizontalLayout.addWidget(self.lineEdit_Search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget_PatientsList = QTableWidget(Dialog)
        if (self.tableWidget_PatientsList.columnCount() < 6):
            self.tableWidget_PatientsList.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_PatientsList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_PatientsList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_PatientsList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_PatientsList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_PatientsList.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_PatientsList.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_PatientsList.setObjectName(u"tableWidget_PatientsList")
        self.tableWidget_PatientsList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.tableWidget_PatientsList)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit_Search.setPlaceholderText(QCoreApplication.translate("Dialog", u"T\u00ecm Ki\u1ebfm...", None))
        ___qtablewidgetitem = self.tableWidget_PatientsList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"STT", None));
        ___qtablewidgetitem1 = self.tableWidget_PatientsList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"M\u00e3 B\u1ec7nh Nh\u00e2n", None));
        ___qtablewidgetitem2 = self.tableWidget_PatientsList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"H\u1ecd v\u00e0 T\u00ean", None));
        ___qtablewidgetitem3 = self.tableWidget_PatientsList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y Sinh", None));
        ___qtablewidgetitem4 = self.tableWidget_PatientsList.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"CCCD", None));
        ___qtablewidgetitem5 = self.tableWidget_PatientsList.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Gi\u1edbi t\u00ednh", None));
    # retranslateUi

