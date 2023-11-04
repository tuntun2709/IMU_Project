from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(323, 326)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.lineEdit_Name = QLineEdit(Dialog)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.horizontalLayout_11.addWidget(self.lineEdit_Name)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.lineEdit_ID = QLineEdit(Dialog)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")

        self.horizontalLayout_16.addWidget(self.lineEdit_ID)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.dateEdit_DateOfBirth = QDateEdit(Dialog)
        self.dateEdit_DateOfBirth.setObjectName(u"dateEdit_DateOfBirth")

        self.horizontalLayout_12.addWidget(self.dateEdit_DateOfBirth)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_13.addWidget(self.label_9)

        self.radioButton_Male = QRadioButton(Dialog)
        self.radioButton_Male.setObjectName(u"radioButton_Male")

        self.horizontalLayout_13.addWidget(self.radioButton_Male)

        self.radioButton_Female = QRadioButton(Dialog)
        self.radioButton_Female.setObjectName(u"radioButton_Female")

        self.horizontalLayout_13.addWidget(self.radioButton_Female)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_14.addWidget(self.label_10)

        self.lineEdit_Weight = QLineEdit(Dialog)
        self.lineEdit_Weight.setObjectName(u"lineEdit_Weight")

        self.horizontalLayout_14.addWidget(self.lineEdit_Weight)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_15.addWidget(self.label_11)

        self.lineEdit_Height = QLineEdit(Dialog)
        self.lineEdit_Height.setObjectName(u"lineEdit_Height")

        self.horizontalLayout_15.addWidget(self.lineEdit_Height)


        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_36 = QLabel(Dialog)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_24.addWidget(self.label_36)

        self.comboBox_Exercise = QComboBox(Dialog)
        self.comboBox_Exercise.addItem("")
        self.comboBox_Exercise.addItem("")
        self.comboBox_Exercise.addItem("")
        self.comboBox_Exercise.setObjectName(u"comboBox_Exercise")

        self.horizontalLayout_24.addWidget(self.comboBox_Exercise)


        self.verticalLayout.addLayout(self.horizontalLayout_24)

        self.pushButton_SaveInfomation = QPushButton(Dialog)
        self.pushButton_SaveInfomation.setObjectName(u"pushButton_SaveInfomation")
        self.pushButton_SaveInfomation.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton_SaveInfomation)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Th\u00f4ng tin b\u1ec7nh nh\u00e2n", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"H\u1ecd v\u00e0 t\u00ean:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"CCCD: ", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Ng\u00e0y sinh:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Gi\u1edbi t\u00ednh:", None))
        self.radioButton_Male.setText(QCoreApplication.translate("Dialog", u"Nam", None))
        self.radioButton_Female.setText(QCoreApplication.translate("Dialog", u"N\u1eef", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"C\u00e2n n\u1eb7ng:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Chi\u1ec1u cao:", None))
        self.label_36.setText(QCoreApplication.translate("Dialog", u"B\u00e0i ki\u1ec3m tra:", None))
        self.comboBox_Exercise.setItemText(0, QCoreApplication.translate("Dialog", u"\u0110i \u0103n", None))
        self.comboBox_Exercise.setItemText(1, QCoreApplication.translate("Dialog", u"\u0110i ng\u1ee7", None))
        self.comboBox_Exercise.setItemText(2, QCoreApplication.translate("Dialog", u"Th\u00eam m\u1edbi", None))

        self.pushButton_SaveInfomation.setText(QCoreApplication.translate("Dialog", u"L\u01b0u th\u00f4ng tin", None))
    # retranslateUi

