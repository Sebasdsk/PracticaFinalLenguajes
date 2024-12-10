# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuSgYvpQ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindowMenu(object):
    def setupUi(self, MainWindowMenu):
        if not MainWindowMenu.objectName():
            MainWindowMenu.setObjectName(u"MainWindowMenu")
        MainWindowMenu.resize(341, 364)
        MainWindowMenu.setMouseTracking(False)
        self.centralwidget = QWidget(MainWindowMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnJugar = QPushButton(self.centralwidget)
        self.btnJugar.setObjectName(u"btnJugar")
        self.btnJugar.setGeometry(QRect(40, 100, 111, 61))
        self.btnEstadistica = QPushButton(self.centralwidget)
        self.btnEstadistica.setObjectName(u"btnEstadistica")
        self.btnEstadistica.setGeometry(QRect(40, 190, 111, 61))
        self.btnConfig = QPushButton(self.centralwidget)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setGeometry(QRect(180, 100, 111, 61))
        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(180, 190, 111, 61))
        MainWindowMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindowMenu)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowMenu)

        QMetaObject.connectSlotsByName(MainWindowMenu)
    # setupUi

    def retranslateUi(self, MainWindowMenu):
        MainWindowMenu.setWindowTitle(QCoreApplication.translate("MainWindowMenu", u"Menu", None))
        self.btnJugar.setText(QCoreApplication.translate("MainWindowMenu", u"Jugar", None))
        self.btnEstadistica.setText(QCoreApplication.translate("MainWindowMenu", u"Estadistica", None))
        self.btnConfig.setText(QCoreApplication.translate("MainWindowMenu", u"Configuracion", None))
        self.btnSalir.setText(QCoreApplication.translate("MainWindowMenu", u"Salir", None))
    # retranslateUi

