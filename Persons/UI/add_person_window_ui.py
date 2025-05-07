# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import Icons_rc

class Ui_d_Person(object):
    def setupUi(self, d_Person):
        if not d_Person.objectName():
            d_Person.setObjectName(u"d_Person")
        d_Person.setWindowModality(Qt.WindowModality.ApplicationModal)
        d_Person.resize(483, 327)
        font = QFont()
        font.setPointSize(12)
        d_Person.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/dollar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        d_Person.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_Person)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_submit = QPushButton(d_Person)
        self.pb_submit.setObjectName(u"pb_submit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/check3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_submit.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_submit, 2, 1, 1, 1)

        self.pb_close = QPushButton(d_Person)
        self.pb_close.setObjectName(u"pb_close")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_close.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_close, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 3)

        self.gb_Person = QGroupBox(d_Person)
        self.gb_Person.setObjectName(u"gb_Person")
        self.gb_Person.setAcceptDrops(False)
        self.gb_Person.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.gb_Person)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_Person)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.le_first_name = QLineEdit(self.gb_Person)
        self.le_first_name.setObjectName(u"le_first_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_first_name)

        self.le_last_name = QLineEdit(self.gb_Person)
        self.le_last_name.setObjectName(u"le_last_name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.le_last_name)

        self.label_2 = QLabel(self.gb_Person)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.gb_Person)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.gb_Person)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.le_email = QLineEdit(self.gb_Person)
        self.le_email.setObjectName(u"le_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.le_email)

        self.le_phoneNumber = QLineEdit(self.gb_Person)
        self.le_phoneNumber.setObjectName(u"le_phoneNumber")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.le_phoneNumber)


        self.gridLayout.addWidget(self.gb_Person, 0, 0, 1, 3)

        self.lb_message = QLabel(d_Person)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 3, 0, 1, 3)

        QWidget.setTabOrder(self.le_first_name, self.le_last_name)
        QWidget.setTabOrder(self.le_last_name, self.pb_submit)
        QWidget.setTabOrder(self.pb_submit, self.pb_close)

        self.retranslateUi(d_Person)

        QMetaObject.connectSlotsByName(d_Person)
    # setupUi

    def retranslateUi(self, d_Person):
        d_Person.setWindowTitle(QCoreApplication.translate("d_Person", u"Sample_Application", None))
        self.pb_submit.setText(QCoreApplication.translate("d_Person", u"Submit", None))
        self.pb_close.setText(QCoreApplication.translate("d_Person", u"Close", None))
        self.gb_Person.setTitle(QCoreApplication.translate("d_Person", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("d_Person", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("d_Person", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("d_Person", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("d_Person", u"Phone Number", None))
        self.lb_message.setText(QCoreApplication.translate("d_Person", u"Message", None))
    # retranslateUi

