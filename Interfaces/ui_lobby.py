# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lobbyvTnfng.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_FormLobby(object):
    def setupUi(self, FormLobby):
        if not FormLobby.objectName():
            FormLobby.setObjectName(u"FormLobby")
        FormLobby.resize(535, 230)
        self.btnCrearPartida = QPushButton(FormLobby)
        self.btnCrearPartida.setObjectName(u"btnCrearPartida")
        self.btnCrearPartida.setGeometry(QRect(80, 50, 91, 51))
        self.btnUnirse = QPushButton(FormLobby)
        self.btnUnirse.setObjectName(u"btnUnirse")
        self.btnUnirse.setGeometry(QRect(220, 50, 101, 51))
        self.btnSalir = QPushButton(FormLobby)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(220, 150, 91, 41))
        self.lineEdit = QLineEdit(FormLobby)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(350, 70, 113, 22))
        self.label = QLabel(FormLobby)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 40, 81, 20))
        self.lbIdGenerado = QLabel(FormLobby)
        self.lbIdGenerado.setObjectName(u"lbIdGenerado")
        self.lbIdGenerado.setGeometry(QRect(60, 10, 121, 16))

        self.retranslateUi(FormLobby)

        QMetaObject.connectSlotsByName(FormLobby)
    # setupUi

    def retranslateUi(self, FormLobby):
        FormLobby.setWindowTitle(QCoreApplication.translate("FormLobby", u"Lobby", None))
        self.btnCrearPartida.setText(QCoreApplication.translate("FormLobby", u"Crear Partida", None))
        self.btnUnirse.setText(QCoreApplication.translate("FormLobby", u"Unirse a Partida", None))
        self.btnSalir.setText(QCoreApplication.translate("FormLobby", u"Salir", None))
        self.label.setText(QCoreApplication.translate("FormLobby", u"ID de la partida", None))
        self.lbIdGenerado.setText("")
    # retranslateUi

