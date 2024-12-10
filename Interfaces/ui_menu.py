# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuAigeaq.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Menu(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName(u"Menu")
        Menu.resize(400, 300)
        self.btnEstadistica = QPushButton(Menu)
        self.btnEstadistica.setObjectName(u"btnEstadistica")
        self.btnEstadistica.setGeometry(QRect(70, 150, 111, 61))
        self.btnJugar = QPushButton(Menu)
        self.btnJugar.setObjectName(u"btnJugar")
        self.btnJugar.setGeometry(QRect(70, 60, 111, 61))
        self.btnConfig = QPushButton(Menu)
        self.btnConfig.setObjectName(u"btnConfig")
        self.btnConfig.setGeometry(QRect(210, 60, 111, 61))
        self.btnSalir = QPushButton(Menu)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(210, 150, 111, 61))

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", u"Menu", None))
        self.btnEstadistica.setText(QCoreApplication.translate("Menu", u"Estadistica", None))
        self.btnJugar.setText(QCoreApplication.translate("Menu", u"Jugar", None))
        self.btnConfig.setText(QCoreApplication.translate("Menu", u"Configuracion", None))
        self.btnSalir.setText(QCoreApplication.translate("Menu", u"Salir", None))
    # retranslateUi

