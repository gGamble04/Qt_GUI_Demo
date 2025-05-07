# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'View_Persons.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_veiw_people_form(object):
    def setupUi(self, veiw_people_form):
        if not veiw_people_form.objectName():
            veiw_people_form.setObjectName(u"veiw_people_form")
        veiw_people_form.resize(385, 311)
        font = QFont()
        font.setPointSize(12)
        veiw_people_form.setFont(font)
        self.verticalLayout = QVBoxLayout(veiw_people_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(veiw_people_form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_search = QLineEdit(self.groupBox)
        self.le_search.setObjectName(u"le_search")

        self.horizontalLayout.addWidget(self.le_search)


        self.verticalLayout.addWidget(self.groupBox)

        self.view_people_table = QTableView(veiw_people_form)
        self.view_people_table.setObjectName(u"view_people_table")

        self.verticalLayout.addWidget(self.view_people_table)


        self.retranslateUi(veiw_people_form)

        QMetaObject.connectSlotsByName(veiw_people_form)
    # setupUi

    def retranslateUi(self, veiw_people_form):
        veiw_people_form.setWindowTitle(QCoreApplication.translate("veiw_people_form", u"Person Data", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("veiw_people_form", u"Search by Name:", None))
    # retranslateUi

