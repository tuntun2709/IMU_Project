from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(318, 328)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_Exercise = QLineEdit(Dialog)
        self.lineEdit_Exercise.setObjectName(u"lineEdit_Exercise")

        self.horizontalLayout.addWidget(self.lineEdit_Exercise)

        self.pb_AddExercise = QPushButton(Dialog)
        self.pb_AddExercise.setObjectName(u"pb_AddExercise")

        self.horizontalLayout.addWidget(self.pb_AddExercise)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget_Exercise = QTableWidget(Dialog)
        if (self.tableWidget_Exercise.columnCount() < 1):
            self.tableWidget_Exercise.setColumnCount(1)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_Exercise.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget_Exercise.setObjectName(u"tableWidget_Exercise")
        self.tableWidget_Exercise.setMinimumSize(QSize(300, 230))
        self.tableWidget_Exercise.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_Exercise.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.verticalLayout.addWidget(self.tableWidget_Exercise)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_EditExercise = QPushButton(Dialog)
        self.pb_EditExercise.setObjectName(u"pb_EditExercise")
        self.pb_EditExercise.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.pb_EditExercise)

        self.pb_RemoveExercise = QPushButton(Dialog)
        self.pb_RemoveExercise.setObjectName(u"pb_RemoveExercise")
        self.pb_RemoveExercise.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.pb_RemoveExercise)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pb_AddExercise.setText(QCoreApplication.translate("Dialog", u"Th\u00eam", None))
        ___qtablewidgetitem = self.tableWidget_Exercise.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"B\u00e0i t\u1eadp", None));
        self.pb_EditExercise.setText(QCoreApplication.translate("Dialog", u"S\u1eeda", None))
        self.pb_RemoveExercise.setText(QCoreApplication.translate("Dialog", u"X\u00f3a", None))
    # retranslateUi

