# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registroDSFHFJ.ui'
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

class Ui_FormRegistro(object):
    def setupUi(self, FormRegistro):
        if not FormRegistro.objectName():
            FormRegistro.setObjectName(u"FormRegistro")
        FormRegistro.resize(605, 509)
        FormRegistro.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.btnLogin = QPushButton(FormRegistro)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(260, 390, 111, 51))
        self.label_2 = QLabel(FormRegistro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 160, 121, 41))
        self.label_2.setStyleSheet(u"font: 16pt \"Malgun Gothic\";")
        self.btnCrearUsr = QPushButton(FormRegistro)
        self.btnCrearUsr.setObjectName(u"btnCrearUsr")
        self.btnCrearUsr.setGeometry(QRect(260, 320, 111, 51))
        self.label = QLabel(FormRegistro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 60, 71, 41))
        self.label.setStyleSheet(u"font: 16pt \"Malgun Gothic\";")
        self.txtPass = QLineEdit(FormRegistro)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(220, 200, 181, 31))
        self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)
        self.txtUsuario = QLineEdit(FormRegistro)
        self.txtUsuario.setObjectName(u"txtUsuario")
        self.txtUsuario.setGeometry(QRect(220, 110, 181, 31))

        self.retranslateUi(FormRegistro)

        QMetaObject.connectSlotsByName(FormRegistro)
    # setupUi

    def retranslateUi(self, FormRegistro):
        FormRegistro.setWindowTitle(QCoreApplication.translate("FormRegistro", u"Registro", None))
        self.btnLogin.setText(QCoreApplication.translate("FormRegistro", u"Ya Tengo Cuenta", None))
        self.label_2.setText(QCoreApplication.translate("FormRegistro", u"Contrase\u00f1a", None))
        self.btnCrearUsr.setText(QCoreApplication.translate("FormRegistro", u"Crear Usuario", None))
        self.label.setText(QCoreApplication.translate("FormRegistro", u"Usuario", None))
        self.txtPass.setText("")
        self.txtUsuario.setText("")
    # retranslateUi

