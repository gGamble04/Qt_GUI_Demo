# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
import Icons_rc

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(543, 457)
        font = QFont()
        font.setPointSize(12)
        mw_Main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/dollar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mw_Main.setWindowIcon(icon)
        self.action_quit = QAction(mw_Main)
        self.action_quit.setObjectName(u"action_quit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_quit.setIcon(icon1)
        font1 = QFont()
        self.action_quit.setFont(font1)
        self.action_addPerson = QAction(mw_Main)
        self.action_addPerson.setObjectName(u"action_addPerson")
        self.action_viewPeople = QAction(mw_Main)
        self.action_viewPeople.setObjectName(u"action_viewPeople")
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 60, 343, 32))
        font2 = QFont()
        font2.setPointSize(18)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QWidget {\n"
" color: rgb(0, 170, 0);\n"
"}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 543, 33))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuPerson = QMenu(self.menubar)
        self.menuPerson.setObjectName(u"menuPerson")
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuPerson.menuAction())
        self.menuFIle.addAction(self.action_quit)
        self.menuPerson.addAction(self.action_addPerson)
        self.menuPerson.addAction(self.action_viewPeople)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"Sample Application", None))
        self.action_quit.setText(QCoreApplication.translate("mw_Main", u"Quit", None))
        self.action_addPerson.setText(QCoreApplication.translate("mw_Main", u"Add Person", None))
        self.action_viewPeople.setText(QCoreApplication.translate("mw_Main", u"View People", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("mw_Main", u"Welcome to the Sample Qt App!", None))
        self.menuFIle.setTitle(QCoreApplication.translate("mw_Main", u"FIle", None))
        self.menuPerson.setTitle(QCoreApplication.translate("mw_Main", u"Person", None))
    # retranslateUi

