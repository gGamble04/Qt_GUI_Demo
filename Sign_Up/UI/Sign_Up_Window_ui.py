# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sign_Up_Window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Icons_rc

class Ui_W_Signup_Form(object):
    def setupUi(self, W_Signup_Form):
        if not W_Signup_Form.objectName():
            W_Signup_Form.setObjectName(u"W_Signup_Form")
        W_Signup_Form.resize(662, 310)
        font = QFont()
        font.setPointSize(12)
        W_Signup_Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/dollar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        W_Signup_Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(W_Signup_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(W_Signup_Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.le_UserID = QLineEdit(self.groupBox)
        self.le_UserID.setObjectName(u"le_UserID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.le_UserID)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")
        self.le_Password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.le_Password)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer)

        self.pb_ok = QPushButton(self.groupBox)
        self.pb_ok.setObjectName(u"pb_ok")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/check3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_ok.setIcon(icon1)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pb_ok)

        self.pb_cancel = QPushButton(self.groupBox)
        self.pb_cancel.setObjectName(u"pb_cancel")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pb_cancel.setIcon(icon2)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.pb_cancel)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.le_retype_password = QLineEdit(self.groupBox)
        self.le_retype_password.setObjectName(u"le_retype_password")
        self.le_retype_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.le_retype_password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.lb_message = QLabel(W_Signup_Form)
        self.lb_message.setObjectName(u"lb_message")

        self.gridLayout.addWidget(self.lb_message, 1, 0, 1, 1)

        QWidget.setTabOrder(self.le_UserID, self.le_Password)
        QWidget.setTabOrder(self.le_Password, self.le_retype_password)
        QWidget.setTabOrder(self.le_retype_password, self.pb_ok)
        QWidget.setTabOrder(self.pb_ok, self.pb_cancel)

        self.retranslateUi(W_Signup_Form)

        QMetaObject.connectSlotsByName(W_Signup_Form)
    # setupUi

    def retranslateUi(self, W_Signup_Form):
        W_Signup_Form.setWindowTitle(QCoreApplication.translate("W_Signup_Form", u"Sample Application", None))
        self.groupBox.setTitle(QCoreApplication.translate("W_Signup_Form", u"Please Sign Up", None))
        self.label.setText(QCoreApplication.translate("W_Signup_Form", u"User ID", None))
        self.label_2.setText(QCoreApplication.translate("W_Signup_Form", u"Password", None))
        self.pb_ok.setText(QCoreApplication.translate("W_Signup_Form", u"Ok", None))
        self.pb_cancel.setText(QCoreApplication.translate("W_Signup_Form", u"Cancel", None))
        self.label_3.setText(QCoreApplication.translate("W_Signup_Form", u"Retype Password", None))
        self.lb_message.setText("")
    # retranslateUi

